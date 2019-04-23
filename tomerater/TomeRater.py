################################################
# Tome Rater Project                           #
# Written by Brandon Griffin                   #
# Started   on 03/15/2019                      #
# Completed on                                 #
################################################

#Imports
from random import randint

#Create method to check for valid email address
def check_email(email):
    #If email has one and only one @ sign
    if email.count('@') == 1:
        #If email ends in .org, .com, or .edu
        if email[-4:] in ('.org', '.com', '.edu'):
            return True
    else:
        return False

################################## USER CLASS #################################

class User(object):

    #Create User class constructor method
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}        

    #Create a method to return a user's email address
    def get_email(self):
        return self.email

    #Create a method to change a user's email address
    def change_email(self, address):
        old_email = self.email
        self.email = address
        print("%s's email has been changed from %s to %s." % \
              (self.name, old_email, self.email))

    #Create a method to return user information
    def __repr__(self):
        return("      User:\t%s\n     Email:\t%s\nBooks Read:\t%s\n" % \
               (self.name, self.email, len(self.books)))

    #Create a method to compare one user to another
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    #Create a method to add a book and its optional rating
    def read_book(self, book, rating = None):
        self.books[book] = rating

    #Create a method to get the average rating of a user object
    def get_average_rating(self):
        
        #Initialize variables
        count = 0
        total = 0
        
        #Loop through all of the books and, if there is a rating,
        #add it to the total and increase the count
        for book in self.books:
            if self.books[book]:
                total += self.books[book]
                count += 1

        #If there is at least one rating, return the average rating
        #Otherwise, return 0
        if count > 0:
            return total / count
        else:
            return 0
        
################################## USER CLASS #################################

#-----------------------------------------------------------------------------#

################################## BOOK CLASS #################################

class Book(object):

    #Create Book class constructor method
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    #Create method to return the title of the book
    def get_title(self):
        return self.title

    #Create method to return the ISBN of the book
    def get_isbn(self):
        return self.isbn

    #Create method to update a book's ISBN
    def set_isbn(self, new_isbn):
        old_isbn = self.isbn
        self.isbn = new_isbn

        print("The ISBN for %s has been changed from %s to %s." % \
              (self.title, old_isbn, self.isbn))

    #Create method to add to a book's ratings
    def add_rating(self, rating):

        #If rating has been provided and is valid
        if rating:
            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")            

    #Create method to get average rating
    def average_rating(self):

        #Initialize variables
        rating_total = 0
        rating_average = 0

        #If there is at least one rating
        if len(self.ratings) > 0:

            #Summarize all of the ratings and get the average
            rating_total = sum(self.ratings)
            rating_average = rating_total / len(self.ratings)

            #Print the average rating
            print(rating_total)
            print("%s has an average rating of %s" % (self.title, \
                rating_average))

        #Otherwise, state that the book has not been rated
        else:
            print("%s has not been rated." % self.title)

    #Create a method to return book information
    def __repr__(self):
        return("Title:\t%s\n ISBN:\t%s\n" % (self.title, self.isbn))

    #Create a method to compare two books
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    #Creat a method to get the average rating of the book
    def get_average_rating(self):

        #Initialize variables
        count = 0
        total = 0

        #Loop through all of the ratings - add each to the total and
        #increment the count
        for rating in self.ratings:
            total += rating
            count += 1

        #If there is at least one rating, return the average
        if count > 0:
            return total / count

        #Otherwise, return 0
        else:
            return 0

    #Method to make book hashable
    def __hash__(self):
        return hash((self.title, self.isbn))
        

################################## BOOK CLASS #################################

#-----------------------------------------------------------------------------#

################################# FICTION CLASS ###############################

class Fiction(Book):

    #Create Fiction class constructor method
    def __init__(self, title, author, isbn):

        #Call init of parent class, Book
        super().__init__(title, isbn)

        #Set author instance variable
        self.author = author

    #Create representation method for Fiction subclass
    def __repr__(self):
        return("%s by %s" % (self.title, self.author))

    #Crate method to return the author of the Fiction object
    def get_author(self):
        return self.author

################################# FICTION CLASS ###############################

