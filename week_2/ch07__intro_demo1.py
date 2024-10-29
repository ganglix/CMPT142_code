# How to import a module
import math

print(
    math.sqrt(2),
    math.pi,
    math.sin(math.pi/2),
    math.degrees(math.pi),
    math.radians(30),
    math.sin(math.radians(30)),
    sep='\n'
)

import math as m

m.sqrt(2)


# real world engineering (my experience)
# scientific computing, matrix, array
import numpy as np
# np.sin()
arr = np.linspace(0, 10, 100)
print(arr)

# visualization
import matplotlib.pyplot as plt
plt.plot(arr, np.sin(arr), linestyle='--', color='blue')
plt.xlabel('number')
plt.ylabel('sin(x)')
plt.show()


# Things I want to mention
# import one or *all
# from math import cos
# cos(2.5)
from math import * # import all    # never recommended
cos()