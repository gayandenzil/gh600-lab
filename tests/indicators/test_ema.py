import pytest

from src.indicators.ema import ema


@pytest.fixture
def sample_prices() -> list[float]:
    return [1.0, 2.0, 3.0, 4.0, 5.0]


def test_ema_uses_initial_period_average_as_seed(
    sample_prices: list[float],
) -> None:
    assert ema(sample_prices, period=3)[0] == 2.0


def test_ema_applies_smoothing_recurrence_to_subsequent_prices(
    sample_prices: list[float],
) -> None:
    assert ema(sample_prices, period=3) == [2.0, 3.0, 4.0]


def test_ema_returns_one_value_per_complete_window(
    sample_prices: list[float],
) -> None:
    result = ema(sample_prices, period=3)

    assert len(result) == len(sample_prices) - 3 + 1


def test_ema_rejects_non_positive_period(sample_prices: list[float]) -> None:
    with pytest.raises(ValueError, match="period must be a positive integer"):
        ema(sample_prices, period=0)


def test_ema_rejects_prices_shorter_than_period(sample_prices: list[float]) -> None:
    with pytest.raises(ValueError, match="prices length must be at least period"):
        ema(sample_prices[:2], period=3)
