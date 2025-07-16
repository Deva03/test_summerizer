import os
from box.exceptions import BoxValueError
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import yaml


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns the contents as a Python object.

    Args:
        path_to_yaml (str): Path to the YAML file.

    Returns:
        ConfigBox type

    Raises:
        FileNotFoundError: If the file does not exist or its empty.
        e : empty file
    """

    try:
        with open(path_to_yaml, 'r') as file:
            content=yaml.safe_load(file)
            logger.info(f"path to yaml: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(paths: list, verbose=True):
    """
    Creates multiple directories if they do not exist.

    Args:
        paths (List[str]): List of directory paths to create.
        verbose (bool): If True, prints a message for each created directory.
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            print(f"✅ Created directory: {path}")

    
@ensure_annotations
def get_file_size(path: Path) -> str:
    """
    Returns the size of the file at the given path in kilobytes (KB).

    Args:
        path (str): Path to the file.

    Returns:
        str: File size in KB as a string, e.g., '2.45 KB'

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File not found: {path}")

    size_in_bytes = os.path.getsize(path)
    size_in_kb = round(size_in_bytes / 1024, 2)
    return f"{size_in_kb} KB"
