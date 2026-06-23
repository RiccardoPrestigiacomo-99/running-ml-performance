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

## Current status

Week 1 completed:

- Project repository created
- Python environment configured
- Exploration notebook created
- Synthetic 10 km dataset added
- Initial data exploration completed
- First feature and target candidates identified