# Python Modules

1. Python Library and Built in functions

2. What is pip and how do we use it

3. APIs with Python

4. Built in functions help us accelerate our development of software

<<<<<<< HEAD
Modules (also called libraries)
Your code starts to get more complex with lots of functions and variables.
To make it easier to organize the code we use Modules.
```
import math
math.sqrt(729) —> 27

import math as m 
m.sqrt(16) —> 4

(specify exactly what to import instead of whole module)
from math import sqrt 
sqrt(121) —> 11
```
- How can we create a customised method and utilise the built in functionality at the same time

- When and why should we do that

- Creating a customised method to add required information and use the functionality provided by sys module
```
def current_system_path():
    print(" this is your current directory ")
    return sys.path

print(current_system_path())
```

### What is pip?
```
- PIP is a package management system used to install and manage software packages/libraries written in Python. 
- These files are stored in a large “on-line repository” termed as Python Package Index (PyPI).
```

Package manager for Python and helps us install external packages such as requests
```
syntax: pip install name_of_the_package pip install requests
```
### 3rd Iteration

- What does requests module bring to the table
```
import requests
>>>>>>> 8dd1c8d8db28cb87f52de9c986765aa557a365b2

from emoji import emojize

live_response = requests.get("https://www.bbc.co.uk/")

def check_response_code():
    if live_response.status_code:
        print(" mission successful !!!! " + str(live_response.status_code))
        print(emojize(":thumbs_up:"))
    elif live_response.status_code == 404:
        print(" the site is unavailable until further notice please contact mobile: ")
    else:
        print("OOPs something went wrong please try later ")


check_response_code()
```
- NOTE
It will evaluate to True if the status code was between 200-400, otherwise False
