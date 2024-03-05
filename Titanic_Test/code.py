import pandas as pd
from sklearn.ensemble import RandomForestClassifier


df_train = pd.read_csv("train.csv")
df_test_data = pd.read_csv("test.csv")

df_survived = df_train[df_train["Survived"] == 1].reset_index(drop=True)
df_died = df_train[df_train["Survived"] == 0].reset_index()
#print(df_train)

#print("Passenger that survived to the titanic crash : \n",df_survived,"\n",df_died)

number_passenger = df_train.shape[0]
#print(number_passenger)

condition_survived = df_train['Survived'] == 1
condition_died = df_train['Survived'] == 0
condition_women = df_train["Sex"] == "female"
condition_men = df_train["Sex"] == "male"

count_rows_condition = (condition_survived & condition_women ).sum()
#print(f"number of women passenger that survived to the titanic is {count_rows_condition} over {number_passenger}, so almost {round(count_rows_condition*100/number_passenger,2)} % of the passengers")
#input('')
men_survived = (condition_survived & condition_men).sum()
men_died = (condition_died & condition_men).sum()
women_survived = (condition_survived & condition_women).sum()
women_died = (condition_died & condition_women).sum()


print("men survived : ",round(men_survived*100/number_passenger,2))
print("women survived : ",round(women_survived*100/number_passenger,2))
print("men died : ",round(men_died*100/number_passenger,2))
print("women died : ",round(women_died*100/number_passenger,2))

#print(df_train.head())

women = df_train.loc[df_train.Sex == 'female']["Survived"]
print(women)
rate_women = sum(women)/len(women)

print("% of women who survived:", round(rate_women*100,2))

men = df_train.loc[df_train.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)

print("% of men who survived:", round(rate_men*100,2))

y = df_train["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(df_train[features])
X_test = pd.get_dummies(df_test_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': df_test_data.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")