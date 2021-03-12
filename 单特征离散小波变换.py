import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import pywt
import matplotlib

matplotlib.rcParams['font.family']='Microsoft Yahei'  #‘font.family’ 用于显示字体的名字 font.style’ 字体风格，正常’normal’ 或斜体’italic’
matplotlib.rcParams['font.weight'] = 'bold'

SaveFile_Path = r'D:\Desktop\2018年5MW运行数据\2018年\处理后数据'  # 要读取和保存的文件路径
threshold = 0.04 # Threshold for filtering 过滤域值
WAVES = 5


def plot_signal_decomp(data, w):
    mode = pywt.Modes.smooth
    """Decompose and plot a signal S.
    S = An + Dn + Dn-1 + ... + D1 #信号重构
    """
    w = pywt.Wavelet(w)#选取小波函数
    a = data
    ca = []#近似分量
    cd = []#细节分量
    for i in range(5):
        (a, d) = pywt.dwt(a, w, mode)#进行1阶离散小波变换
        ca.append(a)
        cd.append(d)

    rec_a = []
    rec_d = []
    for i, coeff in enumerate(ca):
        coeff_list = [coeff, None] + [None] * i #填充长度
        rec_a.append(pywt.waverec(coeff_list, w))#小波重构

    for i, coeff in enumerate(cd):
        coeff_list = [None, coeff] + [None] * i
        rec_d.append(pywt.waverec(coeff_list, w))

    print(len(rec_a))
    print(len(rec_d))
    fig = plt.figure()
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.subplot(3, 1, 1)
    plt.plot(data, label='原始电价数据曲线')
    plt.legend()

    plt.subplot(3, 1,2)
    plt.plot(rec_a[-1],'r', label='电价数据曲线趋势')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(rec_d[0],'g', label='电价数据曲线噪声')
    plt.legend()
    plt.show()
datas = pd.read_csv(SaveFile_Path + '\\' + 'pre.csv', header=0, index_col=0, encoding='gbk')
values = datas.values
plot_signal_decomp(values[:, 0], 'db4')#这里选择sym5小波，小波还有

