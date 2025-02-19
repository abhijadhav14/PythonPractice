import os
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Loading the Iris dataset
iris = pd.read_csv('../data/iris.csv')  # Adjusting the path to iris.csv

# Encode the 'variety' column to numerical values using LabelEncoder
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
iris['variety_encoded'] = label_encoder.fit_transform(iris['variety'])

# Splitting the dataset into features and target
X = iris.drop(['variety', 'variety_encoded'], axis=1)
y = iris['variety_encoded']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating the Random Forest Classifier
rf_classifier = RandomForestClassifier(random_state=42)

# Train the model
rf_classifier.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

classification_rep = classification_report(y_test, y_pred)
print("Classification Report:\n", classification_rep)

# Hyperparameter Tuning using GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10, 15],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(estimator=rf_classifier, param_grid=param_grid, cv=5, verbose=2, n_jobs=-1)
grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
print("Best Parameters:", best_params)

# Save the best model
os.makedirs('models', exist_ok=True)
joblib.dump(grid_search.best_estimator_, 'models/random_forest_iris.pkl')

# Using the best model to make predictions
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)

# Evaluate the best model
accuracy_best = accuracy_score(y_test, y_pred_best)
print("\nBest Model - Accuracy:", accuracy_best)

classification_rep_best = classification_report(y_test, y_pred_best)
print("Best Model - Classification Report:\n", classification_rep_best)
