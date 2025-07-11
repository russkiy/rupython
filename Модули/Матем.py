import math

Пи = math.pi
e = math.e
Тау = math.tau
Бесконечность = math.inf
Не_число = math.nan

def Сочетаний(n, k): return math.comb(n, k)
def Перестановок(n, k): return math.perm(n, k)
def Факториал(n): return math.factorial(n)
def НОД(*целые): return math.gcd(*целые)
def НОК(*целые): return math.lcm(*целые)
def ЦелКвКорень(n): return math.isqrt(n)
def ЦелВверх(x): return math.ceil(x)
def ЦелВниз(x): return math.floor(x)
def Модуль(x): return math.fabs(x)
def УмножСлож(x, y, z): return math.fma(x, y, z)
def Остаток(x, y): return math.fmod(x, y)
def ОстатОтн(x, y): return math.remainder(x, y)
def ДробЦел(x): return math.modf(x)
def ЦелЧасть(x): return math.trunc(x)
def Перенести_знак(x, y): return math.copysign(x, y)
def ВЭксп(x): return math.frexp(x)
def ИзЭксп(x, i): return math.ldexp(x, i)
def Близки(a, b, отнДопуск=1e-09, абсДопуск=0.0): return math.isclose(a, b, rel_tol=отнДопуск, abs_tol=абсДопуск)
def Конечное(x): return math.isfinite(x)
def Бесконечное(x): return math.isinf(x)
def Не_число(x): return math.isnan(x)
def СледПосле(x, y, шаг = 1): return math.nextafter(x, y, steps=шаг)
def НаименьшЗначБит(x): return math.ulp(x)
def КубКорень(x): return math.cbrt(x)
def exp(x): return math.exp(x)
def exp2(x): return math.exp2(x)
def expm1(x): return math.expm1(x)
def log(x, основание = e): return math.log(x, base=основание)
def ln(x): return math.log(x)
def log1p(x): return math.log1p(x)
def log2(x): return math.log2(x)
def lg(x): return math.log10(x)
def Степень(x, y): return math.pow(x, y)
def КвКорень(x): return math.sqrt(x)
def Расстояние(p, q): return math.dist(p, q)
def Сумма(перечислимое): return math.fsum(перечислимое)
def Гипотенуза(*координаты): return math.hypot(*координаты)
def Произведение(перечислимое, нач_знач = 1): return math.prod(перечислимое, start=нач_знач)
def СуммаПроизв(p, q): return math.sumprod(p, q)
def Градусы(x): return math.degrees(x)
def Радианы(x): return math.radians(x)
def sin(x): return math.sin(x)
def cos(x): return math.cos(x)
def tg(x): return math.tan(x)
def ctg(x): return math.cos(x) / math.sin(x)
def sec(x): return 1 / math.cos(x)
def cosec(x): return 1 / math.sin(x)
def arcsin(x): return math.asin(x)
def arccos(x): return math.acos(x)
def arctg(x): return math.atan(x)
def arcctg(x): return math.cos(x / math.sqrt(1 + x ** 2))
def arcsec(x): return math.acos(1 / x)
def arccosec(x): return math.asin(1 / x)
def Угол_по_точке(x, y): return math.atan2(y, x)
def sh(x): return math.sinh(x)
def ch(x): return math.cosh(x)
def th(x): return math.tanh(x)
def cth(x): return 1 / math.tanh(x)
def sch(x): return 1 / math.cosh(x)
def csch(x): return 1 / math.sinh(x)
def arsh(x): return math.asinh(x)
def arch(x): return math.acosh(x)
def arth(x): return math.atanh(x)
def arcth(x): return math.log((x + 1) / (x - 1)) / 2
def arsch(x): return math.acosh(1 / x)
def arcsch(x): return math.asinh(1 / x)
def ФунОшибок(x): return math.erf(x)
def ДопФунОшибок(x): return math.erfc(x)
def Гамма(x): return math.gamma(x)
def ЛогГамма(x): return math.lgamma(x)
