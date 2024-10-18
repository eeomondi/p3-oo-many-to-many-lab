class Author:
    def __init__(self, name: str):
        self.name = name
        self._contracts = []  # Instance variable to track contracts


    def sign_contracts(self, book, date, royalities):
        contract = contract(self, book, date, royalities * 1000)
        self._contracts.append(contract)
        return contract

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
        self._contracts = []  # Instance variable to track contracts
        Book.all_books.append(self)

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    def __init__(self, author: Author, book: Book, date: str, royalties: int):       
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)
        
        # Add this contract to the author's and book's contracts
        author._contracts.append(self)
        book._contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date: str):
        return [contract for contract in cls.all_contracts if contract.date == date]

