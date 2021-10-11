import random
import time

branchs = ['BMW', 'VinFast', 'Toyota', 'Mez', 'Lexus', 'Lambogini']
engines = ['2.0', '1.6', '3.0', 'V6', 'V8']

#list 
def car_list(num_people):
    result = []
    for i in range(num_people):
        car = {
                    'id': i,
                    'name': random.choice(branchs),
                    'engine': random.choice(engines)
                }
        result.append(car)
    return result

#generator
def car_generator(num_people):
    for i in range(num_people):
        car = {
                    'id': i,
                    'name': random.choice(branchs),
                    'engine': random.choice(engines)
                }
        yield car
#if __name__ == "__main__":
# t1 = time.time()
# people = car_list(1000000)
# t2 = time.time()

t1 = time.time()
people = car_generator(1000000)
t2 = time.time()
print(next(people))
print (f'Took {t2-t1} Seconds')