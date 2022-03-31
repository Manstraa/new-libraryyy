my_books=['Sefiller , Semerkant , Golgedekiler']
def bookkkks () :
    password=input('Enter Password : ')
    if password==78 :
        print('Welcome to Books Library')
        print('Kitaplar Herzaman Sinemadan Daha Etkilidir , Cunku Okuyucuya Birsey Gostermez  !')
        print('Your Book List:{0}').format(my_books)
    process=input('Enter For Add : 1 , Enter For Delete : 2')
    if process==1 :
        add=input('Enter  the Book You Want to Add')
        if add in my_books:
            print('Already Available')
        else:
            my_books.append(add)
            print('Your New Book List : {0}').format(my_books)
    else:
        delete=input('Enter the  Book You Want to Delete')
        if delete in my_books :
            my_books.remove(delete)
            print('Your New Book List : {0}').format(my_books)
        else:
            print('Not Listed')