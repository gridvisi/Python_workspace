'''
https://towardsdatascience.com/simulate-a-tiny-solar-system-with-python-fbbb68d8207b

https://github.com/xhinker/orbit
'''

G = 6.67e-11  # constant G
Ms = 2.0e30  # sun
Me = 5.972e24  # earth
AU = 1.5e11  # earth sun distance
daysec = 24.0 * 60 * 60  # seconds of a day
e_ap_v = 29290  # earth velocity at aphelion
gravconst_e = G * Me * Ms
# setup the starting conditions
# earth
xe, ye, ze = 1.0167 * AU, 0, 0
xve, yve, zve = 0, e_ap_v, 0
# sun
xs, ys, zs = 0, 0, 0
xvs, yvs, zvs = 0, 0, 0
t = 0.0
dt = 1 * daysec  # every frame move this time
xelist, yelist, zelist = [], [], []
xslist, yslist, zslist = [], [], []
# start simulation
while t < 1 * 365 * daysec:
    ################ earth #############
    # compute G force on earth
    rx, ry, rz = xe - xs, ye - ys, ze - zs
    modr3_e = (rx ** 2 + ry ** 2 + rz ** 2) ** 1.5
    fx_e = -gravconst_e * rx / modr3_e
    fy_e = -gravconst_e * ry / modr3_e
    fz_e = -gravconst_e * rz / modr3_e

    # update quantities how is this calculated?  F = ma -> a = F/m
    xve += fx_e * dt / Me
    yve += fy_e * dt / Me
    zve += fz_e * dt / Me

    # update position
    xe += xve * dt
    ye += yve * dt
    ze += zve * dt

    # save the position in list
    xelist.append(xe)
    yelist.append(ye)
    zelist.append(ze)

    ################ the sun ###########
    # update quantities how is this calculated?  F = ma -> a = F/m
    xvs += -fx_e * dt / Ms
    yvs += -fy_e * dt / Ms
    zvs += -fz_e * dt / Ms

    # update position
    xs += xvs * dt
    ys += yvs * dt
    zs += zvs * dt
    xslist.append(xs)
    yslist.append(ys)
    zslist.append(zs)

    # update dt
    t += dt

import matplotlib.pyplot as plt
plt.plot(xelist,yelist,'-g',lw=2)
plt.axis('equal')
plt.show()

import matplotlib.pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.grid()

line_e, = ax.plot([], [], '-g', lw=1, c='blue')
point_e, = ax.plot([AU], [0], marker="o"
                   , markersize=4
                   , markeredgecolor="blue"
                   , markerfacecolor="blue")
text_e = ax.text(AU, 0, 'Earth')

point_s, = ax.plot([0], [0], marker="o"
                   , markersize=7
                   , markeredgecolor="yellow"
                   , markerfacecolor="yellow")
text_s = ax.text(0, 0, 'Sun')

exdata, eydata = [], []  # earth track
sxdata, sydata = [], []  # sun track

print(len(xelist))


def update(i):
    exdata.append(xelist[i])
    eydata.append(yelist[i])

    line_e.set_data(exdata, eydata)
    point_e.set_data(xelist[i], yelist[i])
    text_e.set_position((xelist[i], yelist[i]))

    point_s.set_data(xslist[i], yslist[i])
    text_s.set_position((xslist[i], yslist[i]))
    ax.axis('equal')


    ax.set_xlim(-3 * AU, 3 * AU)
    ax.set_ylim(-3 * AU, 3 * AU)

    return line_e, point_s, point_e, text_e, text_s

anim = animation.FuncAnimation(fig
                               , func=update
                               , frames=len(xelist)
                               , interval=1
                               , blit=True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 18}
plt.rc('font',**font)

# initialize the stage
fig,ax = plt.subplots(figsize=(8,8))

# set x, and y axis,and remove top and right
ax.spines[['top','right']].set_visible(False)
ax.spines[['bottom','left']].set_position(('data',0.0))
ax.axis('equal')
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
ax.set_xlim(-3,10)
ax.set_ylim(-3,10)

# draw arrows
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# sun
a = np.linspace(0,2*np.pi,360)
xs = np.sin(a)
ys = np.cos(a)
ax.plot(xs,ys,c='r')
ax.text(-1,1,'sun')

# earth
xec,yec = 6,6
xe = xec+ 0.5*xs
ye = yec+ 0.5*ys
ax.plot(xe,ye,c='b')
ax.text(xec+0.5,yec+0.5,'earth')
ax.text(xec-1,yec+1.1,r"$\vec{v}$")

# r vector
ax.quiver([0,xec,xec-0.3],[0,yec,yec+0.1]
         ,[xec,-2,-3],[yec,2,-3]
         ,units='xy',scale=1,width=0.07)
ax.text(3,2,r"$\vec{r} = \vec{earth}-\vec{sun}$")
f_eq = (r"$\vec{F}=-G\frac{Mm}{|r|^2}\frac{\vec{r}}{|r|}\\$"
        r"$=-G\frac{Mm}{|r|^3}\vec{r}$")
ax.text(0.5,5.5,f_eq)

# plot data
plt.show()