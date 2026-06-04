"""Shared Collatz / weird algorithm logic for CLI and web backend."""

MAX_STEPS = 500_000


class TooManyStepsError(Exception):
    pass


def weird_algorithm(start: int, max_steps: int = MAX_STEPS) -> dict:
    a = start
    steps: list[int] = []
    step = 0
    peak = start

    if start >= 1:
        n = start
        while n != 1:
            if n % 2:
                n = 3 * n + 1
            else:
                n //= 2
            steps.append(n)
            step += 1
            if n > peak:
                peak = n
            if step > max_steps:
                raise TooManyStepsError(
                    f"Sequence exceeded {max_steps:,} steps — try a smaller number."
                )

    is_collatz = (
        len(steps) >= 3
        and steps[-3] == 4
        and steps[-2] == 2
        and steps[-1] == 1
    )

    return {
        "a": a,
        "steps": steps,
        "step": step,
        "peak": peak,
        "full_sequence": [a, *steps],
        "is_collatz": is_collatz,
    }
