from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
import json


def index(request):
    expenses = Expense.objects.all().order_by('-date')
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'tracker/index.html', {'expenses': expenses, 'total': total})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/add_expense.html', {'form': form})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('index')

def expense_stats(request):
    expenses = Expense.objects.all()
    category_data = expenses.values('category').annotate(total=Sum('amount'))
    categories = [item['category'] for item in category_data]
    category_totals = [float(item['total']) for item in category_data]

    date_data = expenses.values('date').annotate(total=Sum('amount')).order_by('date')
    dates = [item['date'].strftime('%Y-%m-%d') for item in date_data]
    date_totals = [float(item['total']) for item in date_data]

    return render(request, 'tracker/stats.html', {
        'categories': json.dumps(categories),
        'category_totals': json.dumps(category_totals),
        'dates': json.dumps(dates),
        'date_totals': json.dumps(date_totals),
    })