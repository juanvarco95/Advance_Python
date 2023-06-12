from typing import List

#* For List
#? new_list = [expression for item in iterable if condition]

numbers_1: List[int] = [1, 2, 3, 4, 5]
numbers_2: List[int] = [2, 4, 6, 8, 10]
squares: List[int] = [x**2 for x in numbers_1 if x > 3]

# print(squares)
#? Another way

for x in numbers_1:
    if x > 3:
        squares.append(x**2)   
# print(squares)

intersection: List[int] = [x for x in numbers_1 for y in numbers_2 if x == y]

print(intersection)
