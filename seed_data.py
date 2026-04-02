import os
import django
from decimal import Decimal
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance_backend.settings')
django.setup()

from users.models import User
from records.models import FinancialRecord

def seed():
    # 1. Create Users
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={'email': 'admin@example.com', 'role': 'admin', 'is_staff': True, 'is_superuser': True}
    )
    if created:
        admin_user.set_password('admin123')
        admin_user.save()
        print("Created Admin User: admin/admin123")

    analyst_user, created = User.objects.get_or_create(
        username='analyst',
        defaults={'email': 'analyst@example.com', 'role': 'analyst'}
    )
    if created:
        analyst_user.set_password('analyst123')
        analyst_user.save()
        print("Created Analyst User: analyst/analyst123")

    viewer_user, created = User.objects.get_or_create(
        username='viewer',
        defaults={'email': 'viewer@example.com', 'role': 'viewer'}
    )
    if created:
        viewer_user.set_password('viewer123')
        viewer_user.save()
        print("Created Viewer User: viewer/viewer123")

    # 2. Create Records
    if not FinancialRecord.objects.exists():
        records = [
            {'amount': Decimal('5000.00'), 'type': 'income', 'category': 'salary', 'notes': 'Monthly Salary', 'date': date.today() - timedelta(days=10)},
            {'amount': Decimal('1200.00'), 'type': 'expense', 'category': 'rent', 'notes': 'Monthly Rent', 'date': date.today() - timedelta(days=5)},
            {'amount': Decimal('150.00'), 'type': 'expense', 'category': 'food', 'notes': 'Groceries', 'date': date.today() - timedelta(days=2)},
            {'amount': Decimal('50.00'), 'type': 'expense', 'category': 'transport', 'notes': 'Fuel', 'date': date.today() - timedelta(days=1)},
            {'amount': Decimal('300.00'), 'type': 'income', 'category': 'other', 'notes': 'Freelance Gig', 'date': date.today()},
        ]
        
        for r_data in records:
            FinancialRecord.objects.create(user=admin_user, **r_data)
        print(f"Created {len(records)} sample financial records.")

if __name__ == '__main__':
    seed()
