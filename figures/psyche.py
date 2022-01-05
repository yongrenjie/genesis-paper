from pathlib import Path

import penguins as pg
import matplotlib.pyplot as plt
import numpy as np

plt.style.use(Path(__file__).parent / 'fira.mplstyle')

path = Path(__file__).parents[1] / 'data' / "211123-7c-psyche-sapphire"
fig = pg.figure(figsize=(7, 5.5), constrained_layout=True)
gs = fig.add_gridspec(2, 2, height_ratios=[1, 0.6])
axn = fig.add_subplot(gs[0,0])
axc = fig.add_subplot(gs[0,1])
axh = fig.add_subplot(gs[1,:])

dss = [pg.read(path, expno) for expno in [24001, 24002, 24004]]
titles = [r"$^{15}$N seHSQC", r"$^{13}$C seHSQC",
          "TSE-PSYCHE"]
dss[0].stage(ax=axn, levels=8e3, f1_bounds="115..129", f2_bounds="7.0..8.7")
dss[1].stage(ax=axc, levels=2e4, f1_bounds="6..78", f2_bounds="0.5..6")
dss[2].stage(ax=axh, bounds="0.5..8.4", color='#333333')

# Change this to true to get an inset for the PSYCHE spectrum. I decided that
# it was too much noise so didn't use it for the paper.
inset = False
if inset:
    axh_inset = pg.mkinset(ax=axh, pos=(0.08, 0.55), size=(0.4, 0.4), show_zoom=False)
    dss[2].stage(ax=axh_inset, bounds="4.7..5.8", color='#333333')
    pg.mkplot(axh_inset, xlabel="", tight_layout=False)
    axh_inset.tick_params(axis='x', labelsize=10)

pg.mkplots([axn, axc, axh], titles=titles, tight_layout=False)
pg.ymove(axn, tight_layout=False)
pg.ymove(axc, tight_layout=False)
pg.cleanup_axes()

pg.label_axes([axn, axc, axh], fstr="({})", fontweight="semibold")

# pg.show()
for filetype in [".png", ".svg"]:
    pg.savefig(str(Path(__file__)).replace(".py", filetype))
