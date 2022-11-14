import random

def get_egg(zero_count:int,one_count:int):
    return random.choice(([0]*zero_count)+([1]*one_count))
