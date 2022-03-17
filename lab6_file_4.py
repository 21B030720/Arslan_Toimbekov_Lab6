import time
import math
def logic(fn, ms, *args):
  time.sleep(ms / 1000)
  return fn(*args)
print("Square root after specific miliseconds:")
print(logic(lambda x: math.sqrt(x), 2123, 25100))