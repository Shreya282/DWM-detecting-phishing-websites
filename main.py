import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

input = (0,1,125,8301,99386,0,4)

# changing the input to numpy array
input_as_numpy_array = np.asarray(input)

# reshape the array as we are predicting for one instance
input_reshaped = input_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_reshaped)
print(prediction)

# y_predrf = classifierrf.predict([input])
if prediction == 0:
  print("It is a phishing website")
else:
  print("It is a legitimate website")