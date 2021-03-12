import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import pywt
import matplotlib

#我们在使用matplotliblib画图的时候经常会遇见中文或者是负号无法显示的情况，pylot使用rc配置文件来自定义图形的各种默认属性，称之为rc配置或rc参数
#matplotlib.rcParams['font.size']=40  #font.size’ 字体大小，整数字号或者’large’   ‘x-small’
matplotlib.rcParams['font.family']='Microsoft Yahei'  #‘font.family’ 用于显示字体的名字 font.style’ 字体风格，正常’normal’ 或斜体’italic’
matplotlib.rcParams['font.weight'] = 'bold'

SaveFile_Path = r'D:\Desktop\2018年5MW运行数据\2018年\处理后数据'  # 要读取和保存的文件路径
threshold = 0.04 # Threshold for filtering 过滤域值

def wavetransform(col):
    df = pd.read_csv(SaveFile_Path + '\\' + 'pre.csv', header=0, index_col=0, encoding='gbk')
    values = df.values

    # Create wavelet object and define parameters
    w = pywt.Wavelet('db8')  # 选用Daubechies8小波
    t = w.dec_len
    maxlev = pywt.dwt_max_level(df.shape[0], w.dec_len) #计算最大有用分解级别。 dwt_max_level(data_len, filter_len) filter_len : int, str or Wavelet小波滤波器的长度。 或者，可以指定离散小波或小波对象的名称。
    print("maximum level is " + str(maxlev))

    # Decompose into wavelet components, to the level selected:分解为小波分量，达到所选水平
    coeffs = pywt.wavedec(values[:, col], 'db8', level=maxlev)  # 将信号进行小波分解
    for j in range(1, len(coeffs)):
        coeffs[j] = pywt.threshold(coeffs[j], threshold * max(coeffs[j]))  # 将噪声滤波
    datarec = pywt.waverec(coeffs, 'db8')  # 将信号进行小波重构
    return values, datarec

def main():
    df = pd.read_csv(SaveFile_Path + '\\' + 'pre.csv', header=0, index_col=0, encoding='gbk')
    col = df.shape[1]
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    f1 = plt.figure()

    for i in range(0, col):
        values, datarec = wavetransform(i)
        plt.subplot(col, 2, 2*i + 1)
        plt.plot(values[:, i])
        plt.title(df.columns[i], y=0.5, loc='right')
        plt.subplot(col, 2, 2*i + 2)
        plt.plot(datarec)
        plt.title(df.columns[i] + '__小波变换', y=0.5, loc='right')

    plt.show()



if __name__ == '__main__':
    main()

    # plt.figure()
    # plt.subplot(2, 1, 1)
    # plt.plot(values[:, 0])
    # plt.subplot(2, 1, 2)
    # plt.plot(datarec)
    # plt.show()

