from rest_framework import viewsets, permissions
from .models import FinancialRecord
from .serializers import FinancialRecordSerializer
from .filters import FinancialRecordFilter
from users.permissions import ReadOnlyPermission, IsAdmin, IsAnalyst, IsViewer

class FinancialRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows financial records to be managed.
    Viewer: Read-only access to all records.
    Analyst: Read-only access to all records. (Wait, requirement says Analyst can view records and dashboard).
    Admin: Full CRUD.
    
    Actually, let's refine based on requirements:
    Viewer: Can only view data.
    Analyst: Can view records and dashboard.
    Admin: Full access (CRUD + user management).
    """
    queryset = FinancialRecord.objects.all()
    serializer_class = FinancialRecordSerializer
    filterset_class = FinancialRecordFilter
    search_fields = ['notes', 'category']
    ordering_fields = ['date', 'amount', 'created_at']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated] # Viewer, Analyst, Admin can view
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin] # Only Admin can perform CRUD
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
