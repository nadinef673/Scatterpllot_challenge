import matplotlib.pyplot as plt
from scipy import stats

x = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
y = [220, 330, 190, 340, 410, 445, 415]
slope, intercept, r, p, std_err = stats.linegress(x, y)

def myfunc(a):
    return slope * a + intercept

mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.title("SOUP SALES IN RELATION TO TEMPERATURE")
plt.xlabel("Temperature")
plt.ylabel("Price in Rands")
plt.plot(x, mymodel)

plt.show()