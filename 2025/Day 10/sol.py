from z3 import Solver, Int, Sum, sat
from sys import stdin

lines = [l.strip() for l in stdin if l.strip()]
sol1 = 0
sol2 = 0

def minimize_with_solver(solver, objective):
    best = None
    while solver.check() == sat:
        model = solver.model()
        val = model.eval(objective).as_long()
        best = val
        solver.add(objective < best)
    return best

light_list = [l.split(" ")[0][1:-1] for l in lines]
button_list = [[list(map(int, b[1:-1].split(","))) for b in l.split(" ")[1:-1]] for l in lines]
joltage_list = [list(map(int, l.split(" ")[-1][1:-1].split(","))) for l in lines]
for i, light in enumerate(light_list):
    buttons = button_list[i]
    matrix = [[0] * len(buttons) for _ in range(len(light))]
    for j in range(len(buttons)):
        for idx in buttons[j]:
            matrix[idx][j] = 1

    s = Solver()
    x = [Int(f"x_{k}") for k in range(len(buttons))]
    h = [Int(f"h_{j}") for j in range(len(light))]
    for v in x:
        s.add(v >= 0, v <= 1)
    for v in h:
        s.add(v >= 0)
    for j in range(len(light)):
        rhs = 1 if light[j] == "#" else 0
        s.add(Sum(matrix[j][k] * x[k] for k in range(len(buttons))) - 2 * h[j] == rhs)
    objective = Sum(x)
    sol1 += minimize_with_solver(s, objective)

for i, joltages in enumerate(joltage_list):
    buttons = button_list[i]
    matrix = [[0] * len(buttons) for _ in range(len(joltages))]
    for j in range(len(buttons)):
        for idx in buttons[j]:
            matrix[idx][j] = 1
    s = Solver()
    x = [Int(f"x_{k}") for k in range(len(buttons))]
    for v in x:
        s.add(v >= 0)
    for j, joltage in enumerate(joltages):
        s.add(Sum(matrix[j][k] * x[k] for k in range(len(buttons))) == joltage)
    objective = Sum(x)
    sol2 += minimize_with_solver(s, objective)
print(sol1)
print(sol2)