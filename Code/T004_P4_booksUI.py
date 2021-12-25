# ECOR 1042 Lab 4: Group submission
# Team Identifier: T004
# Authors: Zane Labonte-Hagar (101239002), Suren Kulasegaram (101220595), Morgan Pleet (101224360), Jeremy Hornung (101219284)
# Date: 10/12/2021
# Version: 1.0

# IMPORTS
from P5_T004_load_dataset import load_dataset
from T004_P2_search_modify_dataset import *  # A function-only library, from which all functions are used
from T004_P3_sorting import *                # A function-only library, from which all functions are used
 
# Main prompt
MENU = """1- Command Line L)oad file
2- Command Line A)dd book
3- Command Line R)emove book
4- Command Line F)ind book by title
5- Command Line NC) Number of books in a category
6- Command Line CA) Categories for an author
7- Command Line CB) Categories for a book title
8- Command Line G)et book
    R)ate A)uthor P)ublisher C)ategory
    CT) Category and Title CR) Category and Rate
9- Command Line S)ort book
    T)itle R)ate P)ublisher C)ategory PA)ageCount
10- Command line Q)uit

: """

# Prompt for sort subcommands
SORT_UI = """
    1- Command Line sort by T)itle
    2- Command Line sort by R)ate
        A)scending    D)escending
    3- Command Line sort by P)ublisher
    4- Command Line sort by C)ategory
    5- Command Line sort by PA)ageCount

: """

# Prompt for direction of rating sort
SORT_BY_RATE_UI = """    1- Command Line sort by A)scending rate
    2- Command Line sort by D)escending rate

: """

COMMANDS = {'L', 'A', 'R', 'F', 'NC', 'CA', 'CB', 'G', 'S'}
SORT_COMMANDS = {'T', 'R', 'P', 'C', 'PA'}
SORT_BY_RATE_COMMANDS = {'A', 'D'}    

# FUNCTION DEFINITIONS
def main_cmd() -> None:
    """
    Authors: Zane Labonte-Hagar (101239002), Suren Kulasegaram (101220595)
    Starts an interactive terminal UI to allow the user to load, search, and modify
    a Google Books Dataset CSV file. Informs the user of valid commands and
    repeatedly prompts the user to run a command until they quit.
    """
    
    dataset = None
    
    cmd = input(MENU).upper()
    while cmd != 'Q':
        
        if cmd not in COMMANDS:
            print('No such command')
    
        elif cmd == 'L':
            # Author: Morgan Pleet (101224360)
            dataset = load_cmd()
        
        elif dataset == None:
            print('No file loaded')
            
        elif cmd == 'A':
            # Author: Morgan Pleet (101224360)
            adding_books_cmd(dataset)
        
        elif cmd == 'R':
            # Author: Morgan Pleet (101224360)
            removing_books_cmd(dataset)
        
        elif cmd == 'F':
            # Author: Morgan Pleet (101224360)
            title = input('Enter the title of the book you wish to search for: ')
            find_books_by_title(title, dataset)     
        
        elif cmd == 'NC':
            # Author: Suren Kulasegaram (101220595)
            print_dictionary_category(input('Please enter category name: '), dataset)
        
        elif cmd == 'CA':
            # Author: Suren Kulasegaram (101220595)
            get_author_categories(input('Please enter a author name: '), dataset)
        
        elif cmd == 'CB':
            # Author: Suren Kulasegaram (101220595)
            all_categories_for_book_title(input('Please enter a book title: '), dataset)
        
        elif cmd == 'G':
            # Author: Zane Labonte-Hagar (101239002)
            get_book_cmd(dataset)
        
        elif cmd == 'S':
            # Author: Jeremy Hornung (101219284)
            sort_cmd(dataset)
        
        #separating result from previous command and prompt for next instruction
        print('\n--------------------------------\n')
        cmd = input(MENU).upper()        
    
    # User has entered quit, Author: Suren Kulasegaram (101220595)
    print("Goodbye")


