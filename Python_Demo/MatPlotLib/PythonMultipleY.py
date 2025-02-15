﻿import numpy as np
import matplotlib.pyplot as plt

# from 0 to 5 step by 0,2
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
