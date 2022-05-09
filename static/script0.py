import numpy as np

x = np.linspace(-2*np.pi, 100, 2*np.pi)
y = np.cos(x) / np.abs(x)
z = {"a": [1,2,3], "b": -2343.3453404, "c": "hello"}

pyscript.write("results-div", (x, y, z))