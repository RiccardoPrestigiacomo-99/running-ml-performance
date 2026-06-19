# Running ML Performance

End-to-end machine learning project to predict next-week running performance from historical running activity data.

## Goal

The goal is to build a production-style ML pipeline using public running activity data first, then later adapt the same pipeline to personal running data.

## Main prediction target

Predict next-week running performance, starting with:

- next-week average pace

## Common activity schema

All data sources will be transformed into the same schema:

- activity_id
- athlete_id
- activity_date
- activity_type
- distance_km
- duration_min
- pace_min_per_km
- avg_heart_rate
- max_heart_rate
- elevation_gain_m
- calories
- source

## Project status

Week 1: project setup and public dataset exploration.