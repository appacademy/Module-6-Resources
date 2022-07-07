# # Problem 1 - Adopted Cats
# cat_list = [
#     {
#         "name": "Lenny",
#         "breed": "Ragdoll",
#         "adopted": False
#     },
#     {
#         "name": "Roger",
#         "breed": "Siamese",
#         "adopted": False
#     },
#     {
#         "name": "Katya",
#         "breed": "Persian",
#         "adopted": True
#     }
# ]

# # Problem 2 - Most Used Card
# # Write your code here.

# def cat_verify(cats):
#     pass

# print(cat_verify(cat_list))    # False

# cards = [
#     {
#         "company": "Wells Fargo",
#         "card_name": "Active Cash",
#         "annual_fee": 0,
#         "intro_reward_type": "cash",
#         "intro_reward_amount": 200,
#         "num_users": 20
#     },
#     {
#         "company": "Chase",
#         "card_name": "Sapphire Preferred",
#         "annual_fee": 95,
#         "intro_reward_type": "points",
#         "intro_reward_amount": 60000,
#         "num_users": 54
#     },
#     {
#         "company": "Citi",
#         "card_name": "Diamond Preferred",
#         "annual_fee": 0,
#         "intro_reward_type": "cash",
#         "intro_reward_amount": 150,
#         "num_users": 13
#     }
# ]

# # Write your code here.

# def sort_cards(card_list):
#     pass


# print(sort_cards(cards))        # Citi, Wells Fargo, Chase


# # Problem 3 - Nested Sort
# teachers = [
#     {
#         "name": "Emily Richardson",
#         "subjects": ["Geometry", "Geometry Honors"],
#         "years_active": 5,
#         "classroom": {
#             "building_id": "A",
#             "room_number": 12,
#             "capacity": 45
#         }
#     },
#     {
#         "name": "Richard Emilyson",
#         "subjects": ["English 11", "AP English Language"],
#         "years_active": 12,
#         "classroom": {
#             "building_id": "J",
#             "room_number": 42,
#             "capacity": 60
#         }
#     },
#     {
#         "name": "Richly Emiardson",
#         "subjects": ["Chemistry", "Chemistry Honors", "AP Chemistry"],
#         "years_active": 8,
#         "classroom": {
#             "building_id": "C",
#             "room_number": 5,
#             "capacity": 32
#         }
#     },
# ]

# # Write your code here.

# def sort_teachers_by_classroom_capacity(card_list):
#     pass


# print(sort_teachers_by_classroom_capacity(teachers)) 
# # Richly Emiardson, Emily Richardson, Richard Emilyson


# Problem 4 - Remove Duplicates
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
    just_models = map(lambda phone: phone['model'], phone_list)
    # print(list(just_models))
    return set(just_models)


print(get_unique_models(phones))
# unique_models = list(get_unique_models(phones))
# print(unique_models)                # iPhone 13 Pro, Galaxy S22+, Pixel 6 (dictionaries)
# print(map_to_names(unique_models))  # iPhone 13 Pro, Galaxy S22+, Pixel 6



def get_unique_models(phone_list):
    seen = []
    return filter(lambda phone: seen.append(phone['model']) is None if phone['model'] not in seen else False, phone_list)
    
    # so what is going on here in the filter method???
    # think of the lambda statement being written like this...
    if phone['model'] not in seen:
        return seen.append(phone['model']) is None
    else:
        return False
    #
    # Because this is a callback in a filter, it needs to return True or False
    # to determine if the value gets added to our filtered list
    #
    # In the else, we return False, makes sense...
    # The append method does not have a return, but we know that if a
    # function does not have a set return value, it returns None!
    # So we check if the return value is None, which will evaluate to true!


