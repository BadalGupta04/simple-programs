# Write a Python program to check whether a specified value is contained in a group of values.
# Test Data:
# c. -> [1, 5, 8, 3]: True
# -1 -> [1, 5, 8, 3]: False

def badal(x, n):
    for num in x:
        if n == num:
            return True
    return False

print(badal([1, 5, 8, 3], 5))
print(badal([1, 5, 8, 3], -1))
