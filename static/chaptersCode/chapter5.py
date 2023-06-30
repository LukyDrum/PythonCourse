# Creating a list of people (strings)
people = ["Lucie", "Lukas", "Petr", "Hana"]

# Print the list and its lenght
print(people, len(people), sep=", ")

# Get the first string in the list (position 0)
person = people[0]
print(person)

# Change string at position 2
people[2] = "Josefa"
print(people, sep=", ")

# Add new string to the list
people.append("Julie")
print(people, len(people), sep=", ")

# Remove string at position 0
people.pop(0)
print(people, len(people), sep=", ")