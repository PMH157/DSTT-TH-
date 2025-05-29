from sympy import Symbol, solve
x = Symbol('x')
bieuthuc = x + 3 - 5
print(solve(bieuthuc))

bieuthuc = x**2 + 3 - 5
nghiem_x = solve(bieuthuc)
print(nghiem_x)
print(nghiem_x[0])
print(nghiem_x[1])