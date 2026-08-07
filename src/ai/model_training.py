"""
model_training.py
--------------------------------
Trains Machine Learning models
using the prepared AI dataset.

Author: Sirama Avinash
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


class AIModelTrainer:

    def __init__(self):

        print("AI Model Trainer initialized.")

    def train(
        self,
        X,
        y,
        test_size=0.2,
        random_state=42
    ):

        print("\n========== MODEL TRAINING ==========\n")

        # -------------------------
        # Train/Test Split
        # -------------------------

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_state
        )

        print(f"Training Samples : {X_train.shape[0]}")
        print(f"Testing Samples  : {X_test.shape[0]}")

        # -------------------------
        # Random Forest
        # -------------------------

        model = RandomForestRegressor(
            n_estimators=100,
            random_state=random_state,
            n_jobs=-1
        )

        print("\nTraining Random Forest...")

        model.fit(X_train, y_train)

        print("Training completed.")

        return model, X_train, X_test, y_train, y_test