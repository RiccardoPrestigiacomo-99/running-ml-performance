# Synthetic 10k Race Prediction Dataset

This synthetic dataset was generated for a portfolio project called **Running ML Performance**.

It contains 100 synthetic athletes training over 13 weeks before a 10 km race. The activity-level file has one row per training activity and includes realistic relationships between training volume, pace, heart rate, elevation, and final 10 km finish time.

Files:

- `running_10k_synthetic_activities.csv`: one row per activity (4,239 rows).
- `running_10k_synthetic_athlete_summary.csv`: one row per athlete (100 rows), useful for first ML modeling.
- `running_10k_synthetic_data_dictionary.csv`: column descriptions.

Important note: this is a synthetic dataset for learning pipeline development. It should not be used to make real physiological or coaching claims.

Recommended first ML target:

- `race_10k_finish_time_min`

Recommended first modeling file:

- Start with `running_10k_synthetic_athlete_summary.csv` for a simple baseline model.
- Later use `running_10k_synthetic_activities.csv` to practice aggregation, cleaning, feature engineering, and time-aware pipeline design.
