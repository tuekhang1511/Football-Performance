import pandas as pd
from unidecode import unidecode

# Load the player database
player_df = pd.read_csv('fbref_players.csv')

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
        
        try:
            # Try with different position IDs
            for position in ["FW", "AM", "MF", "DF", "GK"]:
                try:
                    table_id = f"scout_full_{position}"
                    stats_df = pd.read_html(scout_url, attrs={"id": table_id})[0]
                    return stats_df
                except:
                    continue
            
            # Fallback to reading any table
            stats_df = pd.read_html(scout_url)[0]
            # stats_df = stats_df.dropna(subset=['Statistic'])
            return stats_df
            
        except Exception as e:
            return f"Error fetching stats: {e}"
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

            return stats_df
            
        except Exception as e:
            return f"Error fetching stats: {e}"
    else:
        return f"Player '{player_name}' not in database. Please check spelling or add this player to the database."


# Example usage
player_name = input("Enter player name: ")

player_stats = get_player_stats(player_name)
player_match_logs = get_player_match_logs_24_25(player_name)

print(player_stats)
print(player_match_logs)