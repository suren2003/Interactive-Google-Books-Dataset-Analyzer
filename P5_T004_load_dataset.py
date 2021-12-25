#Team identfier: T004
#Written by: Morgan Pleet(101224360)
#Reviewed by: Suren Kulasegaram (101220595), Zane Labonte-Hagar (101239002), Jeremy Hornung (101219284)
#Refactored by Zane Labonte-Hagar (101239002)
#Date: 10/12/2021
#Version: 1.0

#Import statement 
import csv

#Function definition 
def load_dataset(google_books_dataset: str) -> dict[str,list[dict[str, object]]]:
    """
    Returns a dictionary that stores the information from the specified Google Books Dataset CSV file. The file must be encoded in UTF-8.
    The dictionary keys are the different generes of the books within the file,
    and the values are the individual book entries from the file, including the title of the book,
    the author(s), the language, the rating, the publisher and the page count - each which fall into one of the different genres.

    >>> book_category_function_list('Google_Books_Dataset.csv')
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288}, {another element}, ...], 'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'page_count': 96}, {another element}, ...]...}
    """

    file = open(google_books_dataset, mode = 'r', encoding = 'utf-8')
    csv_reader = csv.reader(file)

    header = next(csv_reader) # header containing column keys

    book_dict = {}
    for line in csv_reader:
        title = line[1]
        author = line[2]
        rating = line[3]
        publisher = line[4]
        page_count = int(line[5])
        generes = line[6]
        language = line[7]

        if rating == '':
            rating = None
        else:
            rating = float(rating)

        if generes not in book_dict:
            # Add an empty set for the category if the category doesn't exist
            # Use a set to not add complete duplicates
            book_dict.update({generes: []})

        book_entry = {header[1]: title,
                      header[2]: author,
                      header[7]: language,
                      header[3]: rating,
                      header[4]: publisher,
                      header[5]: page_count}

        book_list = book_dict[generes]
        if book_entry not in book_list:
            # Don't add books entries that are complete dictionaries; all data includy category are the same
            book_list.append(book_entry)
        
    file.close()
    
    return book_dict

