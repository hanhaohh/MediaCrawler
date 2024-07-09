import argparse
import logging

from .crawler_util import *
from .slider_util import *
from .time_util import *
from config.base_config import LOG_LEVEL

def init_loging_config():
    level = LOG_LEVEL
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(threadName)s] %(name)s %(levelname)s (%(filename)s:%(lineno)d) - %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    _logger = logging.getLogger("MediaCrawler")
    _logger.setLevel(level)
    return _logger


logger = init_loging_config()

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
