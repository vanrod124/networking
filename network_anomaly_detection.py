import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import tkinter as tk

# Load the dataset
data = pd.read_csv("network_data.csv")

# Preprocess the data
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predict on the test set
y_pred = knn.predict(X_test)

# Evaluate the model
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Visualization using Tkinter
def visualize_data():
    root = tk.Tk()
    root.title("Network Anomaly Detection")

    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    # Plot the data points
    for index, row in data.iterrows():
        x, y = row['feature1'], row['feature2']
        color = "blue" if row['label'] == "normal" else "red"
        canvas.create_oval(x * 20, y * 20, x * 20 + 10, y * 20 + 10, outline=color, fill=color)

    root.mainloop()

visualize_data()
