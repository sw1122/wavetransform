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

data_list = []
a5_list = []
d1_list = []
d2_list = []
d3_list = []
d4_list = []
d5_list = []
d6_list = []

def plot_signal_decomp(data, wavelet, WAVES):
    """Decompose and plot a signal S.
    S = An + Dn + Dn-1 + ... + D1
    """
    w = pywt.Wavelet(wavelet)  # 选取小波函数
    a = data
    ca = []  # 近似分量
    cd = []  # 细节分量

    for i in range(WAVES):  # WAVES小波分解层数
        (a, d) = pywt.dwt(a, w, mode='sym')  # 进行5阶离散小波变换
        ca.append(a)
        cd.append(d)

    rec_a = []
    rec_d = []

    for i, coeff in enumerate(ca):  # enumerate(sequence, [start=0]),将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，一般用在 for 循环当中。
        coeff_list = [coeff, None] + [None] * i  #填充长度
        rec_a.append(pywt.waverec(coeff_list, w))  # 重构

    for i, coeff in enumerate(cd):
        coeff_list = [None, coeff] + [None] * i
        rec_d.append(pywt.waverec(coeff_list, w))

    data_list.append(data)
    a5_list.append(rec_a[-1])
    for i in range(1, WAVES + 1):
        globals()['d{}_list'.format(i)].append(rec_d[i - 1])

    return rec_d[0][:len(rec_d[0])] + rec_d[1][:len(rec_d[0])] + rec_d[2][:len(
        rec_d[0])]  # + rec_d[3][:len(rec_d[0])]+ rec_d[4][:len(rec_d[0])] #+ rec_d[5][:len(rec_d[0])]

def main():
    datas = pd.read_csv(SaveFile_Path + '\\' + 'pre.csv', header=0, index_col=0, encoding='gbk')
    dfNew = pd.DataFrame()
    num = datas.shape[1]
    values = datas.values
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.figure()
    i = 0

    for col in datas.columns[1:]:
        print('正在执行%s小波分解...'% col)
        cd = plot_signal_decomp(datas[col].values, 'db4', WAVES)
        dfNew[col] = cd
        plt.subplot(num, 2, 2 * i + 1)
        plt.plot(values[:, i])
        plt.title(datas.columns[i], y=0.5, loc='right')
        plt.subplot(num, 2, 2 * i + 2)
        plt.plot(cd)
        plt.title(datas.columns[i] + '__小波变换', y=0.5, loc='right')
        i += 1
    plt.show()

if __name__ == '__main__':
    main()