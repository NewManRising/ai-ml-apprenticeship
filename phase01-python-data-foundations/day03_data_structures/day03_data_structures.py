#-------------------------------------------------------------------------------------------------------#
# Lists, tuples, sets, and dictionaries                                                                 #
#-------------------------------------------------------------------------------------------------------#

# mutable - lists [], sets {}, dictionaries {}, dict keys immutable
# immutable - tuples ()


# empty_list = []
# empty_list = list()

# empty_tuple = ()
# empty_tuple = tuple()

# empty_set = {} wrong, this is a dictionary
# empty_set = set() correct

#---------------------------------------------------------------------------------------------------------#

## Lists
# .append() adds value to end of list
# .insert() two arguments, adds to specified index position
# .extend() adds new values from a list to the end of the existing one
# .remove() removes string from list
# .pop() removes last string/value from list
# .reverse() changes list to reverse order
# .sort() list sorted to alphabetical/numerical order, (reverse=True) sorts list in descending order (in memory)
# .sorted() function, sorts list without affecting the list/variable in memory. Set it to a variable. Works on any iterable
# .index() finds the index of a value from a list
# .join() new_variable = ', '.join(variable) - prints string values from list separate by commas. List > string.
# .split() string is converted to a list - variable.split(', '). String > list.

# min() minimum number from a list
# max() maximum number from a list
# sum() sum of numbers from list
# enumerate() returns index and value from list - for index, variable in enumerate(list):


## Sets
# .intersection() finds values shared between 2 sets
# .difference()  finds values that are not shared between 2 sets
# .union() combines sets and prints their unique values shared between them


## Dicts
# .get() select dict key to receive value, returns none if it does not exist
# .keys() prints dict keys
# .values() prints dict values
# .items() prints keys and values
# .update({}) updates dict with new keys and values
# .pop() removes key and value from dict
# del variable['key'] - deletes key and value from dict


numbers = [2, 5, 2, 1, 7, 9, 11, 0, 5]


num_dict = {
    "len" : len(numbers),
    "total" : sum(numbers),
    "min" : min(numbers),
    "max" : max(numbers),
    "mean" : sum(numbers) / len(numbers)
}

print(num_dict)


for keys, values in num_dict.items():
    print(keys, values)


food = ["orange", "chicken", "broccoli", "olive oil"]
food_info = ("fruit", "citrus"), ("meat", "poultry"), ("veggie", "cruciferous"), ("fat", "olives")

for food, food_info in zip(food, food_info):
    print(food, food_info)


food_dict = {
    "orange" : ("fruit", "citrus"),
    "chicken" : ("meat", "poultry"),
    "broccoli" : ("veggie", "cruciferous"),
    "olive oil" : ("fat", "olives")
}

print(food_dict)

print("\nYummy foods!\n")
for food in food_dict.keys():
    print(food)


print(food_dict["broccoli"])



