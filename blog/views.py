from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from .forms import ContactUsForm
from .forms import CompareReportForm
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    FormView,
    UpdateView,
    DeleteView
)
from .models import (
    Questionnaire,
    CompareReport
)
from users.models import Profile

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Terima kasih telah menghubungi One Health Laboratory')
    else:
        form = ContactUsForm()
    return render(request, 'blog/home.html', {'form': form})


class ReportListView(LoginRequiredMixin, ListView):
    model = Questionnaire
    template_name = 'blog/report_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'reports'
    ordering = ['-date_posted']

    def get_queryset(self):
        user = self.request.user
        return Questionnaire.objects.filter(author=user)


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Questionnaire  # <app>/<model>_<viewtype>.html
    context_object_name = 'report'


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Questionnaire  # <app>/<model>_form.html
    fields = ['judul_laporan','penilai', 'afiliasi_penilai', 'jenis_penilaian', 'personel_yang_diwawancarai',
              'nilai_no_1', 'keterangan_kebijakan_sistem_manajemen_biorisiko', 'rekomendasi_kebijakan_sistem_manajemen_biorisiko',
              'nilai_no_2', 'keterangan_tujuan_dan_program_manajemen_biorisiko', 'rekomendasi_tujuan_dan_program_manajemen_biorisiko',
              'nilai_no_3', 'keterangan_tanggung_jawab_dan_wewenang', 'rekomendasi_tanggung_jawab_dan_wewenang',
              'nilai_no_4', 'keterangan_pencatatan_dokumen_dan_pengendalian_dokumen', 'rekomendasi_pencatatan_dokumen_dan_pengendalian_dokumen',
              'nilai_no_5', 'keterangan_perubahan_terkait_manajemen_biorisiko', 'rekomendasi_perubahan_terkait_manajemen_biorisiko',
              'nilai_no_6', 'keterangan_komunikasi_dan_konsultasi', 'rekomendasi_komunikasi_dan_konsultasi',
              'nilai_no_7', 'keterangan_perencanaan_dan_program_kerja', 'rekomendasi_perencanaan_dan_program_kerja',
              'nilai_no_8', 'keterangan_persyaratan_legal_aturan_atau_izin', 'rekomendasi_persyaratan_legal_aturan_atau_izin',
              'nilai_no_9', 'keterangan_inspeksi_dan_audit', 'rekomendasi_inspeksi_dan_audit',
              'nilai_no_10', 'keterangan_pengendalian_ketidaksesuaian_dan_perbaikan', 'rekomendasi_pengendalian_ketidaksesuaian_dan_perbaikan',
              'nilai_no_11', 'keterangan_pengembangan_berkelanjutan', 'rekomendasi_pengembangan_berkelanjutan',
              'nilai_no_12', 'keterangan_kontraktor_dan_suplier_purchasing', 'rekomendasi_kontraktor_dan_suplier_purchasing',
              'nilai_no_13', 'keterangan_review_dan_perbaikan_manajemen_biorisiko', 'rekomendasi_review_dan_perbaikan_manajemen_biorisiko',
              'nilai_no_14', 'keterangan_proses_metode_dan_prosedur', 'rekomendasi_proses_metode_dan_prosedur',
              'nilai_no_15', 'keterangan_ruang_lingkup_dan_penjadwalan', 'rekomendasi_ruang_lingkup_dan_penjadwalan',
              'nilai_no_16', 'keterangan_peran_dan_tanggung_jawab', 'rekomendasi_peran_dan_tanggung_jawab',
              'nilai_no_17', 'keterangan_identifikasi_hazard', 'rekomendasi_identifikasi_hazard',
              'nilai_no_18', 'keterangan_pengendalian_risiko', 'rekomendasi_pengendalian_risiko',
              'nilai_no_19', 'keterangan_inventarisasi_informasi_dan_pencatatan', 'rekomendasi_inventarisasi_informasi_dan_pencatatan',
              'nilai_no_20', 'keterangan_penyimpanan_bahan_biologik_dan_bahan_berbahaya_lainnya', 'rekomendasi_penyimpanan_bahan_biologik_dan_bahan_berbahaya_lainnya',
              'nilai_no_21', 'keterangan_transfer_bahan_biologik_dan_bahan_berbahaya_lainnya', 'rekomendasi_transfer_bahan_biologik_dan_bahan_berbahaya_lainnya',
              'nilai_no_22', 'keterangan_pengendalian_dan_monitoring', 'rekomendasi_pengendalian_dan_monitoring',
              'nilai_no_23', 'keterangan_general_safety', 'rekomendasi_general_safety',
              'nilai_no_24', 'keterangan_rekrutmen_pelatihan_dan_kompetensi', 'rekomendasi_rekrutmen_pelatihan_dan_kompetensi',
              'nilai_no_25', 'keterangan_suksesi_dan_eksklusi', 'rekomendasi_suksesi_dan_eksklusi',
              'nilai_no_26', 'keterangan_GMT_personel', 'rekomendasi_GMT_personel',
              'nilai_no_27', 'keterangan_GMT_peralatan', 'rekomendasi_GMT_peralatan',
              'nilai_no_28', 'keterangan_pelabelan', 'rekomendasi_pelabelan',
              'nilai_no_29', 'keterangan_pengadaan_alat_pelindung_diri', 'rekomendasi_pengadaan_alat_pelindung_diri',
              'nilai_no_30', 'keterangan_APD_personel', 'rekomendasi_APD_personel',
              'nilai_no_31', 'keterangan_pemeliharaan_dan_dekontaminasi_reusable_apd', 'rekomendasi_pemeliharaan_dan_dekontaminasi_reusable_apd',
              'nilai_no_32', 'keterangan_latar_belakang_sdm', 'rekomendasi_latar_belakang_sdm',
              'nilai_no_33', 'keterangan_program_kesehatan_kerja', 'rekomendasi_program_kesehatan_kerja',
              'nilai_no_34', 'keterangan_vaksinasi', 'rekomendasi_vaksinasi',
              'nilai_no_35', 'keterangan_kedaruratan_medik', 'rekomendasi_kedaruratan_medik',
              'nilai_no_36', 'keterangan_identifikasi_perencanaan_dan_respon_keadaan_darurat', 'rekomendasi_identifikasi_perencanaan_dan_respon_keadaan_darurat',
              'nilai_no_37', 'keterangan_simulasi_dan_pelatihan_tanggap_darurat', 'rekomendasi_simulasi_dan_pelatihan_tanggap_darurat',
              'nilai_no_38', 'keterangan_rencana_tanggap_darurat_menghadapi_kejadian_luar_duga', 'rekomendasi_rencana_tanggap_darurat_menghadapi_kejadian_luar_duga',
              'nilai_no_39', 'keterangan_ketersediaan_peralatan_keselamatan_untuk_tanggap_darurat', 'rekomendasi_ketersediaan_peralatan_keselamatan_untuk_tanggap_darurat',
              'nilai_no_40', 'keterangan_perencanaan_desain_dan_verifikasi_mencakup_commissioning_dan_decommisioning', 'rekomendasi_perencanaan_desain_dan_verifikasi_mencakup_commissioning_dan_decommisioning',
              'nilai_no_41', 'keterangan_infrastruktur_dan_operasional', 'rekomendasi_infrastruktur_dan_operasional',
              'nilai_no_42', 'keterangan_manajemen_pemeliharaan', 'rekomendasi_manajemen_pemeliharaan',
              'nilai_no_43', 'keterangan_monitoring_peralatan', 'rekomendasi_monitoring_peralatan',
              'nilai_no_44', 'keterangan_kalibrasi', 'rekomendasi_kalibrasi',
              'nilai_no_45', 'keterangan_sertifikasi', 'rekomendasi_sertifikasi',
              'nilai_no_46', 'keterangan_validasi', 'rekomendasi_validasi',
              'nilai_no_47', 'keterangan_pengolahan_limbah_dan_bahan_berbahaya_biologi_kimia', 'rekomendasi_pengolahan_limbah_dan_bahan_berbahaya_biologi_kimia',
              'nilai_no_48', 'keterangan_inaktivasi_bahan_biologik_dan_bahan_berbahaya_lainnya', 'rekomendasi_inaktivasi_bahan_biologik_dan_bahan_berbahaya_lainnya',
              'nilai_no_49', 'keterangan_dekontaminasi_dan_disinfeksi_peralatan', 'rekomendasi_dekontaminasi_dan_disinfeksi_peralatan',
              'nilai_no_50', 'keterangan_prosedur_penerimaan_dan_pengiriman_bahan_biologik_dan_bahan_berbahaya_lainnya', 'rekomendasi_prosedur_penerimaan_dan_pengiriman_bahan_biologik_dan_bahan_berbahaya_lainnya',
              'nilai_no_51', 'keterangan_keamanan_fisik_dan_pengendalian_personel', 'rekomendasi_keamanan_fisik_dan_pengendalian_personel',
              'nilai_no_52', 'keterangan_keamanan_informasi', 'rekomendasi_keamanan_informasi',
              'nilai_no_53', 'keterangan_pengendalian_personel', 'rekomendasi_pengendalian_personel',
              'nilai_no_54', 'keterangan_investigasi_kecelakaan_dan_insiden', 'rekomendasi_investigasi_kecelakaan_dan_insiden',
              'kelemahan_utama', 'kekuatan_utama', 'saran_untuk_perbaikan',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Questionnaire  # <app>/<model>_form.html
    context_object_name = 'report'
    fields = ['judul_laporan','penilai', 'afiliasi_penilai', 'jenis_penilaian', 'personel_yang_diwawancarai',
              'nilai_no_1', 'keterangan_kebijakan_sistem_manajemen_biorisiko', 'rekomendasi_kebijakan_sistem_manajemen_biorisiko',
              'nilai_no_2', 'keterangan_tujuan_dan_program_manajemen_biorisiko', 'rekomendasi_tujuan_dan_program_manajemen_biorisiko',
              'nilai_no_3', 'keterangan_tanggung_jawab_dan_wewenang', 'rekomendasi_tanggung_jawab_dan_wewenang',
              'nilai_no_4', 'keterangan_pencatatan_dokumen_dan_pengendalian_dokumen', 'rekomendasi_pencatatan_dokumen_dan_pengendalian_dokumen',
              'nilai_no_5', 'keterangan_perubahan_terkait_manajemen_biorisiko', 'rekomendasi_perubahan_terkait_manajemen_biorisiko',
              'nilai_no_6', 'keterangan_komunikasi_dan_konsultasi', 'rekomendasi_komunikasi_dan_konsultasi',
              'nilai_no_7', 'keterangan_perencanaan_dan_program_kerja', 'rekomendasi_perencanaan_dan_program_kerja',
              'nilai_no_8', 'keterangan_persyaratan_legal_aturan_atau_izin', 'rekomendasi_persyaratan_legal_aturan_atau_izin',
              'nilai_no_9', 'keterangan_inspeksi_dan_audit', 'rekomendasi_inspeksi_dan_audit',
              'nilai_no_10', 'keterangan_pengendalian_ketidaksesuaian_dan_perbaikan', 'rekomendasi_pengendalian_ketidaksesuaian_dan_perbaikan',
              'nilai_no_11', 'keterangan_pengembangan_berkelanjutan', 'rekomendasi_pengembangan_berkelanjutan',
              'nilai_no_12', 'keterangan_kontraktor_dan_suplier_purchasing', 'rekomendasi_kontraktor_dan_suplier_purchasing',
              'nilai_no_13', 'keterangan_review_dan_perbaikan_manajemen_biorisiko', 'rekomendasi_review_dan_perbaikan_manajemen_biorisiko',
              'nilai_no_14', 'keterangan_proses_metode_dan_prosedur', 'rekomendasi_proses_metode_dan_prosedur',
              'nilai_no_15', 'keterangan_ruang_lingkup_dan_penjadwalan', 'rekomendasi_ruang_lingkup_dan_penjadwalan',
              'nilai_no_16', 'keterangan_peran_dan_tanggung_jawab', 'rekomendasi_peran_dan_tanggung_jawab',
              'nilai_no_17', 'keterangan_identifikasi_hazard', 'rekomendasi_identifikasi_hazard',
              'nilai_no_18', 'keterangan_pengendalian_risiko', 'rekomendasi_pengendalian_risiko',
              'nilai_no_19', 'keterangan_inventarisasi_informasi_dan_pencatatan', 'rekomendasi_inventarisasi_informasi_dan_pencatatan',
              'nilai_no_20', 'keterangan_penyimpanan_bahan_biologik_dan_bahan_berbahaya_lainnya', 'rekomendasi_penyimpanan_bahan_biologik_dan_bahan_berbahaya_lainnya',
              'nilai_no_21', 'keterangan_transfer_bahan_biologik_dan_bahan_berbahaya_lainnya', 'rekomendasi_transfer_bahan_biologik_dan_bahan_berbahaya_lainnya',
              'nilai_no_22', 'keterangan_pengendalian_dan_monitoring', 'rekomendasi_pengendalian_dan_monitoring',
              'nilai_no_23', 'keterangan_general_safety', 'rekomendasi_general_safety',
              'nilai_no_24', 'keterangan_rekrutmen_pelatihan_dan_kompetensi', 'rekomendasi_rekrutmen_pelatihan_dan_kompetensi',
              'nilai_no_25', 'keterangan_suksesi_dan_eksklusi', 'rekomendasi_suksesi_dan_eksklusi',
              'nilai_no_26', 'keterangan_GMT_personel', 'rekomendasi_GMT_personel',
              'nilai_no_27', 'keterangan_GMT_peralatan', 'rekomendasi_GMT_peralatan',
              'nilai_no_28', 'keterangan_pelabelan', 'rekomendasi_pelabelan',
              'nilai_no_29', 'keterangan_pengadaan_alat_pelindung_diri', 'rekomendasi_pengadaan_alat_pelindung_diri',
              'nilai_no_30', 'keterangan_APD_personel', 'rekomendasi_APD_personel',
              'nilai_no_31', 'keterangan_pemeliharaan_dan_dekontaminasi_reusable_apd', 'rekomendasi_pemeliharaan_dan_dekontaminasi_reusable_apd',
              'nilai_no_32', 'keterangan_latar_belakang_sdm', 'rekomendasi_latar_belakang_sdm',
              'nilai_no_33', 'keterangan_program_kesehatan_kerja', 'rekomendasi_program_kesehatan_kerja',
              'nilai_no_34', 'keterangan_vaksinasi', 'rekomendasi_vaksinasi',
              'nilai_no_35', 'keterangan_kedaruratan_medik', 'rekomendasi_kedaruratan_medik',
              'nilai_no_36', 'keterangan_identifikasi_perencanaan_dan_respon_keadaan_darurat', 'rekomendasi_identifikasi_perencanaan_dan_respon_keadaan_darurat',
              'nilai_no_37', 'keterangan_simulasi_dan_pelatihan_tanggap_darurat', 'rekomendasi_simulasi_dan_pelatihan_tanggap_darurat',
              'nilai_no_38', 'keterangan_rencana_tanggap_darurat_menghadapi_kejadian_luar_duga', 'rekomendasi_rencana_tanggap_darurat_menghadapi_kejadian_luar_duga',
              'nilai_no_39', 'keterangan_ketersediaan_peralatan_keselamatan_untuk_tanggap_darurat', 'rekomendasi_ketersediaan_peralatan_keselamatan_untuk_tanggap_darurat',
              'nilai_no_40', 'keterangan_perencanaan_desain_dan_verifikasi_mencakup_commissioning_dan_decommisioning', 'rekomendasi_perencanaan_desain_dan_verifikasi_mencakup_commissioning_dan_decommisioning',
              'nilai_no_41', 'keterangan_infrastruktur_dan_operasional', 'rekomendasi_infrastruktur_dan_operasional',
              'nilai_no_42', 'keterangan_manajemen_pemeliharaan', 'rekomendasi_manajemen_pemeliharaan',
              'nilai_no_43', 'keterangan_monitoring_peralatan', 'rekomendasi_monitoring_peralatan',
              'nilai_no_44', 'keterangan_kalibrasi', 'rekomendasi_kalibrasi',
              'nilai_no_45', 'keterangan_sertifikasi', 'rekomendasi_sertifikasi',
              'nilai_no_46', 'keterangan_validasi', 'rekomendasi_validasi',
              'nilai_no_47', 'keterangan_pengolahan_limbah_dan_bahan_berbahaya_biologi_kimia', 'rekomendasi_pengolahan_limbah_dan_bahan_berbahaya_biologi_kimia',
              'nilai_no_48', 'keterangan_inaktivasi_bahan_biologik_dan_bahan_berbahaya_lainnya', 'rekomendasi_inaktivasi_bahan_biologik_dan_bahan_berbahaya_lainnya',
              'nilai_no_49', 'keterangan_dekontaminasi_dan_disinfeksi_peralatan', 'rekomendasi_dekontaminasi_dan_disinfeksi_peralatan',
              'nilai_no_50', 'keterangan_prosedur_penerimaan_dan_pengiriman_bahan_biologik_dan_bahan_berbahaya_lainnya', 'rekomendasi_prosedur_penerimaan_dan_pengiriman_bahan_biologik_dan_bahan_berbahaya_lainnya',
              'nilai_no_51', 'keterangan_keamanan_fisik_dan_pengendalian_personel', 'rekomendasi_keamanan_fisik_dan_pengendalian_personel',
              'nilai_no_52', 'keterangan_keamanan_informasi', 'rekomendasi_keamanan_informasi',
              'nilai_no_53', 'keterangan_pengendalian_personel', 'rekomendasi_pengendalian_personel',
              'nilai_no_54', 'keterangan_investigasi_kecelakaan_dan_insiden', 'rekomendasi_investigasi_kecelakaan_dan_insiden', 
              'kelemahan_utama', 'kekuatan_utama', 'saran_untuk_perbaikan',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        questionnaire = self.get_object()
        if self.request.user == questionnaire.author:
            return True
        return False


class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Questionnaire  # <app>/<model>_<viewtype>.html
    context_object_name = 'report'
    success_url = '/report'

    def test_func(self):
        questionnaire = self.get_object()
        if self.request.user == questionnaire.author:
            return True
        return False
        
@login_required
def tentang_manajement(request):
    return render(request, 'blog/tentang_manajement.html')
@login_required
def tentang_biorisiko(request):
    return render(request, 'blog/tentang_biorisiko.html')
@login_required
def tentang_SMBL(request):
    return render(request, 'blog/tentang_SMBL.html')

class ReportPDFView(LoginRequiredMixin, DetailView):
    model = Questionnaire  # <app>/<model>_<viewtype>.html
    context_object_name = 'report'
    template_name = 'blog/report_pdf.html'
    
@login_required
def compare_laporan(request):
    if request.method == 'POST':
        form = CompareReportForm(request.POST, instance=request.user)
        if form.is_valid():
            pilihan_1 = form.cleaned_data.get('pilihan_1')
            pilihan_2 = form.cleaned_data.get('pilihan_2')
            try:
                report_1 = Questionnaire.objects.filter(author=request.user).get(id=pilihan_1)
                report_2 = Questionnaire.objects.filter(author=request.user).get(id=pilihan_2)
                reports = Questionnaire.objects.filter(author=request.user)
            except:
                report_1 = None
                report_2 = None
            context = {
                'report_1': report_1,
                'report_2': report_2,
                'reports': reports,
            }
            return render(request, 'blog/compare_laporan.html', context)
    else:
        form = CompareReportForm(instance=request.user)
        context_2 = {
            'this_form': form,
            'reports': Questionnaire.objects.filter(author=request.user)
        }
        return render(request, 'blog/compare_laporan.html', context_2)

