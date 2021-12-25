#Team Identifier: T004
#Authors: Morgan Pleet (101224360), Jeremy Hornung (101219284), Zane Labonte-Hagar (101239002), Suren Kulasegaram (101220595)
#Date: 10/12/2021
#Version: 1.0

#Function 1: print_dictionary_category
def print_dictionary_category(category: str, dictionary: dict) -> int:
    """
    Author: Morgan Pleet, 101224360
    Returns the number of books associated with the specified 'category', given the 'dictionary' where the books are located, as well as a list of all books within the 'category' specified. 
    
    >>> print_dictionary_category('Fiction', book_dictionary)
    The category Fiction has 39 books. This is the list of books in the category Fiction :
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288}]
    [{'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 544}]
    [{another element}]
    ...
    [{another element}]
    >>> print_dictionary_category('Children', book_dictionary)
    The category Children has 0 books
    
    """
    book_list = []
    
    if category in dictionary:
        book_list = dictionary.get(category)
        print("The category", category, "has",  len(book_list), "books. This is the list of books in the category", category, " : ")    
        for book in book_list:
            print([book])        
    else: #The book does not exist if the category is not a key of the dictionary, and thus there are no books in the category specified
        print('The category', category, 'has 0 books')
    return len(book_list)


#Function 2: add_book
def add_book(dictionary: dict, book_information: tuple) -> dict:
    """
    Author: Morgan Pleet, 101224360
    Returns a new dictionary given the 'dictionary' where the 'book_information' must be added. The 'book_information' contains seven values; the title, author, language, publisher, category, rating and page count of the book- and confims that the book has been added to the 'dictionary' successfuly. 
    
    >>> add_book(dataset, ('The Dark Hours', 'Michael Connolly', 'English', 'Random House', 'Fiction', 4.6, 367))
    The book has been added correctly.
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288}, {all other elements in the category Fiction}, {'title': 'The Dark Hours', 'author': 'Michael Connolly', 'rating': 4.6, 'publisher': 'Random House', 'page_count': 367, 'language': 'English'}, {all other elements in the dictionary}]
    >>> add_book(dataset, ('A Diary of a Wimpy Kid', 'Jeff Kinney', 'English', 'Amulet Books', 'Children', 5.0, 213))
    The book has been added correctly.
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288}, {all other elements in the dictionary}], 'Children': [{'title': 'A Diary of a Wimpy Kid', 'author': 'Jeff Kinney', 'language': 'English', 'rating': 5.0, 'publisher': 'Amulet Books', 'page_count': 213}]}

    """
    
    title = book_information[0]
    author = book_information[1]
    language = book_information[2]
    publisher = book_information[3]
    category = book_information[4]
    rating = book_information[5]
    page_count = book_information[6]
    
    books_of_category = dictionary.get(category)
   
    book = {'title': title, 'author': author, 'language': language, 'rating': rating, 'publisher': publisher,'page_count': page_count}
    
    if category in dictionary:
        if book in dictionary.get(category): #check to see if the book is already in the dictionary - if so, it does not need to be added again
            print('There was an error adding the book - this book is already in the dictionary.')
        else:
            dictionary[category].append(book)
            book_in_category = book in dictionary.get(category)
            if book_in_category:
                print('The book has been added correctly.')
            else:
                print('There was an error adding the book.')
    else:
        dictionary.update({category:[book]})
        book_in_category = book in dictionary.get(category)
        if book_in_category: 
            print('The book has been added correctly.')
        else:
            print('There was an error adding the book.')        
    return dictionary   


#Function 3: remove_book
def remove_book(title_book: str, category: str, dictionary: dict) -> dict:
    """
    Author: Morgan Pleet, 101224360
    Returns an updated version of the 'dictionary', after having removed the book specified by the 'title_book' and 'category' from the 'dictionary'.
    
    >>> remove_book("Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Fiction', dataset)
    {'Fiction': [{'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 544}, {all other elements in the dictionary}]}
    >>> remove_book('Yesterday', 'Mystery', DATASET)
    There was an error removing the book. Book not found
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288}, {all other elements within the original dictionary}]} 
    
    """
    

    if category in dictionary: #if category is in the dictionary, the title of the book must be checked to verify if the book exists.
        book_list = dictionary.get(category) #creates a list of all of the elements wthin the category specified
        for book in book_list: #each book is a dictionary with one value per key
            if title_book == book.get('title'):
                book_list.remove(book)
                print('The book has been removed correctly')
                return dictionary
    
    print('There was an error removing the book. Book not found')    
    return dictionary  
            

