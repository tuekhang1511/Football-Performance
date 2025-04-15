import numpy as np
import pandas as pd
import data_prep as dp
import time

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

uel = pd.read_html('https://fbref.com/en/comps/19/schedule/Europa-League-Scores-and-Fixtures', 
                  attrs={"id":"sched_all"})[0]

time.sleep(30)

pl1 = pd.read_html('https://fbref.com/en/comps/9/2023-2024/schedule/2023-2024-Premier-League-Scores-and-Fixtures', 
                  attrs={"id":"sched_2023-2024_9_1"})[0]

llg1 = pd.read_html('https://fbref.com/en/comps/12/2023-2024/schedule/2023-2024-La-Liga-Scores-and-Fixtures', 
                  attrs={"id":"sched_2023-2024_12_1"})[0]

sra1 = pd.read_html('https://fbref.com/en/comps/11/2023-2024/schedule/2023-2024-Serie-A-Scores-and-Fixtures', 
                  attrs={"id":"sched_2023-2024_11_1"})[0]

bdlg1 = pd.read_html('https://fbref.com/en/comps/20/2023-2024/schedule/2023-2024-Bundesliga-Scores-and-Fixtures', 
                  attrs={"id":"sched_2023-2024_20_1"})[0]

l11 = pd.read_html('https://fbref.com/en/comps/13/2023-2024/schedule/2023-2024-Ligue-1-Scores-and-Fixtures', 
                  attrs={"id":"sched_2023-2024_13_1"})[0]

ucl1 = pd.read_html('https://fbref.com/en/comps/8/2023-2024/schedule/2023-2024-Champions-League-Scores-and-Fixtures', 
                  attrs={"id":"sched_all"})[0]

uel1 = pd.read_html('https://fbref.com/en/comps/19/2023-2024/schedule/2023-2024-Europa-League-Scores-and-Fixtures', 
                  attrs={"id":"sched_all"})[0]

time.sleep(30)

pl2 = pd.read_html('https://fbref.com/en/comps/9/2022-2023/schedule/2022-2023-Premier-League-Scores-and-Fixtures', 
                  attrs={"id":"sched_2022-2023_9_1"})[0]

llg2 = pd.read_html('https://fbref.com/en/comps/12/2022-2023/schedule/2022-2023-La-Liga-Scores-and-Fixtures', 
                  attrs={"id":"sched_2022-2023_12_1"})[0]

sra2 = pd.read_html('https://fbref.com/en/comps/11/2022-2023/schedule/2022-2023-Serie-A-Scores-and-Fixtures', 
                  attrs={"id":"sched_2022-2023_11_1"})[0]

bdlg2 = pd.read_html('https://fbref.com/en/comps/20/2022-2023/schedule/2022-2023-Bundesliga-Scores-and-Fixtures', 
                  attrs={"id":"sched_2022-2023_20_1"})[0]

l12 = pd.read_html('https://fbref.com/en/comps/13/2022-2023/schedule/2022-2023-Ligue-1-Scores-and-Fixtures', 
                  attrs={"id":"sched_2022-2023_13_1"})[0]

ucl2 = pd.read_html('https://fbref.com/en/comps/8/2022-2023/schedule/2022-2023-Champions-League-Scores-and-Fixtures', 
                  attrs={"id":"sched_all"})[0]

uel2 = pd.read_html('https://fbref.com/en/comps/19/2022-2023/schedule/2022-2023-Europa-League-Scores-and-Fixtures', 
                  attrs={"id":"sched_all"})[0]

time.sleep(30)

pl3 = pd.read_html('https://fbref.com/en/comps/9/2021-2022/schedule/22021-2022-Premier-League-Scores-and-Fixtures', 
                  attrs={"id":"sched_2021-2022_9_1"})[0]

llg3 = pd.read_html('https://fbref.com/en/comps/12/2021-2022/schedule/2021-2022-La-Liga-Scores-and-Fixtures', 
                  attrs={"id":"sched_2021-2022_12_1"})[0]

