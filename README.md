# Python Modules

1. Python Library and Built in Functions

2. What is pip and how do we use it

3. APIs with python

4. Built in functions help us accelerate our development of software

Modules (also called libraries)
Your code starts to get more complex with lots of functions and variables.
To make it easier to organize the code we use Modules.

import math
math.sqrt(729) —> 27

import math as m 
m.sqrt(16) —> 4

(specify exactly what to import instead of whole module)
from math import sqrt 
sqrt(121) —> 11


Create a module 
by creating a file like basic_operations.py

def add(first_num, second_num):
    return first_num + second_num
def subtract(first_num, second_num):
    return first_num - second_num
def multiply(first_num, second_num):
    return first_num * second_num
def divide(first_num, second_num):
    return first_num / second_num

import basic_operations

basic_operations.add(10,2) —> 12
basic_operations.subtract(10,2) —> 8
basic_operations.multiply(10,2) —> 20
basic_operations.divide(10,2) —>5
