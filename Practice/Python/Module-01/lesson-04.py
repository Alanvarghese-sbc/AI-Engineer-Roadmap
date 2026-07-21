# ==========================================
# Exercise 1: Convert "25" (string) to an integer
# ==========================================
num1 = "25"
num1 = int(num1)
print("Exercise 1:", num1, type(num1))


# ==========================================
# Exercise 2: Convert 45 (int) to a float
# ==========================================
num2 = 45
num2 = float(num2)
print("Exercise 2:", num2, type(num2))


# ==========================================
# Exercise 3: Convert 99.99 (float) to an integer
# ==========================================
num3 = 99.99
num3 = int(num3)
print("Exercise 3:", num3, type(num3))


# ==========================================
# Exercise 4: Convert 100 (int) to a string
# ==========================================
num4 = 100
num4 = str(num4)
print("Exercise 4:", num4, type(num4))


# ==========================================
# Exercise 5: Print types before and after conversion
# ==========================================
print("\nExercise 5:")
num = "25"
print(type(num))
num = int(num)
print(type(num))


# ==========================================
# Exercise 6: bool() conversions
# ==========================================
print("\nExercise 6:")
print(bool(0))
print(bool(1))
print(bool(-5))
print(bool(""))
print(bool("Python"))
print(bool(None))