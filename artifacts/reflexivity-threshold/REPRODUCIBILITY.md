# Reproduction check

Checked on 20 October 2026 using Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8. The optional progress-bar package was absent; the scripts correctly ran without it. BLAS/OpenMP thread counts were set to one and Matplotlib used its noninteractive Agg backend.

The documented full reproduction command completed successfully in a separate working copy. The published original outputs were preserved.

- Iteration-complexity CSV: all 200 rows and five columns matched exactly.
- Rho-sweep CSV: 201 rows and six columns matched within a maximum absolute difference of 4.451e-6 in the stored log-distance summaries.
- Raw trajectory arrays: labels, spectral radii, time grid, and epsilon matched exactly. The maximum absolute difference in log10-distance trajectories was 8.591e-5; the mean absolute difference was 2.853e-6. This is consistent with the package's documented numerical sensitivity across eigensolver/library versions.
- Both original figure PDFs match the camera-ready manuscript figure PDFs byte for byte.
- The spectral-radius sanity checks printed by the iteration-complexity script passed.

This check verifies successful execution and agreement with the supplied numerical outputs; it does not independently validate the mathematical theorems.
