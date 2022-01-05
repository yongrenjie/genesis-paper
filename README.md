# genesis-paper

Source code for the publication accompanying the GENESIS website.
You can find the paper itself at LINK, or if you don't have access to that, the `genesis.pdf` file in this repository (LINK) has essentially identical content.
This repository also hosts the necessary code for generating all the figures, which in requires all the raw data.

## Raw data

Since the raw data is quite large (875 MB before compression), it's not in the repository itself.
You can download a compressed version either from Zenodo (LINK), or from a GitHub release (LINK).

## Figures

The `figures` directory in this repository contains all the original code used to generate the figures for the publication.

To recreate the figures, follow these steps:

 1. Clone this repository.

 2. Download the raw data and extract it. Place the entire `data` directory inside the `genesis` folder which you cloned this repository to.

 3. Install the specific version of the [`penguins` package](https://github.com/yongrenjie/penguins), which was released specifically for this paper. You need at least Python 3.7 for this.

        python -m pip install penguins==0.5.0

 4. Run any of the scripts to generate the appropriate figure. You have to figure out which script corresponds to which figure (or look at the LaTeX sources to be sure), but it honestly shouldn't be too difficult.

## Problems? Questions?

Let me know by opening an issue.