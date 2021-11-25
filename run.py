import os
import sklearn as sk
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

with open(os.path.join(os.getcwd(), "test", "testdata","data.npy"), "rb") as file:
    data = np.load(file)
with open(os.path.join(os.getcwd(), "test", "testdata","labels.npy"), "rb") as file:
    labels = np.load(file)

X_train, X_test, y_train, y_test = train_test_split(data,labels, test_size=0.2)

fclf = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
fclf.fit(X_train, y_train)

accuracy = fclf.score(X_test, y_test)

f1_score = sk.metrics.f1_score(y_test,fclf.predict(X_test), pos_label='Not Ice')

print(f"raw accuracy: {accuracy} \n f1 score: {f1_score}")
