# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

plt.figure(1, figsize=(10, 8), dpi=300)
# generate x values
x = np.random.randn(1000)
# random measurements, no correlation
y1 = np.random.randn(len(x))
# strong correlation
y2 = 1.2 + np.exp(x)
ax1 = plt.subplot(121)
plt.scatter(x, y1, color='indigo', alpha=0.3, edgecolors='white', label='no correl')
plt.xlabel('no correlation')
plt.grid(True)
plt.legend()
ax2 = plt.subplot(122, sharey=ax1, sharex=ax1)
plt.scatter(x, y2, color='green', alpha=0.3, edgecolors='grey', label='correl')
plt.xlabel('strong correlation')
plt.grid(True)
# 显示图例
plt.legend()
plt.show()