#Function 4: get_books_by_rate
def get_books_by_rate(rating: int, book_dictionary_by_genre: dict[str, list[dict[str, object]]]) -> dict[int, list[dict[str, object]]]:
    """
    Author: Jeremy Hornung, 101219284
    Precondition: 0 <= rating <= 5
    Returns a dictionary where the sole key is "rating" and the sole value is a list of dictionaries. Each dictionary within the list represents a book from within "book_dictionary_by_genre" with a rating in the range "rating" (inclusive) to "rating" + 1 (exclusive). Every book in "book_dictionary_by_genre" with a rating within the specified range will be included in the list, however books will not be repeated. The function will also print the details of these books to the user (see examples for the format in which it will be printed).
    
    >>> #example 1:
    >>> from T004_load_data import load_dataset
    ... book_dictionary_by_genre = load_dataset('Google_Books_Dataset.csv')
    ... book_dictionary_by_rating = get_books_by_rate(2, book_dictionary_by_genre)
    ...
    
    >>> book_dictionary_by_rating
        {2: []}
    
    
    >>> #example 2:
    >>> from T004_load_data import load_dataset
    ... book_dictionary_by_genre = load_dataset('Google_Books_Dataset.csv')
    ... book_dictionary_by_rating = get_books_by_rate(5, book_dictionary_by_genre)
    ... 
    
        Title: "Final Option: 'The best one yet'"
        Author: "Clive Cussler"
        Language: "English"
        Rating: 5.0
        Publisher: "Penguin UK"
        Category: "Fiction"
        Page Count: 400
        
        ...
        
        Title: "No One Is Too Small to Make a Difference"
        Author: "Greta Thunberg"
        Language: "English"
        Rating: 5.0
        Publisher: "Penguin"
        Category: "Biography"
        Page Count: 112

    >>> book_dictionary_by_rating
        {5: [{'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'language': 'English', 'rating': 5.0, 'publisher': 'Penguin UK', 'page_count': 400, 'category': 'Fiction'}, ..., {'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg', 'language': 'English', 'rating': 5.0, 'publisher': 'Penguin', 'page_count': 112, 'category': 'Biography'}]}
    """
    book_dictionary_by_rating = {rating: []}
    
    if rating == 0:
        rating = None
    
    for genre, books in book_dictionary_by_genre.items():
        for book in books:
            already_found = False
            
            for book2 in book_dictionary_by_rating[rating or 0]:
                if book2['title'] == book['title']:
                    already_found = True
                    
            if not already_found and ((bool(book['rating']) == False == bool(rating)) or (type(rating) == int and type(book['rating']) == float and rating <= book['rating'] < rating + 1)):
                
                book.update({'category': genre})
                
                book_dictionary_by_rating[rating or 0].append(book)
    
    print()

    for book in book_dictionary_by_rating[rating or 0]:
        print('Title:', '"' + book['title'] + '"')
        print('Authors:', '"' + book['author'] + '"')
        print('Language:', '"' + book['language'] + '"')
        print('Rating:', book['rating'] or 0)
        print('Publisher:', '"' + book['publisher'] + '"')
        print('Category:', '"' + book['category'] + '"')
        print('Page Count:', book['page_count'], '\n')
        
    return book_dictionary_by_rating


#Function 5: find_books_by_title
def find_books_by_title(title: str, book_dictionary_by_genre: dict[str, list[dict[str, object]]]) -> bool:
    """
    Author: Jeremy Hornung, 101219284
    Returns True if the book with the title "title" is within "book_dictionary_by_genre" and False if it is not. Will also print whether or not the book is found within "book_dictionary_by_genre".
    
    >>> #example 1:
    >>> from T004_load_data import load_dataset
    ... book_dictionary_by_genre = load_dataset('Google_Books_Dataset.csv')
    ... found = find_books_by_title("Final Option: 'The best one yet'", book_dictionary_by_genre)
    ...
        The book has been found
    >>> found
        True
        
        
    >>> #example 2:
    >>> from T004_load_data import load_dataset
    ... book_dictionary_by_genre = load_dataset('Google_Books_Dataset.csv')
    ... found = find_books_by_title("Harry Potter and the Goblet of Fire", book_dictionary_by_genre)
    ...
    
        The book has NOT been found
    >>> found
        False
    """
    found = False
    
    for books in book_dictionary_by_genre.values():
        for book in books:
            if book['title'] == title:
                found = True

    if found:
        print('\nThe book has been found')
    else:
        print('\nThe book has NOT been found')
        
    return found


