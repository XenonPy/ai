import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

model = numpy.poly1d(numpy.polyfit(x, y, 3))

prediction = model(17)
# Relationship is a measure of how the data fits with a polynomial regression.
print(f"Prediction: {prediction}\n Relationship: {r2_score(y, model(x))}")