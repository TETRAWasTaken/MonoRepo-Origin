import datetime
current_time = str(datetime.datetime.now())
import ast
import json
with open('/Users/anshumaansoni/PycharmProjects/pythonProject/text cache txt', 'r') as file:
    text = file.read()
    dictionary = ast.literal_eval(text)

lister = []
a = list(dictionary.keys())
for i in dictionary[(a[0])].keys():
    if dictionary[(a[0])][i][1] == 0:
        lister.append(dictionary[(a[0])][i][0])
        dictionary[(a[0])][i][1] = 1
    else:
        continue

print(lister)

dictionary[a[0]][current_time]=['Hello',0]

with open('/Users/anshumaansoni/PycharmProjects/pythonProject/text cache txt', 'w') as file:
    file.write(json.dumps(dictionary))