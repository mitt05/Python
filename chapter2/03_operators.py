# Arithmetic Operators
a = 10
b = 5

print("Addition:", a + b) #15
print("Subtraction:", a - b) #5
print("Multiplication:", a * b) #50
print("Division:", a / b) #2.0
print("Modulus:", a % b) #0
print("Floor Division:", a // b) #2
print("Exponentiation:", a ** b) #100000

#assignment Operators

x = 15

x += 5  # Equivalent to x = x + 5
print("After += :", x) #20

x -= 3  # Equivalent to x = x - 3
print("After -= :", x) #17

x *= 2  # Equivalent to x = x * 2
print("After *= :", x) #34

x /= 4  # Equivalent to x = x / 4
print("After /= :", x) #8.5

x %= 1  # Equivalent to x = x % 4 
print("After %= :", x) #0.5

x **= 2  # Equivalent to x = x ** 3
print("After **= :", x) #  0.25

x //= 2  # Equivalent to x = x // 2
print("After //= :", x) #0.0


# Comparison Operators 

p = 10
q = 20

print("Equal to:", p == q) #False
print("Not equal to:", p != q) #True
print("Greater than:", p > q) #False    
print("Less than:", p < q) #True
print("Greater than or equal to:", p >= q) #False
print("Less than or equal to:", p <= q) #True

# Logical Operators

m = True
n = False
print("Logical AND:", m and n) #False
print("Logical OR:", m or n) #True
print("Logical NOT:", not m) #False

# truth table of logical operators

# A       B       A and B    A or B     not A
# True    True    True       True       False
# True    False   False      True       False  
# False   True    False      True       True
# False   False   False      False      True     
