import math
import random
def objective(x):
    return 2*(x ** 2.0) +5


best = random.uniform(-100,100)

for x in range(0,10000):
    tmp = random.uniform(-100,100)
    if(objective(tmp)<objective(best)):
        best = tmp
    print(objective(tmp))

print('Result:')
print('x:', best)
print('Fitness:', objective(best))