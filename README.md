###  gym_surfacecode

A surface code environment aimed at facilitating the development of decoders (decoding agents) for fault tolerant quantum computing.

The environment provided here was previously used for the development of <a href="https://github.com/R-Sweke/DeepQ-Decoding"> deepQ decoders</a> . To get started conceptually, and for an introduction to fault-tolerant quantum computing, and particularly the surface code, we highly suggest reading the associated manuscript <a href="https://arxiv.org/pdf/1810.07207.pdf">Reinforcement Learning Decoders for Fault-Tolerant Quantum Computation</a>.

Additionally, if you use this environment, or any of the code provided here, please cite the above mentioned work as follows:


    R. Sweke, M.S. Kesselring, E.P.L. van Nieuwenburg, J. Eisert,
    Reinforcement Learning Decoders for Fault-Tolerant Quantum Computation,
    arXiv:1810.07207 [quant-ph], 2018.  

<hr>

#### 0) Installation and Getting Started

This environment requires python 3, along with the additional packages:

    1. gym
    2. keras

To install the package first clone this repository, and then from the root directory run

```python
python setup.py install
```

Alternatively, this package can be installed via pip or pipenv (which is recommended).

<hr>

#### 1) Documentation

The environment provided here inherits directly from the openAI gym base class gym.env - as such, we recommend starting with the <a href="https://gym.openai.com/docs/"> openAI gym documentation </a> to familiarize yourself with the openAI gym API format.


