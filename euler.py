#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import math
import numpy
from operator import mul

class Euler():

	# -- I/O stuffs -- #
	def read_lines(self, file):
		f = open(file)
		return f.readlines()

	def sieve(self, limit):
		"""return the list of primes 
		less than or equal to the limit.
		"""

		primes = range(2, limit + 1)
		limit = int(math.sqrt(limit))
		for divisor in range(2, limit + 1):
			primes = [n for n in primes if (n == divisor or n % divisor != 0)]
		return primes
		
	def prime_factors(self, n):
		"Returns all the prime factors of a positive integer"
		factors = []
		d = 2
		while (n > 1):
			while (n%d==0):
				factors.append(d)
				n /= d
			d = d + 1

		return factors	

	def unique_prime_factors(self, n):
		"Returns all the prime factors of a positive integer"
		factors = set()
		d = 2
		while (n > 1):
			while (n%d==0):
				factors.add(d)
				n /= d
			d = d + 1

		return factors	

	def largest_prime_factor(self, n):
		"Returns the largest prime factor of a positive integer"
		d = 2
		while (n > 1):
			while (n%d==0):
				n /= d
			d = d + 1

		return d - 1

	def gen_factors(self, n):
		"""Return the factors of a number"""
		yield 1
		for i in range(2, int(math.floor(math.sqrt(n)))):
			if n % i == 0:
				yield i
				yield n/i
		yield n

	def factors(self, n):
		return list(self.gen_factors(n)) 

class P1(Euler):
	"""Find the sum of all the multiples 
	of 3 or 5 below 1000.
	"""

	def soln0(self):
		sum = 0
		for i in range(3, 1000):
			if i % 3 == 0 or i % 5 == 0:
				sum += i
		return sum

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)
		
class P2(Euler):
	"""By considering the terms in the Fibonacci 
	sequence whose values do not exceed four million, 
	find the sum of the even-valued terms.

	1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
	"""

	def fibLim(self, limit):
		a = 1
		b = 2
		sum = 0
		while(b <= limit):
			if b % 2 == 0:
				sum += b
			tmp = a
			a = b
			b = tmp + b
		return sum

	def test(self):
		start = time.time()
		answer = self.fibLim(4000000)
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)
		
class P3(Euler):
	"""The prime factors of 13195 are 5, 7, 13 and 29.
	What is the largest prime factor of the number 600851475143 ?
	"""

	TARGET = 600851475143

	def soln0(self):
		limit = int(math.ceil(math.sqrt(self.TARGET)))
		sieve = self.sieve(limit)
		for i in range(0, len(sieve)):
			div = sieve[len(sieve) - 1 - i]
			if 600851475143 % div == 0:
				return div
		return None

	def soln1(self):
		return max(self.unique_prime_factors(self.TARGET))

	def soln2(self):
		return self.largest_prime_factor(self.TARGET)

	def test(self):
		start = time.time()
		answer = self.soln1()
		elapsed = (time.time() - start)
		print "soln1: %s, time: %s" % (answer, elapsed)
		start = time.time()
		answer = self.soln2()
		elapsed = (time.time() - start)
		print "soln2: %s, time: %s" % (answer, elapsed)

class P4(Euler):
	"""A palindromic number reads the same both ways. 
	The largest palindrome made from the product of 
	two 2-digit numbers is 9009 = 91 * 99.

	Find the largest palindrome made from the 
	product of two 3-digit numbers.
	"""		

	MAX = 999 * 999
	MIN = 100 * 100

	def palindromic(self, n):
		"""return True iff n is palindromic"""
		n = str(n)
		return n == n[::-1]

	def palindromic_seq(self, min=MIN, max=MAX):
		seq = []
		for n in range(min, max+1):
			if self.palindromic(n):
				seq.append(n)
		return seq
		
	def palindromic_soln(self, min=MIN, max=MAX):
		factors = []
		window = range(min, max+1)
		window.reverse()
		for n in window:
			if self.palindromic(n):
				factors = self.factors(n)
				for f in factors:
					if f >= 100 and f <= 999 and n/f >= 100 and n/f <= 999:
						return n, [f, n/f]
		return None, []
		
	def soln0(self):
		return self.palindromic_soln()

	def test(self):
		start = time.time()
		answer, factors = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)
		print "factors of %s: %s" % (answer, factors)

