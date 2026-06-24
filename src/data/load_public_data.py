from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_SAMPLE_DIR = PROJECT_ROOT / "data" / "sample"
DATA_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

ACTIVITIES_FILE = DATA_SAMPLE_DIR / "running_10k_synthetic_activities.csv"
ATHLETE_SUMMARY_FILE = DATA_SAMPLE_DIR / "running_10k_synthetic_athlete_summary.csv"
DATA_DICTIONARY_FILE = DATA_SAMPLE_DIR / "running_10k_synthetic_data_dictionary.csv"

PROCESSED_ATHLETE_SUMMARY_FILE = DATA_PROCESSED_DIR / "athlete_summary_processed.csv"


REQUIRED_ACTIVITY_COLUMNS = [
    "activity_id",
    "athlete_id",
    "activity_date",
    "week_number",
    "activity_type",
    "distance_km",
    "duration_min",
    "pace_min_per_km",
    "avg_heart_rate",
    "max_heart_rate",
    "elevation_gain_m",
    "calories",
    "race_10k_finish_time_min",
]


REQUIRED_ATHLETE_SUMMARY_COLUMNS = [
    "athlete_id",
    "athlete_profile",
    "training_scenario",
    "total_3month_km",
    "avg_training_pace_min_per_km",
    "avg_heart_rate",
    "total_elevation_gain_m",
    "longest_run_km",
    "last_4w_km",
    "avg_weekly_km_last_4w",
    "active_weeks_last_4w",
    "avg_weekly_runs_last_4w",
    "race_10k_finish_time_min",
]


MODELING_COLUMNS = [
    "athlete_id",
    "athlete_profile",
    "training_scenario",
    "total_3month_km",
    "avg_training_pace_min_per_km",
    "avg_heart_rate",
    "total_elevation_gain_m",
    "longest_run_km",
    "last_4w_km",
    "avg_weekly_km_last_4w",
    "active_weeks_last_4w",
    "avg_weekly_runs_last_4w",
    "race_10k_finish_time_min",
]


def check_file_exists(file_path: Path) -> None:
    """Raise an error if the expected data file does not exist."""
    if not file_path.exists():
        raise FileNotFoundError(f"Expected file not found: {file_path}")


def load_csv(file_path: Path) -> pd.DataFrame:
    """Load a CSV file after checking that it exists."""
    check_file_exists(file_path)
    return pd.read_csv(file_path)


def validate_required_columns(
    dataframe: pd.DataFrame,
    required_columns: list[str],
    dataset_name: str,
) -> None:
    """Check that a dataframe contains all required columns."""
    missing_columns = [
        column for column in required_columns if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            f"{dataset_name} is missing required columns: {missing_columns}"
        )


def load_activities(validate: bool = True) -> pd.DataFrame:
    """Load the synthetic activity-level running dataset."""
    activities = load_csv(ACTIVITIES_FILE)

    if validate:
        validate_required_columns(
            dataframe=activities,
            required_columns=REQUIRED_ACTIVITY_COLUMNS,
            dataset_name="Activities dataset",
        )

    return activities


def load_athlete_summary(validate: bool = True) -> pd.DataFrame:
    """Load the synthetic athlete-level summary dataset."""
    athlete_summary = load_csv(ATHLETE_SUMMARY_FILE)

    if validate:
        validate_required_columns(
            dataframe=athlete_summary,
            required_columns=REQUIRED_ATHLETE_SUMMARY_COLUMNS,
            dataset_name="Athlete summary dataset",
        )

    return athlete_summary


def load_data_dictionary() -> pd.DataFrame:
    """Load the synthetic dataset data dictionary."""
    return load_csv(DATA_DICTIONARY_FILE)


def build_processed_athlete_summary(athlete_summary: pd.DataFrame) -> pd.DataFrame:
    """Select the columns needed for the first modeling dataset."""
    validate_required_columns(
        dataframe=athlete_summary,
        required_columns=MODELING_COLUMNS,
        dataset_name="Athlete summary modeling dataset",
    )

    processed = athlete_summary[MODELING_COLUMNS].copy()

    return processed


def save_dataframe(dataframe: pd.DataFrame, output_path: Path) -> None:
    """Save a dataframe to CSV, creating the parent folder if needed."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_path, index=False)


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
    """Load sample data, validate it, and save the processed modeling dataset."""
    activities = load_activities(validate=True)
    athlete_summary = load_athlete_summary(validate=True)
    data_dictionary = load_data_dictionary()

    processed_athlete_summary = build_processed_athlete_summary(athlete_summary)

    save_dataframe(
        dataframe=processed_athlete_summary,
        output_path=PROCESSED_ATHLETE_SUMMARY_FILE,
    )

    print("All required column checks passed.")

    print_dataset_summary("Activities dataset", activities)
    print_dataset_summary("Athlete summary dataset", athlete_summary)
    print_dataset_summary("Data dictionary", data_dictionary)
    print_dataset_summary("Processed athlete summary dataset", processed_athlete_summary)

    print(f"\nProcessed athlete summary saved to: {PROCESSED_ATHLETE_SUMMARY_FILE}")


if __name__ == "__main__":
    main()