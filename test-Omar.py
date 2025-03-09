books = ['book1', 'book2', 'book3', 'book4', 'book5']
exit = False

def display(list):
    for i in list:
        print(list[i])

print('allowed operations are \n  view \n add \n remove  \n search \n exit')
temp = input('please select your desired operation')

if temp == 'view':
    display(books)