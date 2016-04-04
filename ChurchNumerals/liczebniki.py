#!/usr/bin/python

zero = lambda f: lambda x:x  # f x = x
succ = lambda n: lambda f: lambda x: f(n(f)(x)) # n f x = f ( n f x )
add = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x)) # m n f x = m f ( n f x )
mult = lambda m: lambda n: lambda f: lambda x: m(n(f))(x)	# m n f x = m ( n f ) x 
exp = lambda m: lambda n: lambda f: lambda x: (n)(m)(f)(x)	# m n f x = ( n m ) f x

f1 = lambda x:x+1 	# x = x+1 
f2 = lambda x:x*2	# x = x*2

arg1 = 0
arg2 = 1

getNum = lambda f: f(f1)(arg1) # f = f f1 arg1

def printAndEval(x):
	print x, ' = ', eval(x)
	return

def getChurch (x):
	if x==0:
		return zero
	else:
		return succ(getChurch(x-1))

print  "\nWykorzystanie jako argumentow funkcji f1 i zmiennej arg1:\n"
printAndEval('(zero)(f1)(arg1)')
printAndEval('(succ(zero))(f1)(arg1)')
printAndEval('(succ(succ(zero)))(f1)(arg1)')
print  '\nDodanie dwoch liczb churcha 50 i 23 da ten sam wynik co liczba churcha 73:'
printAndEval('(add(getChurch(50))(getChurch(23)))(f1)(arg1)')
printAndEval('(getChurch(73))(f1)(arg1)')
print  '\nMnozenie dwoch liczb churcha 4 i 3 da ten sam wynik co liczba churcha 12:'
printAndEval('(mult(getChurch(4))(getChurch(3)))(f1)(arg1)')
printAndEval('(getChurch(12))(f1)(arg1)')
print  '\nPotegowanie dwoch liczb churcha 2 i 5 da ten sam wynik co liczba churcha 32:'
printAndEval('(exp(getChurch(2))(getChurch(5)))(f1)(arg1)')
printAndEval('(getChurch(32))(f1)(arg1)')

print  "\nTeraz zmienimy nasza funkcje oraz argument."

print  "\nWykorzystanie jako argumentow funkcji f2 i zmiennej arg2:\n"
printAndEval('(zero)(f2)(arg2)')
printAndEval('(succ(zero))(f2)(arg2)')
printAndEval('(succ(succ(zero)))(f2)(arg2)')
print  '\nDodanie dwoch liczb churcha 3 i 8 da ten sam wynik co liczba churcha 11:'
printAndEval('(add(getChurch(3))(getChurch(8)))(f2)(arg2)')
printAndEval('(getChurch(11))(f2)(arg2)')
print  '\nMnozenie dwoch liczb churcha 4 i 3 da ten sam wynik co liczba churcha 12:'
printAndEval('(mult(getChurch(4))(getChurch(3)))(f2)(arg2)')
printAndEval('(getChurch(12))(f2)(arg2)')
print  '\nPotegowanie dwoch liczb churcha 2 i 5 da ten sam wynik co liczba churcha 32:'
printAndEval('(exp(getChurch(3))(getChurch(2)))(f2)(arg2)')
printAndEval('(getChurch(9))(f2)(arg2)')

print  "\nDla ulatwienia mozna zaimplementowac sobie"
print  "funkcje taka jak getNum = lambda f: f(f1)(arg1)\n"
printAndEval('getNum(zero)')
printAndEval('getNum(add(getChurch(35))(getChurch(23)))')
printAndEval('getNum(mult(getChurch(5))(getChurch(5)))')

