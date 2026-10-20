# Synthetic Simulation Artifact

This folder documents the synthetic simulations used to generate the fixed
threshold figures in the paper.

## Scope

The artifact reproduces:

- `figures/fig_iteration_complexity.png`
- `figures/fig_iteration_complexity.pdf`
- `figures/fig_iteration_complexity.csv`
- `figures/fig_rho_sweep_five_lines.png`
- `figures/fig_rho_sweep_five_lines.pdf`
- `figures/fig_rho_sweep_five_lines.csv`
- `figures/fig_rho_sweep_five_lines.npz`

## Source Code

The released source scripts are included in this folder:

- `plot_iteration_complexity.py`
- `plot_rho_sweep_five_lines.py`
- `run_reflexivity_experiments.py`
- `generate_figures.py`

The folder also provides the documentation, dependency list, seed manifest,
license, and a convenience runner.

## Setup

From this folder's parent directory:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r synthetic_simulation_artifact/requirements.txt
```

## Reproduce the Figures

From this folder's parent directory:

```bash
python synthetic_simulation_artifact/reproduce.py --clean
```

Equivalent direct command from inside `synthetic_simulation_artifact/`:

```bash
python generate_figures.py --clean
```

The `--clean` flag removes the previous generated figure/data files before
rerunning the simulations.

## Simulation Summary

The iteration-complexity panel samples sparse nonnegative reflexivity matrices,
rescales them to target spectral radius values, and records the first iteration
at which the Perron-weighted norm falls below `1e-3`. The plotted curve is the
median over trajectories with an interquartile band.

The rho-sweep panel simulates repeated retraining at spectral radii `0.50`,
`0.99`, `1.01`, and `1.50`, plus a strongly non-normal subcritical example at
spectral radius `0.50`. Curves show the mean normalized log-distance to
equilibrium with interquartile uncertainty bands.

## Notes

Small numerical differences may occur across versions because the simulations use eigenvalue computations and random
matrix rescaling.
