from sympy import solve, Symbol
x = Symbol('x')
ptb2 = x**2 + 9*x +8 
print(solve(ptb2, dict = True))

ptb2 = x**2 + 1*x + 10
nghiem_x = solve(ptb2, dict = True) 
print(nghiem_x)