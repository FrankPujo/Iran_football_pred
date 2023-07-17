from sklearn.linear_model import LogisticRegression
import pickle

# create model
model = LogisticRegression()

# save model with model number 0
filename = "model_0.sav"
pickle.dump(model, open(filename, 'wb'))