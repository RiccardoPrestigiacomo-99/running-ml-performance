from pathlib import Path

import pandas as pd

from src.data.load_public_data import load_activities, load_athlete_summary


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

CLEAN_ACTIVITIES_FILE = DATA_PROCESSED_DIR / "activities_clean.csv"
CLEAN_ATHLETE_SUMMARY_FILE = DATA_PROCESSED_DIR / "athlete_summary_clean.csv"


ACTIVITY_NUMERIC_COLUMNS = [
    "distance_km",
    "duration_min",
    "pace_min_per_km",
    "avg_heart_rate",
    "max_heart_rate",
    "elevation_gain_m",
    "calories",
]


ATHLETE_SUMMARY_NUMERIC_COLUMNS = [
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


def clean_activity_dates(activities: pd.DataFrame) -> pd.DataFrame:
    """Convert activity_date to datetime, remove invalid dates, and sort rows."""
    activities = activities.copy()

    activities["activity_date"] = pd.to_datetime(
        activities["activity_date"],
        errors="coerce",
    )

    invalid_dates_count = activities["activity_date"].isna().sum()

    if invalid_dates_count > 0:
        print(f"Removing {invalid_dates_count} activities with invalid dates.")

    activities = activities.dropna(subset=["activity_date"])

    activities = activities.sort_values(
        ["athlete_id", "activity_date", "activity_id"]
    ).reset_index(drop=True)

    return activities


def convert_numeric_columns(
    dataframe: pd.DataFrame,
    numeric_columns: list[str],
) -> pd.DataFrame:
    """Convert selected columns to numeric values."""
    dataframe = dataframe.copy()

    for column in numeric_columns:
        dataframe[column] = pd.to_numeric(dataframe[column], errors="coerce")

    return dataframe


def remove_invalid_activity_values(activities: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with impossible or invalid activity values."""
    activities = activities.copy()

    initial_rows = len(activities)

    activities = activities[
        (activities["distance_km"] > 0)
        & (activities["duration_min"] > 0)
        & (activities["pace_min_per_km"] > 0)
        & (activities["avg_heart_rate"] > 0)
        & (activities["max_heart_rate"] > 0)
        & (activities["elevation_gain_m"] >= 0)
        & (activities["calories"] > 0)
    ]

    removed_rows = initial_rows - len(activities)

    if removed_rows > 0:
        print(f"Removed {removed_rows} activities with invalid numeric values.")

    return activities.reset_index(drop=True)


def validate_activity_ranges(activities: pd.DataFrame) -> None:
    """Print warnings for suspicious but not necessarily impossible values."""
    checks = {
        "very_long_distance": activities["distance_km"] > 50,
        "very_long_duration": activities["duration_min"] > 300,
        "very_fast_pace": activities["pace_min_per_km"] < 2.5,
        "very_slow_pace": activities["pace_min_per_km"] > 10,
        "very_low_hr": activities["avg_heart_rate"] < 80,
        "very_high_hr": activities["avg_heart_rate"] > 210,
    }

    for check_name, condition in checks.items():
        count = condition.sum()
        if count > 0:
            print(f"Warning: {count} rows detected for check: {check_name}")


def clean_activities(activities: pd.DataFrame) -> pd.DataFrame:
    """Apply basic cleaning rules to the activity-level dataset."""
    activities = activities.copy()

    activities = clean_activity_dates(activities)
    activities = convert_numeric_columns(activities, ACTIVITY_NUMERIC_COLUMNS)
    activities = remove_invalid_activity_values(activities)
    validate_activity_ranges(activities)

    return activities


def clean_athlete_summary(athlete_summary: pd.DataFrame) -> pd.DataFrame:
    """Apply basic cleaning rules to the athlete-level summary dataset."""
    athlete_summary = athlete_summary.copy()

    athlete_summary = convert_numeric_columns(
        dataframe=athlete_summary,
        numeric_columns=ATHLETE_SUMMARY_NUMERIC_COLUMNS,
    )

    athlete_summary = athlete_summary.dropna(
        subset=["race_10k_finish_time_min"]
    ).reset_index(drop=True)

    return athlete_summary


def save_dataframe(dataframe: pd.DataFrame, output_path: Path) -> None:
    """Save a dataframe to CSV, creating the parent folder if needed."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_path, index=False)


def main() -> None:
    """Load raw sample data, clean it, and save cleaned outputs."""
    activities = load_activities(validate=True)
    athlete_summary = load_athlete_summary(validate=True)

    activities_clean = clean_activities(activities)
    athlete_summary_clean = clean_athlete_summary(athlete_summary)

    save_dataframe(activities_clean, CLEAN_ACTIVITIES_FILE)
    save_dataframe(athlete_summary_clean, CLEAN_ATHLETE_SUMMARY_FILE)

    print("Cleaned activities shape:", activities_clean.shape)
    print("Cleaned athlete summary shape:", athlete_summary_clean.shape)
    print(f"Saved cleaned activities to: {CLEAN_ACTIVITIES_FILE}")
    print(f"Saved cleaned athlete summary to: {CLEAN_ATHLETE_SUMMARY_FILE}")


if __name__ == "__main__":
    main()