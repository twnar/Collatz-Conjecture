from collatz_core import TooManyStepsError, weird_algorithm

n = a = int(input("Entet a integer to apply the weird algorithm to: "))
try:
    result = weird_algorithm(n)
except TooManyStepsError as exc:
    print(exc)
    raise SystemExit(1) from exc

s = " ".join(str(v) for v in result["steps"])
if result["steps"]:
    s += " "

print(str(a), s)
print("Number of steps:", result["step"])
print(
    "Is this a collatz number?:",
    "Yes"
    if result["is_collatz"]
    else "Wow! U just broke the collatz conjecture! Write down the number you tried and send it to twnarx@gmail.com lol :D",
)
