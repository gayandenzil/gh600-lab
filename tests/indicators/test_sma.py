import pytest

from src.indicators.sma import sma


def test_sma_returns_rolling_averages() -> None:
    assert sma([1.0, 2.0, 3.0, 4.0], 3) == [2.0, 3.0]


def test_sma_rejects_non_positive_period() -> None:
    with pytest.raises(ValueError, match="period must be a positive integer"):
        sma([1.0, 2.0, 3.0], 0)