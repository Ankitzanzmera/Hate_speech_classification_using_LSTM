from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source: Path
    local_data_filepath: Path
    unzip_dir: Path