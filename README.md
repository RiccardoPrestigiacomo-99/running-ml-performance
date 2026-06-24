# Running ML Performance

End-to-end machine learning project to predict 10 km race finish time from training activity data.

## Project objective

The objective of this project is to predict a runner's 10 km race finish time using the previous 3 months of training data.

The first target variable is:

`race_10k_finish_time_min`

The model will use features such as:

- weekly running volume
- monthly running volume
- average training pace
- training duration
- heart rate
- elevation gain
- training consistency

## Dataset

The first version of the project uses a realistic synthetic dataset containing:

- 100 athletes
- 13 weeks of training
- one row per activity
- one row per athlete in the modeling summary table
- athlete profiles from beginner to elite
- simulated 10 km race finish times

The dataset is synthetic because no suitable public dataset was found with all the required fields: training history, heart rate, elevation, and 10 km race outcome.

The goal of the synthetic data is to build and demonstrate the full end-to-end machine learning pipeline. Future versions can replace the synthetic data with personal running data.

## Data loading pipeline

The first reusable data pipeline has been created in:

`src/data/load_public_data.py`

This script performs the following steps:

1. Loads the synthetic activity-level dataset.
2. Loads the athlete-level summary dataset.
3. Loads the data dictionary.
4. Checks that the expected files exist.
5. Validates that required columns are present.
6. Selects the first modeling columns from the athlete summary dataset.
7. Saves a processed modeling dataset to:

`data/processed/athlete_summary_processed.csv`

The processed athlete summary dataset is the first modeling-ready table. It contains one row per athlete and the target variable:

`race_10k_finish_time_min`

The processed file is generated locally and is not committed to GitHub because `data/processed/` is ignored. This keeps the repository clean while ensuring that the dataset can be regenerated from source files.

## How to run the data loading step

From the project root, run:

`python src/data/load_public_data.py`

This command loads the sample data, validates the expected columns, and creates the first processed dataset.

Expected output:

`All required column checks passed.`

The script saves the processed athlete summary dataset to:

`data/processed/athlete_summary_processed.csv`


## Current status

Week 1 completed:

- Project repository created
- Python environment configured
- Exploration notebook created
- Synthetic 10 km dataset added
- Initial data exploration completed
- First feature and target candidates identified

Week 2 completed:

- First reusable data loading script created
- File existence checks added
- Required column validation added
- Modeling columns selected
- Processed athlete summary dataset generated