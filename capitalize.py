lines = []
while True:
  input1 = input()
  if input1 == "":
    break

  lines.append(input1.upper())

for i in lines:
  print(i)
