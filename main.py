from src.data_collection import get_historical_data, get_live_data
from src.data_preprocessing import preprocess_data
from src.strategy_model import train_model, save_model
from src.strategy_evaluation import evaluate_strategy
import joblib

if __name__ == "__main__":
    try:
        # Get historical data and preprocess
        get_historical_data()
        historical_data = preprocess_data('data/historical_data.csv')
        print("data preprocessed.")
        
        # Train model
        model = train_model(historical_data)
        save_model(model, 'models/strategy_model.pkl')
        print("model trained")
        
        # Get live data and preprocess
        get_live_data()
        live_data = preprocess_data('data/live_data.csv')
        print("data precrpocessed")
        
        # Evaluate strategy using trained model
        evaluate_strategy(model, live_data)
    
    except ValueError as ve:
        print(f"Error : {ve}")
