# coding=gbk
# ʹ��С������������ֵȥ����,ʹ��pywt.threshold

import pywt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

data = np.linspace(1, 10, 10)
print(data)
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
# pywt.threshold(data, value, mode, substitute) mode ģʽ��4�֣�soft, hard, greater, less; substitute���滻ֵ

data_soft = pywt.threshold(data=data, value=6, mode='soft', substitute=12)
print(data_soft)
# [12. 12. 12. 12. 12.  0.  1.  2.  3.  4.] ��С��6 ��ֵ����Ϊ12�� ���ڵ���6 ��ֵȫ����ȥ6

data_hard = pywt.threshold(data=data, value=6, mode='hard', substitute=12)
print(data_hard)
# [12. 12. 12. 12. 12.  6.  7.  8.  9. 10.] ��С��6 ��ֵ����Ϊ12�� �����ֵ����

data_greater = pywt.threshold(data, 6, 'greater', 12)
print(data_greater)
# [12. 12. 12. 12. 12.  6.  7.  8.  9. 10.] ��С��6 ��ֵ����Ϊ12�����ڵ�����ֵ��ֵ���仯

data_less = pywt.threshold(data, 6, 'less', 12)
print(data_less)
# [ 1.  2.  3.  4.  5.  6. 12. 12. 12. 12.] ������6 ��ֵ����Ϊ12�� С�ڵ�����ֵ��ֵ����
