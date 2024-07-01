import requests
import pandas as pd


def get_historical_data():
    response = requests.get('https://api.openf1.org/v1/laps?session_key=latest')
    data = response.json()
    
    # Check if data is empty
    if not data:
        raise ValueError("API response is empty or invalid.")
    
    # Extract relevant features
    features_data = []
    for entry in data:
        features = {
            'lap_duration': entry.get('lap_duration'),
            'st_speed': entry.get('st_speed'),
            'duration_sector_1': entry.get('duration_sector_1'),
            'duration_sector_2': entry.get('duration_sector_2'),
            # Add more relevant features here as needed
        }
        features_data.append(features)
    
    # Create DataFrame
    df = pd.DataFrame(features_data)
    
    # Save to CSV with all relevant columns
    df.to_csv('data/historical_data.csv', index=False)

    print(f"Saved {len(df)} rows to data/historical_data.csv")

# Example usage:
if __name__ == "__main__":
    get_historical_data()




def get_live_data():
    response = requests.get('https://api.openf1.org/v1/laps?session_key=latest')
    data = response.json()

    # Extract relevant features similar to historical data
    live_data_features = []
    for entry in data:
        features = {
            'lap_duration': entry.get('lap_duration'),
            'st_speed': entry.get('st_speed'),
            'duration_sector_1': entry.get('duration_sector_1'),
            'duration_sector_2': entry.get('duration_sector_2'),
            # Add more relevant features here as needed
        }
        live_data_features.append(features)

    # Create DataFrame
    df = pd.DataFrame(live_data_features)

    # Save to CSV with all relevant columns
    df.to_csv('data/live_data.csv', index=False)

    print(f"Saved {len(df)} rows to data/live_data.csv")

get_live_data()
