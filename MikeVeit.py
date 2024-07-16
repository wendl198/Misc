import numpy as np
import matplotlib.pyplot as plt
import os

def plot_polyfit(x_data,poly_coefficents):
    l = len(x_data)
    output = np.zeros(l)
    for i,a in enumerate(poly_coefficents[::-1]):
        for j in range(l):
            output[j] += a*x_data[j]**i 
    return output

read_path = 'C:/Users/blake/Documents/VSCode/Python/Greven/RawData/ContactedResistivity/Hg1201/'
data_paths =  os.listdir(read_path)
linear_fit = [True,False]
quad_fit = [False,True]
# data_paths = ['C:/Users/blake/Documents/VSCode/Python/Greven/RawData/MikeVeitResistivityasgrown.csv']
for i, data_path in enumerate(data_paths):
    data = np.loadtxt(read_path+data_path,delimiter=",", dtype=np.float64)
    # print(data)
    temp = data[:,0] # kelvin
    res = data[:,1] #mohm cm = 1000 micro ohm cm

    fig = plt.figure(constrained_layout = True)
    ax = fig.add_subplot(1, 1, 1)
    ind = np.logical_and(temp>77, temp<160)
    ax.scatter(temp[ind],res[ind],label = data_path[:-4])
    if linear_fit[i]:
        fit = np.polyfit(temp[ind],res[ind],1)
        ax.plot(temp[ind],plot_polyfit(temp[ind],fit),c='red',label = 'Linear Fit')
    if quad_fit[i]:
        fit = np.polyfit(temp[ind],res[ind],2)
        ax.plot(temp[ind],plot_polyfit(temp[ind],fit),c='red',label = 'Quadratic Fit')
    ax.legend()
    print(fit)
plt.show()