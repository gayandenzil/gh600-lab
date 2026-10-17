## Goal
Add an RSI(14) indicator that returns one RSI value for each price change after the initial `period` changes, and rejects input whose length is not greater than the period.

## Files to change (path + reason)
- `src/indicators/rsi.py` — implement the typed RSI function and validate its inputs.
- `tests/indicators/test_rsi.py` — test normal calculations, output shape, and invalid inputs, following the test naming instructions.

## Steps (numbered, each independently verifiable)
1. Implement `rsi(prices: list[float], period: int = 14) -> list[float]`, using Wilder’s initial average gains/losses and subsequent smoothing.
2. Validate the period and raise `ValueError` when `len(prices) <= period`.
3. Add behavior-named pytest tests for the default period, a custom period, expected RSI values/output length, and invalid input cases.
4. Run `pytest` and `mypy --disallow-untyped-defs src tests`; address any failures within the two permitted directories.

## Risks
- RSI output length and zero-gain/zero-loss behavior can vary by convention. Define those cases explicitly in the implementation and tests.
- Built-in generic annotations such as `list[float]` require a compatible Python version; the requested function signature specifies this form.

## Acceptance Criteria (testable)
- `src/indicators/rsi.py` exposes the requested typed function with `period=14` by default.
- Inputs with `len(prices) <= period` raise `ValueError`.
- RSI calculation, output length, and edge-case behavior are covered by tests in `tests/indicators/test_rsi.py`.
- `pytest` and `mypy --disallow-untyped-defs src tests` pass.
- No files outside `src/indicators` and `tests/indicators` are changed.