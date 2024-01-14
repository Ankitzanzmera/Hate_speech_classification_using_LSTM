from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source: Path
    local_data_filepath: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    transformed_data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    cleaned_data: Path
    tokenizer_path: Path
    model_path: Path
    X_test_path: Path
    y_test_path: Path
    MAX_LEN: int
    MAX_WORDS: int
    EPOCHS: int
    BATCH_SIZE: int
    VALIDATION_SPLIT: float
    LOSS: str
    METRICS: list
    ACTIVATION: str

@dataclass(frozen=True)
class ModelEvaluationCOnfig:
    root_dir: Path
    tokenizer_path: Path
    model_path: Path
    evaluation_file_path: Path
    X_test_path: Path
    y_test_path: Path
    MAX_LEN: int