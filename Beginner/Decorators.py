#Decorators
import time
def cal_time(func):
    def timer(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(func.__name__ + " took " + str((end - start) * 1000) +  "ms")
        return result
    return timer

@cal_time
def square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@cal_time
def cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
out_square = square(array)
out_cube = cube(array)