a = 5
# a += 4 IS SAME AS a = a + 4
# print(a)  Output: 9 

# a -= 2 IS SAME AS a = a - 2
# print(a)  Output: 7

# a *= 3 IS SAME AS a = a * 3
# print(a)  Output: 21

# a /= 7 IS SAME AS a = a / 7
# print(a)  Output: 3.0

# a //= 2 IS SAME AS a = a // 2
# print(a)  Output: 1.0

# a %= 2 IS SAME AS a = a % 2
# print(a) Output: 1.0

# a **= 3 IS SAME AS a = a ** 3
# print(a)  Output: 1.0

#if both sides of and operator are true then it will return true otherwise it will return false
print(True and True) # Output: True
print(True and False) # Output: False
print(False and True) # Output: False
print(False and False) # Output: False

#if both sides of or operator are false then it will return false otherwise it will return true
print(True or True) # Output: True
print(True or False) # Output: True
print(False or True) # Output: True
print(False or False) # Output: False

#if both sides of not operator are true then it will return false otherwise it will return true
print(not True) # Output: False
print(not False) # Output: True

#if both sides of xor operator are true then it will return false otherwise it will return true
print(True ^ True) # Output: False
print(True ^ False) # Output: True
print(False ^ True) # Output: True
print(False ^ False) # Output: False

# Comparison Operators
print(5 == 5) # Output: True
print(5 != 5) # Output: False
print(5 > 3) # Output: True
print(5 < 3) # Output: False
print(5 >= 5) # Output: True
print(5 <= 5) # Output: True

# Identity Operators
print(5 is 5) # Output: True
print(5 is not 5) # Output: False
print(5 is 3) # Output: False
print(5 is not 3) # Output: True
 
print(True and False or True and True) # Output: True
print(True and (False or True) and True) # Output: True

a = int("500")
b = int("500")
print(id(a)) # Output: 140736799441472
print(id(b)) # Output: 140736799441472

a = [5]
b = [5]
a == b # Output: True
a is b # Output: False
# In Python, small integers (from -5 to 256) are cached and reused, so they have the same memory address. However, larger integers and other objects like lists are not cached, so they have different memory addresses even if their contents are the same.

a = {1, 2, 3}
b = {1, 2, 3}
a == b # Output: True
a is b # Output: False
# In Python, sets are not cached, so even if two sets have the same contents, they will have different memory addresses. Therefore, a is b will return False because they are different objects in memory.

a = (1, 2, 3)
b = (1, 2, 3)
a == b # Output: True
a is b # Output: False
# In Python, tuples are not cached, so even if two tuples have the same contents, they will have different memory addresses. Therefore, a is b will return False because they are different objects in memory.

a = 5
b = "5" 
print(a == b) # Output: False
print(a is b) # Output: False

if 5 > 3 and 2 < 4:
    print("Condition is True") # Output: Condition is True
# you need 4 spaces for indentation in python to indicate that the code block belongs to the if statement. If you use less than 4 spaces, you will get an IndentationError. If you use more than 4 spaces, it will still work but it is not recommended as it can lead to confusion and inconsistency in your code.
#elif is used to check multiple conditions. It stands for "else if". You can have as many elif statements as you want, but only one else statement. The else statement is optional and it will be executed if none of the previous conditions are true.

txt = "welldone!"
print(txt[1])   # 


