import matplotlib.pyplot as plt
import pywt

# Get data:
ecg = pywt.data.ecg()  # 生成心电信号
index = []
data = []
for i in range(len(ecg)-1):
    X = float(i)
    Y = float(ecg[i])
    index.append(X)
    data.append(Y)

# Create wavelet object and define parameters
w = pywt.Wavelet('db8')  # 选用Daubechies8小波
t = w.dec_len
maxlev = pywt.dwt_max_level(len(data), w.dec_len) #计算最大有用分解级别。 dwt_max_level(data_len, filter_len) filter_len : int, str or Wavelet小波滤波器的长度。 或者，可以指定离散小波或小波对象的名称。
print("maximum level is " + str(maxlev))
threshold = 0.04  # Threshold for filtering 过滤域值

# Decompose into wavelet components, to the level selected:分解为小波分量，达到所选水平
coeffs = pywt.wavedec(data, 'db8', level=maxlev)  # 将信号进行小波分解

plt.figure()
for i in range(1, len(coeffs)):
    coeffs[i] = pywt.threshold(coeffs[i], threshold*max(coeffs[i]))  # 将噪声滤波

datarec = pywt.waverec(coeffs, 'db8')  # 将信号进行小波重构
print(type(datarec))

mintime = 0
maxtime = mintime + len(data) + 1

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(index[mintime:maxtime], data[mintime:maxtime])
plt.xlabel('time (s)')
plt.ylabel('microvolts (uV)')
plt.title("Raw signal")
plt.subplot(2, 1, 2)
plt.plot(index[mintime:maxtime], datarec[mintime:maxtime-1])
plt.xlabel('time (s)')
plt.ylabel('microvolts (uV)')
plt.title("De-noised signal using wavelet techniques")

plt.tight_layout()
plt.show()
