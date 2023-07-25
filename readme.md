# Deep Learning Template

This is a template for deep learning projects based on _Pytorch, Pytorch Lightning, conda-project and Hydra_.

## How to initialize a new project

1. Clone this repository
2. Rename deep_learning_template to your project name in _conda-project.yml_ and folder name
3. Create your model and, optionally, your dataset in _{src}/model_ and _{src}/dataset_ respectively


## Install

1. Clone the repository

```bash
git clone https://github.com/Michedev/deep-learning-template.git
```

2. Install [anaconda](https://www.anaconda.com/) if you don't have it


3. Open your terminal with the anaconda environment enabled in the project folder

4. Install dependencies


```bash
conda-project prepare
```

## Train

Train your model

```bash
conda-project run train
```

You can also specify additional arguments according to `config/train.yaml` like

```bash
conda-project run train accelerator=cpu  # train on cpu
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
    ├── conda-project.yml  # Project configuration
    ├── saved_models  # where models are saved
    └── readme.md  # This file

### Design keypoints
- Root folder should contain only entrypoint
- Add tasks to conda-project.yml via the command `conda-project add-command`


### conda-project FAQ

#### How to add a new command?
Example:
```bash
conda-project add-command generate "python ddpm_pytorch/generate.py
```
#### Mac OS support in lock file

_[Short]_ Run these commands:

```bash
conda-project remove-packages cudatoolkit;
conda-project add-platforms osx-64;
```

_[Long]_
1. Remove cudatoolkit dependency from _conda-project.yml_
```bash
conda-project remove-packages cudatoolkit
```
2. Add Mac OS platform to _conda-project-lock.yml_:
```bash
conda-project add-platforms osx-64
``` 
