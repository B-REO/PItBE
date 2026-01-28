# PItBE

[![DOI](https://zenodo.org/badge/811062694.svg)](https://zenodo.org/badge/latestdoi/811062694)

## Introduction

This Python package implements the Block-Encoding (BE) method, which allows for simulating non-unitary operators on a quantum circuit, assuming that the Hamiltonian can be expressed as a linear combination of Pauli products.

The program is designed to work in conjunction with the following quantum software frameworks:

- [OpenFermion](https://github.com/quantumlib/OpenFermion): A library for quantum chemistry simulations on quantum computers.  
- [Qulacs](https://github.com/qulacs/qulacs) (recommended): A high-speed quantum circuit simulator optimized for performance.  
- [Qiskit](https://github.com/Qiskit/qiskit): IBM's open-source quantum computing framework.

To use this package effectively, we **strongly recommend** installing one of the above platforms—preferably **Qulacs**.

Some parts of this package were developed with reference to the behavior and outputs of [PennyLane](https://github.com/PennyLaneAI/pennylane), a quantum machine learning library developed by **Xanadu**.

If you prefer the Japanese version, please refer to [this page](src/rst_files/read_me_jp.md).


## How to use
We recommend using this package by either:

- cloning the entire `PItBE` folder, or  
- cloning only the `pitbe` subfolder inside the `src` directory from the GitHub repository to your local machine.

The theoretical background of the Block-Encoding method, as well as documentation for the functions included in `pitbe`, is available on the package’s [GitHub Pages](https://b-reo.github.io/PItBE/). We highly recommend reading through this documentation before use.

You can also refer to the Jupyter notebooks in the `src/rst_files` directory. Each notebook is named after a corresponding function in `pitbe`, making it easy to find example usages and explanations.

As a practical example of how to use the package, the [GitHub Pages](https://b-reo.github.io/PItBE/) site includes a section titled **Demo Play**, which we also recommend reviewing.

> **Note:** Files and folders other than `pitbe` and `src` in this repository are not necessary for running the program and can be safely ignored.

## License
All source code in this repository, including Python scripts and Jupyter Notebooks, is licensed under the MIT License.You are free to use, modify, and distribute the code, including for commercial purposes, provided that proper attribution is given.

See [LICENSE-MIT](https://opensource.org/license/mit) for the full text.

## Finally
This program is still in an early and experimental stage, and we acknowledge that it is far from being user-friendly or polished.  
However, this also indicates its potential for further development and improvement.  
We hope you will look forward to future updates.

## Update Information
### 2025/06/20 Updated
feat: Implement `mat_maker`; updated GitHub Pages docs from `mat_make` to `mat_maker`\
fix: Corrected unitary matrix generation in `mat_make`\
feat: Add read_general `function`\
feat: Add `qiskit_circ_make` function\
fix: Resolved major `GitHub Pages` issues and republished site\

### 2025/06/25 Updated
docs: Update `How to use` section in `README`。

### 2025/06/26 Updated
docs: Add `Demo Play` usage explanation page to [Github pages](https://b-reo.github.io/PItBE/)

### 2025/06/30 Updated
docs: Add Japanese version of Block-Encoding theoretical background page on [GitHub Pages](https://b-reo.github.io/PItBE/)\
English version and explanation of PItBE to be released in future updates

### 2025/07/01 Updated
docs: Add page explaining this module `PItBE` on [Github]()

### 2025/07/07 Updated
docs: Publish English version of documentation 
docs: Replace default `README` with English version
docs: Move Japanese `README` to [here](src/rst_files/read_me_jp.md)

### 2026/01/23 Updated
README.md: Add a section describing the license

### 2026/01/26 Updated
Module `circ_make.py`: Fixed an error caused by the lack of consideration for ancilla qubits.
