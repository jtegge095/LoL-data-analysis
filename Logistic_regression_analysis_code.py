# Logistic Regression Analyis Code

# Import Setup Code
from project_setup_code import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Use this in notebook to show plots
# %matplotlib inline

def logRegModel(X, y):
	'''
	X: data used to predict outcome
	y: outcome data

	function used to split data into train and test sections,
	create a logistic regression model, and train the model
	with the train data. Finally, the function will print
	a classification report to results.
	'''

	# Split the data (X, y)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=101)

	# Create and train model
	logmodel = LogisticRegression()
	logmodel.fit(X_train, y_train)
	predictions = logmodel.predict(X_test)

	# Evaluate the model
	print(classification_report(y_test, predictions))

# heatmap to explore correlation
fig = plt.figure(figsize=(10,10))
sns.heatmap(data[['t1_towerKills','t1_inhibitorKills','t1_dragonKills','t1_baronKills',
                  't2_towerKills','t2_inhibitorKills','t2_dragonKills','t2_baronKills','winner']].corr(),annot=True,square=True)

# create lists of columns we want to train our model on
X1 = data[['t1_baronKills', 't1_dragonKills', 't2_baronKills', 't2_dragonKills']]
y1 = data['winner']

X2 = data[['t1_towerKills','t1_inhibitorKills','t2_towerKills','t2_inhibitorKills']]
y2 = data['winner']

X3 = data[['t1_baronKills', 't1_dragonKills', 't2_baronKills', 't2_dragonKills',
         't1_towerKills','t1_inhibitorKills','t2_towerKills','t2_inhibitorKills']]
y3 = data['winner']

# Use logRegModel function to run these datasets and see how they compare