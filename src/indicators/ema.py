def ema(prices: list[float], period: int) -> list[float]:
    """Calculate the exponential moving average for a list of prices."""
    if period <= 0:
        raise ValueError("period must be a positive integer")
    if len(prices) < period:
        raise ValueError("prices length must be at least period")

    smoothing_factor = 2 / (period + 1)
    average = sum(prices[:period]) / period
    result = [average]

    for price in prices[period:]:
        average = (price - average) * smoothing_factor + average
        result.append(average)

    return result
