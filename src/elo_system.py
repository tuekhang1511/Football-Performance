import numpy as np
import pandas as pd
import data_prep as dp

# Load data from fbref.com
pl = pd.read_html('https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures', 
                  attrs={"id":"sched_2024-2025_9_1"})[0]

llg = pd.read_html('https://fbref.com/en/comps/12/schedule/La-Liga-Scores-and-Fixtures', 
                  attrs={"id":"sched_2024-2025_12_1"})[0]

sra = pd.read_html('https://fbref.com/en/comps/11/schedule/Serie-A-Scores-and-Fixtures', 
                  attrs={"id":"sched_2024-2025_11_1"})[0]

bdlg = pd.read_html('https://fbref.com/en/comps/20/schedule/Bundesliga-Scores-and-Fixtures', 
                  attrs={"id":"sched_2024-2025_20_1"})[0]

l1 = pd.read_html('https://fbref.com/en/comps/13/schedule/Ligue-1-Scores-and-Fixtures', 
                  attrs={"id":"sched_2024-2025_13_1"})[0]

ucl = pd.read_html('https://fbref.com/en/comps/8/schedule/Champions-League-Scores-and-Fixtures', 
                  attrs={"id":"sched_all"})[0]

# Apply the clean_data function to each league
pl_teams, pl = dp.clean_data(pl)
pl['League'] = 'Premier League'

llg_teams, llg = dp.clean_data(llg)
llg['League'] = 'La Liga'

sra_teams, sra = dp.clean_data(sra)
sra['League'] = 'Serie A'

bdlg_teams, bdlg = dp.clean_data(bdlg)
bdlg['League'] = 'Bundesliga'

l1_teams, l1 = dp.clean_data(l1)
l1['League'] = 'Ligue 1'

ucl_teams, ucl = dp.clean_data(ucl)
ucl['League'] = 'Champions League'

# Concatenate all leagues into one, sorted by Date
all_teams = np.unique(np.concatenate([pl_teams, llg_teams, sra_teams, bdlg_teams, l1_teams, ucl_teams]))

all_leagues = pd.concat([pl, llg, sra, bdlg, l1, ucl], ignore_index=True)

all_leagues = all_leagues.sort_values('Date')

all_leagues = all_leagues.reset_index(drop=True)

# Apply the clean_attendance_column function
pl = dp.clean_attendance_column(pl)
llg = dp.clean_attendance_column(llg)
sra = dp.clean_attendance_column(sra)
bdlg = dp.clean_attendance_column(bdlg)
l1 = dp.clean_attendance_column(l1)
ucl = dp.clean_attendance_column(ucl)
all_leagues = dp.clean_attendance_column(all_leagues)

# Intializing elo ratings
def intial_ratings(teams, initial_ratings=1500):
    return {team: initial_ratings for team in teams}

# Updating ratings for each match
def update_elo_match(home, away, result, league, attendance, df, ratings, home_bonus=20, k_factor=24):
    if pd.isna(attendance):
        attendance = df['Attendance'].dropna().mean()

    if league == 'Champions League':
        k_factor = 16
        
    q_home = 10 ** ((float(ratings[home]) + home_bonus * (float(attendance) / 100000)) / 400)
    q_away = 10 ** (float(ratings[away]) / 400)
    
    e_home = q_home/(q_home + q_away)
    e_away = q_away/(q_home + q_away)

    ratings[home] = ratings[home] + k_factor * (result - e_home)
    ratings[away] = ratings[away] + k_factor * ((1-result) - e_away)

# Updating ratings after all matches
def update_elo(ratings, df, home_bonus=20, k_factor=24):
    for index, row in df.iterrows():
        home = row['Home']
        away = row['Away']
        result = row['Result']
        league = row['League']
        attendance = row['Attendance']
        update_elo_match(home, away, result, league, attendance, df, ratings, home_bonus=home_bonus, k_factor=k_factor)

# Intializing elo ratings
all_ratings = intial_ratings(all_teams)
all_ratings = pd.Series(all_ratings).astype(float)

# Updating ratings
update_elo(all_ratings, all_leagues)

# Sorted version of ratings
sorted_ratings = all_ratings.sort_values(ascending=False)
print(sorted_ratings)


# Testing the accuracy when using elo to predict
threshold = 10
home_bonus = 20

matches = 0
corrects = 0
for index, row in ucl.iterrows():
    home = row['Home']
    away = row['Away']
    result = row['Result']
    if all_ratings[home] + home_bonus - all_ratings[away] > threshold:
        predict = 1
    elif all_ratings[away] - all_ratings[home] - home_bonus > threshold:
        predict = 0
    else:
        predict = 0.5

    if result == predict:
        corrects += 1
    matches += 1
    
print("Accuracy by using elo system: ", corrects / matches)

# Results distribution
print(ucl['Result'].value_counts(normalize=True))