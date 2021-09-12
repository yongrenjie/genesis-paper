import penguins as pg
from aptenodytes import nmrd
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.patches import Rectangle

plt.style.use(Path(__file__).parent / 'fira.mplstyle')

path = nmrd() / '210909-7a-hmbc'
expnos = [4001, 3001]
dss = [pg.read(path, expno) for expno in expnos]
labels = ['without $^{13}$C 90°', 'with $^{13}$C 90°']

fig = plt.figure(figsize=(7, 5.5), constrained_layout=True)
gs = fig.add_gridspec(2, 2, height_ratios=[0.9, 1])
axs = [fig.add_subplot(gs[0, :]),
       fig.add_subplot(gs[1, 0]),
       fig.add_subplot(gs[1, 1])]

# Pulse programme (imported from Inkscape)
hmbc_pulprog = plt.imread(Path(__file__).parent / "hmbc_pulprog.png")
axs[0].imshow(hmbc_pulprog, aspect='auto')
axs[0].xaxis.set_visible(False)
axs[0].yaxis.set_visible(False)
for spine in ["top", "left", "right", "bottom"]:
    axs[0].spines[spine].set_visible(False)

# Spectra
red = pg.color_palette('bright')[3]
for ds, ax, lbl in zip(dss, axs[1:], labels):
    ds.stage(ax, levels=1300, f1_bounds="32..84", f2_bounds="3..5.2")
    ax.add_patch(Rectangle((3.84, 73.3), 0.77, 2.8, fill=False, color=red))
    ax.add_patch(Rectangle((3.70, 61.5), 0.3, 2.8, fill=False, color=red))
    pg.mkplot(ax, title=lbl, tight_layout=False)
    pg.ymove(ax, tight_layout=False)

pg.cleanup_axes()
pg.label_axes(axs[1:], start=2, fstr='({})', fontweight='semibold')
bbox = axs[0].get_position()
axs[0].set_position([0.03, bbox.y0+0.1, 0.95, bbox.height*0.95])
pg.label_axes(axs[0], fstr='({})', fontweight='semibold', offset=(-0.02, 0.02))

# pg.show()
for filetype in [".png", ".svg"]:
    pg.savefig(str(Path(__file__)).replace(".py", filetype))
