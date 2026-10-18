def rsi(prices: list[float], period: int = 14) -> list[float]:
    if period <= 0:
        raise ValueError("period must be a positive integer")
    if len(prices) <= period:
        raise ValueError("prices length must be greater than period")

    gains: list[float] = []
    losses: list[float] = []
    for index in range(1, len(prices)):
        change = prices[index] - prices[index - 1]
        gains.append(max(change, 0.0))
        losses.append(max(-change, 0.0))

    average_gain = sum(gains[:period]) / period
    average_loss = sum(losses[:period]) / period
    result = [100.0 if average_loss == 0 else
              100.0 - 100.0 / (1.0 + average_gain / average_loss)]

    for index in range(period, len(gains)):
        """ Index starts from period because we already calculated the first RSI value using the first 'period' gains and losses. """
        average_gain = (average_gain * (period - 1) + gains[index]) / period
        average_loss = (average_loss * (period - 1) + losses[index]) / period
        result.append(
            100.0 if average_loss == 0 else
            100.0 - 100.0 / (1.0 + average_gain / average_loss)
        )

    return result
