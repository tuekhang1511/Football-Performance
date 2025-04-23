import pandas as pd
from unidecode import unidecode

# Load the player database
player_df = pd.read_csv('/kaggle/input/queryx/query.csv')

# Remove accents from 'playerLabel' and create a dictionary
player_df['playerLabel_normalized'] = player_df['playerLabel'].apply(unidecode).str.lower()
PLAYER_DATABASE = dict(zip(player_df['playerLabel_normalized'], player_df['fbrefID']))

def get_player_stats(player_name):
    """Get player stats using pre-defined IDs."""
    # Normalize and convert to lowercase
    player_name_normalized = unidecode(player_name).lower().strip()
    
    if player_name_normalized in PLAYER_DATABASE:
        player_id = PLAYER_DATABASE[player_name_normalized]
        formatted_name = '-'.join(player_name.split())
        
        # Construct URL
        scout_url = f"https://fbref.com/en/players/{player_id}/scout/365_m1/{formatted_name}-Scouting-Report"
        
        # Try with different position IDs
        for position in ["FW", "AM", "MF", "DF", "CB", "GK"]:
            try:
                table_id = f"scout_full_{position}"
                stats_df = pd.read_html(scout_url, attrs={"id": table_id})[0]
                return stats_df, position
            except:
                continue
            
        # Fallback to reading any table
        stats_df = pd.read_html(scout_url)[0]
        # stats_df = stats_df.dropna(subset=['Statistic'])
        return stats_df, position
            
    else:
        return f"Player '{player_name}' not in database. Please check spelling or add this player to the database."
        

def get_player_match_logs_24_25(player_name):
    """Get player stats using pre-defined IDs."""
    # Normalize and convert to lowercase
    player_name_normalized = unidecode(player_name).lower().strip()
    
    if player_name_normalized in PLAYER_DATABASE:
        player_id = PLAYER_DATABASE[player_name_normalized]
        formatted_name = '-'.join(player_name.split())
        
        # Construct URL
        match_logs_url = f"https://fbref.com/en/players/{player_id}/matchlogs/2024-2025/{formatted_name}-Match-Logs"
        
        try:
            table_id = "matchlogs_all"
            stats_df = pd.read_html(match_logs_url, attrs={"id": table_id})[0]
            stats_df.columns = ['_'.join(col).strip() for col in stats_df.columns.values]
            
            # # Fallback to reading any table
            # stats_df = pd.read_html(match_logs_url)[0]
            return stats_df
            
        except Exception as e:
            return f"Error fetching stats: {e}"
    else:
        return f"Player '{player_name}' not in database. Please check spelling or add this player to the database."
        

def extract_each_feature(stat_name):
    rows = player_stats[player_stats.iloc[:, 0] == stat_name].index.tolist()
    feature = player_stats.iloc[rows[0], 1:3].to_dict()
    feature = {key[1]: value for key, value in feature.items()}

    return feature


