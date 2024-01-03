# 1. print "softwarica" 10 times
def print_softwarica(n):
  for i in range(n):
    print("softwarica")

print_softwarica(10)

# 2. Sum of a list
def sum_list(lst):
  total = 0
  for x in lst:
    total += x
  return total

lst = [1, 2, 3, 4, 5]
print(sum_list(lst))

# 3. print each character using indexing
def print_char(s):
  for i in range(len(s)):
    print(s[i])

s = "softwarica"
print_char(s)

# 4. write a program to display integer from of a list. given list=[1,"a","c",2,3,4]
def display_int(lst):
  for x in lst:
    if type(x) == int:
      print(x)

lst = [1, "a", "c", 2, 3, 4]
display_int(lst)

# 5. multiplication of a each element. given list=[4,5,3,2]
def multiply_list(lst):
  product = 1
  for x in lst:
    product *= x
  return product

lst = [4, 5, 3, 2]
print(multiply_list(lst))

# 6. multiplication table of a given number
def multiplication_table(n):
  for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

n = 5
multiplication_table(n)

# 7. reverse a list
def reverse_list(lst):
  return lst[::-1]

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))

# 8. given list is [1,2,3,4] but expected output in new list [2,3,4,5]
def increment_list(lst):
  new_list = []
  for x in lst:
    new_list.append(x + 1)
  return new_list

lst = [1, 2, 3, 4]
print(increment_list(lst))

# 9. Given list is lst=[1,2,3,4] but print 1 and 4 only
def print_first_and_last(lst):
  print(lst[0])
  print(lst[-1])

lst = [1, 2, 3, 4]
print_first_and_last(lst)

# 10. Given list is lst=[1,2,3,4] but print 1 2 and 4 only
def print_except_third(lst):
  for i in range(len(lst)):
    if i != 2:
      print(lst[i])

lst = [1, 2, 3, 4]
print_except_third(lst)

# 11. Given list is [1,2,3,4] but expected output is [1,"a",2,4]
def replace_third(lst):
  lst[2] = "a"
  return lst

lst = [1, 2, 3, 4]
print(replace_third(lst))

# 12. Given list is [1,2,3,4,5] separate the elements into odd and even categories.
def separate_odd_even(lst):
  odd = []
  even = []
  for x in lst:
    if x % 2 == 0:
      even.append(x)
    else:
      odd.append(x)
  return odd, even

lst = [1, 2, 3, 4, 5]
print(separate_odd_even(lst))

# 13. Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types
def separate_types(lst):
  int_list = []
  str_list = []
  for x in lst:
    if type(x) == int:
      int_list.append(x)
    elif type(x) == str:
      str_list.append(x)
  return int_list, str_list

lst = [1, 2, 3, "d", 4, 5, "a"]
print(separate_types(lst))

# 14. Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
def append_types(lst):
  int_list = []
  str_list = []
  for x in lst:
    if type(x) == int:
      int_list.append(type(x))
    elif type(x) == str:
      str_list.append(type(x))
  return int_list, str_list

lst = [1, 2, 3, 4, "a", "b"]
print(append_types(lst))

# 15. Python program that accepts a string and calculate the number of digits and letters and space
def count_digits_letters_space(s):
  digits = 0
  letters = 0
  space = 0
  for c in s:
    if c.isdigit():
      digits += 1
    elif c.isalpha():
      letters += 1
    elif c.isspace():
      space += 1
  return digits, letters, space

s = "Hello, this is Bing 2024"
print(count_digits_letters_space(s))

# 16. Python program to check the validity of username and password input by users
def check_validity(username, password):
  valid_username = "softwarica"
  valid_password = "123456"
  if username == valid_username and password == valid_password:
    return True
  else:
    return False

username = input("Enter username: ")
password = input("Enter password: ")
print(check_validity(username, password))

# 17. program to print the given number is odd or even
def odd_or_even(n):
  if n % 2 == 0:
    print(f"{n} is even")
  else:
    print(f"{n} is odd")

n = 5
odd_or_even(n)

# 18. factorial of a given number
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

n = 4
print(factorial(n))

# 19. Print multiplication table of  1,2,3,4,5,6,7,8 
def multiplication_table(lst):
  for n in lst:
    for i in range(1, 11):
      print(f"{n} x {i} = {n * i}")
    print()

lst = [1, 2, 3, 4, 5, 6, 7, 8]
multiplication_table(lst)

# 20. Given list is lst=[1,2,3,4] but print 1 and 2 only
def print_first_two(lst):
  print(lst[0])
  print(lst[1])

lst = [1, 2, 3, 4]
print_first_two(lst)

# 21. Python program to calculate the sum of all the odd numbers within the given range.
def sum_odd(start, end):
  total = 0
  for i in range(start, end + 1):
    if i % 2 == 1:
      total += i
  return total

