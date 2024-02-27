import random # To assign random values
from enum import Enum
import time # to calculate the efficiency of each algorithm

class ChocolateKind(Enum): # To have specific type of chocolate
    MILK_CHOCOLATE = "Milk Chocolate"
    DARK_CHOCOLATE = "Dark Chocolate"
    WHITE_CHOCOLATE = "White Chocolate"
    ALMOND_CHOCOLATE = "Almond Chocolate"
    PENUT_BUTTER_CHOCOLATE = "Penut Butter Chocolate"


class Chocolate:
    """ A class that represents the chocolates"""

    # Constructor
    def __init__(self, chocolate_id, price, weight, kind):
        self.chocolate_id = chocolate_id
        self.price = price
        self.weight = weight
        self.kind = kind

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

chocolate_list = []  # An empty list that will represent chocolates
n = 10
start_time_creating_chocolates = time.time()

for i in range(1, n):   # A for loop that will create an object in each iteration
    chocolate_id = i  # Assign the ID numbers in order: 1,2,3,4...
    price = random.randint(1, 50)  # Assign random price from 1 to 50
    weight = random.randint(1, 10)  # Assign random weight from 1 to 10
    kind = random.choice(list(ChocolateKind))  # Assign random kind from the Enum

    chocolate_instance = Chocolate(chocolate_id, price, weight, kind)  # Create an object
    chocolate_list.append(chocolate_instance)  # Add it to the empty list

print("The chocolates: ")
# Print the chocolate objects in the list
for chocolate in chocolate_list:
    print(f"ID: {chocolate.chocolate_id}, Price: {chocolate.price}, Weight: {chocolate.weight}, Kind: {chocolate.kind}")

end_time_creating_chocolates = time.time()
time_creating_chocolates = end_time_creating_chocolates - start_time_creating_chocolates

print("-----------------------------------------------------------------")
student_list = []  # An empty list that will represent students

start_time_creating_students = time.time()
for i in range(1, n):  # Create objects of the student class
    student_name = f"student{i}"
    student_id = random.randint(10000, 20000)
    student_instance = Student(student_name, student_id)
    student_list.append(student_instance)

print("The students: ")
# Print the student objects in the list
for student in student_list:
    print(f"Student Name: {student.name}, Student ID: {student.student_id}")

end_time_creating_students = time.time()
time_creating_students = end_time_creating_students - start_time_creating_students
print("------------------------------------------------------------------")
# TASK 1
start_time_iterative = time.time()

# ITERATIVE FUNCTION
def distribute_chocolates_iterative (chocolates, students): # Creating function
    students_chocolates_dictionary = {}  # Empty dictionary
    # we will assign students as keys and chocolates as values

    if len(chocolates) == 0 or len(students) == 0:  # if one of the arguments was empty, the function will stop
        print("There is an empty list!")
        return students_chocolates_dictionary

    for student, chocolate in zip(students, chocolates):  # student goes through the elements of students' list - chocolate goes through the elements of chocolate list
        students_chocolates_dictionary.update({student: chocolate})  # update the list within each iteration


    print("Chocolates distributed to students (iteratively):")
    for student, chocolate in students_chocolates_dictionary.items():  # After creating the dictionary: print all of the items in the dictionary
       print(f"{student.name}, (ID: {student.student_id}):,"
             f"Chocolate ID: {chocolate.chocolate_id}, "
             f"Chocolate Price: {chocolate.price}, "
             f"Chocolate Weight: {chocolate.weight}, "
             f"Chocolate Kind: {chocolate.kind}")

    return students_chocolates_dictionary

student_chocolate_dict = distribute_chocolates_iterative (chocolate_list, student_list)

end_time_iterative = time.time()
time_iterative = end_time_iterative - start_time_iterative

print("---------------------------------------------------------------")
# RECURSIVE FUNCTION

start_time_recursive = time.time()
def distribute_chocolates_recursive(chocolates, students, index=0):  # Creating function

    if len(chocolates) == 0 or len(students) == 0:  # if one of the arguments was empty, the function will stop
        print("There is an empty list!")
        return

    if index < len(students):
        student = students[index]
        chocolate = chocolates[index]

        print(f"{student.name},"
              f" (ID: {student.student_id}),"
              f": Chocolate ID: {chocolate.chocolate_id},"
              f" Chocolate Price: {chocolate.price},"
              f" Chocolate Weight: {chocolate.weight},"
              f" Chocolate Kind: {chocolate.kind}")

        distribute_chocolates_recursive(chocolates, students, index + 1)

print("Chocolates distributed to students (recursively):")
distribute_chocolates_recursive(chocolate_list, student_list, 0)

end_time_recursive = time.time()
time_recursive = end_time_recursive - start_time_recursive

print("------------------------------------------------------------------")

# TASK 2

start_time_sort_price = time.time()

def merge_sort_divide_price(dict):
    if len(dict) <= 1:
        return dict

    middle = len(dict) // 2
    left_half = dict[:middle]
    right_half = dict[middle:]

    left_half = merge_sort_divide_price(left_half)
    right_half = merge_sort_divide_price(right_half)

    return merge_sort_conquer_price(left_half, right_half)

