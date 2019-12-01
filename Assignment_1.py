import numpy as np
import matplotlib.pyplot as plt
def Trigo():
  x1 = np.arange(0, 2*np.pi, 0.01)
  y1 = np.sin(x1)
  y2 = np.cos(x1)
  plt.plot(x1, y1)
  plt.plot(x1, y2)
  plt.title("sin()&cos()")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.legend(["sin(x)","cos(x)"])
  plt.show()
if __name__ == "main":
  Trigo()

