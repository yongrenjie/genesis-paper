import penguins as pg
from aptenodytes import nmrd
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.style.use(Path(__file__).parent / 'fira.mplstyle')

path = nmrd() / '200926-7z-n15-sehsqc-full'

bad = pg.read(path, 101003)
good = pg.read(path, 12003)
dss = [bad, good]
labels = ['4 × 1 ms HMQC gradients', '2 × 2.5 ms HMQC gradients']

fig = plt.figure(figsize=(7, 5.5), constrained_layout=True)
gs = fig.add_gridspec(2, 2, height_ratios=[0.9, 1])
axs = [fig.add_subplot(gs[0, :]),
       fig.add_subplot(gs[1, 0]),
       fig.add_subplot(gs[1, 1])]

hmqc_pulprog = plt.imread(Path(__file__).parent / "hmqc_pulprog.png")
axs[0].imshow(hmqc_pulprog, aspect='auto')
axs[0].xaxis.set_visible(False)
axs[0].yaxis.set_visible(False)
for spine in ["top", "left", "right", "bottom"]:
    axs[0].spines[spine].set_visible(False)

for ds, ax, lbl in zip(dss, axs[1:], labels):
    bounds = "1..8.5"
    ds.stage(ax, levels=1e5, f1_bounds=bounds, f2_bounds=bounds)
    pg.mkplot(ax, tight_layout=False, title=lbl)
    pg.ymove(ax, tight_layout=False)

c = pg.color_palette('bright')[3]
axs[1].add_patch(Rectangle((2, 5), width=2.5, height=1.1, fill=False, color=c))
axs[1].add_patch(Rectangle((7.14, 7.6), width=0.38, height=0.57, fill=False, color=c))
axs[1].add_patch(Rectangle((7.14, 6.55), width=0.75, height=0.33, fill=False, color=c))

pg.label_axes(axs[1:], start=4, fstr="({})", fontweight="semibold")

bbox = axs[0].get_position()
axs[0].set_position([0.03, bbox.y0+0.1, 0.95, bbox.height*0.95])
pg.label_axes(axs[0], fstr='({})', fontweight='semibold', offset=(-0.02, 0.02))
pg.label_axes(axs[0], start=2, fstr='({})', fontweight='semibold',
              offset=(0.46, 0.02))
pg.label_axes(axs[0], start=3, fstr='({})', fontweight='semibold',
              offset=(0.74, 0.02))

# pg.show()
for filetype in [".png", ".svg"]:
    pg.savefig(str(Path(__file__)).replace(".py", filetype))