#Function 6: get_books_by_author
def get_books_by_author(author_full_name: str, book_dictionary_by_genre: dict[str, list[dict[str, object]]]) -> list[str]:
    """ 
    Author: Jeremy Hornung, 101219284
    Returns a list containing the titles of all books written by "author_full_name" that our stored within "book_dictionary_by_genre". Each book will only appear in the list once. The function will also print out these books (see examples for the format in which it will be printed).
    
    >>> #example 1:
    >>> from T004_load_data import load_dataset
    ... book_dictionary_by_genre = load_dataset('Google_Books_Dataset.csv')
    ... books_by_author = get_books_by_author('J. R. R. Tolkien', book_dictionary_by_genre)
    ...
    
        The author “J. R. R. Tolkien” has published the following books:
    >>> books_by_author
        []
        
        
    >>> #example 2:
    >>> from T004_load_data import load_dataset
    ... book_dictionary_by_genre = load_dataset('Google_Books_Dataset.csv')
    ... books_by_author = get_books_by_author('Barbara Allan', book_dictionary_by_genre)
    ...
    
        The author “Barbara Allan” has published the following books:
        1- Antiques Chop
        2- Antiques Roadkill: A Trash 'n' Treasures Mystery
        3- Antiques Knock-Off
        4- Antiques Con
    >>> books_by_author
        ['Antiques Chop', "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Antiques Knock-Off', 'Antiques Con']
    """
    books_by_author = set()
    
    for books in book_dictionary_by_genre.values():
        for book in books:
            if book['author'] == author_full_name:
                books_by_author.add(book['title'])
                
    print('\nThe author “' + author_full_name + '” has published the following books:')
    
    i = 1
    for title in books_by_author:
        print(i, '- ', title, sep = '')
        i += 1
        
    return list(books_by_author)

# Function 7: get_books_by_publisher
def get_books_by_publisher(publisher: str, book_data: dict[str, list[dict[str, object]]]) -> list[str]:
    """ 
    Author: Zane Labonte-Hagar (101239002)
    Returns a list of book names published by the given publisher, taken from
    the given dictionary of Google Books Dataset information. Also prints the 
    books to the terminal as shown in the examples below.
    
    >>> get_books_by_publisher("AMACOM", books_dataset)
    The publisher "AMACOM" has published the following books:
    1 -  Personal Success (The Brian Tracy Success Library)
    2 -  Management (The Brian Tracy Success Library)
    3 -  Business Strategy (The Brian Tracy Success Library)
    4 -  Marketing (The Brian Tracy Success Library)
    5 -  The Essentials of Finance and Accounting for Nonfinancial Managers
    ['Personal Success (The Brian Tracy Success Library)', 'Management (The Brian Tracy Success Library)', 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'Business Strategy (The Brian Tracy Success Library)', 'Marketing (The Brian Tracy Success Library)']
    >>> get_books_by_publisher("DC", books)
    The publisher "DC" has published the following books:
    1 -  Young Justice Vol. 1
    2 -  The Joker
    ['Young Justice Vol. 1', 'The Joker']
    """
    
    # Although a set may seem more applicable here to avoid duplicates, we must 
    # check if the collection contains the book title anyway so that it is not printed twice.     
    titles = []
    
    print('The publisher "', publisher, '" has published the following books:', sep = '')
    
    i = 1 # Used for printed list counter
    for book_list in book_data.values():
        for book in book_list:
            if book.get("publisher") == publisher:
                title = book["title"]
                if title not in titles:
                    # Ensure not to add duplicates to list and to not print twice
                    titles.append(title)
                    print(i, "- ", title, sep='')
                    i += 1
                    
    return titles
        
# Function 8: check_category_and_title
def check_category_and_title(category: str, title: str, book_data: dict[str, list[dict[str, object]]]) -> bool:
    """ 
    Author: Zane Labonte-Hagar (101239002)
    Returns True if and only if the given category exists and contains a book with the given title, within
    the dictionary of Google Books Dataset information. Also prints a statement of whether or 
    not the given category contains a book with the given title, as shown in the examples below.
    
    >>> check_category_and_title("Fiction", "Antiques Con", books_dataset)
    The category "Fiction" has the book title "Antiques Con".
    True
    >>> check_category_and_title("Non Fiction", "Antiques Con", books_dataset)
    The category "Non Fiction" does not have the book title "Antiques Con".
    False
    >>> check_category_and_title("Mystery", "The Mysterious Affair at Styles", books_dataset)
    The category "Mystery" does not have the book title "The Mysterious Affair at Styles".
    False
    """
    
    contains = False
    
    book_list = book_data.get(category)
    if book_list != None:
        i = 0
        length = len(book_list)
        while (not contains and i < length):
            if book_list[i]["title"] == title:
                # Stop looping once an instance of the book title is found
                contains = True
                
            i += 1

    if contains:
        words = "has"
    else:
        words = "does not have"
    print('The category "', category, '" ', words, ' the book title \"', title, '".', sep = '')
    
    return contains

