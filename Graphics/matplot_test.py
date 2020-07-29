# https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites
# Python: Select Interpreter command from the Command Palette. /usr/local/bin/python3/

import matplotlib.pyplot as p
import numpy as n

x = n.linspace(0, 10, 100)
p.plot(x, n.sin(x))
p.show()
