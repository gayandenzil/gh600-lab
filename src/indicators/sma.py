from typing import List, Sequence


def sma(values: Sequence[float], period: int) -> List[float]:
    if period <= 0:
        raise ValueError("period must be a positive integer")

    return [
        sum(values[start:start + period]) / period
        for start in range(len(values) - period + 1)
    ]