#Iris Vance
#1270481

input_string = input()
user_input = input_string.split()

for x in user_input:
  freq = user_input.count(x)
  print(x, freq)