def extract_core_features(player_name):  
    # --- BASIC OFFENSIVE METRICS ---
    goals = extract_each_feature("Goals")
    assists = extract_each_feature("Assists")
    shots = extract_each_feature("Shots Total")
    xG = extract_each_feature("xG: Expected Goals")
    npxG = extract_each_feature("npxG: Non-Penalty xG")
    xAG = extract_each_feature("xAG: Exp. Assisted Goals")
    key_passes = extract_each_feature("Key Passes")
    
    # --- PROGRESSION METRICS ---
    progressive_carries = extract_each_feature("Progressive Carries")
    progressive_passes = extract_each_feature("Progressive Passes")
    successful_take_ons = extract_each_feature("Successful Take-Ons")
    success_rate = extract_each_feature("Successful Take-On %")
    
    # --- ATTACKING ACTION METRICS ---
    goal_creating_actions = extract_each_feature("Goal-Creating Actions")
    shot_creating_actions = extract_each_feature("Shot-Creating Actions")
    touches_in_attack_penalty_area = extract_each_feature("Touches (Att Pen)")
    
    # --- DEFENSIVE & PRESSING METRICS ---
    tackles_att_third = extract_each_feature("Tackles (Att 3rd)")
    pct_dribblers_tackled = extract_each_feature("% of Dribblers Tackled")
    ball_recoveries = extract_each_feature("Ball Recoveries")
    
    # --- BALL RETENTION --- 
    dispossessed = extract_each_feature("Dispossessed")
    miscontrols = extract_each_feature("Miscontrols")
    
    # --- CALCULATE DERIVED METRICS ---
    per90_key = 'Per 90'
    
    # Shooting efficiency metrics
    shot_quality = {
        per90_key: float(npxG[per90_key]) / float(shots[per90_key]) if float(shots[per90_key]) > 0 else 0
    }
    
    finishing_ability = {
        per90_key: float(goals[per90_key]) - float(xG[per90_key])
    }
    
    # Creativity metrics
    chance_creation_quality = {
        per90_key: float(xAG[per90_key]) / float(key_passes[per90_key]) if float(key_passes[per90_key]) > 0 else 0
    }
    
    creativity_index = {
        per90_key: (float(xAG[per90_key]) * 2) + (float(shot_creating_actions[per90_key]) * 0.5)
    }
    
    # Style indicators
    progression_style = {
        per90_key: float(progressive_carries[per90_key]) / float(progressive_passes[per90_key]) 
                  if float(progressive_passes[per90_key]) > 0 else 999
    }
    
    # Dribbling effectiveness 
    # dribbling_impact = {
    #     per90_key: float(successful_take_ons[per90_key]) * (float(success_rate[per90_key]) / 100)
    # }
    
    # Defensive and pressing metrics
    pressing_intensity = {
        per90_key: float(tackles_att_third[per90_key]) / float(ball_recoveries[per90_key])
                  if float(ball_recoveries[per90_key]) > 0 else 0
    }
    
    # Ball security metric
    # touches = extract_each_feature("Touches")
    # ball_security = {
    #     per90_key: 1 - ((float(dispossessed[per90_key]) + float(miscontrols[per90_key])) / float(touches[per90_key]))
    #               if float(touches[per90_key]) > 0 else 0
    # }
    
    return {
        # --- RAW OFFENSIVE STATS ---
        "Goals": goals,
        "Assists": assists, 
        "Shots": shots,
        "xG": xG,
        "npxG": npxG,
        "xAG": xAG,
        "Key Passes": key_passes,
        "Goal+Assist": {per90_key: float(goals[per90_key]) + float(assists[per90_key])},
        "npxG+xAG": {per90_key: float(npxG[per90_key]) + float(xAG[per90_key])},
        
        # --- CALCULATED SHOOTING METRICS ---
        "Shot Quality": shot_quality,           # Higher value = takes better shots
        "Finishing Ability": finishing_ability, # Positive = overperforms xG
        
        # --- CALCULATED CREATIVE METRICS ---
        "Chance Creation Quality": chance_creation_quality, # Avg xG per key pass
        "Creativity Index": creativity_index,               # Weighted creative impact
        
        # --- PROGRESSION METRICS ---
        "Progressive Carries": progressive_carries,
        "Progressive Passes": progressive_passes,
        "Progression Style": progression_style,  # >1 = dribbler, <1 = passer
        
        # --- DRIBBLING METRICS ---
        "Successful Take-Ons": successful_take_ons,
        "Take-On Success Rate": success_rate,
        # "Dribbling Impact": dribbling_impact,    # Volume + accuracy combined
        
        # --- PENALTY AREA IMPACT ---
        "Penalty Area Touches": touches_in_attack_penalty_area,
        "Goal-Creating Actions": goal_creating_actions,
        "Shot-Creating Actions": shot_creating_actions,
        
        # --- DEFENSIVE & PRESSING METRICS ---
        "Tackles in Attacking Third": tackles_att_third,
        "% Dribblers Tackled": pct_dribblers_tackled,
        "Ball Recoveries": ball_recoveries,
        "Pressing Intensity": pressing_intensity,      # High = active high presser
        "Defensive Duel Success": pct_dribblers_tackled,
        
        # --- BALL RETENTION ---
        "Dispossessed": dispossessed,
        "Miscontrols": miscontrols,
        # "Ball Security": ball_security,  # Higher = better at keeping possession
    }


# Example usage
player_name = input("Enter player name: ")

player_stats, position = get_player_stats(player_name)
# player_match_logs = get_player_match_logs_24_25(player_name)
stats = extract_core_features(player_name)

from tabulate import tabulate

rows = []
for metric, values in stats.items():
    raw_per90  = values.get("Per 90", "")
    pct        = values.get("Percentile", "")

    # if it’s numeric, force 3 decimals; otherwise leave it
    try:
        per90_str = f"{float(raw_per90):.3f}"
    except (ValueError, TypeError):
        per90_str = raw_per90

    rows.append([metric, per90_str, pct])
    
print(position)
print(
    tabulate(
        rows,
        headers=["Metric", "Per 90", "Percentile"],
        tablefmt="grid"
    )
)

print(player_stats)

# print(player_match_logs)

print(position)
print(stats)