# Function 9: all_categories_for_book_title
def all_categories_for_book_title(title: str, book_data: dict[str, list[dict[str, object]]]) -> list[str]:
    """
    Author: Zane Labonte-Hagar (101239002)
    Returns a list of categories which the given book title belongs to, from
    the given dictionary of Google Books Dataset information. Also prints the list
    of categories it belows to as shown in the examples below.
    
    >>> all_categories_for_book_title("Sword of Destiny: Witcher 2: Tales of the Witcher", books_dataset)
    The book title “Sword of Destiny: Witcher 2: Tales of the Witcher” has the following categories:
    1-  Fiction 
    2-  Adventure 
    3-  Mythical Creatures
    ['Fiction', 'Adventure', 'Mythical Creatures']
    >>> all_categories_for_book_title("Watchmen (2019 Edition)", books_dataset)
    The book title “Watchmen (2019 Edition)” has the following categories:
    1- Superheroes
    2- Comics
    ['Comics', 'Superheroes']
    """
    
    # Although a set may seem more applicable here to avoid duplicates, we must 
    # check if the collection contains the category anyway so that it is not printed twice. 
    categories = [] 
    
    print('The book title "', title, '" has the following categories:', sep = '')
    i = 1 # Number counter for the printed list
    for cat, books in book_data.items():
        for book in books:
            if book['title'] == title:
                if cat not in categories:
                    # Ensure category is not added/printed twice
                    categories.append(cat)
                    print(i, '- ', cat, sep='')
                    i += 1
                    
    return categories

#Function 10: get_books_by_category
def get_books_by_category(category: str, book_dictionary: dict) -> list[str]:
    """
    Author: Suren Kulasegaram, 101220595
    Function takes in a string which will be the desired category and the key
    to the dictionary where their desired book are stored and the 
    dictionary the books are stored in. The function will return a list of 
    strings where each element is the title of the books in their desired 
    category
    
    >>> from T004_load_data import load_dataset
    >>> get_books_by_category("", load_dataset(FILENAME))
    []
    >>> get_books_by_category("Comics", load_dataset(FILENAME))
    ['Deadpool Kills the Marvel Universe', 'Young Justice Vol. 1', 'Ultimate Spider-Man Vol. 11: Carnage', 'Immortal Hulk Vol. 1: Or Is He Both?', 'Watchmen (2019 Edition)', 'The Joker', 'Venomized']
    >>> get_books_by_category("Comic", load_dataset(FILENAME))
    []
    >>> get_books_by_category("comic", load_dataset(FILENAME))
    []
    >>> get_books_by_category("Investing", load_dataset(FILENAME))
    ['The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further']
    """
    
    book_titles_list_in_category = []       #variable to be returned
    
    books_in_category = book_dictionary.get(category, [])
    #using [] as return if category does not exist as key so when 
    #books_in_category is iterated, through in coming for loop, it won't cause
    #a error and will iterate 0 times 
    
    #printing each book in category
    for book in books_in_category:
        book_titles_list_in_category.append(book.get('title'))
    
    print('The category "', category,'" has the following books:', sep='')
    #printing valid titles to screen
    for i in range(len(book_titles_list_in_category)):
        print(i+1, ' - ', book_titles_list_in_category[i], sep='')
      
    
    return book_titles_list_in_category

