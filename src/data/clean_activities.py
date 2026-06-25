from pathlib import Path

import pandas as pd

from src.data.load_public_data import load_activities, load_athlete_summary


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

CLEAN_ACTIVITIES_FILE = DATA_PROCESSED_DIR / "activities_clean.csv"
CLEAN_ATHLETE_SUMMARY_FILE = DATA_PROCESSED_DIR / "athlete_summary_clean.csv"


def clean_activity_dates(activities: pd.DataFrame) -> pd.DataFrame:
    """Convert activity_date to datetime and sort activities."""
    activities = activities.copy()

    activities["activity_date"] = pd.to_datetime(activities["activity_date"])

    activities = activities.sort_values(
        ["athlete_id", "activity_date"]
    ).reset_index(drop=True)

    return activities


def clean_activities(activities: pd.DataFrame) -> pd.DataFrame:
    """Apply basic cleaning rules to the activity-level dataset."""
    activities = activities.copy()

    activities = clean_activity_dates(activities)

    return activities


def clean_athlete_summary(athlete_summary: pd.DataFrame) -> pd.DataFrame:
    """Apply basic cleaning rules to the athlete-level summary dataset."""
    athlete_summary = athlete_summary.copy()

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