import logging

logging.basicConfig(filename='app1.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s , level=logging.debug')
logging.warning('This will get logged to a file')

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

num_1 = 20
num_2 = 10

add_result = add(num_1,num_2)
logging.debug(add_result)
sub_result = subtract(num_1,num_2)
logging.debug(sub_result)
multiply_result = multiply(num_1,num_2)
logging.debug(multiply_result)
divide_result = divide(num_1,num_2)
logging.debug(divide_result)