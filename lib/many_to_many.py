class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        contract_list = [] 
        for contract in Contract.all:
            if contract.author == self:
                contract_list.append(contract)   
        return contract_list
    
    def books(self):
        book_list = []
        for contract in Contract.all:
            if contract.author == self:
              print(contract.book)
              book_list.append(contract.book)  
        return book_list
    
    def sign_contract(self,book,date,royalties):
            return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = 0
        for contract in Contract.all:
            if contract.author == self:
               total =+ total + contract.royalties
        return total

class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        contract_list = [] 
        for contract in Contract.all:
            if contract.book == self:
                contract_list.append(contract)   
        return contract_list

    def authors(self):
        author_list= []
        for contract in Contract.all:
            if contract.book == self:
                author_list.append(contract.author)
        return author_list
    
class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance Author Class")
        self._author = value    

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self,value):
        if not isinstance(value, Book):
            raise TypeError("Book must be an instance book Class")
        self._book = value        

    @property  
    def date(self):
        return self._date
   
    @date.setter
    def date(self,value):
        if not isinstance(value, str):
            raise TypeError("Date must be of type string")
        self._date = value

    @property 
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self,value):
        if not isinstance(value, int):
            raise TypeError("Royalties must be of type int") 
        self._royalties = value

    @classmethod
    def contracts_by_date(cls):
        datelist=[]
        contractlist = []
        datelist = [contract.date for contract in Contract.all]
        datelist.sort()
        for date in datelist:
            for contract in Contract.all:
                if date == contract.date:
                    contractlist.append(contract)
        print (contractlist)
        return contractlist            
 


Contract.all = []
author = Author("Name")
book1 = Book("Title 1")
book2 = Book("Title 2")
book3 = Book("Title 3")
contract1 = Contract(author, book1, "02/01/2001", 10)
contract2 = Contract(author, book2, "01/01/2001", 20)
contract3 = Contract(author, book3, "03/01/2001", 30)