import penguins as pg
from aptenodytes import nmrd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.style.use(Path(__file__).parent / 'fira.mplstyle')

path = nmrd() / "201101-7g-noah-psyche"
fig = pg.figure(figsize=(7, 5.5), constrained_layout=True)
gs = fig.add_gridspec(2, 2, height_ratios=[1, 0.6])
axn = fig.add_subplot(gs[0,0])
axc = fig.add_subplot(gs[0,1])
axh = fig.add_subplot(gs[1,:])

dss = [pg.read(path, expno) for expno in [3001, 3002, 3004]]
titles = [r"$^{15}$N seHSQC", r"$^{13}$C seHSQC",
          "TSE-PSYCHE"]
dss[0].stage(ax=axn, levels=8e3, f1_bounds="111..130", f2_bounds="7..9.3")
dss[1].stage(ax=axc, levels=2e4, f1_bounds="14..65", f2_bounds="0.5..5.1")
dss[2].stage(ax=axh, bounds="1..5", color='#333333')

pg.mkplots([axn, axc, axh], titles=titles, tight_layout=False)
pg.ymove(axn, tight_layout=False)
pg.ymove(axc, tight_layout=False)
pg.cleanup_axes()

# pg.show()
for filetype in [".png", ".svg"]:
    pg.savefig(str(Path(__file__)).replace(".py", filetype))
