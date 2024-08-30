import numpy as np
import matplotlib.pyplot as plt

N = 100

x = np.linspace(-10, 10, N)
y = 3 * x**3 + 2 * x**2 + x + np.random.normal(0, 100, N)

degree = 3
coefficients = np.polyfit(x, y, degree)

polynomial = np.poly1d(coefficients)

x_fit = np.linspace(-10, 10, 1000)
y_fit = polynomial(x_fit)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Исходные данные')
plt.plot(x_fit, y_fit, color='red', label=f'Подогнанный полином (степень {degree})')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Fitting a polynomial to data")
plt.legend()
plt.grid(True)
plt.show()