start = 1
end = 10
print(sum_odd(start, end))

# 22. Python program to calculate the sum of all the even numbers within the given range.
def sum_even(start, end):
  total = 0
  for i in range(start, end + 1):
    if i % 2 == 0:
      total += i
  return total

start = 1
end = 10
print(sum_even(start, end))

# 23. Python program to count the space of a given string
def count_space(s):
  space = 0
  for c in s:
    if c.isspace():
      space += 1
  return space

s = "Hello, this is Bing"
print(count_space(s))

# 24. given list is [1,2,3,4] but expected output is [1,8,27,64]
def cube_list(lst):
  new_list = []
  for x in lst:
    new_list.append(x ** 3)
  return new_list

lst = [1, 2, 3, 4]
print(cube_list(lst))

# 25. reverse of a string a="programming". 
def reverse_string(s):
  return s[::-1]

s = "programming"
print(reverse_string(s))

# 26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)
def print_until(n):
  for i in range(50):
    if i > n:
      break
    print(i)

n = 7
print_until(n)

# 27. Write a for loop that iterates through a string and prints every letter.
def print_letter(s):
  for c in s:
    print(c)

s = "softwarica"
print_letter(s)

# 28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
def greet_list(lst):
  for x in lst:
    print(f"Hello!, {x}")

lst = ["ram", "shyam", 1, 2]
greet_list(lst)

# 29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
def prefix_list(lst):
  new_list = []
  for x in lst:
    new_list.append(f"Dr.{x}")
  return new_list

lst = ["ram", "shyam", 1, 2]
print(prefix_list(lst))

# 30. Write a for loop which appends the square of each number to the new list.
def square_list(lst):
  new_list = []
  for x in lst:
    new_list.append(x ** 2)
  return new_list

lst = [1, 2, 3, 4, 5]
print(square_list(lst))

# 31. Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]
def append_positive(lst1):
  lst2 = []
  for x in lst1:
    if x > 0:
      lst2.append(x)
  return lst2

lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
print(append_positive(lst1))

# 32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6]
def print_except(lst):
  for x in lst:
    if x == 3 or x == 6:
      continue
    print(x)

lst = [0, 1, 2, 3, 4, 5, 6]
print_except(lst)

# 33. Write a for loop which appends the type of each element in the first list to the second list.
def append_type(lst1):
  lst2 = []
  for x in lst1:
    lst2.append(type(x))
  return lst2

lst1 = [1, 2, 3, "a", "b", "c"]
print(append_type(lst1))

# 34. Use else block to display a message “Done” after successful execution of for loop.
def print_done(lst):
  for x in lst:
    print(x)
  else:
    print("Done")

lst = [1, 2, 3, 4, 5]
print_done(lst)

# 35. Write a for loop statement to print the following series: 
# 105 98 -------7
def print_series(n, d):
  for i in range(n, 0, -d):
    print(i)

n = 105
d = 7
print_series(n, d)

# 36. removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
def remove_bad_chars(string, bad_chars):
  new_string = ""
  for c in string:
    if c not in bad_chars:
      new_string += c
  return new_string

string = "py;th* o:n ! ;py * t*h:o !n"
bad_chars = [';', ':', '!', "*"]
print(remove_bad_chars(string, bad_chars))

# 37. Python program to count the number of even and odd numbers from a series of numbers.  
def count_even_odd(lst):
  even = 0
  odd = 0
  for x in lst:
    if x % 2 == 0:
      even += 1
    else:
      odd += 1
  return even, odd

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count_even_odd(lst))

# 38. Write a python program to display all the prime numbers within a given range.
def display_prime(start, end):
  for n in range(start, end + 1):
    if n > 1:
      prime = True
      for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
          prime = False
          break
      if prime:
        print(n)

start = 10
end = 50
display_prime(start, end)

# 39. given number is prime or not
def is_prime(n):
  if n > 1:
    for i in range(2, int(n ** 0.5) + 1):
      if n % i == 0:
        return False
    return True
  else:
    return False

n = 17
print(is_prime(n))

# 40. program to check given number is palindrome or not
def is_palindrome(n):
  s = str(n)
  return s == s[::-1]

n = 121
print(is_palindrome(n))

# 41. program to check given number is armstrong or not
def is_armstrong(n):
  s = str(n)
  k = len(s)
  total = 0
  for c in s:
    total += int(c) ** k
  return total == n

n = 153
print(is_armstrong(n))

# 42. Python program to check a number is perfect square
def is_perfect_square(n):
  x = int(n ** 0.5)
  return x * x == n

n = 16
print(is_perfect_square(n))

# 43. python program to check a number is perfect number
def is_perfect_number(n):
  total = 0
  for i in range(1, n):
    if n % i == 0:
      total += i
  return total == n

n = 6
print(is_perfect_number(n))