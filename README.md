# T004 Data Analyzer - Version 1.0 - 10/12/2021
___
The project can be reached at:  
Suren Kulasegaram  
Email: surenkulasegaram@cmail.carleton.ca

README.md written by Jeremy Hornung (101219284)
## Description:
___
* The project contains a single program which allows the user to load a Google Books dataset (CSV file) and then analyze the dataset in a variety of different ways.
    1. It allows the user to add or remove books from the dataset.
    2. It allows the user to search the dataset by book title, rating, author, publisher, category, category and title, or category and rating.
    3. It allows the user to view the books in the dataset sorted by page count (ascending) or rating (ascending or descending), or sorted alphabetically by title, publisher name, or category.
    4. It allows the user to view the number of books in a category, the categories containing books written by a specified author, or the categories that a specified book falls into.  
* The project is made up of a number of files that must all be placed within the same directory when running the program.
    * T004\_P4\_BooksUI.py
        * A python script containing the code for the UI of the program.
    * P5\_T004\_load\_dataset.py
        * A python script containing the code that allows the user to upload a google books dataset.
    * T004\_P2\_search\_modify\_dataset.py
        * A python script containing the code that executes the 1st (i), 2nd (ii) and 4rth (iv) types of analysis (above).    
    * T004\_P3\_sorting.py
        * A python script containing the code that executes the 3rd (iii) type of analysis (above).
    * **NOTE**: You will also need a google books dataset file (xxx.csv) in the same directory as the rest of the project to be able to run this project effectively, where xxx is the name of a google books dataset file of your choosing.
## Installation:
___
The project has been developed with Python 3.9. It may work with any 3.x, however 3.9 is only supported.
The project uses only python buit-in modules, so no other modules must be installed. 
## Usage:
___
When the project is run, a menu will display your command options within the program. A Google Books dataset file (csv file) must be loaded into the program using the L)oad file command before any of the other commands may be used. To select a command, input the first letter (the letter before the closing parenthese, e.g. input "L" for the L)oad file command) of the command that you would like to execute. Once you have selected a command, follow the simple prompts that will appear on the screen. Also note that the program contains error-handling, so an incorrect input should not cause the program to crash.
  
The following are examples of the project being run from the command line (once the current directory has been set to the directory containing the project files). These examples show some (but not all) of the menus and prompts that you will encounter throughout the program. They do not, however, give detail on the output that a specific command will produce. For examples of the outputs that each specific command will produce, see the docstrings of the functions in P5\_T004\_load\_dataset.py, T004\_P2\_search\_modify\_dataset.py and T004\_P3\_sorting.py (the name of the function will line up with the name of the corresponding command, e.g. the A)dd book command corresponds to the add_book function):  

#Example 1: starting up the program and selecting the S)ort book, R)ate, A)scending command  
```
> python T004_P4_booksUI.py  
1- Command Line L)oad file  
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
  
: S  
  
    1- Command Line sort by T)itle  
    2- Command Line sort by R)ate  
        A)scending D)escending  
    3- Command Line sort by P)ublisher  
    4- Command Line sort by C)ategory  
    5- Command Line sort by PA)ageCount    
  
: R  
  
    1- Command Line sort by A)scending rate  
    2- Command Line sort by D)escending rate  
  
: A  
<books in the dataset output in order of ascending rating, see the sort_books_ascending_rate function in the T004_P3_sorting.py file for examples>  
```

#Example 2: starting up the program and selecting the R)emove book command
```
> python T004\_P4\_booksUI.py  
1- Command Line L)oad file  
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
  
: R  
Enter the title of the book you wish to remove: <book title>  
Enter the category of the book you wish to remove: <book category>  
The book has been removed correctly
```
## Credits:
---
The following shows who is the author of the functions within each of the project files:  
* T004\_P4\_BooksUI.py
    * Author: Zane Labonte-Hagar (101239002)
        * main\_cmd (co-written with Suren Kulasegaram (101220595))
        * get\_book\_cmd
        * parse\_unsigned\_int
    * Author: Suren Kulasegaram (101220595)
        * main\_cmd (co-written with Zane Labonte-Hagar (101239002))
    * Author: Morgan Pleet (101224360)
        * load\_cmd
        * adding\_books\_cmd
        * removing\_books\_cmd
    * Author: Jeremy Hornung (101219284)
        * sort\_cmd
        * sort\_by\_rate\_cmd
* P5\_T004\_load\_dataset.py
    * Author: Morgan Pleet (101224360)
        * load\_dataset
    * Refactored by: Zane Labonte-Hagar (101239002)
        *  load\_dataset
* T004\_P2\_search\_modify\_dataset.py
    * Author: Morgan Pleet (101224360)
        * print\_dictionary\_category
        * add\_book
        * remove\_book
    * Author: Jeremy Hornung (101219284)
        * get\_books\_by\_rate
        * find\_books\_by\_title
        * get\_books\_by\_author
    * Author: Zane Labonte-Hagar (101239002)
        * get\_books\_by\_publisher
        * check\_category\_and\_title
        * all\_categories\_for\_book\_title
    * Author: Suren Kulasegaram (101220595)
        * get\_books\_by\_category
        * get\_books\_by\_category\_and\_rate
        * get\_author\_categories
* T004\_P3\_sorting.py
    * Author: Zane Labonte-Hagar (101239002)
        * dictionary\_to\_list
        * sort\_books\_ascending\_rate
        * sort\_books\_descending\_rate
    * Author: Morgan Pleet (101224360)
        * sort\_books\_title
    * Author: Jeremy Hornung (101219284)
        * sort\_books\_publisher
        * sort\_books\_category
    * Author: Suren Kulasegaram (101220595)
        * sort\_books\_pageCount
___
Copyright 2021 Suren Kulasegaram, Zane Labonte-Hagar, Morgan Pleet and Jeremy Hornung