sra3 = pd.read_html('https://fbref.com/en/comps/11/2021-2022/schedule/2021-2022-Serie-A-Scores-and-Fixtures', 
                  attrs={"id":"sched_2021-2022_11_1"})[0]

bdlg3 = pd.read_html('https://fbref.com/en/comps/20/2021-2022/schedule/2021-2022-Bundesliga-Scores-and-Fixtures', 
                  attrs={"id":"sched_2021-2022_20_1"})[0]

l13 = pd.read_html('https://fbref.com/en/comps/13/2021-2022/schedule/2021-2022-Ligue-1-Scores-and-Fixtures', 
                  attrs={"id":"sched_2021-2022_13_1"})[0]

ucl3 = pd.read_html('https://fbref.com/en/comps/8/2021-2022/schedule/2021-2022-Champions-League-Scores-and-Fixtures', 
                  attrs={"id":"sched_all"})[0]

uel3 = pd.read_html('https://fbref.com/en/comps/19/2021-2022/schedule/2021-2022-Europa-League-Scores-and-Fixtures', 
                  attrs={"id":"sched_all"})[0]

time.sleep(30)


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

uel_teams, uel = dp.clean_data(uel)
uel['League'] = 'Europa League'

pl1_teams, pl1 = dp.clean_data(pl1)
pl1['League'] = 'Premier League'

llg1_teams, llg1 = dp.clean_data(llg1)
llg1['League'] = 'La Liga'

sra1_teams, sra1 = dp.clean_data(sra1)
sra1['League'] = 'Serie A'

bdlg1_teams, bdlg1 = dp.clean_data(bdlg1)
bdlg1['League'] = 'Bundesliga'

l11_teams, l11 = dp.clean_data(l11)
l11['League'] = 'Ligue 1'

ucl1_teams, ucl1 = dp.clean_data(ucl1)
ucl1['League'] = 'Champions League'

uel1_teams, uel1 = dp.clean_data(uel1)
uel1['League'] = 'Europa League'

pl2_teams, pl2 = dp.clean_data(pl2)
pl2['League'] = 'Premier League'

llg2_teams, llg2 = dp.clean_data(llg2)
llg2['League'] = 'La Liga'

sra2_teams, sra2 = dp.clean_data(sra2)
sra2['League'] = 'Serie A'

bdlg2_teams, bdlg2 = dp.clean_data(bdlg2)
bdlg2['League'] = 'Bundesliga'

l12_teams, l12 = dp.clean_data(l12)
l12['League'] = 'Ligue 1'

ucl2_teams, ucl2 = dp.clean_data(ucl2)
ucl2['League'] = 'Champions League'

uel2_teams, uel2 = dp.clean_data(uel2)
uel2['League'] = 'Europa League'

pl3_teams, pl3 = dp.clean_data(pl3)
pl3['League'] = 'Premier League'

llg3_teams, llg3 = dp.clean_data(llg3)
llg3['League'] = 'La Liga'

sra3_teams, sra3 = dp.clean_data(sra3)
sra3['League'] = 'Serie A'

bdlg3_teams, bdlg3 = dp.clean_data(bdlg3)
bdlg3['League'] = 'Bundesliga'

l13_teams, l13 = dp.clean_data(l13)
l13['League'] = 'Ligue 1'

ucl3_teams, ucl3 = dp.clean_data(ucl3)
ucl3['League'] = 'Champions League'

uel3_teams, uel3 = dp.clean_data(uel3)
uel3['League'] = 'Europa League'

# Concatenate all leagues into one, sorted by Date
all_leagues = pd.concat([pl, llg, sra, bdlg, l1, ucl, uel,
                         pl1, llg1, sra1, bdlg1, l11, ucl1, uel1,
                         pl2, llg2, sra2, bdlg2, l12, ucl2, uel2,
                         pl3, llg3, sra3, bdlg3, l13, ucl3, uel3
                        ], ignore_index=True)

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

# Generating all teams
all_teams = set(all_leagues['Home']).union(all_leagues['Away'])

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