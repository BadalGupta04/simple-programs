# Practical based on Strings (Length finding, change specific character, palindrome, concatenation)

# Length finding
a = "Cloudy"
print(len(a))

# change specific character
x = a.replace("u", "x")
print(x)

# palindrome
# b = reversed(a)
if a == a[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# concatenation
y = "boiii"
z = a + " " + y
print(z)

