def update_car_info(*args):
    car = {}
    keys = ['brand', 'price']
    
    
    for key, value in zip(keys, args):
        car['is_aviable'] = True
        return car


result = update_car_info('BMW', 77777)
print(result)   