#-----------------------------------------------------------------------------#

############################## NON FICTION CLASS ##############################

class Non_Fiction(Book):

    #Create Non-Fiction class constructor method
    def __init__(self, title, subject, level, isbn):

        #Call init of parent class, Book
        super().__init__(title, isbn)

        #Set subject and level instance variables
        self.subject = subject
        self.level = level

    #Create method to return the subject of the Non-Fiction object
    def get_subject(self):
        return self.subject

    #Create a method to return the level of the Non-Fiction object
    def get_level(self):
        return self.level

    #Create representation method for Non-Fiction subclass
    def __repr__(self):
        return("%s, a %s manual on %s" % (self.title, self.level, \
            self.subject))

############################## NON FICTION CLASS ##############################     

#-----------------------------------------------------------------------------#

############################## TOME RATER CLASS ###############################

class TomeRater:

    #Create constructor method
    def __init__(self):

        #Initialize users and books dictionaries
        self.users = {}
        self.books = {}

    #Create method to create and return a Book object
    def create_book(self, title, isbn):
        return Book(title, isbn)

    #Create method to create and return a novel/Fiction object
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    #Create a method to create and return a Non-Fiction object
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    #Create a method to add a book to a user
    def add_book_to_user(self, book, email, rating = None):

        #If the user exists
        if self.users[email]:

            #Call read_book method on the user instance
            self.users[email].read_book(book, rating)

            #Add the user's rating to the book's ratings
            book.add_rating(rating)

            #Increment number of reads if book already exists
            #Otherwise, set the number of reads to 1
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1

        #User with supplied email does not exist
        else:
            print("No user with email %s!" % email)            

    #Create method to add a user
    def add_user(self, name, email, user_books = None):

        #Check for valid email address
        if check_email(email):            

            #Check to make sure the user does not already exist
            if email not in self.users.keys():

                #Create new User instance
                new_user = User(name, email)

                #Add user to users
                self.users[email] = new_user

                #If the user has read at least one book
                if user_books != None:

                    #Loop thorugh books the user has read
                    for book in user_books:

                        #Add the book to the user
                        self.add_book_to_user(book, email)

            #User already exists
            else:
                print("%s already exists!" % email)

        #Notify of invalid email address
        else:
            print("%s is not a valid email address." % email)

    #Create method to loop through and print the catalog of books
    def print_catalog(self):
        for book in self.books:
            print(book)

    #Create a method loop through and print all of the users
    def print_users(self):
        for user in self.users:
            print(user)

    #Create a method to find the book with the most reads
    def most_read_book(self):

        #Create separate lists for the values and keys
        values = list(self.books.values())
        keys = list(self.books.keys())

        #Return the book with the most reads
        return keys[values.index(max(values))]

    #Create a method to find the highest rated book
    def highest_rated_book(self):

        #Initialize values list
        values = []

        #Loop through all of the books
        for book in self.books:

            #Add the books average rating to the values list
            values.append(book.get_average_rating())

        #Create a list of the keys from the books dictionary
        keys = list(self.books.keys())

        #Return the book with the highest average rating
        return keys[values.index(max(values))]

    #create a method to find the highest rating user
    def most_positive_user(self):

        #Initialize a values list
        values = []

        #Loop through each user
        for user in self.users.values():

            #Add each user's average rating to the values list
            values.append(user.get_average_rating())

        #Create a list of all of the users dictionary keys
        keys = list(self.users.keys())

        #Return the user that provided the highest average ratings
        return keys[values.index(max(values))]

    #Create method to print TomeRater object
    def __repr__(self):

        #Initialize catalog and users strings
        catalog = ''
        users = ''

        #Get number of books and users in TomeRater
        book_count = len(self.books)
        user_count = len(self.users)

        #Add books and users to output strings
        for book in self.books:
            catalog += book.title + "\n"

        for user in self.users:
            users += user + "\n"

        #Compile output string and return
        output = "\nThis TomeRater contains:\n\n" + str(book_count) \
                 + " Books:\n" + catalog + "\n" + str(user_count) +\
                 " Users:\n" + users

        return output

############################## TOME RATER CLASS ###############################
