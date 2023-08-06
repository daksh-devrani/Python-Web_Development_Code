from miestoneProject4BookScraping.app import books

user_input='''Select from the following options:
'b'- to look at the 5 best rated books
'c'- to look at the 5 cheapest books
'n'- to look at the next book from the catalogue
'q'- to quit the menu
Enter your choice: '''

def best_book():
    best_book=sorted(books , key=lambda x: x.rating * -1)[:5]
    for book in best_book:
        print(book)


def cheapest_book():
    cheapest_book=sorted(books , key=lambda x: x.price)[:5]
    for book in cheapest_book:
        print(book)


def menu():
    user_choice=input(user_input)
    i=0
    while user_choice !='q':
        if user_choice=='b':
            best_book()

        elif user_choice=='c':
            cheapest_book()

        elif user_choice=='n':
            print(books[i])
            i+=1

        user_choice=input(user_input)

menu()