#PROCCESS
import multiprocessing
from multiprocessing import process
import time
result = []
def square(numbers):
    global result
    print("Calculate square of numberse")
    for x in numbers:
        result.append(x*x)
    print("Result is: " + str(result))
"""
def cube(numbers):
    time.sleep(10)
    print("Calculate cube of numberse")
    for x in numbers:
        print('Cube: ', x*x*x)
"""
if __name__ == "__main__":
    arr = [1 , 3 , 5, 7 ,9]
    process1 = multiprocessing.Process(target=square, args = (arr,))
    process1.start()
    process1.join()
    print("Result is: " + str(result))
    print("Done procsess!")