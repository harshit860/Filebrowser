import os

path = os.getcwd()

for i in os.walk(path):
    print(i)