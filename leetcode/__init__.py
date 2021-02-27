from typing import Dict, List, Tuple  # noqa

from .convert import main  # noqa
from .etc.imported import *  # noqa
from .etc.list_node import *  # noqa
from .etc.tree_node import *  # noqa

null = None  # noqa

try:
    import pkg_resources

    __version__ = pkg_resources.get_distribution(__package__).version
except pkg_resources.DistributionNotFound:
    __version__ = "Unknown"
