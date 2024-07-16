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

read_path = 'C:/Users/blake/Documents/VSCode/Python/Greven/RawData/HeProbe/MPMSFiles/'
data_paths =  os.listdir(read_path)
# data_paths = ['C:/Users/blake/Documents/VSCode/Python/Greven/RawData/MikeVeitResistivityasgrown.csv']
for i, data_path in enumerate(data_paths):
    if data_path[-3:] == 'csv':
        data = np.loadtxt(read_path+data_path,delimiter=",",skiprows=1)
        # print(data)
        temp = data[:,0] # kelvin
        res = data[:,3] #mohm cm = 1000 micro ohm cm
        fig = plt.figure(constrained_layout = True)
        ax = fig.add_subplot(1, 1, 1)
        ax.set_xlabel('Temperature (K)',fontsize=15)
        ax.set_ylabel(r'$|M_3|$ (A.U.)',fontsize=15)
        ax.tick_params(axis='x', labelsize=15)
        ax.tick_params(axis='y', labelsize=15)
        ind = np.logical_and(temp>77, temp<110)
        ax.scatter(temp[ind],res[ind],label = data_path[:-4],s=6)
        # ax.legend()
        ax.set_yscale('log')
plt.show()