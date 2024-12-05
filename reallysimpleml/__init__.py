from scipy import stats
import matplotlib.pyplot as plt

def linear_regression(x: int, data_x: list = [5,7,8,7,2,17,2,9,4,11,12,9,6], data_y: list = [99,86,87,88,111,86,103,87,94,78,77,85,86]):
  slope, intercept, r, p, std_err = stats.linregress(data_x, data_y)
  def predict(x):
    return slope * x + intercept
  prediction = predict(x)
  model = list(map(predict, data_x))
  plt.scatter(data_x, data_y)
  plt.plot(data_x, model)
  plt.show()
  return {
    "prediction":prediction,
    "r":r,
  }

print(f"{linear_regression(10)['prediction']}")

