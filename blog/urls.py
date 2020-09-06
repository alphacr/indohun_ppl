from django.urls import path
from .views import (
    ReportListView,
    ReportDetailView,
    ReportCreateView,
    ReportUpdateView,
    ReportDeleteView,
    ReportPDFView,
)
from . import views

urlpatterns = [
    path('report/', ReportListView.as_view(), name='report-list'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('report/new/', ReportCreateView.as_view(), name='report-create'),
    path('report/<int:pk>/update', ReportUpdateView.as_view(), name='report-update'),
    path('report/<int:pk>/delete', ReportDeleteView.as_view(), name='report-delete'),
    path('tentang_manajement/', views.tentang_manajement, name='tentang_manajement'),
    path('tentang_biorisiko/', views.tentang_biorisiko, name='tentang_biorisiko'),
    path('tentang_SMBL/', views.tentang_SMBL, name='tentang_SMBL'),
    path('pdf_view/<int:pk>/', ReportPDFView.as_view(), name='pdf_view'),
    path('compare_laporan/', views.compare_laporan, name='compare_laporan'),
]
