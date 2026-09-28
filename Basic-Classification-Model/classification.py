import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# load the dataset
iris = load_iris() 

# convert dataset into dataframes
df= pd.DataFrame(iris.data,columns= iris.feature_names)

#add target column
df["target"]= iris.target
#understand the dataset
print("first 5 rows:")
print(df.head())

print("\n dataset shape:")
print(df.shape)

print("\n dataset informaton")
print(df.info())

#sepearte features and target

X = df.drop("target",axis=1)
Y =df["target"]

#split data into training and testing
X_train,X_test,Y_train, Y_test =train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state= 42
)

print("\n Training data:", X_train.shape)
print("Testing data:", X_test.shape)

# create the classification model
model = LogisticRegression(max_iter=200)

#train the model
model.fit(X_train, Y_train)

#make prediction
Y_pred=model.predict(X_test)

#check accuracy
accuracy = accuracy_score(Y_test,Y_pred)
print("\nModel Accuracy:",accuracy)

#detailed evaluation
print("\nClassification Report:")
print(classification_report(Y_test,Y_pred))