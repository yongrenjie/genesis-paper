import penguins as pg
from aptenodytes import nmrd, enzip
import matplotlib.pyplot as plt
from pathlib import Path

path = nmrd() / '210916-7a-hmbc-morescans'
plt.style.use(Path(__file__).parent / 'fira.mplstyle')

expnos = [8, 7, 4001, 3001]
dss = [pg.read(path, expno) for expno in expnos]
labels = ['standard LP3',
          'standard LP2',
          'NOAH without 90',
          'NOAH with 90'
          ]
nexpts = len(expnos)

f1s = [15.2, 38.0, 74.8, 108.68, 146.7]
f2bs = ['0.50..0.84', '2.16..2.51', '3.84..4.61', '4.42..5.04', '6.44..6.83']
npeaks = len(f1s)

fig, axs = pg.subplots2d(npeaks+1, nexpts, sharey='row', figsize=(12, 10),
                         height_ratios=([1.9]+[1.0]*npeaks),
                         constrained_layout=True)
for j, ax, label, ds in enzip(axs[0], labels, dss):
    ds.stage(ax, f1_bounds="5..174", f2_bounds="0.4..6.9", levels=3.3e3)
    pg.mkplot(ax, title=label)
    ax.yaxis.set_tick_params(labelright=True)
    pg.ymove(ax)
for char, f1 in zip("bcdefghijk", f1s):   # only uses as many chars as needed
    axs[0][0].annotate(text=f"({char})", fontsize=10,
                       horizontalalignment="right",
                       verticalalignment="center",
                       xy=(-0.02, f1), xytext=(-0.15, f1),
                       xycoords=axs[0][0].get_yaxis_transform(),
                       textcoords=axs[0][0].get_yaxis_transform(),
                       arrowprops={"arrowstyle": "->"},
                       )
for i, ax_row, f1, f2b in enzip(axs[1:], f1s, f2bs):
    for j, ax, ds in enzip(ax_row, dss):
        ds.f2projp(bounds=(f1 - 0.6, f1 + 0.6)).stage(ax, bounds=f2b)
        pg.mkplot(ax, xlabel=(None if i == npeaks - 1 else ""))
        if j == 0:
            ax.text(s=f"$f_1$ = {f1:.1f} ppm", x=0.02, y=0.7, fontsize=12,
                    horizontalalignment="left", verticalalignment="top",
                    transform=ax.transAxes)

pg.label_axes([ax_row[0] for ax_row in axs], fstr="({})",
              fontweight="semibold", fontsize=14)
# pg.show()
for filetype in [".png", ".svg"]:
    pg.savefig(str(Path(__file__)).replace(".py", filetype))
