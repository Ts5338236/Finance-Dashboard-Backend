from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count, Q
from django.db.models.functions import TruncMonth
from records.models import FinancialRecord
from users.permissions import IsAnalyst
from decimal import Decimal

class DashboardSummaryView(APIView):
    """
    Dashboard summary API for total income, expenses, balance, 
    category-wise totals, recent transactions, and monthly trends.
    Only accessible by Analyst and Admin.
    """
    permission_classes = [IsAnalyst]

    def get(self, request):
        user = request.user
        
        # Base QuerySet
        records = FinancialRecord.objects.all()

        # 1. Totals
        totals = records.aggregate(
            total_income=Sum('amount', filter=Q(type='income')),
            total_expenses=Sum('amount', filter=Q(type='expense'))
        )
        
        total_income = totals['total_income'] or Decimal('0.00')
        total_expenses = totals['total_expenses'] or Decimal('0.00')
        net_balance = total_income - total_expenses

        # 2. Category-wise Totals
        category_totals = records.values('category', 'type').annotate(
            total_amount=Sum('amount')
        ).order_by('-total_amount')

        # 3. Recent Transactions (Limit 5)
        recent_transactions = records.order_by('-date', '-created_at')[:5]
        recent_data = [
            {
                'id': rec.id,
                'amount': rec.amount,
                'type': rec.type,
                'category': rec.category,
                'date': rec.date,
                'notes': rec.notes
            } for rec in recent_transactions
        ]

        # 4. Monthly Trends (Group by month)
        monthly_trends = records.annotate(month=TruncMonth('date')).values('month', 'type').annotate(
            total=Sum('amount')
        ).order_by('month')

        data = {
            'summary': {
                'total_income': total_income,
                'total_expenses': total_expenses,
                'net_balance': net_balance
            },
            'category_breakdown': category_totals,
            'recent_transactions': recent_data,
            'monthly_trends': monthly_trends
        }

        return Response(data)
