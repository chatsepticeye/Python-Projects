import random
from collections import Counter
def generate_random(seed_v):
    random.seed(seed_v)
    random_integers=[random.randint(90,100) for i in range(1500)]
    frequency=dict(Counter(random_integers))
    return frequency
frequency_seed_2=generate_random(2)
print(frequency_seed_2)
