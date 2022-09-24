from path import Path

CODE_ROOT = Path(__file__).parent
CODE_MODEL = CODE_ROOT / 'model'
ROOT = CODE_ROOT.parent
CONFIG = CODE_ROOT / 'config'
DATA = ROOT / 'data'
CONFIG_DATA = CONFIG / 'dataset'
CONFIG_MODEL = CONFIG / 'model'
CONFIG_MODEL_DATASET = CONFIG / 'model_dataset'

SAVED_MODELS = ROOT / 'saved_models'
