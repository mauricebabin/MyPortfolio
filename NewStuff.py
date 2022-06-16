import datetime

OrderDate = datetime.datetime.now()
DueDate = OrderDate + datetime.timedelta(days=30)

print(OrderDate)
print(DueDate)
