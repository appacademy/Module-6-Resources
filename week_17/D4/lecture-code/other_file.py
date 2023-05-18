from w17d4 import timer




@timer
def do_stuff(num):
  counter = 1
  for val in range(num):
    counter += 1
  return counter


print(do_stuff(1_000_000))