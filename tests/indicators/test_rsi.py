import pytest

from src.indicators.rsi import rsi


def test_rsi_returns_one_value_per_change_after_default_period() -> None:
    prices = [float(value) for value in range(15)]

    assert rsi(prices) == [100.0]


def test_rsi_uses_wilder_smoothing_for_custom_period() -> None:
    actual = rsi([1.0, 2.0, 3.0, 2.0, 3.0, 2.0, 4.0], period=3)
    expected = [
        200.0 / 3.0,
        700.0 / 9.0,
        1400.0 / 27.0,
        2050.0 / 27.0,
    ]

    assert actual == pytest.approx(expected)


def test_rsi_returns_zero_when_prices_only_decrease() -> None:
    assert rsi([4.0, 3.0, 2.0], period=2) == [0.0]


def test_rsi_returns_one_when_prices_are_flat() -> None:
    assert rsi([5.0, 5.0, 5.0], period=2) == [100.0]


def test_rsi_rejects_non_positive_period() -> None:
    with pytest.raises(ValueError, match="period must be a positive integer"):
        rsi([1.0, 2.0], period=0)


def test_rsi_rejects_prices_not_longer_than_period() -> None:
    with pytest.raises(ValueError, match="prices length must be greater than period"):
        rsi([1.0, 2.0, 3.0], period=3)
