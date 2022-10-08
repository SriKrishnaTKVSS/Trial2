import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0,10,50)
plt.plot(x,np.sin(x))  # type: ignore
plt.show()