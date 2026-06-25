import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import tkinter as tk
from tkinter import ttk
import datetime


class LeavePredictorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Resource Leave Predictor")

        # Data storage
        self.resources_data = {}

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Resource Name Entry
        tk.Label(self.root, text="Resource Name:").grid(row=0, column=0, padx=5, pady=5)
        self.resource_name = tk.Entry(self.root)
        self.resource_name.grid(row=0, column=1, padx=5, pady=5)

        # Previous Year Data Frame
        prev_year = datetime.datetime.now().year - 1
        tk.Label(self.root, text=f"Previous Year ({prev_year}) Data").grid(row=1, column=0, columnspan=2)

        # Create entries for each quarter
        self.quarters_planned = []
        self.quarters_taken = []

        for i in range(4):
            tk.Label(self.root, text=f"Q{i + 1} Planned:").grid(row=i + 2, column=0)
            planned = tk.Entry(self.root)
            planned.grid(row=i + 2, column=1)
            self.quarters_planned.append(planned)

            tk.Label(self.root, text=f"Q{i + 1} Taken:").grid(row=i + 2, column=2)
            taken = tk.Entry(self.root)
            taken.grid(row=i + 2, column=3)
            self.quarters_taken.append(taken)

        # Current Year Data
        curr_year = datetime.datetime.now().year
        tk.Label(self.root, text=f"Current Year ({curr_year}) Data").grid(row=6, column=0, columnspan=2)

        # Current quarter planned leaves
        curr_q = (datetime.datetime.now().month - 1) // 3 + 1
        tk.Label(self.root, text=f"Current Q{curr_q} Planned:").grid(row=7, column=0)
        self.current_planned = tk.Entry(self.root)
        self.current_planned.grid(row=7, column=1)

        # Predict Button
        tk.Button(self.root, text="Predict Leaves", command=self.predict_leaves).grid(row=8, column=0, columnspan=2,
                                                                                      pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=9, column=0, columnspan=4)

    def predict_leaves(self):
        # Collect data
        resource = self.resource_name.get()
        historical_data = []

        for i in range(4):
            planned = float(self.quarters_planned[i].get())
            taken = float(self.quarters_taken[i].get())
            historical_data.append([i + 1, planned, taken])

        # Prepare data for ML
        X = np.array(historical_data)
        y = X[:, 2]  # Taken leaves

        # Train model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X[:, :2], y)

        # Predict current quarter
        curr_q = (datetime.datetime.now().month - 1) // 3 + 1
        current_planned = float(self.current_planned.get())
        prediction = model.predict([[curr_q, current_planned]])

        # Display result
        self.result_label.config(text=f"Predicted leaves for {resource}: {prediction[0]:.1f} days")


# Create main window
if __name__ == "__main__":
    root = tk.Tk()
    app = LeavePredictorGUI(root)
    root.mainloop()
