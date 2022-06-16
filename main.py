import datetime
import math
import FormatValues as FV
import matplotlib.pyplot as plt
from matplotlib import style


ToDo = ["Study, study and study some more."]
'''
print(ToDo)
print(ToDo[1])

TaskNum = 1
for Task in ToDo:
    print(f" {TaskNum}. {Task}")
    TaskNum += 1

NewTask = input("Enter a new task: ")
ToDo.append(NewTask)

TaskNum = 1
for Task in ToDo:
    print(f" {TaskNum}. {Task}")
    TaskNum += 1

print()
DelItem = int(input("What item do you want to delete: "))
ToDo.__delitem__(DelItem - 1)

if len(ToDo) != 0:
    TaskNum = 1
    for Task in ToDo:
        print(f" {TaskNum}. {Task}")
        TaskNum += 1
else:
    print("ToDo list is currently empty.")

while True:
    NewTask = input("Enter a new task (END to quit): ")
    if NewTask.upper() == "END":
        break
    else:
        ToDo.append(NewTask)

if len(ToDo) != 0:
    TaskNum = 1
    for Task in ToDo:
        print(f" {TaskNum}. {Task}")
        TaskNum += 1
else:
    print("ToDo list is currently empty.")
'''

t = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
s = [200, 100, 600, 300, 200, 400, 250]

plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')

plt.title('Sine Wave')
plt.grid(True)

plt.show()