def load_cmd() -> dict[str, list[dict[str, object]]]:
    """
    Author: Morgan Pleet (101224360)
    Prompts the terminal for a Google Books Dataset CSV file, and returns a dictionary
    with keys of categories and values of lists of dictionaries (each a book entry).
    
     ---user enters l/L when promted for a comand, load_file is called---
     >>> load_file()
     Please enter a file name: Google_Books_Dataset.csv
     
     Dataset loaded
     #What will be displayed as a result of the call on load_dataset
     {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288}, ... {all other elements within the given file}]}
     
    """
    
    file_name = input('Please enter a file name: ')
    print("Dataset loaded")
    return load_dataset(file_name)

def adding_books_cmd(dataset_loaded: dict[str, list[dict[str, object]]]) -> None:
    """
    Author: Morgan Pleet (101224360)
    Prompts the user for everything required to construct full metadata for a book.
    Adds the new book to the given dataset after the prompting is finished.
    
     
     ---user enters a/A when promted for a comand, adding_books is called (after a file has been loaded)---
     >>> adding_books(dataset)
     Enter the title of the book you wish to add: Once Upon a Time
     Enter the author of the book you wish to add: Hailey Scott
     Enter the language of the book you wish to add: English
     Enter the publisher of the book you wish to add: Eagles Nest
     Enter the category/genere of the book you wish to add: Mystery
     Enter the rating of the book you wish to add: 4.0
     Enter the page count of the book you wish to add: 544
     
     #What will be displayed as a result of the call on add_book
     The book has been added correctly 
     
     {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288}, ... {all other elements within the category Fiction, and before the category Mystery}], 'Mystery': [{all elements within the category Mystery}, {'title': 'Once Upon a Time', 'author': 'Hailey Scott', 'language': 'English', 'rating': 4.0, 'publisher': 'Eagles Nest', 'page_count': 544}], ... {all other elements within the dataset}]}
     
    """
    
    dictionary = dataset_loaded
    title = input('Enter the title of the book you wish to add: ')
    author = input('Enter the author of the book you wish to add: ')
    language = input('Enter the language of the book you wish to add: ')
    publisher = input('Enter the publisher of the book you wish to add: ')
    category = input('Enter the category/genere of the book you wish to add: ')
    rating = float(input('Enter the rating (positive integer between 0-5) of the book you wish to add: '))
    page_count = int(input('Enter the page count of the book you wish to add: '))
    
    book_information = (title, author, language, publisher, category, rating, page_count)
    add_book(dictionary, book_information)

def removing_books_cmd(dataset_loaded: dict[str, list[dict[str, object]]]) -> None:
    """
    Author: Morgan Pleet (101224360)
    Prompts the user to enter the title and category of the book they wish to remove, and removed the respective book from the given 'dataset'.
     
     ---user enters r/R when promted for a comand, removing_books is called (after a file has been loaded)---
     >>> removing_books(dataset)
     Enter the title of the book you wish to remove: Antiques Roadkill: A Trash 'n' Treasures Mystery
     Enter the category of the book you wish to remove: Fiction
     
     #What will be displayed as a result of the call on remove_book
     The book has been removed correctly
     
     {'Fiction': [{'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 544}, {all other elements in the dataset}]}
     
     ---user enters r/R when promted for a comand, removing_books is called (after a file has been loaded)---
     >>> removing_books(dataset)
     Enter the title of the book you wish to remove: Charlie and the Chocolate Factory
     Enter the category of the book you wish to remove: Children
     
     #What will be displayed as a result of the call on remove_book
     There was an error removing the book. Book not found
     
     {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288}, {all other elements within the original dataset}]} 
    
    """    
    
    title = input('Enter the title of the book you wish to remove: ')
    category = input('Enter the category of the book you wish to remove: ')
    remove_book(title, category, dataset_loaded)                

