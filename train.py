from sklearn.linear_model import LogisticRegression
import pickle
import pandas

# all data
data = pandas.read_excel("data.xlsx")
sta = int(input("First line of data: "))
end = int(input("Last line of data: ")) + 1
# training input data
inDataDf = data.iloc[:, 0:3].iloc[sta:end]
inData = inDataDf.values.tolist()
# training expected output data
outDataDf = data.iloc[:, 5:6].iloc[sta:end]
outDataArred = outDataDf.values.tolist()
outData = list()
for smallArr in outDataArred:
	outData.append(smallArr[0])

# load last model
oldModelName = "model_" + input("Insert old model number: ") + ".sav"
model = pickle.load(open(oldModelName, "rb"))

# train model with data
#model.fit(inData, outData)
#print("Model trained")

# save trained model
newModelName = "model_" + input("Insert new model number: ") + ".sav"
pickle.dump(model, open(newModelName, "wb"))