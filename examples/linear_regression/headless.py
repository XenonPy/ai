# Linear Regression
from scipy import stats

# Arrays to correlate.
# Data is speeds of cars and their ages.
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

# Actual prediction function
def predict(x):
  return slope * x + intercept

speed = predict(10)

print(f"Predicted Value: {speed}\nRelationship: {r}")
