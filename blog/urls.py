from django.urls import path
from .views import (
    ReportListView,
    ReportDetailView,
    ReportCreateView,
    ReportUpdateView,
    ReportDeleteView,
    ReportPDFView,
    ReportCreateView35001,
    ReportListView35001,
    ReportDetailView35001,
    ReportDeleteView35001,
    ReportUpdateView35001
)
from . import views

urlpatterns = [
    path('report/', ReportListView.as_view(), name='report-list'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('report/new/', ReportCreateView.as_view(), name='report-create'),
    path('report/<int:pk>/update', ReportUpdateView.as_view(), name='report-update'),
    path('report/<int:pk>/delete', ReportDeleteView.as_view(), name='report-delete'),
    path('tentang_manajement/', views.tentang_manajement,
         name='tentang_manajement'),
    path('tentang_biorisiko/', views.tentang_biorisiko, name='tentang_biorisiko'),
    path('tentang_SMBL/', views.tentang_SMBL, name='tentang_SMBL'),
    path('pdf_view/<int:pk>/', ReportPDFView.as_view(), name='pdf_view'),
    path('compare_laporan/', views.compare_laporan, name='compare_laporan'),

    # New Report 35001
    path('report_35001/', ReportListView35001.as_view(), name='report_list_35001'),
    path('report_35001/<int:pk>/', ReportDetailView35001.as_view(), name='report_detail_35001'),
    path('report_35001/new/', ReportCreateView35001.as_view(),
         name='report_create_35001'),
    path('tentang_35001/', views.tentang_35001, name='tentang_35001'),
    path('report_35001/<int:pk>/update', ReportUpdateView35001.as_view(), name='report_update_35001'),
    path('report_35001/<int:pk>/delete', ReportDeleteView35001.as_view(), name='report_delete_35001'),
    # path('pdf_view_35001/<int:pk>/', ReportPDFView.as_view(), name='pdf_view_35001'),
    path('compare_laporan_35001/', views.compare_laporan_35001, name='compare_laporan_35001'),
]
