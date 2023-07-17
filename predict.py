from sklearn.linear_model import LinearRegression
import pickle
import pandas
from statistics import mean

oldModelName = "model_" + input("Insert model number to use in prediction: ") + ".sav"
model = pickle.load(open(oldModelName, "rb"))

# get right data
data = pandas.read_excel("data.xlsx")
sta = int(input("First line of data: "))
end = int(input("Last line of data: ")) + 1
inDataDf = data.iloc[:, 0:3].iloc[sta:end]
inData = inDataDf.values.tolist()

# predict results
orig_predictions = model.predict(inData)

# turn prediction into 1 x 2 format
ord_predictions = sorted(orig_predictions, reverse=True)

avg_win = mean(ord_predictions[:3])
avg_tie = mean(ord_predictions[3:6])
avg_los = mean(ord_predictions[6:])
avg_values = [avg_win, avg_tie, avg_los]

results = list()
for pred in orig_predictions:
	real_value = min(avg_values, key = lambda x: abs(x-pred))
	if real_value == avg_win:
		results.append("1")
	elif real_value == avg_tie:
		results.append("x")
	else:
		results.append("0")

print( orig_predictions, results )