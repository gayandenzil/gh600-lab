---
task: Add EMA indicator
issue: 3
risk: low
autonomy: L2
files:
  - src/indicators/ema.py
  - tests/indicators/test_ema.py
acceptance:
  - id: AC1
    text: "src/indicators/ema.py exposes ema(prices: list[float], period: int) -> list[float]."
    verified_by: review
  - id: AC2
    text: ema raises ValueError when period <= 0 or len(prices) < period.
    verified_by: pytest
  - id: AC3
    text: tests/indicators/test_ema.py covers EMA behavior and invalid inputs using behavior-descriptive test names.
    verified_by: pytest
  - id: AC4
    text: pytest and mypy complete cleanly.
    verified_by: mypy
---
## Goal
Implement an exponential moving average indicator with the requested public signature, validation, and tests.

## Steps
1. Add the typed `ema(prices: list[float], period: int) -> list[float]` function in `src/indicators/ema.py`, validating the period and input length as required by AC1 and AC2.
2. Define the EMA series using the SMA of the first `period` prices as its initial value, then apply the smoothing factor `2 / (period + 1)` to each subsequent price. Return one value per complete window, satisfying AC1.
3. Add `tests/indicators/test_ema.py` cases for the initial average, smoothing recurrence, output length, and both invalid-input conditions. Name each test to describe the behavior, condition, and expected result, satisfying AC2 and AC3.
4. Run `pytest` and `mypy`; fix any failures relevant to this change and confirm both are clean, satisfying AC4.

## Risks and mitigations
- EMA conventions differ in their initial seed and output alignment. Use the initial-period SMA seed and emit the first result at index `period - 1`; test these choices explicitly.
- The required built-in generic signature `list[float]` must remain consistent with the project’s Python and mypy setup; check it with mypy.
- The test instruction file matches `test/**/*.py`, while the requested file is under `tests/`. Preserve the required test filename and use the behavior-descriptive naming rule in either case.

## Out of scope
- Modifying existing indicators or adding third-party dependencies.
