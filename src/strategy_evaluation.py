import matplotlib.pyplot as plt
from src.data_preprocessing import preprocess_data

def evaluate_strategy(model, data):
    predictions = model.predict(data.drop('lap_duration', axis=1))
    plt.figure(figsize=(10,5))
    plt.plot(data['lap_duration'], label='Actual')
    plt.plot(predictions, label='Predicted')
    plt.legend()
    plt.show()

# For testing or immediate execution
if __name__ == "__main__":
    live_data = preprocess_data('data/live_data.csv')
    # Example: Assuming model is loaded or created in this context
    model = None  # Replace with loading or creating your model
    evaluate_strategy(model, live_data)
