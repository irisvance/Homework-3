#Iris Vance
#1270481

input_string = input()
user_input = []

for x in input_string.split(' '):
  if int(x) >= 0:
    user_input.append(int(x))
    user_input.sort()

for x in user_input:
  print(x,end=' ')
