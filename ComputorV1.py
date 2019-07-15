#!/usr/bin/python3.4
# -*-coding:Utf-8-*-

from sys import argv, exit

max_power = 2

#
#   Add parentheses to a negativ number
#

def bracket_neg(nb):
    r = ""
    if nb < 0:
        r += "(" + str(nb) + ")"
    else:
        r += str(nb)
    return r

#
#   Resolve an equation of degree 2,
#   calculating his discriminent first
#

def resolve_d2(nb):
    print("Form : a * X^2 + b * X + c = 0\n")
    delta = nb[1] * nb[1] - 4 * nb[2] * nb[0]
    print("Δ = b^2 - 4 * a * c")
    r = "    " + bracket_neg(nb[1]) + "^2 - 4 * " + bracket_neg(nb[2]) + " * " + bracket_neg(nb[0])
    print(r)
    print("    " + str(delta))
    if delta > 0:
        print("Δ is positive, means there are two real solutions :")
        print("      -b - √Δ                         -b + √Δ")
        print("s1 = ---------          and     s2 = ---------")
        print("        2a                              2a\n")
        s = (-nb[1] - delta ** 0.5) / (2 * nb[2])
        if s == 0:
            s = abs(s)
        print("s1 = " + str(s))
        s = (-nb[1] + delta ** 0.5) / (2 * nb[2])
        if s == 0:
            s = abs(s)
        print("s2 = " + str(s))
    if delta == 0:
        print("Δ is null, means there is one solution :")
        print("     -b")
        print("s = ----")
        print("     2a")
        s = -nb[1] / (2 * nb[2])
        if s == 0:
            s = abs(s)
        print("s = " + str(s))
    if delta < 0:
        print("Δ is negative, means there are two complex solutions :")
        print("      -b -i * √-Δ                        -b + i * √-Δ")
        print("s1 = -------------   and           s2 = --------------")
        print("          2a                                  2a\n")
        a = -nb[1] / (2 * nb[2])
        s = 1
        while s < 3:
            b = ((-delta) ** 0.5) / (2 * nb[2])
            if s > 1:
                b *= -1
            r = "s" + str(s) + " = "
            if a < 0:
                r += " - "
            if a != 0:
                r += str(abs(a)) + " "
            if b < 0:
                r += "- "
            elif a != 0:
                r+= "+ "
            r += "i * " + str(abs(b))
            print(r)
            s += 1

#
#   Resolve an equation of degree 1
#   Note : nb[1] can't be null.
#

def resolve_d1(nb):
    print("Form : a * X + b = 0\n")
    print("The solution is :")
    print("     -b")
    print("s = ----")
    print("      a")
    s = -nb[0] / nb[1]
    if s == 0:
        s = abs(s)
    print("s = " + str(s))

#
#   Resolve an equation of degree 0,
#   checking if it is valid or not.
#

def resolve_d0(nb):
    if nb[0] == 0:
        print("All real numbers are solution\ns = ℝ")
    else:
        print("The equation is not valid !")

#
#   Get the number after a '^'
#

def get_power(s):
    if len(s) > 3:
        return int(s[2:])
    else:
        return int(s[2])
#
#   Parsing, checking argument number, storing power of X in a dict nb
#

if len(argv) != 2:
    print("Wrong argument number")
    exit()
nb = {
        0:0.0,
        1:0.0,
        2:0.0
}
i = 0
list_eq = list(argv[1])
while i < len(list_eq):
    if list_eq[i] == '+' or list_eq[i] == '-':
        del list_eq[i + 1]
        i += 1
    i += 1
eq = "".join(list_eq)
split = eq.split(" ")
equal = split.index("=")
i = 0
while i < len(split):
    if split[i] == '*':
        power = get_power(split[i + 1])
        if not power in nb:
            nb[power] = float(split[i - 1])
        elif i < equal:
            nb[power] += float(split[i - 1])
        else:
            nb[power] -= float(split[i - 1])
    i += 1

#
#   Dict nb set, try to solve the equation.
#   First check the equation's degree and
#   calls the corresponding function to solve it.
#

degre = 0
for k, v in list(nb.items()):
    if k > degre and v != 0:
        degre = k
    if k > 2 and v == 0:
        del nb[k]
if degre != 0:
    print("Reduced form :")
    eq = ""
    for k, v in reversed(list(nb.items())):
        if v != 0:
            if eq != "":
                eq += ' '
            if v < 0:
                eq += "- "
            elif v > 0 and eq != "":
                eq += "+ "
            eq += str(abs(v)) + " * X^" + str(k)
    eq += " = 0"
    print(eq + "\n")
print("Polynomial degree : " + str(degre) + "\n")
if degre == 0:
    resolve_d0(nb)
elif degre == 1:
    resolve_d1(nb)
elif degre == 2:
    resolve_d2(nb)
else:
    print("Degrees above 2 Not supported")
