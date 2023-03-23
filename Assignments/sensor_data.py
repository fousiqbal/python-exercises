import random
with open("sensor_values",'w') as f:
    for i in range(100):
        f.write(str(random.randint(10,100))+'\n')