import hydra
import pkg_resources
from omegaconf import DictConfig, OmegaConf
from path import Path
from pytorch_lightning.callbacks import ModelCheckpoint, EarlyStopping

from torch.utils.data import Dataset, DataLoader
import pytorch_lightning as pl
import omegaconf
import os
from deep_learning_template.utils.paths import CODE_MODEL


@hydra.main(pkg_resources.resource_filename("deep_learning_template", 'config'), 'train.yaml')
def train(config: DictConfig):
    ckpt = None
    pl.seed_everything(config.seed)
    if config.ckpt is not None:
        ckpt = Path(config.ckpt)
        assert ckpt.exists() and ckpt.isdir(), f"Checkpoint {ckpt} does not exist or is not a directory"
        config = OmegaConf.load(ckpt / 'config.yaml')
        os.chdir(ckpt.abspath())
    with open('config.yaml', 'w') as f:
        omegaconf.OmegaConf.save(config, f)
    model: pl.LightningModule = hydra.utils.instantiate(config.model)
    train_dataset: Dataset = hydra.utils.instantiate(config.dataset.train)
    val_dataset: Dataset = hydra.utils.instantiate(config.dataset.val)

    CODE_MODEL.copytree('model')  # copy source code of model under experiment directory

    model.save_hyperparameters(OmegaConf.to_object(config)['model'])  # save model hyperparameters in tb

    pin_memory = 'gpu' in config.accelerator
    train_dl = DataLoader(train_dataset, batch_size=config.batch_size, pin_memory=pin_memory)
    val_dl = DataLoader(val_dataset, batch_size=config.batch_size, pin_memory=pin_memory)
    ckpt_callback = ModelCheckpoint('./', 'best',
                                    monitor='loss/valid_loss_epoch',
                                    auto_insert_metric_name=False, save_last=True)
    callbacks = [ckpt_callback]
    if config.early_stop:
        callbacks.append(EarlyStopping('loss/valid_loss_epoch', min_delta=config.min_delta,
                                       patience=config.patience))
    trainer = pl.Trainer(callbacks=callbacks, accelerator=config.accelerator, devices=config.devices,
                         gradient_clip_val=config.gradient_clip_val,
                         gradient_clip_algorithm=config.gradient_clip_algorithm,
                         resume_from_checkpoint=ckpt)
    trainer.fit(model, train_dl, val_dl)


if __name__ == '__main__':
    train()
