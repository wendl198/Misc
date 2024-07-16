import numpy as np
import matplotlib.pyplot as plt


data_path = 'C:/Users/blake/Documents/VSCode/Python/Greven/RawData/HeProbe/MPMSFiles/SB107_1Aftercontacontactless.dc.dat'
data_path = 'C:/Users/blake/Documents/VSCode/Python/Greven/RawData/HeProbe/MPMSFiles/2023_8_5.dc.dat'


f = open(data_path,'r')

# Parse Header
# Skip 1 more row that what is picked out by the loop below. (In order to skip the column headings)
skip = 1

# Loop over lines to find the beginning of the data section
for line in f:
    skip += 1
    # Stop at the beginning of the Data section
    if line == "[Data]\n":
        break
    # Extract the measurement date and time
    else:
        if line[:12] == "FILEOPENTIME":
            splitLine = line.split(" ")
            timestamp = splitLine[1]

# Parse data
field, temp, moment, fit, err, dTemp = np.loadtxt(data_path, delimiter=',', skiprows=skip, usecols=(2,3,4,7,8,25), unpack=True)

f.close()

'''
old stuff
data_path = 'C:/Users/blake/Documents/VSCode/Python/Greven/RawData/BW60_ZFC_FCC_FCW_rpt.dc.dat'
# all_data = np.genfromtxt(data_path,delimiter=',')
# # t1 = np.array(all_data[1:,0])
# # field = np.array(all_data1[1:,2])

# T1 = np.array(all_data[:,3])
# ind1 = np.logical_and(T1 >= 50, T1 <= 120)
# T1 = T1[ind1]
# moment = np.array(all_data[0:,4])
# moment = (moment[ind1] - moment[ind1].max())/-moment[ind1].min()'''

inds = np.logical_and(temp>85,temp<110)

fig = plt.figure(constrained_layout = True)
ax = fig.add_subplot(1, 1, 1)
ax.scatter(temp[inds],moment[inds]/np.max(np.abs(moment[inds])),color='blue')
ax.set_ylabel(r'Magnetization (A.U.)',fontsize = 15)
ax.set_xlabel('Temperature (K)',fontsize = 15)
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)
# ax.set_title(r'SQUID Measurement of $\chi_{DC}$',fontsize = 18)
plt.show()