from pathlib import Path

import penguins as pg
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.style.use(Path(__file__).parent / 'fira.mplstyle')
path = Path(__file__).parents[1] / 'data' / '200926-7z-n15-sehsqc-full'

bad = pg.read(path, 101001)
good = pg.read(path, 12001)
dss = [bad, good]
labels = ['4 × 1 ms HMQC PFGs', '2 × 2.5 ms HMQC PFGs']

fig, axs = pg.subplots2d(2, 2, height_ratios=[1, 0.4],
                         constrained_layout=True)

bounds = (1.5, 12)
for ds, label, ax in zip(dss, labels, axs[0]):
    ds.stage(ax, levels=2e3, f2_bounds=bounds)
    pg.mkplot(ax, title=label)
    pg.ymove(ax)
    ax.add_patch(Rectangle((7.3, 85), width=3.8, height=48, fill=False,
                           color=pg.color_palette('deep')[0], linestyle="--"))
for ds, ax in zip(dss, axs[1]):
    ds.f2projp().stage(ax, bounds=bounds, color='#333333')
    pg.mkplot(ax)
    ax.set_xlim(bounds[1], bounds[0])

for peak in (10.70, 7.77, 2.22):
    ref_integ = bad.f2projp().integrate(peak=peak, margin=0.3, mode="max")
    integ = good.f2projp().integrate(peak=peak, margin=0.3, mode="max")
    ratio = integ / ref_integ
    axs[1][1].text(x=peak - 0.1, y=integ, s=f"{ratio:.2f}×",
                   color=pg.color_palette('bright')[0], fontsize=10,
                   horizontalalignment="left", verticalalignment="top")

pg.label_axes(axs.flat, fstr="({})", fontweight="semibold")
# pg.show()
for filetype in [".png", ".svg"]:
    pg.savefig(str(Path(__file__)).replace(".py", filetype))
