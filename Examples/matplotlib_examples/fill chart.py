# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2, 0.01)
# two different signals are measured
y1 = np.sin(2 * np.pi * x)
y2 = 1.2 * np.sin(4 * np.pi * x)
fig = plt.figure(1, figsize=(4, 3), dpi=300)
ax = plt.gca()
# plot and fill between y1 and y2 where a logical condition is met
ax.plot(x, y1, x, y2, color='black')
ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='darkblue', interpolate=True)
ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor='deeppink', interpolate=True)
ax.set_title('filled between')
plt.show()
