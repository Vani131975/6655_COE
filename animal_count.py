di1 = {"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}
d12 = {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}
di3 = {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}
di4 = {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}

total_puppies = 0
try:
  for di in [di1, d12, di3, di4]:
    if "Puppies" in di:
      total_puppies += di["Puppies"]

except KeyError as e:
  print("Error: ", e)

finally:
  print("Total number of puppies:", total_puppies)
