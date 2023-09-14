import random

def create_random_num(length: int = 0):
    num_list = '0123456789'
    code = ''.join(random.choice(num_list) for i in range(length))
    return code
