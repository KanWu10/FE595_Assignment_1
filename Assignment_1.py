import numpy as np
import matplotlib.pyplot as plt
x1 = np.arange(0, 2*np.pi, 0.01)
y1 = np.sin(x1)
y2 = np.cos(x1)
y3 = np.tan(x1)
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.plot(x1, y3)
plt.title("Plot of trigonometric function")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["sin(x)","cos(x)","tan(x)"])
plt.show()
