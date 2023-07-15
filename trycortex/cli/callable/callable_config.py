import dataclasses
import os
from typing import Optional

from trycortex.cli import utils

@dataclasses.dataclass
class CallableConfig(utils.DataClassYamlMixin):
    # Represents an callable.yaml config file
    name: str
    description: str = ""
    visibility: str = "private"
    template: str = "barbone"
    entry_point: str = "main:callable"

def normalize_path(path: Optional[str] = None) -> str:
    """Normalizes paths to an AgentConfig.

    Args:
        path: Optional path to either a directory or YAML file. If unspecified,
            will return "agent.yaml".
    """
    if not path:
        path = "callable.yaml"
    elif os.path.isdir(path):
        path = os.path.join(path, "callable.yaml")

    return path

def load_config(path: Optional[str] = None) -> CallableConfig:
    path = normalize_path(path)
    with open(path, "r") as fp:
        return CallableConfig.from_yaml(fp)