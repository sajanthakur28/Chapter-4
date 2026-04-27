a =(1, "aaika", "vikram", 28 ,90, False,646)
print(a)
no = a.count(28)
print(no)
my_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 7)

#1. count()

# Count how many times the number 7 appears
sevens_count = my_tuple.count(7)

print(sevens_count) 
# Output: 3

#2. index()
my_tuple = ("apple", "banana", "cherry", "banana")

# Find the index of "cherry"
cherry_position = my_tuple.index("cherry")
print(cherry_position) 
# Output: 2

# Find the index of the FIRST "banana"
banana_position = my_tuple.index("banana")
print(banana_position) 
# Output: 1
print(len(my_tuple))