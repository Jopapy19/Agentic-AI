"""
_2_oop_classes.py

Classes, taught clean -- no Agent in sight. Class 1 only ever showed
you a class wearing an "Agent" costume; this file is the bare pattern,
on its own, so it actually generalizes instead of feeling like
something you can only use for AI.

Run with: uv run _2_oop_classes.py
"""

# --- A class is a blueprint. An instance is one specific thing built from it. ---

class BankAccount:
    """A blueprint for a bank account -- nothing to do with AI."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.history.append(f"Deposited {amount}")

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print(
                f"Insufficient funds: tried to withdraw {amount}, "
                f"balance is {self.balance}"
            )
            return

        self.balance -= amount
        self.history.append(f"Withdrew {amount}")

    def show_history(self) -> None:
        if not self.history:
            print("  No transactions yet.")
            return

        for entry in self.history:
            print(f"  - {entry}")


# ---------------------------------------------------------------------
# Build two separate accounts from the same blueprint.
# ---------------------------------------------------------------------

account_1 = BankAccount(owner="Mayank", balance=1000)
account_2 = BankAccount(owner="Krish", balance=500)

account_1.deposit(200)
account_1.withdraw(50)

account_2.withdraw(1000)  # Deliberately too much

print(f"{account_1.owner}'s balance: {account_1.balance}")
account_1.show_history()

print(f"\n{account_2.owner}'s balance: {account_2.balance}")
account_2.show_history()


# ---------------------------------------------------------------------
# Book class (replaces @dataclass version)
# ---------------------------------------------------------------------

class Book:
    """The same blueprint concept, written without @dataclass."""

    def __init__(
        self,
        title: str,
        author: str,
        pages_read: int = 0,
        tags=None,
    ):
        self.title = title
        self.author = author
        self.pages_read = pages_read

        # Avoid using a mutable default argument.
        if tags is None:
            self.tags = []
        else:
            self.tags = tags

    def read(self, pages: int) -> None:
        self.pages_read += pages

    def add_tag(self, tag: str) -> None:
        self.tags.append(tag)

    def __repr__(self) -> str:
        return (
            f"Book(title='{self.title}', "
            f"author='{self.author}', "
            f"pages_read={self.pages_read}, "
            f"tags={self.tags})"
        )


# ---------------------------------------------------------------------
# Create and use a Book object.
# ---------------------------------------------------------------------

my_book = Book(title="Atomic Habits", author="James Clear")

my_book.read(40)
my_book.add_tag("self-help")

print(f"\n{my_book}")


# ---------------------------------------------------------------------
# Main entry point.
# ---------------------------------------------------------------------

if __name__ == "__main__":
    print("\nOOP done.")
    print("Two completely ordinary classes -- a bank account and a book.")
    print("Notice how both classes encapsulate their own state and behavior.")