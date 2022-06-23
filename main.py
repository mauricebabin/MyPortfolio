import datetime
import math
import FormatValues as FV
import matplotlib.pyplot as plt


x = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
y = []

for months in range(1,13):
    MonthSales = input("Enter month sales for " + x[months - 1] + ": ")
    y.append(MonthSales)

plt.title("Monthly Sales Over The Past 12 Months ")
plt.plot(x,y)
plt.show()