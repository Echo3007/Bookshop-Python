# Angela Pellillo

class Product:
    def __init__(self, ID, price, prime_eligible, number_in_stock, date_added):
        self.ID = ID
        self.price = price
        self.prime_eligible = prime_eligible
        self.number_in_stock = number_in_stock
        self.date_added = date_added

    def set_ID(self, ID):
        self.ID = ID
    def get_ID(self):
        return self.ID

    def set_price(self, price):
        self.price = price
    def get_price(self):
        return self.price

    def set_prime_eligible(self, prime_eligible):
        self.prime_eligible = prime_eligible
    def get_prime_eligible(self):
        return self.prime_eligible

    def set_number_in_stock(self, number_in_stock):
        self.number_in_stock = number_in_stock

    def get_number_in_stock(self):
        return self.number_in_stock

    def set_date_added(self, date_added):
        self.date_added = date_added
    def get_date_added(self):
        return self.date_added

    def print_info(self):
        print("Product ISBN-10: " + self.ID,"\nPrice: " + str(self.price)+"£","\nIs this product included in Prime?: " + self.prime_eligible,
              "\nAvailable in stock: " + str(self.number_in_stock),"\nDate added: " + self.date_added)
        
#Angela Pellillo       

class Book(Product):
    def __init__(self,ID, price, prime_eligible, number_in_stock, date_added, title, author, num_pages, publisher, publication_date):
        super().__init__(ID, price, prime_eligible, number_in_stock, date_added)
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.publisher = publisher
        self.publication_date = publication_date

    def set_title(self, title):
        self.title = title
    def get_title(self):
        return self.title

    def set_author(self, author):
        self.author = author
    def get_author(self):
        return self.author

    def set_num_pages(self, num_pages):
        self.num_pages = num_pages
    def get_num_pages(self):
        return self.num_pages

    def set_publisher(self, publisher):
        self.publisher = publisher
    def get_publisher(self):
        return self.publisher

    def set_publication_date(self, publication_date):
        self.publication_date = publication_date
    def get_publication_date(self):
        return self.publication_date

    def print_book_info(self):
        
        print("Book's title: "+ self.title, "\nAuthor's name: " + self.author,"\nNumber of pages: " + str(self.num_pages),"\nPublisher: " + self.publisher,"\nPublication date: " + self.publication_date)
        self.print_info() 

b1 = Book("0751540471", 6.69, "Yes", 52, "02 December 2007", "The Notebook", "Nicholas Sparks",272, "Sphere", "1st Nov. 2007")
b1.print_book_info()
print("\n")

b2 = Book("0571334644", 21.99, "Not included", 13, "14th July 2018", "Normal People", "Sally Rooney", 288, "Faber & Faber", "30th Aug. 2018")
b2.print_book_info()
print("\n")

b3 = Book("3125776929",11.04, "Not included", 12, "Sept. 2015", "The Handmaid's Tale","Margaret Atwood",398, "Klett Sprachen GmbH", "12th Sept. 2005")
b3.print_book_info() 
print("\n")

#Angela Pellillo 
#Below setters and getters from book and product class to test the objects created (all the updated info below is purely fictional. Unfortunately.)
print("Updated info on the following books!")
b1.set_title("The Notebook - Hard Cover")
b1.set_price(10.50)
b1.set_number_in_stock(30)
print(b1.get_title())
print("New price for b1: £",b1.get_price())
print("Available in stock now:", b1.get_number_in_stock())

print("\n")
b2.set_publisher("Mondadori")
b2.set_publication_date("25th Sept. 2021")
b2.set_num_pages(300)
print("New publisher for b2: ",b2.get_publisher())
print("Updated publication date for b2: ", b2.get_publication_date())
print("Number of pages now:", b2.get_num_pages())

print("\n")
b3.set_date_added("October 2016")
b3.set_prime_eligible("Yes")
b3.set_ID("12345678")
b3.set_author("Margaret Atwood, in collab. with Angela Pellillo")      
print("New b3 ID: ", b3.get_ID())
print("Date added updated for b3: ", b3.get_date_added())
print("Prime Availability for b3 now: ", b3.get_prime_eligible())
print("Author updated:", b3.get_author())




    
        
