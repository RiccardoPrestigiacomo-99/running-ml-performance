from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_SAMPLE_DIR = PROJECT_ROOT / "data" / "sample"
DATA_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

ACTIVITIES_FILE = DATA_SAMPLE_DIR / "running_10k_synthetic_activities.csv"
ATHLETE_SUMMARY_FILE = DATA_SAMPLE_DIR / "running_10k_synthetic_athlete_summary.csv"
DATA_DICTIONARY_FILE = DATA_SAMPLE_DIR / "running_10k_synthetic_data_dictionary.csv"


def load_activities() -> pd.DataFrame:
    """Load the synthetic activity-level running dataset."""
    activities = pd.read_csv(ACTIVITIES_FILE)
    return activities


def load_athlete_summary() -> pd.DataFrame:
    """Load the synthetic athlete-level summary dataset."""
    athlete_summary = pd.read_csv(ATHLETE_SUMMARY_FILE)
    return athlete_summary


def load_data_dictionary() -> pd.DataFrame:
    """Load the synthetic dataset data dictionary."""
    data_dictionary = pd.read_csv(DATA_DICTIONARY_FILE)
    return data_dictionary


def main() -> None:
    """Load all public/sample datasets and print basic information."""
    activities = load_activities()
    athlete_summary = load_athlete_summary()
    data_dictionary = load_data_dictionary()

    print("Activities shape:", activities.shape)
    print("Athlete summary shape:", athlete_summary.shape)
    print("Data dictionary shape:", data_dictionary.shape)


if __name__ == "__main__":
    main()