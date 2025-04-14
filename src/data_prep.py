import numpy as np
import pandas as pd

# Cleaning data function
def clean_data(df):
    df = df.copy()
    # Drop rows with missing scores
    df.dropna(subset=['Score'], inplace=True)
    df = df[~df['Score'].str.contains('\(', na=False)]
    
    df = df[['Date', 'Home', 'Score', 'Away', 'Attendance']]

    # Remove country codes from team names
    df['Home'] = df['Home'].str.replace(r'(\s+[a-z]{2,3})$|\b[a-z]{2,3}\s+', '', regex=True)
    df['Away'] = df['Away'].str.replace(r'(\s+[a-z]{2,3})$|\b[a-z]{2,3}\s+', '', regex=True)
    
    # Split the scores and handle potential issues
    df[['HomeGoals', 'AwayGoals']] = df['Score'].str.split('–', expand=True)

    # Convert to numeric first to handle any remaining invalid formats
    df['HomeGoals'] = pd.to_numeric(df['HomeGoals'], errors='coerce')
    df['AwayGoals'] = pd.to_numeric(df['AwayGoals'], errors='coerce')
    
    # Drop rows with NaN goals after conversion
    df.dropna(subset=['HomeGoals', 'AwayGoals'], inplace=True)
    
    # Now it's safe to convert to int
    df['HomeGoals'] = df['HomeGoals'].astype(int)
    df['AwayGoals'] = df['AwayGoals'].astype(int)
    
    # Calculate results
    df['Result'] = df.apply(
        lambda row: 1 if row['HomeGoals'] > row['AwayGoals']
        else (0 if row['HomeGoals'] < row['AwayGoals'] else 0.5),
        axis=1
    )
    
    # Get unique teams
    teams = df['Home'].unique()
    return teams, df



# I created this function because I had some bugs when using the attendance attribute
def clean_attendance_column(df):
    # Turn everything into a string, strip non‑digits, empty → NaN, then float
    df['Attendance'] = (
        df['Attendance']
          .astype(str)
          .str.replace(r'[^0-9]', '', regex=True)  # keep only 0–9
          .replace('', np.nan)                      # blanks → NaN
          .astype(float)                            # cast to float
    )
    return df



