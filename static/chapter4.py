# Declaration of variables
typeInt = 42
typeFloat = 69.69
typeString = "Luke... I AM YOUR FATHER!"
typeBool = True

print(typeInt, typeFloat, typeString, typeBool, sep=", ")

# Operations with number
# Artimetic operations
print(typeInt + typeFloat, typeInt - typeFloat, typeInt * typeFloat, typeInt / typeFloat, sep=", ")
# Division
print(typeInt / 10, typeInt // 10, sep=", ")
# Comparassions
print(5 == 5, 1 > 5, 12 != 21, sep=", ")

# Operations with strings
print(typeString + " NOOOOOOOOOOOOO", len(typeString), "YES" * 3, sep=", ")

# Operations with booleans
print(not typeBool, True and False, True or False, sep=", ")