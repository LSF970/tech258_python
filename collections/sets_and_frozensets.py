# Sets and Frozen Sets

# Create a set

fruits = {"apple", "banana", "cherry"}
print(fruits)

# Sets are UNORDERED and UNINDEXED

# Add an element
fruits.add("orange")
print(fruits)

# Remove an element
fruits.remove("apple")
print(fruits)

# Attempt to add a duplicate
# There can be no duplicates in a set
fruits.add("banana")
print(fruits)

# Convert list to a set to remove duplicates
example = ["one", "two", "three", "one"]
no_dupes = set(example)
print(no_dupes)

# frozen set --> IMMUTABLE SET

frozen_set = frozenset(["hello", "world"])
print(frozen_set)

# frozen_set.add("!")
# print(frozen_set)

normal_set = {"let's", "learn"}
normal_set.add(frozen_set)
print(normal_set)

