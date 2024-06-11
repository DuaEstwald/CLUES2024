import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

CLUES = ['#08000C','#401F3A','#79405F','#AD517A','#BF6A4A','#D8AA80','#FFFFFF']

fig = plt.figure( figsize=(2,4) )
ax = fig.add_axes([0, 0.05, 0.25, 0.9])
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("my_colormap", CLUES)
norm = mpl.colors.Normalize(vmin=5, vmax=10)

cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                norm=norm)
fig.show()
