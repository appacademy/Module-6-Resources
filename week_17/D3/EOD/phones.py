phones = [
    {
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "cost": 929,
        "color": "alpine green"
    },
    {
        "brand": "Samsung",
        "model": "Galaxy S22+",
        "cost": 999,
        "color": "black"
    },
    {
        "brand": "Google",
        "model": "Pixel 6",
        "cost": 599,
        "color": "kinda coral"
    },
    {
        "brand": "Apple",
        "model": "iPhone 13 Pro",
        "cost": 929,
        "color": "gold"
    },
    {
        "brand": "Google",
        "model": "Pixel 6",
        "cost": 599,
        "color": "stormy black"
    }
]

def get_unique_models(phone_list):
    just_models = map(lambda phone: phone["model"], phone_list)
    print(list(set(just_models)))


get_unique_models(phones)

# def get_unique_models(phone_list):
#     seen = []
#     return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)
    
#     # so what is going on here in the filter method???
#     # think of the lambda statement being written like this...
#     if phone['model'] not in seen:
#         return seen.append(phone['model']) is None
#     else:
#         return False
#     #
#     # Because this is a callback in a filter, it needs to return True or False
#     # to determine if the value gets added to our filtered list
#     #
#     # In the else, we return False, makes sense...
#     # The append method does not have a return, but we know that if a
#     # function does not have a set return value, it returns None!
#     # So we check if the return value is None, which will evaluate to true!


