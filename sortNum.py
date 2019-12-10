import random

def selectionSort(nums, debug = False):
	orig = nums
	count = 0

	for j in range(0, len(nums)):
		#count += 1
		high = j
		for i in range(1 + j, len(nums)):
			count += 1
			if nums[i] < nums[high]:
				high = i
		nums[j], nums[high] = nums[high], nums[j]

		if debug: print "Step", j, "(" + str(count) + ")", "\t\t", nums
   
	if debug: print "\n"
	print "Selection Sort\t(len = " + str(len(nums)) + ", count = " + str(count) + ")\t", nums

def bubbleSort(nums, debug = False):
	orig = nums
	count = 0

	for j in range(0, len(nums)):
		swapped = False
		#count += 1
		for i in range(0, len(nums) - 1):
			count += 1
			if nums[i + 1] < nums[i]:
				nums[i], nums[i + 1] = nums[i + 1], nums[i]
				swapped = True

				if debug: print "Step", j, "(" + str(count) + ")", "\t\t", nums
		if not swapped: break

	if debug: print "\n"
	print "Bubble Sort\t(len = " + str(len(nums)) + ", count = " + str(count) + ")\t", nums

count = 0
def partition(a, hi, debug, lo = 0):
	global count

	if lo >= hi:
		return a

	aa = a[:]
	a[(hi - lo) // 2 + lo], a[hi] = a[hi], a[(hi - lo) // 2 + lo]
	count += 1
	piv = hi
	if debug: print "doing:", aa[lo:hi+1], lo, hi, "[", (hi - lo) // 2 + lo, "]=", aa[(hi - lo) // 2 + lo]

	l = lo
	r = hi - 1
	foundL = False
	foundR = False
	
	while True:
		if a[l] > a[piv] and not foundL:
			if debug > 2: print "foundL:", l, a[l]
			foundL = True
		if a[r] <= a[piv] and not foundR:
			if debug > 2: print "foundR:", r, a[r]
			foundR = True

		if foundL and foundR:
			a[l], a[r] = a[r], a[l]
			count += 1
			if debug > 1: print "swapped:", a[lo:hi+1], l, r
			foundL, foundR = False, False

		if l == r: break
		if not foundL: l += 1
		if l == r: break
		if not foundR: r -= 1
		if l == r: break

	if a[l] <= a[piv]:
		a[l + 1], a[piv] = a[piv], a[l + 1]
		count += 1
		piv = l + 1
	else:
		a[l], a[piv] = a[piv], a[l]
		count += 1
		piv = l

	if hi - lo == 1:
		return a

	if debug > 2: print "breaking into:[", piv - 1, ":",lo,"]"
	a = partition(a, piv - 1, debug, lo)
	if hi == piv:
		return a
	else:S
		if debug > 2: print "breaking into:[", hi, ":",piv,"]"
		return partition(a, hi, debug, piv)

def quickSort(a, debug = 0):
	global count
	count = 0
	nums = partition(a, len(a) - 1, debug)
	print "Quick Sort\t(len = " + str(len(nums)) + ", count = " + str(count) + ")\t", nums

def testQS():
	for i in range(0, 500):
		l = random.randint(1, 100)
		a = []
		for b in range(0, l):
			a.append(random.ranfdint(-9999, 9999))
		sorted = quickSort(a)	
		a.sort()
		if a != sorted:
			print "Bad code Areez", a, sorted

#selectionSort([4.12, 1, 3, -3, 7, -0])
#bubbleSort([4.12, 1, 3, -3, 7, -0])
quickSort([4.12, 1, 3, -3, 7, -0])

#selectionSort([1, 3.12, 1, -0])
#bubbleSort([1, 3.12, 1, -0])
#quickSort([1, 3.12, 1, -0])

#selectionSort([4.12, 1, 4, -0, 1, 8.12, 6.16])
#bubbleSort([4.12, 1, 4, -0, 1, 8.12, 6.16])
#quickSort([4.12, 1, 4, -0, 1, 8.12, 6.16])

#selectionSort([-1, -0.12, 1, 10, 20, 30])
#bubbleSort([-1, -0.12, 1, 10, 20, 30])
#quickSort([-1, -0.12, 1, 10, 20, 30])

#selectionSort([10, 6, 5, 1, 0, -2])
#bubbleSort([10, 6, 5, 1, 0, -2])
#quickSort([10, 6, 5, 1, 0, -2])