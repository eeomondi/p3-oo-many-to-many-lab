class Author:
    all_authors = []

    def __init__(self, name: str):
        self.name = name
        self._contracts = []  # 
        Author.all_authors.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date: str, royalties: int):
        if not isinstance(book, Book):
            raise Exception("Invalid book.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int) or royalties < 0 or royalties > 100:
            raise Exception("Royalties must be an integer between 0 and 100.")
        
        contract = Contract(author=self, book=book, date=date, royalties=royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all_books = []

    def __init__(self, title: str):
        self.title = title
        Book.all_books.append(self)


class Contract:
    all_contracts = []

    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date: str):
        return [contract for contract in cls.all_contracts if contract.date == date]


#use 
if __name__ == "__main__":
    author1 = Author("John Doe")
    book1 = Book("Great Novel")
    
    contract1 = author1.sign_contract(book1, "2023-01-01", 10)
    
    print(author1.total_royalties())  # Output: 10
    print(author1.books())             # Output: [<__main__.Book object at ...>]
    print(Contract.contracts_by_date("2023-01-01"))  # Output: [<__main__.Contract object at ...>]
