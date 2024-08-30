from dashboard.models import User, Transaction
from datetime import datetime

def run():
    users = [
        User(name='Rajkumar', email='raj@example.com', join_date='2024-01-15'),
        User(name='Anjali', email='anjali@example.com', join_date='2024-03-10'),
        User(name='Ravi', email='ravi@example.com', join_date='2024-05-25'),
        User(name='Neha', email='neha@example.com', join_date='2024-07-30'),
    ]

    User.objects.bulk_create(users)

    transactions = [
        Transaction(user=users[0], amount=150.00, transaction_date='2024-02-20'),
        Transaction(user=users[0], amount=200.50, transaction_date='2024-03-15'),
        Transaction(user=users[1], amount=300.00, transaction_date='2024-04-10'),
        Transaction(user=users[2], amount=450.75, transaction_date='2024-06-05'),
        Transaction(user=users[2], amount=120.00, transaction_date='2024-07-15'),
    ]

    Transaction.objects.bulk_create(transactions)
