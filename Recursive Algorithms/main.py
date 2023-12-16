# Factorials

def iterative_factorial(n):
	fact = 1
	for i in range(2, n + 1):
		fact *= i
	return fact


def recursive_factorial(n):
	if n == 1:
		return n
	else:
		temp = recursive_factorial(n - 1)
		temp = temp * n
	return temp


# Permutation

def permute(string, pocket=""):
	if len(string) == 0:
		print(pocket)
	else:
		for i in range(len(string)):
			letter = string[i]
			front = string[0:i]
			back = string[i + 1:]
			together = front + back
			permute(together, letter + pocket)


print(permute("ABCD", ""))
