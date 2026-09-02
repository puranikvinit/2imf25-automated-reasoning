from z3 import Solver, Int, sat

s = Solver()
x = Int('x')
y = Int('y')

# x + y == 10, x > 5, y > 3
s.add(x + y == 10)
s.add(x > 5)
s.add(y > 3)

print("Checking test system...")
result = s.check()
print(f"Solver status: {result}")

if result == sat:
    m = s.model()
    print(f"Z3 install works! x = {m[x]}, y = {m[y]}")
else:
    print("Z3 installed incorrectly!")
