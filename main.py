# Author: Yanling Wang yuw17@psu.edu
# Collaborator:aks6979@psu.edu
# Collaborator:xzl5423@psu.edu
# Section: 1
# Breakout: 11

def num_of_divisors(n):
 count=0
 i=0
 while i in range(2,n):
   if(n % i)!= 0:
     count=count+1
     return count

   return 0

def num_of_primes(n):
  count=0
  i=0
  for i in range(2,n):
   if(n % i)== 0:
     count=count+1
     return count

  return 0

def sum_n(n):
  sum=0
  i=0
  while i in range(0,n+1,1):
    sum=sum+i
    return sum

def print_n(s, n):
  i=0
  for i in range(1,n+1,1):
   print(s)

  return

def run():
  num = int(input("Enter an int: "))
  print(f"sum is {sum_n(num)}.")
  print(f"{num} has {num_of_divisors(num)} divisors.")
  print(f"There are {num_of_primes(num)} primes <= {num}.")
  line = input("Enter a string: ")
  print_n(line, num)

if __name__ == "__main__":
  run()