from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_SAMPLE_DIR = PROJECT_ROOT / "data" / "sample"
DATA_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

ACTIVITIES_FILE = DATA_SAMPLE_DIR / "running_10k_synthetic_activities.csv"
ATHLETE_SUMMARY_FILE = DATA_SAMPLE_DIR / "running_10k_synthetic_athlete_summary.csv"
DATA_DICTIONARY_FILE = DATA_SAMPLE_DIR / "running_10k_synthetic_data_dictionary.csv"


def check_file_exists(file_path: Path) -> None:
    """Raise an error if the expected data file does not exist."""
    if not file_path.exists():
        raise FileNotFoundError(f"Expected file not found: {file_path}")


def load_csv(file_path: Path) -> pd.DataFrame:
    """Load a CSV file after checking that it exists."""
    check_file_exists(file_path)
    return pd.read_csv(file_path)


def load_activities() -> pd.DataFrame:
    """Load the synthetic activity-level running dataset."""
    return load_csv(ACTIVITIES_FILE)


def load_athlete_summary() -> pd.DataFrame:
    """Load the synthetic athlete-level summary dataset."""
    return load_csv(ATHLETE_SUMMARY_FILE)


def load_data_dictionary() -> pd.DataFrame:
    """Load the synthetic dataset data dictionary."""
    return load_csv(DATA_DICTIONARY_FILE)


def print_dataset_summary(name: str, dataframe: pd.DataFrame) -> None:
    """Print basic information about a dataframe."""
    print(f"\n{name}")
    print("-" * len(name))
    print(f"Rows: {dataframe.shape[0]}")
    print(f"Columns: {dataframe.shape[1]}")
    print("Column names:")
    for column in dataframe.columns:
        print(f"  - {column}")


def main() -> None:
    """Load all public/sample datasets and print basic information."""
    activities = load_activities()
    athlete_summary = load_athlete_summary()
    data_dictionary = load_data_dictionary()

    print_dataset_summary("Activities dataset", activities)
    print_dataset_summary("Athlete summary dataset", athlete_summary)
    print_dataset_summary("Data dictionary", data_dictionary)


if __name__ == "__main__":
    main()