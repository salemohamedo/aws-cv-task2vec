from setuptools import find_packages, setup
setup(
    name='aws-cv-task2vec',
    version='0.0.1',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=['torch>=1.9.0',
                      'torchvision>=0.10.0',
                      'tqdm',
                      'seaborn',
                      'scipy',
                      'matplotlib',
                      'omegaconf',
                      'fastcluster',
                      # torch
                      # torchvision
                      'numpy',
                      'pandas',
                      'hydra-core',
                      'sklearn',
                      'tqdm',
                      ]
)
