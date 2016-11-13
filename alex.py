import math
def prime(number):
	if type(number) != int:
		print('''
===== Ошибка типа данных =====
Входной аргумент данных должен быть целочисленным!
[type(number) = integer]
''')
	else:
		prime_bool = True
		for i in range(2, abs(number)):
			if number % i == 0:
				prime_bool = bool(prime_bool * False)
		return prime_bool
def divisors(number):
	if type(number) != int:
		print('''
===== Ошибка типа данных =====
Входной аргумент данных должен быть целочисленным!
[type(number) = integer]
''')
	else:
		if prime(number) == True:
			return False
		else:
			divisors_list = []
			for i in range(2, abs(number)):
				if number % i == 0:
					divisors_list.append(i)
			if number < 0:
				sec_divisors_list = []
				for i in divisors_list:
					sec_divisors_list.append(-i)
				for i in sec_divisors_list:
					divisors_list.append(i)
			return divisors_list
def gerohn(a, b, c):
	sides = [a, b, c]
	type_correct = True
	for i in sides:
		if (type(i) != int) and (type(i) != float):
			print('''
===== Ошибка типа данных =====
Входные аргументы данных должны быть числами!
[type(a, b, c) = integer/float]
''')
			type_correct = False
			break
	if type_correct == True:
		p = (a + b + c) / 2
		sqr = math.sqrt(p * (p - a) * (p - b) * (p - c))
		return sqr
