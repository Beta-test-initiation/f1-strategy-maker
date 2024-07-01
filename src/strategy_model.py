from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(data):
    if 'lap_duration' not in data.columns:
        raise ValueError("lap_duration column 'lap_duration' not found in the data.")
    
    X = data.drop('lap_duration', axis=1)
    y = data['lap_duration']
    
    print(f"X shape: {X.shape}, y shape: {y.shape}")  # Debug statement
    
    # Ensure all columns in X are numeric
    X = X.astype('float64')  # Convert all features to float64
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")  # Debug statement
    
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    
    return model

def save_model(model, filename):
    joblib.dump(model, filename)
