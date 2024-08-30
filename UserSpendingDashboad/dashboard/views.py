from django.shortcuts import render
from .models import User, Transaction
from django.db.models import Sum, Avg
from datetime import datetime

def dashboard_view(request):
    # Task 1: Specific date range query
    date_range_users = User.objects.filter(join_date__range=["2024-01-01", "2024-12-31"])

    # Task 2: Total amount spent by each user
    user_spending = User.objects.annotate(total_spent=Sum('transaction__amount'))

    # Task 3: Join users and transactions for report
    user_report = user_spending.values('name', 'email', 'total_spent')

    # Task 4: Top 3 users by spending
    top_3_users = user_spending.order_by('-total_spent')[:3]

    # Task 5: Average transaction amount
    average_spending = Transaction.objects.all().aggregate(Avg('amount'))

    # Task 6: Users with no transactions
    no_transaction_users = User.objects.filter(transaction__isnull=True)

    context = {
        'date_range_users': date_range_users,
        'user_report': user_report,
        'top_3_users': top_3_users,
        'average_spending': average_spending,
        'no_transaction_users': no_transaction_users,
    }

def dashboard_view(request):
    print("Request Method:", request.method)
    print("User:", request.user)
    return render(request, 'dashboard/dashboard.html')