def get_book_cmd(dataset: dict[str, list[dict[str, object]]]) -> None:
    """
    Author: Zane Labonte-Hagar (101239002)
    Prompts the user to enter a subcommand of Get book, and any command arguments necessary.
    The user is only given one chance to enter a valid subcommand. 
    """
    
    cmd = input("Enter a Get book subcommand: ").upper()
    if cmd == "R": # Rating
        rate = input("Enter a positive integer rating to search for: ").strip()
        rate = parse_unsigned_int(rate)
        if rate != None:
            get_books_by_rate(rate, dataset)
        
    elif cmd == "A": # Author
        author = input("Enter an author to search for: ")
        get_books_by_author(author, dataset)
        
    elif cmd == "P": # Publisher
        publisher = input("Enter a publisher to search for: ")
        get_books_by_publisher(publisher, dataset)
        
    elif cmd == "C": # Category
        category = input("Enter a category to get books from: ")
        get_books_by_category(category, dataset)
        
    elif cmd == "CT": # Category and title
        category = input("Enter a category to get books from: ")
        title = input("Enter a book title to search for: ")
        check_category_and_title(category, title, dataset)
        
        
    elif cmd == "CR": # Category and rate
        category = input("Enter a category to get books from: ")
        rate = parse_unsigned_int(input("Enter a positive integer rating to search for: "))
        if rate != None:
            get_book_by_category_and_rate(category, rate, dataset)
            
    else:
        print("No such sub command")
        
def parse_unsigned_int(number: str) -> int:
    """
    Author: Zane Labonte-Hagar (101239002)
    Returns an integer from a clean string representation of an integer. If the string
    cannot be parsed into an int, None is returned, and "Not a positive integer" is printed.
    
    >>> parse_unsigned_int("-2")
    None
    >>> parse_unsigned_int("0")
    0
    >>> parse_unsigned_int("3")
    3
    >>> parse_unsigned_int("3 ") 
    None
    >>> parse_unsigned_int("3.0") 
    None
    """
    
    if number.isdigit():
        return int(number)
    else:
        print("Not a positive integer")
        return None

#defining function to interact with the user when they want to sort the dataset
def sort_cmd(dataset: dict[str, list[dict[str, object]]]) -> list[dict[str, object]]:
    """
    Author: Jeremy Hornung
    Student Number: 101219284
    
    Returns the information from within the "datset", but sorted in the way the user would like, specified by user input within this function. A couple of examples of this function's user interactions are below. For examples of the format in which the "dataset" will be sorted, see the examples from within the functions in the module "T004_P3_sorting".
    
    >>> #example 1:
    
        ...
    
    >>> sorted_by_x_dataset = sort(<dataset>)
    
            1- Command Line sort by T)itle
            2- Command Line sort by R)ate
                A)scending    D)escending
            3- Command Line sort by P)ublisher
            4- Command Line sort by C)ategory
            5- Command Line sort by PA)ageCount

        : 5
        
        No such command
        
            1- Command Line sort by T)itle
            2- Command Line sort by R)ate
                A)scending    D)escending
            3- Command Line sort by P)ublisher
            4- Command Line sort by C)ategory
            5- Command Line sort by PA)ageCount

        : t
        
        <calls the "sort_books_title" function with the <dataset> as the sole argument, so see the examples from that function in the "T004_P3_sorting" module to see what would be output here>
        
    >>> sorted_by_x_dataset
        
        <again, see the examples from the "sort_books_title" function in the "T004_P3_sorting" module to see potentiel outputs (the output here would be the return value from the "sort_books_title" function)>
        
    >>> #------------------------------------------------------------------------------------------------------------------
    >>>
    >>> example 2:
    
        ...
        
    >>> sorted_by_x_dataset = sort(<dataset>)

            1- Command Line sort by T)itle
            2- Command Line sort by R)ate
                A)scending    D)escending
            3- Command Line sort by P)ublisher
            4- Command Line sort by C)ategory
            5- Command Line sort by PA)ageCount

        : R
        
        <calls the "sort_by_rate" function with the <dataset> as the sole argument, so see the examples from that function (below) to see what would be output here>
        
    >>> sorted_by_x_dataset
        
        <to see what would be output here, see the examples from both the "sort_books_ascending_rate" and "sort_books_descending_rate" functions in the "T004_P3_sorting" module (the output here would be the return value from one of those functions). There are two potential functions you need to look at here because either one could be called from within the "sort_by_rate" function, dependant on user input within that function>
                
    """
        
    #get user input (which command they would like to execute)
    sort_command = input(SORT_UI).upper()
    #allows the user to enter a command again if the command entered was invalid
    while sort_command not in SORT_COMMANDS:
        print('\nNo such command')
        sort_command = input(SORT_UI).upper()
    
    #initializing list to store the sorted dataset when it is returned
    sorted_data = []
    
    #calls the function that will sort the dataset in the requested manner
    print() #for aesthetics
    if sort_command == 'T':
        sorted_data = sort_books_title(dataset)
    elif sort_command == 'R':
        sorted_data = sort_by_rate_cmd(dataset)
    elif sort_command == 'P':
        sorted_data = sort_books_publisher(dataset)
    elif sort_command == 'C':
        sorted_data = sort_books_category(dataset)
    elif sort_command == 'PA':
        sorted_data = sort_books_pageCount(dataset)
    
    #returns the sorted dataset
    return sorted_data

