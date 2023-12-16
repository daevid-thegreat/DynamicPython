array = [100, 50, 20, 10, 5, 200, 500, 1000]
A = [9, 4, 1, 3, 5, 6, 7, 2]
tgt = 200


# Linear Search

def search(arr, target):
	for i in range(len(arr)):
		if arr[i] == target:
			return i


# Binary Search

# Iterative

def binary_itr(arr, start, end, target):
	while start <= end:
		mid = (start + end) // 2
		if arr[mid] < target:
			start = mid + 1
		elif arr[mid] > target:
			end = mid - 1
		else:
			return mid
	return start


# Recursive

def binary_recur(arr, start, end, target):
	if end >= start:
		mid = start + end - 1 // 2
		if arr[mid] < target:
			binary_itr(arr, mid + 1, end, target)
		elif arr[mid] > target:
			return binary_itr(arr, start, mid - 1, target)
		else:
			return mid
	else:
		return -1


# Bubble sort


def bubble_optimized(a):
	iterations = 0
	for i in range(len(a)):
		for j in range(len(a) - i - 1):
			iterations += 1
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
		return a, iterations


print(bubble_optimized(A))
