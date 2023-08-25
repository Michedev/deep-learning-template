from typing import Iterator, Tuple
from path import Path
from utils.paths import SAVED_MODELS
from omegaconf import DictConfig, OmegaConf
import pytorch_lightning as pl
import hydra
import curses


def iter_experiments() -> Iterator[Tuple[Path, DictConfig]]:
    """
    Iterate over all saved experiments and their corresponding configuration files.

    Returns:
        Iterator[Tuple[Path, DictConfig]]: A tuple containing the experiment path and its configuration.
    """
    for experiment in SAVED_MODELS.dirs():
        config_path = experiment / 'config.yaml'
        config = OmegaConf.load(config_path)
        yield experiment, config


def iter_experiments_with_checkpoint() -> Iterator[Tuple[Path, DictConfig, pl.LightningModule]]:
    """
    Iterate over all saved experiments that have a checkpoint and their corresponding configuration files and models.

    Returns:
        Iterator[Tuple[Path, DictConfig, pl.LightningModule]]: A tuple containing the experiment path, its configuration, and the loaded model from 'best.ckpt'.
    """
    for experiment_path, config in iter_experiments():
        model = hydra.utils.instantiate(config.model)
        model.load_from_checkpoint(experiment_path / 'best.ckpt')
        yield experiment_path, config, model


def iter_experiments_containing_ckpts() -> Iterator[Path]:
    """
    Iterate over all saved experiments that have a checkpoint with name 'best.ckpt'.

    Returns:
        Iterator[Path]: A path to the experiment folder that contains a checkpoint.
    """
    for folder in SAVED_MODELS.dirs():
        if 'best.ckpt' in folder.files():
            yield folder


def select_run() -> Path:
    """
    Display a list of saved experiments that have a checkpoint and allow the user to select one.

    Returns:
        Path: The path to the selected experiment folder.
    """
    runs_list = list(iter_experiments_containing_ckpts())
    items = [run.basename for run in runs_list]
    idx = curses.wrapper(_select_item, items, 0)
    return runs_list[idx]


def _select_item(stdscr, items, selected_item):
    """
    Display a list of items and allow the user to select one.

    Args:
        stdscr: The curses screen object.
        items: A list of items to display.
        selected_item: The index of the currently selected item.

    Returns:
        int: The index of the selected item.
    """
    # Initialize curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.keypad(1)

    while True:
        # Clear the screen
        stdscr.clear()

        # Display the list of items
        for i, item in enumerate(items):
            if i == selected_item:
                stdscr.addstr(f"> {item}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(f"  {item}\n")

        # Get user input
        key = stdscr.getch()

        # Process user input
        if key == curses.KEY_UP:
            selected_item = (selected_item - 1) % len(items)
        elif key == curses.KEY_DOWN:
            selected_item = (selected_item + 1) % len(items)
        elif key == ord('\n'):
            break

        # Refresh the screen
        stdscr.refresh()

    # Clean up curses
    curses.curs_set(1)
    stdscr.nodelay(0)
    stdscr.keypad(0)

    return selected_item
