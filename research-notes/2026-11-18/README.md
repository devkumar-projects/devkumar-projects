# Independent artifact reanalyses - 18 November 2026

Five author manuscripts examine the scope and reproducibility of existing engineering projects. Their origin in academic projects or an internship is explicit. No journal acceptance, new hardware experiment or proprietary TCAD execution is claimed. All named contributors are retained; scientific supervisors are acknowledged separately. Editorial and computational AI assistance is disclosed in the manuscripts.

## Reproduce on CPU

Use Python 3.12 with NumPy, SciPy and Matplotlib. The recorded run used NumPy 2.5.5 and SciPy 1.17.1; the exact versions and results are in results.json. Download only the pinned public input files and verify SHA-256:

```sh
python fetch_sources.py
python reproduce.py
```

The source downloader retrieves the original public reports and selected source files. It does not retrieve or redistribute proprietary runtimes, private data or credentials. Upstream source copyrights and licences remain applicable; downloading an original report does not grant rights to its third-party illustrations.

The calculations regenerate the five plots, results.json, rst-length-sweep.csv (221 reduced plants), and cmm-monte-carlo.csv (100 synthetic trials). They do not execute MATLAB/Simulink, dSPACE or Ecorce. CMM data in the new comparison are synthetic and explicitly parameterized.

## Manuscripts

1. RST: nominal polynomial reconstruction and frozen-controller stability samples.
2. Twin rotor: input-model normalization, integral-output selection and shifted-LQR spectrum.
3. CMM: planar nullspace, spherical-band conditioning and a declared contamination experiment.
4. Turbine: energy feasibility and separate hydraulic/air/industrial boundaries.
5. GaN: recovered lateral-deck static checks and a corrupted-contact negative control.

The texts are author versions, not peer reviewed. Preparation is not HAL acceptance. The original reports remain unchanged at their sources; these narrower methodological notes are separate works and should not be cited as a new hardware campaign.

## Rights

The new manuscript texts are copyright their named authors, all rights reserved, with authorization to disseminate through HAL. This does not relicense original source code or third-party material. Exact project authorship, source versions and report checksums are retained in each manuscript and the input manifest.
