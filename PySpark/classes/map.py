from typing import List
#? Mapping funtions - Examples

numbers: List[int] = [1, 2, 3, 4, 5]
numbers_2: List[int] = [11, 21, 31, 41, 51]
square_numbers: List[int] = map(lambda x, y: y - x,numbers, numbers_2)

print(list(square_numbers))

names: List[str] = ['Juan', 'Camila', 'Vargas']
capitalized_names: List[str] = map(str.capitalize, names)

print(list(capitalized_names))


celsius_temps: List[int] = [0, 10, 20, 30, 40]
to_fahrenheit: List[int] = lambda c: c * 9/5 + 32
fahrenheit_temps = map(to_fahrenheit, celsius_temps)

print(list(fahrenheit_temps))