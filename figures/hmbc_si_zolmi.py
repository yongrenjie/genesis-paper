import penguins as pg
from aptenodytes import nmrd, enzip
import matplotlib.pyplot as plt
from pathlib import Path

path = nmrd() / '210519-7z-hmbc'
plt.style.use(Path(__file__).parent / 'fira.mplstyle')

expnos = [102, 101, 1001, 2001]
dss = [pg.read(path, expno) for expno in expnos]
labels = ['standard LP3',
          'standard LP2',
          'NOAH without 90',
          'NOAH with 90'
          ]
nexpts = len(expnos)

f1s = [45.41, 60.19, 68.57, 119.19, 123.07]
f2bs = ['2.10..2.55', '2.43..2.73', '3.86..4.40', '7.21..7.53', '6.78..7.10']
npeaks = len(f1s)

fig, axs = pg.subplots2d(npeaks+1, nexpts, sharey='row', figsize=(12, 10),
                         height_ratios=([1.9]+[1.0]*npeaks),
                         constrained_layout=True)
for j, ax, label, ds in enzip(axs[0], labels, dss):
    ds.stage(ax, f1_bounds="21..161", f2_bounds="2.0..10.95", levels=2.5e3)
    pg.mkplot(ax, title=label)
    ax.yaxis.set_tick_params(labelright=True)
    pg.ymove(ax)
for i, ax_row, f1, f2b in enzip(axs[1:], f1s, f2bs):
    for j, ax, ds in enzip(ax_row, dss):
        proj = ds.f2projp(bounds=(f1 - 0.6, f1 + 0.6))
        proj.stage(ax, bounds=f2b)
        pg.mkplot(ax, xlabel=(None if i == npeaks - 1 else ""))
        if j == 0:
            ax.text(s=f"$f_1$ = {f1:.1f} ppm", x=0.02, y=0.7, fontsize=12,
                    horizontalalignment="left", verticalalignment="top",
                    transform=ax.transAxes)
        if i == 0:
            ax.text(s="*", fontweight="semibold", x=2.275,
                    y=proj.integrate(peak=2.277, margin=0.03, mode="max")+1e4,
                    verticalalignment="center", horizontalalignment="center",
                    color=pg.color_palette('bright')[3])

pg.label_axes([ax_row[0] for ax_row in axs], fstr="({})",
              fontweight="semibold", fontsize=14)
# pg.show()
for filetype in [".png", ".svg"]:
    pg.savefig(str(Path(__file__)).replace(".py", filetype))