def merge_sort_conquer_price(left, right):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][1].price < right[right_index][1].price:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

student_chocolate_list = list(student_chocolate_dict.items())
sorted_chocolate_price = merge_sort_divide_price(student_chocolate_list)

print("Chocolates sorted by price:")
for student, chocolate in sorted_chocolate_price:
    print(f"{student.name} (ID: {student.student_id}): "
          f"Chocolate ID: {chocolate.chocolate_id}, "
          f"Price: {chocolate.price}, "
          f"Weight: {chocolate.weight}, "
          f"Kind: {chocolate.kind}")

print("----------------------------------------------------------------------")

end_time_sort_price = time.time()
time_sort_price = end_time_sort_price - start_time_sort_price

start_time_sort_weight = time.time()

# Sorting by weight
def merge_sort_divide_weight(dict):
    if len(dict) <= 1:
        return dict

    middle = len(dict) // 2
    left_half = dict[:middle]
    right_half = dict[middle:]

    left_half = merge_sort_divide_weight(left_half)
    right_half = merge_sort_divide_weight(right_half)

    return merge_sort_conquer_weight(left_half, right_half)

def merge_sort_conquer_weight(left, right):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][1].weight < right[right_index][1].weight:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

sorted_chocolate_weight = merge_sort_divide_weight(student_chocolate_list)


print("Chocolates sorted by weight:")
for student, chocolate in sorted_chocolate_weight:
    print(f"{student.name} (ID: {student.student_id}): "
          f"Chocolate ID: {chocolate.chocolate_id}, "
          f"Price: {chocolate.price}, "
          f"Weight: {chocolate.weight}, "
          f"Kind: {chocolate.kind}")

end_time_sort_weight = time.time()
time_sort_weight = end_time_sort_weight - start_time_sort_weight

# TASK 3
# Search by price

start_time_search_price = time.time()
def binary_search_chocolate_by_price(sorted_chocolates, target_price):
    min = 0
    max = len(sorted_chocolates) - 1

    while min <= max:
        mid = (min + max) // 2
        current_chocolate = sorted_chocolates[mid][1]

        if current_chocolate.price == target_price:
            return current_chocolate  # Found the chocolate with the target price
        elif current_chocolate.price < target_price:
            min = mid + 1  # Search in the right half
        else:
            max = mid - 1  # Search in the left half

    return None  # Chocolate with the target price not found

target_price_to_search = 25
found_chocolate_price = binary_search_chocolate_by_price(sorted_chocolate_price, target_price_to_search)
print("-----------------------------------------------------------------------------------------------")
if found_chocolate_price:
    print(f"Chocolate with price {target_price_to_search} found:")
    print(f"Chocolate ID: {found_chocolate_price.chocolate_id}, "
          f"Price: {found_chocolate_price.price}, "
          f"Weight: {found_chocolate_price.weight}, "
          f"Kind: {found_chocolate_price.kind}")
else:
    print(f"No chocolate found with price {target_price_to_search}.")

end_time_search_price = time.time()
time_search_price = end_time_search_price - start_time_search_price

# Search by weight

start_time_search_weight = time.time()
def binary_search_chocolate_by_weight(sorted_chocolates, target_weight):
    min = 0
    max = len(sorted_chocolates) - 1

    while min <= max:
        mid = (min + max) // 2
        current_chocolate = sorted_chocolates[mid][1]

        if current_chocolate.weight == target_weight:
            return current_chocolate  # Found the chocolate with the target price
        elif current_chocolate.weight < target_weight:
            min = mid + 1  # Search in the right half
        else:
            max = mid - 1  # Search in the left half

    return None  # Chocolate with the target price not found

target_weight_to_search = 6
found_chocolate_weight = binary_search_chocolate_by_weight(sorted_chocolate_weight, target_weight_to_search)
print("----------------------------------------------------------------------------------------")
if found_chocolate_weight:
    print(f"Chocolate with weight {target_weight_to_search} found:")
    print(f"Chocolate ID: {found_chocolate_weight.chocolate_id}, "
          f"Price: {found_chocolate_weight.price}, "
          f"Weight: {found_chocolate_weight.weight}, " 
          f"Kind: {found_chocolate_weight.kind}")
else:
    print(f"No chocolate found with weight {target_weight_to_search}.")

end_time_search_weight = time.time()
time_search_weight = end_time_search_weight - start_time_search_weight

print("---------------------------------------------------------------------------------------------")
print(f"Creating chocolates takes {time_creating_chocolates:.4f} seconds with {n} input.")
print(f"Creating students takes {time_creating_students:.4f} seconds with {n} input.")
print(f"Assigning chocolates to students iteratively was done in {time_iterative:.4f} seconds with {n} input.")
print(f"Assigning chocolates to students recursively was done in {time_recursive:.4f} seconds with {n} input.")
print(f"Sorting the chocolates based on price took {time_sort_price:.4f} seconds with {n} input")
print(f"Sorting the chocolates based on weight took {time_sort_weight:.4f} seconds with {n} input")
print(f"Searching for a chocolate with a specific price took {time_search_price:.4f} seconds with {n} input")
print(f"Searching for a chocolate with a specific weight took {time_search_weight:.4f} seconds with {n} input")
