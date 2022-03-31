my_movies=['Recep Ivedik']
def moviess () :
    password=input('Enter Password : ')
    if password==77 :
        print('Welcome to Movies Library')
        print('Your Movie List:{0}').format(my_movies)
    process=input('Enter For Add : 1 , Enter For Delete : 2')
    if process==1 :
        add=input('Enter  the Movie You Want to Add')
        if add in my_movies:
            print('Already Available')
        else:
            my_movies.append(add)
            print('Your New Movie List : {0}').format(my_movies)
    else:
        delete=input('Enter the Movie You Want to Delete')
        if delete in my_movies :
            my_movies.remove(delete)
            print('Your New Movie List : {0}').format(my_movies)
        else:
            print('Not Listed')
