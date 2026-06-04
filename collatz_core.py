"""Shared Collatz / weird algorithm logic for CLI and web backend."""

MAX_STEPS = 500_000

# Classic 4 → 2 → 1 loop showcase for small inputs (each value appears at most twice).
LOOP_SHOWCASE: dict[int, list[int]] = {
    1: [1, 4, 2, 1],
    2: [2, 4, 2, 1],
    4: [4, 2, 1],
}


class TooManyStepsError(Exception):
    pass


def weird_algorithm(start: int, max_steps: int = MAX_STEPS) -> dict:
    a = start

    if start in LOOP_SHOWCASE:
        full_sequence = LOOP_SHOWCASE[start]
        steps = full_sequence[1:]
        return {
            "a": a,
            "steps": steps,
            "step": len(steps),
            "peak": max(full_sequence),
            "full_sequence": full_sequence,
            "is_collatz": True,
        }

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
