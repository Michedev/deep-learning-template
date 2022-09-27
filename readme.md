# Deep Learning Template

This is a template for deep learning projects based on _Pytorch, Pytorch Lightning, Poetry and Hydra_.

## How to initialize a new project

1. Clone this repository
2. Rename deep_learning_template to your project name in _pyproject.toml_ and folder name
3. Create your model and, optionally, your dataset in _{src}/model_ and _{src}/dataset_ respectively

## Install

To install the dependencies in a isolated virtualenv, run:

```bash
poetry install
```

## Train

To train the model, run the following command:

```bash
poetry run python deep_learning_template/train.py
```

or alternatively, to train single GPU:


```bash
poe train-gpu
 ```

## Project structure

    ├── data  # Data folder
    ├── deep_learning_template  # source code
    │   ├── config
    │   │   ├── dataset  # Dataset config
    │   │   ├── model  # Model config
    │   │   ├── model_dataset  # model and dataset specific config
    │   │   ├── test.yaml   # testing configuration
    │   │   └── train.yaml  # training configuration
    │   ├── dataset  # Dataset definition
    │   ├── model  # Model definition
    │   ├── utils
    │   │   ├── experiment_tools.py # Iterate over experiments
    │   │   └── paths.py  # common paths
    │   ├── train.py  # Entrypoint point for training
    │   └── test.py  # Entrypoint point for testing
    ├── pyproject.toml  # Project configuration
    ├── saved_models  # where models are saved
    └── readme.md  # This file

### Design keypoints
- Code root folder (_deep_learning_template/_) should preferably contains only entrypoint
- Add tasks to pyproject.toml via poe the poet [link](https://github.com/nat-n/poethepoet) like '_clean-empty-runs_'
