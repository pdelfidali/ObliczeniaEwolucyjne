import math
import random
def objective(x):
    return 2*(x ** 2.0) +5


best = random.uniform(-100,100)
step_size = 0.5

for x in range(0,1000):
    tmp = best + random.uniform(-100,100) * step_size
    best = tmp
    print(objective(tmp))

print('Result:')
print('x:', best)
print('Fitness:', objective(best))