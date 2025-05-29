#1.2.1
danhsach1 = [1. , 3.]
danhsach2 = [5. , 7.]
danhsach = danhsach1 + danhsach2
print(danhsach)
danhsach_gapdoi = 2 * danhsach
print(danhsach_gapdoi)
print(danhsach * 2)
dsc2 = [x/2 for x in danhsach]
print(dsc2)
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]
anh_xa = zip(thu_tu, mon_hoc, diem_so)
print(anh_xa)
tap_hop = set(anh_xa)
print(tap_hop)
lay_TT = zip(*anh_xa)
lay_monhoc = zip(*anh_xa)
lay_diem = zip(*anh_xa)
print(lay_TT)
print(lay_monhoc)
print(lay_diem)
import itertools
tap_sinh = list(itertools.chain(range(4), range(5,10), range(15,20)))
print(tap_sinh)
print(list(zip(range(4), range(7, 12), reversed(range(11)))))
import itertools
tap_sinh = list(itertools.chain(range(4), range(5,10), range(15,20) ))
print(tap_sinh)
print(list(zip(range(4), range(7, 12), reversed(range(11)))))
#2.1
x = 1
x + x + x + 2
from sympy import Symbol
x = Symbol('x')
f = x + x + x + 2
print(f)
a= Symbol('Noi')
b = Symbol('Chim')
print(3*b + 7*a)
print(a.name)
print(b.name)
from sympy import Symbol, expand
x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
print(s)
p = x*(x+2*x)
print(p)
p = x*(-x+2*x-x)
print(p)
p = (x+2)*(y+3)
print(p.expand())
#2.2.1
from sympy import factor
bieuthuc = x**3 - y**3
print(factor(bieuthuc))
from sympy import expand
bieuthuc = (x - y)*(x**2 + x*y + y**2)
print(expand(bieuthuc))
#2.2.2
from sympy import pprint
bieuthuc = x*x - 2*x*y + y**2
pprint(bieuthuc)
from sympy import pprint
from sympy import init_printing
init_printing(order='rev-lex')
bieuthuc = x*x - 2*x*y + y**2
pprint(bieuthuc)
bieuthuc1 = factor(bieuthuc)
pprint(bieuthuc1)
#2.2.3
from sympy import Symbol, Subs
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
print(bieuthuc)
giatri = bieuthuc.subs({x:3, y:2})
print(giatri)
print(x)
print(y)