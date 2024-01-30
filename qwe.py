import math
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y1 = x
plt.title('Линейная зависимость y = x') # заголовок
plt.xlabel('x') # ось абсцисс
plt.ylabel('y') # ось ординат
plt.grid() # включение отображение сетки
plt.plot(x, y1)
plt.show()