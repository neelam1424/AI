import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error



df = pd.read_csv("data.csv")


X= df.drop("target", axis=1)
y= df["target"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size= 0.2,
    random_state = 42
)

print("Training samples: ", len(X_train))
print("Testing samples: ", len(X_test))