#defining function to interact with the user when they want to sort the dataset by rate
def sort_by_rate_cmd(dataset: dict[str, list[dict[str, object]]]) -> list[dict[str, object]]:
    """
    Author: Jeremy Hornung
    Student Number: 101219284
    
    Returns the information from within the "datset", but sorted by either ascending or desending rate, which is specified by user input within this function. A couple of examples of this function's user interactions are below. For examples of the format in which the "dataset" will be sorted, see the examples from within the functions "sort_books_ascending_rate" and "sort_books_descending_rate", in the module "T004_P3_sorting".
    
    >>> #example 1:
    
        ...
    
    >>> sorted_by_rate_dataset = sort_by_rate(<dataset>)
            1- Command Line sort by A)scending rate
            2- Command Line sort by D)escending rate

        : x
        
        No such command
        
            1- Command Line sort by A)scending rate
            2- Command Line sort by D)escending rate

        : A
        
        <calls the "sort_books_ascending_rate" function with the <dataset> as the sole argument, so see the examples from that function in the "T004_P3_sorting" module to see what would be output here>
        
    >>> sorted_by_x_dataset
        
        <again, see the examples from the "sort_books_ascending_rate" function in the "T004_P3_sorting" module to see potentiel outputs (the output here would be the return value from the "sort_books_ascending_rate" function)>
        
    >>> #------------------------------------------------------------------------------------------------------------------
    >>>
    >>> example 2:
    
        ...
        
    >>> sorted_by_rate_dataset = sort_by_rate(<dataset>)
            1- Command Line sort by A)scending rate
            2- Command Line sort by D)escending rate

        : d
        
        <calls the "sort_books_descening_rate" function with the <dataset> as the sole argument, so see the examples from that function in the "T004_P3_sorting" module to see what would be output here>
        
    >>> sorted_by_x_dataset
        
        <again, see the examples from the "sort_books_descending_rate" function in the "T004_P3_sorting" module to see potentiel outputs (the output here would be the return value from the "sort_books_descending_rate" function)>
                
    """
        
    #get user input (which command they would like to execute)
    rate_command = input(SORT_BY_RATE_UI).upper()
    
    #allows the user to enter a command again if the command entered was invalid
    while rate_command not in SORT_BY_RATE_COMMANDS:
        print('\nNo such command\n')
        rate_command = input(SORT_BY_RATE_UI).upper()    
    
    #initializing list to store the sorted dataset when it is returned
    sorted_by_rate_dataset = []
    
    #calls the function that will sort the dataset in the requested manner
    print() #for aesthetics
    if rate_command == "A":
        sorted_by_rate_dataset = sort_books_ascending_rate(dataset)
    elif rate_command == "D":
        sorted_by_rate_dataset = sort_books_descending_rate(dataset)
        
    #returns the sorted dataset
    return sorted_by_rate_dataset

# MAIN SCRIPT
if __name__ == "__main__":
    main_cmd()