class P5(Euler):
	"""2520 is the smallest number that can be divided by 
	each of the numbers from 1 to 10 without any remainder.

	What is the smallest positive number that is evenly 
	divisible by all of the numbers from 1 to 20?
	"""

	def soln0(self):
		"""Note that we only need to check for the 
		smallest number divisible by all of [11, 20], 
		since if that number n is evenly divisible by 
		all of the numbers in the in [11, 20], it is 
		guaranteed to be divisible by all of the numbers 
		in [1, 10]."""
		factors = set([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
		i = 44
		while i < math.factorial(20):
			non_divisors = [d for d in factors if i % d != 0]
			if len(non_divisors) == 0:
				return i	
			i += 11
		return None

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P6(Euler):
	"""The sum of the squares of the first ten natural numbers is:
	1^2 + 2^2 + ... + 10^2 = 385
	
	The square of the sum of the first ten natural numbers is:
	(1 + 2 + ... + 10)^2 = 552 = 3025

	Hence the difference between the sum of the squares of the 
	first ten natural numbers and the square of the sum is: 
	3025 - 385 = 2640.

	Find the difference between the sum of the squares of the 
	first one hundred natural numbers and the square of the sum.
	"""

	def sum_of_squares(self, n):
		return sum([math.pow(m, 2) for m in range(1, n+1)])	

	def square_of_sum(self, n):
		return math.pow(sum(range(1, n+1)), 2)
		
	def soln0(self):
		return int(self.square_of_sum(100) - self.sum_of_squares(100))

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P7(Euler):
	"""By listing the first six prime numbers: 
	2, 3, 5, 7, 11, and 13, we can see that the 
	6th prime is 13. What is the 10,001st prime number?
	"""
		
	def soln0(self):
		#return self.sieve(104750)[-1]
		init = 10001
		nth_primes = self.sieve(init)
		while len(nth_primes) < 10001:
			init *= 20
			nth_primes = self.sieve(init)

		return nth_primes[10001-1]

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P8(Euler):
	"""Find the greatest product of five consecutive digits in the 1000-digit number."""

	number = "73167176531330624919225119674426574742355349194934"
	number += "96983520312774506326239578318016984801869478851843"
	number += "85861560789112949495459501737958331952853208805511"
	number += "12540698747158523863050715693290963295227443043557"
	number += "66896648950445244523161731856403098711121722383113"
	number += "62229893423380308135336276614282806444486645238749"
	number += "30358907296290491560440772390713810515859307960866"
	number += "70172427121883998797908792274921901699720888093776"
	number += "65727333001053367881220235421809751254540594752243"
	number += "52584907711670556013604839586446706324415722155397"
	number += "53697817977846174064955149290862569321978468622482"
	number += "83972241375657056057490261407972968652414535100474"
	number += "82166370484403199890008895243450658541227588666881"
	number += "16427171479924442928230863465674813919123162824586"
	number += "17866458359124566529476545682848912883142607690042"
	number += "24219022671055626321111109370544217506941658960408"
	number += "07198403850962455444362981230987879927244284909188"
	number += "84580156166097919133875499200524063689912560717606"
	number += "05886116467109405077541002256983155200055935729725"
	number += "71636269561882670428252483600823257530420752963450"
		
	def soln0(self):
		curr_best = 0
		left_idx = 0
		right_idx = 5
		while right_idx <= len(self.number):
			str_digits = self.number[left_idx:right_idx]
			product = reduce(mul, [int(n) for n in str_digits])
			if product > curr_best:
				curr_best = product

			left_idx += 1
			right_idx += 1
			
		return curr_best

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P9(Euler):
	"""A Pythagorean triplet is a set of three natural numbers,
	a < b < c, for which a^2 + b^2 = c^2

	For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

	There exists exactly one Pythagorean triplet for which a + b + c = 1000.
	Find the product abc."""

	def find_pyth_triplets(self, n):
		"""Find solutions to: 
			a^2 + b^2 = c^2
			a + b + c = 1000
		"""
		for a in range(1, n):
			for b in range(1, n):
				sum = a*a + b*b
				root = math.sqrt(sum)
				if int(root) == root and (a + b + int(root) == n):
					return a, b, int(root)

	def soln0(self):
		a, b, c = self.find_pyth_triplets(1000)
		return a*b*c

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P10(Euler):
	"""Calculate the sum of all the primes below 2,000,000."""

	def soln0(self):
		return sum(self.sieve(2000000 - 1))

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P11(Euler):
	"""In the 2020 grid below, four numbers along a diagonal 
	line have been marked in red. The product of these numbers is:
	 26 * 63 * 78 * 14 = 1788696.

	What is the greatest product of four adjacent numbers in any 
	direction (up, down, left, right, or diagonally) in the 2020 grid?
	"""
	
	GRID = numpy.array([
		[8,  2,  22, 97, 38, 15, 0,  40, 0,  75, 4,  5,  7,  78, 52, 12, 50, 77, 91, 8],
		[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4,  56, 62, 0],
		[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
		[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
		[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
		[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
		[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
		[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
		[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
		[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
		[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
		[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
		[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
		[19, 80, 81, 68, 05, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 04, 89, 55, 40],
		[4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
		[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
		[4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
		[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
		[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
		[1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]])

	COUNT = 3 # how many adjacent neighbors do we consider
	
	def walk_grid(self):
		curr_best = 0
		for row in range(len(self.GRID)):
			for column in range(len(self.GRID[row])):
				local_max = self.max_adjacent_product(row, column)
				if local_max > curr_best:
					curr_best = local_max
		return curr_best
			

	def max_adjacent_product(self, row, column):
		"""Computes the greatest product of the three
		adjacent neighbors of cell (row, column) as well 
		as cell (row, column).

		NOTE: we need only examine the horizontal-left, 
		up-left-diagonal, vertical, and up-right-diagonal
		neighbors since we're guaranteed to examine the 
		other positions by walking the grid AND we do not
		want to duplicate work."""
		anchor = self.GRID[row][column]
		products = []

		#print "------- (row, column): (%s, %s) -------" % (row, column)
		# horizontal-left
		if column - self.COUNT >= 0:
			neighbors = self.GRID[row][column - self.COUNT:column + 1]
			#print "horizontal-left: %s" % neighbors
			products.append(reduce(mul, neighbors))

		# up-left-diagonal
		if column - self.COUNT >= 0 and row - self.COUNT >= 0:
			neighbors = []
			for i in range(self.COUNT + 1):
				neighbors.append(self.GRID[row - i][column - i])
			#print "up-left-diagonal: %s" % neighbors
			products.append(reduce(mul, neighbors))
		
		# verical
		if row - self.COUNT >= 0:
			col = self.GRID[:,column]
			#print "column: %s" % col
			neighbors = col[row - self.COUNT:row + 1]
			#print "vertical: %s" % neighbors
			products.append(reduce(mul, neighbors))					
		
		# up-right-diagonal
		if (column + self.COUNT) <= (len(self.GRID[row]) - 1) and (row - self.COUNT >= 0):
			neighbors = []
			for i in range(self.COUNT + 1):
				neighbors.append(self.GRID[row - i][column + i])
			#print "up-right-diagonal: %s" % neighbors
			products.append(reduce(mul, neighbors))

		# if local products have been computed
		# then return the max 
		if products:
			return max(products)
		return 0
		
	def soln0(self):
		return self.walk_grid()

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P12(Euler):
	"""The sequence of triangle numbers is generated 
	by adding the natural numbers. So the 7th triangle 
	number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
	The first ten terms would be 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
	
	In general the nth term of the sequence is given by 1 + 2 + 3 ... + n.
	
	Let us list the factors of the first seven triangle numbers:
	1: 1
	3: 1, 3
	6: 1, 2, 3, 6
	10: 1, 2, 5, 10
	15: 1, 3, 5, 15
	21: 1, 3, 7, 21
	28: 1, 2, 4, 7, 14, 28
	
	We can see that 28 is the first triangle number to have over 5 divisors.
	
	What is the value of the first triangle number to have over 500 divisors?
	"""
		
	def gen_triangle_seq(self, n):
		"""Returns the first n elements of the triangle sequence"""
		seq = []
		for i in range(1, n + 1):
			seq.append(sum(range(1, i + 1)))
		return seq
		
	def triangle_seq_soln(self, n):
		"""Returns the first n elements of the triangle sequence"""
		i = 1
		cont = True
		while cont:
			tri_num = sum(range(1, i + 1))
			if len(self.factors(tri_num)) > n:
				return tri_num
			i += 1

	def soln0(self):
		return self.triangle_seq_soln(500)

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P13(Euler):
	"""Work out the first ten digits of the sum of 
	the following one-hundred 50-digit numbers.
	(See P13.txt)"""

	def soln0(self):
		lines = self.read_lines("P13.txt")
		numbers = [long(n.replace("\n", "")) for n in lines]
		return str(sum(numbers))[0:10]

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P14(Euler):
	"""The following iterative sequence is defined for the set of positive integers:
		n --> n/2 (n is even)
		n --> 3n + 1 (n is odd)

	Using the rule above and starting with 13, we generate the following sequence:
		13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1

	It can be said that this sequence (starting at 13 and finishing at 1) contains 10
	terms. although it has not been proved yet (Collatz problem), it is thought that all
	starting numbers finish at 1.

	Which starting number, under one million, produces the longest chain?

	NOTE: Once the chain starts the terms are allowed to go above one million.
	"""

	def collatz_seq(self, start, cache={}):
		seq = [start]
		while start > 1:
			if start % 2 == 0:
				start = int(start/2)
			else:
				start = 3*start + 1

			if cache.has_key(start):
				# then we know the rest of the sequence
				# so use it and return!
				seq.extend(cache[start])
				return seq
			else:
				seq.append(start)

		return seq

	def collatz_soln(self):
		cache = {}
		curr_best = 0
		best_start = 1
		for i in range(1, 1000000):
			seq = self.collatz_seq(i, cache)
			cache[i] = seq
			if len(seq) > curr_best:
				curr_best = len(seq)
				best_start = i
		return best_start

	def soln0(self):
		#return self.collatz_seq(837799)
		return self.collatz_soln()

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P15(Euler):
	"""Starting in the top left corner of a 22 grid, 
	there are 6 routes (without backtracking) 
	to the bottom right corner.

	How many routes are there through a 2020 grid?"""

	def soln0(self):
		"""The number of unique paths to get to any vertex 
		in the square grid (not counting back-tracking),
		is equal to the sum of the number of unique paths 
		that exist to get to the vertex directly above it 
		(if it exists), and directly left of it (if it exists)
		"""
		grid_sums = [[] for i in range(21)]
		grid_sums[0].append(1)
		for row in range(21):
			for column in range(21):
				# if there exists a row above
				# add its score to this vertex's tally
				if row - 1 >= 0:
					up_score = grid_sums[row - 1][column]
				else:
					up_score = 0
				# if there exists a column to the left
				# add its score to this vertex's tally
				if column - 1 >= 0:
					left_score = grid_sums[row][column - 1]
				else:
					left_score = 0
				# set the current vertex's score
				if up_score + left_score == 0:
					vertex_score = 1
				else:
					vertex_score = up_score + left_score
				grid_sums[row].append(vertex_score)
			print grid_sums[row]
		return grid_sums[20][20]

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P16(Euler):
	"""2^15 = 32768 and the sum of its digits is 
	3 + 2 + 7 + 6 + 8 = 26. 
	
	What is the sum of the digits of the number 2^1000?
	"""

	def soln0(self):
		"""The pow function supports arbitrary precision."""
		exp_str = str(pow(2, 1000))
		print exp_str
		sum = 0
		for char in exp_str:
			sum += int(char)
		return sum

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P17(Euler):
	"""If the numbers 1 to 5 are written out in words: 
	one, two, three, four, five, then there are 
	3 + 3 + 5 + 4 + 4 = 19 letters used in total.

	If all the numbers from 1 to 1000 (one thousand) 
	inclusive were written out in words, how many letters would be used?

	NOTE: Do not count spaces or hyphens. For example, 
	342 (three hundred and forty-two) contains 23 letters 
	and 115 (one hundred and fifteen) contains 20 letters. 
	The use of "and" when writing out numbers is in compliance 
	with British usage."""

	MAP = {
		1: 3, #one
		2: 3, #two
		3: 5, #three
		4: 4, #four
		5: 4, #five
		6: 3, #six
		7: 5, #seven
		8: 5, #eight
		9: 4, #nine
		10: 3, #ten
		11: 6, #eleven
		12: 6, #twelve
		13: 8, #thirteen
		14: 8, #fourteen
		15: 7, #fifteen
		16: 7, #sixteen
		17: 9, #seventeen
		18: 8, #eighteen
		19: 8, #nineteen
		20: 6, #twenty
		30: 6, #thirty
		40: 5, #forty
		50: 5, #fifty
		60: 5, #sixty
		70: 7, #seventy
		80: 6, #eighty
		90: 6, #ninety
		100: 10, #one hundred
		1000: 11, #one thousand
	}

	HUNDRED = 7 #len("hundred")

	def tens(self, n):
		if n == 0:
			return 0
		if self.MAP.has_key(n):
			return self.MAP[n]
		tens = (n/10)*10
		ones = n % tens
		return self.MAP[tens] + self.MAP[ones]

	def soln0(self):
		total = 0
		for i in range(1, 1001):
			length = 0
			if i <= 20:
				length += self.MAP[i]
			elif i < 100:
				length += self.tens(i)
			elif i == 100:
				length += self.MAP[i]
			elif i < 1000:
				hundreds = (i/100)*100
				tens = i % hundreds
				num_hundreds = hundreds/100 
				length += self.MAP[num_hundreds] + self.HUNDRED + self.tens(tens)
			elif i == 1000:
				length += self.MAP[i]

			if i > 100 and i < 1000 and i % 100 != 0:
				# accounting for the "and" in 
				# "nine hundred and seventy three"
				length += 3

			print i, length
			total += length
				
		return total

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

class P18(Euler):
	"""By starting at the top of the triangle below and 
	moving to adjacent numbers on the row below, the maximum 
	total from top to bottom is 23.

            3
           7 4
          2 4 6
         8 5 9 3

	That is, 3 + 7 + 4 + 9 = 23.

	Find the maximum total from top to bottom of the triangle below:
	"""

	TRI = [
		                            [75],
		                          [95, 64],
		                        [17, 47, 82],
		                      [18, 35, 87, 10],
		                    [20,  4, 82, 47, 65],
		                  [19,  1, 23, 75,  3, 34],
		                [88,  2, 77, 73,  7, 63, 67],
		              [99, 65,  4, 28,  6, 16, 70, 92],
		            [41, 41, 26, 56, 83, 40, 80, 70, 33],
		          [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
		        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
		      [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
		    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
		  [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
		[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
	]

	def soln0(self):
		"""The highest route to any node in the triangle is equal to:
		max(highest route to left parent, highest route to right parent).
		With this in mind we will keep a max route score cached for each node."""
		node_scores = [[75]]
		print self.TRI

	def test(self):
		start = time.time()
		answer = self.soln0()
		elapsed = (time.time() - start)
		print "soln0: %s, time: %s" % (answer, elapsed)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		usg =  "usage: euler.py <problem-class>\n"
		usg += "ex. ./euler.py P1 or\n"
		usg += "./euler.py P2"
		raise ValueError(usg)

	problem = sys.argv[1]
	p = getattr(__import__("euler"), problem)()
	p.test()

