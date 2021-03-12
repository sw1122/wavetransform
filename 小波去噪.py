# coding=gbk
# 使用小波分析进行阈值去噪声,使用pywt.threshold

import pywt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = np.linspace(1, 10, 10)
print(data)
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
# pywt.threshold(data, value, mode, substitute) mode 模式有4种，soft, hard, greater, less; substitute是替换值

data_soft = pywt.threshold(data=data, value=6, mode='soft', substitute=12)
print(data_soft)
# [12. 12. 12. 12. 12.  0.  1.  2.  3.  4.] 将小于6 的值设置为12， 大于等于6 的值全部减去6

data_hard = pywt.threshold(data=data, value=6, mode='hard', substitute=12)
print(data_hard)
# [12. 12. 12. 12. 12.  6.  7.  8.  9. 10.] 将小于6 的值设置为12， 其余的值不变

data_greater = pywt.threshold(data, 6, 'greater', 12)
print(data_greater)
# [12. 12. 12. 12. 12.  6.  7.  8.  9. 10.] 将小于6 的值设置为12，大于等于阈值的值不变化

data_less = pywt.threshold(data, 6, 'less', 12)
print(data_less)
# [ 1.  2.  3.  4.  5.  6. 12. 12. 12. 12.] 将大于6 的值设置为12， 小于等于阈值的值不变
