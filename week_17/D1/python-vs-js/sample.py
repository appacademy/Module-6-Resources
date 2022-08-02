# Example #1 Ternary Operator
is_good = False
dragon = "Tootless" if is_good else "Smaug"
print(dragon)


# Example #2 Random Numbers
# import random
# dragons = ['Puff', 'Toothless', 'Falkor', 'Draco']
# # dragonPick = dragons[random.randint(0, len(dragons) - 1)]
# dragonPick = random.choice(dragons)
# print(dragonPick)


# Example #3 User Input
# answer = input('Who is the coolest dragon? ')
# print(f'You thought {answer} was the coolest dragon...')


# Example #4 Reading Files
# f = open("words.txt", "r")
# words = [ data.split(',') for data in f ][0]
# print(words)


# Example #5 List.map and Lambda
# array1 = [1, 4, 9, 16] 
# # map1 = map(lambda x: x * 2, array1)
# # print(list(map1))
# map2 = [ x * 2 for x in array1 ]
# print(map2)





# Example #6 Classes
class Book:
    def __init__(self, title, series, author):
        self.title = title
        self.series = series
        self.author = author

    def get_information(self):
        # if self.title == "Two Towers":
        #     pass
        # else:
        return f'{self.title} by {self.author}'

    def new_method(self):  
        pass

book = Book("Two Towers", 'Lord of the Rings', 'JRR Tolkien');
print(book.get_information())




# Example #7 Routes  (can't test)
@app.route('/item/<id>')
def item(id):
    return f'<h1>Item ID:{id}</h1>'

