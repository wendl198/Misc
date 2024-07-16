import numpy as np
import matplotlib.pyplot as plt
import os

read_path = 'C:/Users/blake/Documents/VSCode/Python/Greven/RawData/ContactedResistivity/STO'
#sample is 2.1mm by 2.1mm
data_paths =  os.listdir(read_path)
for data_path in data_paths:
    filename = read_path+'/'+data_path
    f = open(filename,'r')
    

    # Parse Header
    # Skip 1 more row that what is picked out by the loop below. (In order to skip the column headings)
    skip = 1

    # Loop over lines to find the beginning of the data section
    break_next = False
    for line in f:
        if break_next:
            print(line)
            headers = line.split(',')
            break
        skip += 1
        # Stop at the beginning of the Data section
        if line == "[Data]\n":
            break_next = True
        # Extract the measurement date and time
        else:
            if line[:12] == "FILEOPENTIME":
                splitLine = line.split(" ")
                timestamp = splitLine[1]

    for i, header in enumerate(headers):
        new = header.replace(' ','_').strip()
        # print(new)
        output = ''
        had = False
        for j in range(len(new)-1):
            if new[j+1] == '(':
                had = True
                break
            else:
                output += new[j]
                print(new[j])
        if had:
            headers[i] = output
        else:
            headers[i] = new


    print(headers)
    # Comment,Time Stamp (sec),Status (code),Temperature (K),Magnetic Field (Oe),Sample Position (deg),Bridge 1 Resistivity (Ohm-m),Bridge 1 Excitation (uA),Bridge 2 Resistivity (Ohm-m),Bridge 2 Excitation (uA),Bridge 3 Resistivity (Ohm-m),Bridge 3 Excitation (uA),Bridge 4 Resistivity (Ohm-m),Bridge 4 Excitation (uA),Bridge 1 Std. Dev. (Ohm-m),Bridge 2 Std. Dev. (Ohm-m),Bridge 3 Std. Dev. (Ohm-m),Bridge 4 Std. Dev. (Ohm-m),Number of Readings,Bridge 1 Resistance (Ohms),Bridge 2 Resistance (Ohms),Bridge 3 Resistance (Ohms),Bridge 4 Resistance (Ohms)
    # time, temp, field, 
    
    # field, temp, moment, fit, err, dTemp = np.loadtxt(filename, delimiter=',', skiprows=skip, usecols=(2,3,4,7,8,25), unpack=True)
    print(np.loadtxt(filename, delimiter=',', skiprows=skip,dtype=str))
    included = []
    for i, col in enumerate(np.loadtxt(filename, delimiter=',', skiprows=skip,dtype=str)[0]):
        if col != '':
            included.append(i)
    included_headers = []
    for i in included:
        included_headers.append(headers[i])
    for index, item in enumerate(included_headers):
        print(f"{item}: {index}")    
    # print(included_headers)
    # print(np.loadtxt(filename, delimiter=',', skiprows=skip, usecols=included))
    input_str = input('Rows to include (separate indices with ,): ')  
    inds = input_str.split(',')
    output = []
    for i in inds:
        output.append(included[int(i)])
    print(output)
    temp,resistiance = np.loadtxt(filename, delimiter=',', skiprows=skip, usecols=output, unpack=True)
    f.close()


    fig4 = plt.figure(constrained_layout = True)
    ax1 = fig4.add_subplot(1, 1, 1)
    ax1.set_ylabel(r'Resistance $\Omega$')
    ax1.set_xlabel('Temperature (K)')
    ax1.scatter(temp,resistiance)
plt.show()