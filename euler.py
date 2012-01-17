#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import math

class Euler():

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

if __name__ == "__main__":
	if len(sys.argv) != 2:
		usg =  "usage: euler.py <problem-class>\n"
		usg += "ex. ./euler.py P1 or\n"
		usg += "./euler.py P2"
		raise ValueError(usg)

	problem = sys.argv[1]
	p = getattr(__import__("euler"), problem)()
	p.test()

