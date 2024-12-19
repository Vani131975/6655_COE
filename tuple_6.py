given_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def get_last(tuple):
  return tuple[-1]


given_list.sort(key=get_last)
print(given_list)
