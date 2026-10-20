# The Reflexivity Threshold

Code and synthetic simulations for [The Reflexivity Threshold: A Phase Transition for Multi-Agent Performative Prediction](https://amahrous.com/papers/reflexivity-threshold/), Ahmed Mahrous and Roberto Di Pietro, NeurIPS 2026.

## Reproduce the figures

Requires Python 3.10 or newer. From this folder:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r synthetic_simulation_artifact/requirements.txt
python synthetic_simulation_artifact/reproduce.py --clean
```

Outputs are saved in `synthetic_simulation_artifact/figures/`. The package includes the original figures, data, and seeds. Small numerical differences can occur across library versions.

## Citation

```bibtex
@inproceedings{mahrous2026reflexivity,
  title     = {The Reflexivity Threshold: A Phase Transition for Multi-Agent Performative Prediction},
  author    = {Mahrous, Ahmed and Di Pietro, Roberto},
  booktitle = {Advances in Neural Information Processing Systems},
  year      = {2026},
  note      = {Accepted paper},
  url       = {https://amahrous.com/papers/reflexivity-threshold/}
}
```

[MIT license](synthetic_simulation_artifact/LICENSE)
