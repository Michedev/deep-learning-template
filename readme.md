# Deep Learning Template

This is a template for deep learning projects based on _Pytorch, Pytorch Lightning and Hydra_.

## How to initialize a new project

1. Clone this repository
2. Rename deep_learning_template to your project name in _conda-project.yml_ and folder name
3. Create your model and, optionally, your dataset in _{src}/model_ and _{src}/dataset_ respectively


## Install

1. Clone the repository

```bash
git clone https://github.com/Michedev/deep-learning-template.git
```

1. Install hatch `pip install hatch` if you don't have it


2. Open your terminal in the project folder

3. Install dependencies


```bash
hatch env create
```
This install the default environment which uses torch with gpu support. If you want to use cpu instead, run

```bash
hatch env create cpu
```

## Train

Train your model

```bash
hatch run train
```


You can also specify additional arguments according to `config/train.yaml` like

```bash
hatch run train batch_size=64
```
To run commands from a different environment, add the environment name before the command, e.g.

```bash
hatch run cpu:train
```

## Project structure

    ├── data  # Data storage folder
    ├── config
    │   ├── dataset  # Dataset config
    │   ├── model  # Model config
    │   ├── model_dataset  # (model, dataset) specific config
    │   ├── test.yaml   # test configuration
    │   └── train.yaml  # train configuration
    ├── dataset  # Dataset definition
    ├── model  # Model definition
    ├── utils
    │   ├── experiment_tools.py # Iterate over experiments
    │   └── paths.py  # common paths
    ├── train.py  # Entrypoint point for training
    ├── test.py  # Entrypoint point for testing
    ├── pyproject.toml # Project configuration
    ├── saved_models  # where models are saved
    └── readme.md  # This file

### Design keypoints
- Root folder should contain only entrypoint
- All hyperparameters should be under config/
- All paths should be stored in utils/paths.py
