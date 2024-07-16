import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

V1 = 3593.31554371
V2 = 34325.6412004
V3 = 5974.42825339
a = (10+3/8)*2.54
b =(10+3/8+13.25)*2.54
c = (10+3/8+13.25+17.25)*2.54
# print(a,b,c)
x1 = np.linspace(0,a)
x2 = np.linspace(a,b)
x3 = np.linspace(b,c)

A1 = 136.355774356
A2 = 1019.92694103

#print out 1

# fig1 = plt.figure(constrained_layout = True,figsize=((11-2),(8.5-2)))
# ax = fig1.add_subplot(1, 1, 1)
# ax.plot(x1,x1*A1/1000,c= 'black')
# ax.plot(x2,A2/1000*(x2-a)+V1/1000,c= 'black')
# ax.plot(x3,A1/1000*(x3-b)+(V1+V2)/1000,c= 'black')
# ax.set_xlabel('Depth (cm)')
# ax.set_ylabel('Liquid Helium Level (Liters)')
# ax.set_xticks(np.arange(0, 110, step=5))
# ax.set_yticks(np.arange(0, 48, step=3))
# ax.set_xlim(0,105)
# ax.set_ylim(0,45)
# ax.minorticks_on()
# ax.grid(True)
# ax.yaxis.set_minor_locator(FixedLocator(np.arange(0, 48, step=1)))
# bx = ax.twiny()
# depth = 121.5
# bx.set_xticks(np.arange(120, 15, step=-5))
# # bx.set_xticks(np.arange(-depth, -depth+110, step=5))
# bx.set_xlim(-depth,105-depth)
# bx.set_xlim(depth,-105+depth)
# bx.xaxis.set_ticks_position('top')
# bx.minorticks_on()
# # bx.xaxis.set_tick_params(which='both', direction='out')
# bx.set_xlabel('Stick Insertion Depth (cm)')


#print out 2
depth = 2.54*(45+3/8)
fig1 = plt.figure(constrained_layout = True,figsize=((11-2),(8.5-2)))
ax = fig1.add_subplot(1, 1, 1)
ax.plot(-(x1-depth)/2.54,x1*A1/1000,c= 'black')
ax.plot(-(x2-depth)/2.54,A2/1000*(x2-a)+V1/1000,c= 'black')
ax.plot(-(x3-depth)/2.54,A1/1000*(x3-b)+(V1+V2)/1000,c= 'black')
ax.set_xlabel('Stick Insertion Depth (in)')
ax.set_ylabel('Liquid Helium Level (Liters)')
ax.set_xticks(np.arange(6, 50, step=1))
ax.set_yticks(np.arange(0, 48, step=2))
ax.set_xlim(6,46)
ax.set_ylim(0,45)
ax.minorticks_on()
ax.grid(True)
ax.yaxis.set_minor_locator(FixedLocator(np.arange(0, 48, step=1)))
bx = ax.twiny()
cx = ax.twinx()

cx.set_ylabel('Liquid Helium Level (Liters)')
cx.set_yticks(np.arange(0, 48, step=2))
cx.set_ylim(0,45)

bx.set_xticks(np.arange(20, 125, step=5))
bx.set_xlim(6*2.54,46*2.54)
bx.xaxis.set_ticks_position('top')
bx.minorticks_on()
# bx.xaxis.set_tick_params(which='both', direction='out')
bx.set_xlabel('Stick Insertion Depth (cm)')
plt.show()