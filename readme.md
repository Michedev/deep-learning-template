# Deep Learning Template

This is a template for deep learning projects based on _Pytorch, Pytorch Lightning and Hydra_.

## How to initialize a new project

1. Clone this repository
2. Rename deep_learning_template to your project name in _pyproject.toml_ and folder name
3. Create your model and, optionally, your dataset in _{src}/model_ and _{src}/dataset_ respectively

## Project structure

    ├── data  # Data folder
    ├── deep_learning_template  # source code
    │   ├── config  # Hydra configuration files
    │   ├── dataset  # Dataset definition
    │   ├── experiment_tools.py  # Iterate over experiments
    │   ├── model  # Model definition
    │   ├── paths.py  # Paths definition
    │   └── train.py  # Training script
    ├── pyproject.toml  # Project configuration
    ├── saved_models  # where models are saved
    └── readme.md  # This file