#Function 11: get_book_by_category_and_rate
def get_book_by_category_and_rate(category: str, rating: int, 
                                  book_dictionary: dict) -> list[str]:
    """
    Author: Suren Kulasegaram, 101220595
    Takes in a string as the desired category and its also the key to the 
    dictionary where the desired books are, also takes a positive integer
    argument as the rating and the dictionary the books are stored in, and 
    returns a list of all book titles as strings which are in the given category
    and their rating is equal or greather than given rating argument and less 
    than the given rating + 1.
    
    >>> from T004_load_data import load_dataset
    >>> get_book_by_category_and_rate('comic', 4, load_dataset(FILENAME))
    []
    >>> get_book_by_category_and_rate('Comics', 4, load_dataset(FILENAME))
    ['Deadpool Kills the Marvel Universe', 'Young Justice Vol. 1', 'Ultimate Spider-Man Vol. 11: Carnage', 'Immortal Hulk Vol. 1: Or Is He Both?', 'Watchmen (2019 Edition)', 'The Joker', 'Venomized']
    >>> get_book_by_category_and_rate('Comics', 5, load_dataset(FILENAME))
    []
    >>> get_book_by_category_and_rate('Comics', 3, load_dataset(FILENAME))
    []
    >>> get_book_by_category_and_rate('Comics', 2, load_dataset(FILENAME))
    []
    >>> get_book_by_category_and_rate('Comics', 1, load_dataset(FILENAME))
    []
    >>> get_book_by_category_and_rate('Comics', 0, load_dataset(FILENAME))
    []
    >>> get_book_by_category_and_rate('', 4, load_dataset(FILENAME))
    []
    >>> get_book_by_category_and_rate('Business', 0, load_dataset(FILENAME))   #testing unrated novels since their value was assumed to be 0 in function
    ['Business Strategy (The Brian Tracy Success Library)', 'Personal Success (The Brian Tracy Success Library)', 'Summary: Think and Grow Rich', 'The Essentials of Finance and Accounting for Nonfinancial Managers']
    """
    
    book_titles_list_in_category = []       #variable to be returned
    
    books_in_category = book_dictionary.get(category, [])
    #using [] as return if category does not exist as key so when 
    #books_in_category is iterated, through in coming for loop, it won't cause
    #a error and will iterate 0 times 
    
    #adding each book in category and rating interval to list
    for book in books_in_category:
        #some ratings are None if they were empty in file so assuming that rate 
        #is 0.0 for comparison
        if book.get('rating') == None:
            current_book_rate = 0.0
        else: 
            current_book_rate = book.get('rating')
            
        if rating <= current_book_rate and (rating + 1) > current_book_rate:
            book_titles_list_in_category.append(book.get('title'))
    
    print('The category "', category,'" and rate ', rating, 
          ' has the following books:', sep='')   
    #printing valid title to screen
    for i in range(len(book_titles_list_in_category)):
            print(i+1, ' - ', book_titles_list_in_category[i], sep='')          
    
    return book_titles_list_in_category    
    
#Function 12: get_author_categories
def get_author_categories(author: str, book_dictionary: dict) -> list[str]:
    """
    Author: Suren Kulasegaram, 101220595
    Returns a list of strings which are the categories an author has written 
    under when provided an author name as a string, and a dictionary with the 
    books
    
    >>> from T004_load_data import load_dataset
    >>> get_author_categories('Blake Pierce', load_dataset(FILENAME))
    ['Detective', 'Fiction', 'Mystery', 'Thrillers']
    >>> get_author_categories('Cullen Bunn', load_dataset(FILENAME))
    ['Comics']
    >>> get_author_categories('', load_dataset(FILENAME))
    []
    get_author_categories('Cullen bunn', load_dataset(FILENAME))
    []
    get_author_categories('B A Paris', load_dataset(FILENAME))
    ['Crime', 'Fiction', 'Thrillers']
    """
    #initially saving in a set to avoid duplicates 
    author_categories_list = set() 
    
    for category in book_dictionary:
        for i in range(len(book_dictionary[category])):
            if author == book_dictionary[category][i]['author']:
                author_categories_list.add(category)    #adding to set
    
    #converting to set to list to be used in specific manner in for loop and returned
    author_categories_list = list(author_categories_list)
    
    #sorting list alphabetically for easier testing since sets are unordered
    if len(author_categories_list):
        for i in range(len(author_categories_list)-1):  #doesn't need to hit last index since j will be last and i will be second last
            for j in range(i + 1, len(author_categories_list)):
                if author_categories_list[i] > author_categories_list[j]:     #the smaller the ascii value, the further up alpahbet it is
                    author_categories_list[j], author_categories_list[i] = author_categories_list[i], author_categories_list[j] #switching places
    
    print('The author "', author, '" has published books under the following categories:', sep='')
    
    #printing categories author has written as, since the list was originally a
    #set, the values are unordered.
    if len(author_categories_list):
        for i in range(len(author_categories_list)):
            print(i+1, '-', author_categories_list[i])
    else: 
        print('\tNo books were found by this author.')
    return author_categories_list