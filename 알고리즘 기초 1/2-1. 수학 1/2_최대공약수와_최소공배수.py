#2609

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

def max_f(n1, n2):

def min_f(n1, n2):


import sys
n1, n2 = map(int, sys.stdin.readline().split())

