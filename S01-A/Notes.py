import numpy as np
import pandas as pd
df = pd.read_csv("./test.csv")

# Conditional statements
bool = False

# Ternary operator
greeting = "hi" if bool else "hello"

if bool:
    print("Boolean est true {}".format(greeting))
else:
    print("Boolean est false {}".format(greeting))


# For loops
for i in range(0, 10, 3):
    print(i)

# While loops
num = 0
while (num < 10):
    print(num)
    num += 1
