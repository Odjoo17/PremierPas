import pandas as pd
from sklearn.ensemble import RandomForestClassifier


df_train = pd.read_csv("train.csv")
#print(df_train)
df_test_data = pd.read_csv("test.csv")

df_survived = df_train[df_train["Survived"] == 1].reset_index(drop=True)
df_died = df_train[df_train["Survived"] == 0].reset_index(drop=True)
#print(df_survived)

#print("Passenger that survived to the titanic crash : \n",df_survived,"\n Passenger that died : \n",df_died)

number_passenger = df_train.shape[0]
#print(number_passenger)

condition_survived = df_train['Survived'] == 1
condition_died = df_train['Survived'] == 0
condition_women = df_train["Sex"] == "female"
condition_men = df_train["Sex"] == "male"
condition_majeur = df_train["Age"] >=18
condition_mineur = df_train["Age"] < 18


# count_rows_condition = (condition_survived & condition_women ).sum()
#print(f"number of women passenger that survived to the titanic is {count_rows_condition} over {number_passenger}, so almost {round(count_rows_condition*100/number_passenger,2)} % of the passengers")
#input('')
men = condition_men.sum()
women = condition_women.sum()
old = condition_majeur.sum()
young = condition_mineur.sum()

men_survived = (condition_survived & condition_men).sum()
men_died = (condition_died & condition_men).sum()
women_survived = (condition_survived & condition_women).sum()
women_died = (condition_died & condition_women).sum()
majeur_survived = (condition_survived & condition_majeur).sum()
mineur_survived = (condition_survived & condition_mineur).sum()
majeur_died = (condition_died & condition_majeur).sum()
mineur_died = (condition_died & condition_mineur).sum()


# print("men survived : ",round(men_survived*100/men,2))
# print("women survived : ",round(women_survived*100/women,2))
# print("men died : ",round(men_died*100/men,2))
# print("women died : ",round(women_died*100/women,2))
# print("majeur survived : ",round(majeur_survived*100/old,2))
# print("mineur survived : ",round(mineur_survived*100/young,2))
# print("majeur died : ",round(majeur_died*100/old,2))
# print("mineur died : ",round(mineur_died*100/young,2))

#print(df_train.head())

df_women_survived = df_train.loc[df_train.Sex == 'female']["Survived"]
#print(df_women_survived)

rate_women = sum(df_women_survived)/len(df_women_survived)
#print("% of women who survived:", round(rate_women*100,2))

df_men_survived = df_train.loc[df_train.Sex == 'male']["Survived"]
rate_men = sum(df_men_survived)/len(df_men_survived)
#print("% of men who survived:", round(rate_men*100,2))

y = df_train["Survived"]
print("y",y)
features = ["Sex","Pclass","Fare","Age","SibSp","Parch","Embarked"]
# X = (df_train[features])
X = pd.get_dummies(df_train[features])
print("X",X)
X_test = pd.get_dummies(df_test_data[features])
print("X_test",X_test)

model = RandomForestClassifier(n_estimators=1000, max_depth=8, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': df_test_data.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")