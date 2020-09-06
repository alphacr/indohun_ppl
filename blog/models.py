from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from users.models import Profile
import hashlib
import random
import sys


# Create your models here.


class ContactUs(models.Model):
    nama_lengkap = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    alamat = models.CharField(max_length=100, blank=True)
    pesan = models.TextField()

    def __str__(self):
        return f'Pesan dari {self.nama_lengkap}'

class Questionnaire(models.Model):
    # Operational
    judul_laporan = models.CharField(max_length=50, blank=False, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    jenis_penilaian_choices = (
        ('Penilaian Mandiri (Self Assessment)',
         'Penilaian Mandiri (Self Assessment)'),
        ('Penilaian Pendampingan (Technical Assessment)',
         'Penilaian Pendampingan (Technical Assessment)'),
    )
    # Stage 0 fields
    penilai = models.CharField(max_length=50, blank=False, null=True)
    afiliasi_penilai = models.CharField(max_length=50, blank=False, null=True)
    jenis_penilaian = models.CharField(
        max_length=50,  blank=True, null=True, choices=jenis_penilaian_choices)
    personel_yang_diwawancarai = models.CharField(
        max_length=50, blank=False, null=True)
    
     # Stage 1 fields
    nilai_no_1 = models.IntegerField(default=0, null=True)
    keterangan_kebijakan_sistem_manajemen_biorisiko = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_kebijakan_sistem_manajemen_biorisiko = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_2 = models.IntegerField(default=0, null=True)
    keterangan_tujuan_dan_program_manajemen_biorisiko = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_tujuan_dan_program_manajemen_biorisiko = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_3 = models.IntegerField(default=0, null=True)
    keterangan_tanggung_jawab_dan_wewenang = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_tanggung_jawab_dan_wewenang = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_4 = models.IntegerField(default=0, null=True)
    keterangan_pencatatan_dokumen_dan_pengendalian_dokumen = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_pencatatan_dokumen_dan_pengendalian_dokumen = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_5 = models.IntegerField(default=0, null=True)
    keterangan_perubahan_terkait_manajemen_biorisiko = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_perubahan_terkait_manajemen_biorisiko = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_6 = models.IntegerField(default=0, null=True)
    keterangan_komunikasi_dan_konsultasi = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_komunikasi_dan_konsultasi = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_7 = models.IntegerField(default=0, null=True)
    keterangan_perencanaan_dan_program_kerja = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_perencanaan_dan_program_kerja = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_8 = models.IntegerField(default=0, null=True)
    keterangan_persyaratan_legal_aturan_atau_izin = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_persyaratan_legal_aturan_atau_izin = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_9 = models.IntegerField(default=0, null=True)
    keterangan_inspeksi_dan_audit = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_inspeksi_dan_audit = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_10 = models.IntegerField(default=0, null=True)
    keterangan_pengendalian_ketidaksesuaian_dan_perbaikan = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_pengendalian_ketidaksesuaian_dan_perbaikan = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_11 = models.IntegerField(default=0, null=True)
    keterangan_pengembangan_berkelanjutan = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_pengembangan_berkelanjutan = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_12 = models.IntegerField(default=0, null=True)
    keterangan_kontraktor_dan_suplier_purchasing = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_kontraktor_dan_suplier_purchasing = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_13 = models.IntegerField(default=0, null=True)
    keterangan_review_dan_perbaikan_manajemen_biorisiko = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_review_dan_perbaikan_manajemen_biorisiko = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    # Stage 2 fields
    nilai_no_14 = models.IntegerField(default=0, null=True)
    keterangan_proses_metode_dan_prosedur = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_proses_metode_dan_prosedur = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_15 = models.IntegerField(default=0, null=True)
    keterangan_ruang_lingkup_dan_penjadwalan = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_ruang_lingkup_dan_penjadwalan = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_16 = models.IntegerField(default=0, null=True)
    keterangan_peran_dan_tanggung_jawab = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_peran_dan_tanggung_jawab = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_17 = models.IntegerField(default=0, null=True)
    keterangan_identifikasi_hazard = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_identifikasi_hazard = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_18 = models.IntegerField(default=0, null=True)
    keterangan_pengendalian_risiko = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_pengendalian_risiko = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_19 = models.IntegerField(default=0, null=True)
    keterangan_inventarisasi_informasi_dan_pencatatan = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_inventarisasi_informasi_dan_pencatatan = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_20 = models.IntegerField(default=0, null=True)
    keterangan_penyimpanan_bahan_biologik_dan_bahan_berbahaya_lainnya = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_penyimpanan_bahan_biologik_dan_bahan_berbahaya_lainnya = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_21 = models.IntegerField(default=0, null=True)
    keterangan_transfer_bahan_biologik_dan_bahan_berbahaya_lainnya = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_transfer_bahan_biologik_dan_bahan_berbahaya_lainnya = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_22 = models.IntegerField(default=0, null=True)
    keterangan_pengendalian_dan_monitoring = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_pengendalian_dan_monitoring = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    # Stage 3 fields
    nilai_no_23 = models.IntegerField(default=0, null=True)
    keterangan_general_safety = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_general_safety = models.TextField(default='Isi Laporan', blank=True, null=True)

    # Stage 4 fields
    nilai_no_24 = models.IntegerField(default=0, null=True)
    keterangan_rekrutmen_pelatihan_dan_kompetensi = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_rekrutmen_pelatihan_dan_kompetensi = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_25 = models.IntegerField(default=0, null=True)
    keterangan_suksesi_dan_eksklusi = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_suksesi_dan_eksklusi = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_26 = models.IntegerField(default=0, null=True)
    keterangan_GMT_personel = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_GMT_personel = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_27 = models.IntegerField(default=0, null=True)
    keterangan_GMT_peralatan = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_GMT_peralatan = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_28 = models.IntegerField(default=0, null=True)
    keterangan_pelabelan = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_pelabelan = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_29 = models.IntegerField(default=0, null=True)
    keterangan_pengadaan_alat_pelindung_diri = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_pengadaan_alat_pelindung_diri = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_30 = models.IntegerField(default=0, null=True)
    keterangan_APD_personel = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_APD_personel = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_31 = models.IntegerField(default=0, null=True)
    keterangan_pemeliharaan_dan_dekontaminasi_reusable_apd = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_pemeliharaan_dan_dekontaminasi_reusable_apd = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_32 = models.IntegerField(default=0, null=True)
    keterangan_latar_belakang_sdm = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_latar_belakang_sdm = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_33 = models.IntegerField(default=0, null=True)
    keterangan_program_kesehatan_kerja = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_program_kesehatan_kerja = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_34 = models.IntegerField(default=0, null=True)
    keterangan_vaksinasi = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_vaksinasi = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_35 = models.IntegerField(default=0, null=True)
    keterangan_kedaruratan_medik = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_kedaruratan_medik = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_36 = models.IntegerField(default=0, null=True)
    keterangan_identifikasi_perencanaan_dan_respon_keadaan_darurat = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_identifikasi_perencanaan_dan_respon_keadaan_darurat = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_37 = models.IntegerField(default=0, null=True)
    keterangan_simulasi_dan_pelatihan_tanggap_darurat = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_simulasi_dan_pelatihan_tanggap_darurat = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_38 = models.IntegerField(default=0, null=True)
    keterangan_rencana_tanggap_darurat_menghadapi_kejadian_luar_duga = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_rencana_tanggap_darurat_menghadapi_kejadian_luar_duga = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_39 = models.IntegerField(default=0, null=True)
    keterangan_ketersediaan_peralatan_keselamatan_untuk_tanggap_darurat = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_ketersediaan_peralatan_keselamatan_untuk_tanggap_darurat = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_40 = models.IntegerField(default=0, null=True)
    keterangan_perencanaan_desain_dan_verifikasi_mencakup_commissioning_dan_decommisioning = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_perencanaan_desain_dan_verifikasi_mencakup_commissioning_dan_decommisioning = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_41 = models.IntegerField(default=0, null=True)
    keterangan_infrastruktur_dan_operasional = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_infrastruktur_dan_operasional = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_42 = models.IntegerField(default=0, null=True)
    keterangan_manajemen_pemeliharaan = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_manajemen_pemeliharaan = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_43 = models.IntegerField(default=0, null=True)
    keterangan_monitoring_peralatan = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_monitoring_peralatan = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_44 = models.IntegerField(default=0, null=True)
    keterangan_kalibrasi = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_kalibrasi = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_45 = models.IntegerField(default=0, null=True)
    keterangan_sertifikasi = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_sertifikasi = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_46 = models.IntegerField(default=0, null=True)
    keterangan_validasi = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_validasi = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_47 = models.IntegerField(default=0, null=True)
    keterangan_pengolahan_limbah_dan_bahan_berbahaya_biologi_kimia = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_pengolahan_limbah_dan_bahan_berbahaya_biologi_kimia = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_48 = models.IntegerField(default=0, null=True)
    keterangan_inaktivasi_bahan_biologik_dan_bahan_berbahaya_lainnya = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_inaktivasi_bahan_biologik_dan_bahan_berbahaya_lainnya = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_49 = models.IntegerField(default=0, null=True)
    keterangan_dekontaminasi_dan_disinfeksi_peralatan = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_dekontaminasi_dan_disinfeksi_peralatan = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_50 = models.IntegerField(default=0, null=True)
    keterangan_prosedur_penerimaan_dan_pengiriman_bahan_biologik_dan_bahan_berbahaya_lainnya = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_prosedur_penerimaan_dan_pengiriman_bahan_biologik_dan_bahan_berbahaya_lainnya = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_51 = models.IntegerField(default=0, null=True)
    keterangan_keamanan_fisik_dan_pengendalian_personel = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_keamanan_fisik_dan_pengendalian_personel = models.TextField(
        default='Isi Laporan' , blank=True, null=True)

    nilai_no_52 = models.IntegerField(default=0, null=True)
    keterangan_keamanan_informasi = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_keamanan_informasi = models.TextField(default='Isi Laporan', blank=True, null=True)

    nilai_no_53 = models.IntegerField(default=0, null=True)
    keterangan_pengendalian_personel = models.TextField(default='Isi Laporan', blank=True, null=True)
    rekomendasi_pengendalian_personel = models.TextField(default='Isi Laporan', blank=True, null=True)

    # Stage 5 fields
    nilai_no_54 = models.IntegerField(default=0, null=True)
    keterangan_investigasi_kecelakaan_dan_insiden = models.TextField(
        default='Isi Laporan' , blank=True, null=True)
    rekomendasi_investigasi_kecelakaan_dan_insiden = models.TextField(
        default='Isi Laporan' , blank=True, null=True)


    kelemahan_utama = models.TextField(default='Isi Laporan', blank=True, null=True)
    kekuatan_utama = models.TextField(default='Isi Laporan', blank=True, null=True)
    saran_untuk_perbaikan = models.TextField(default='Isi Laporan', blank=True, null=True)

    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('report-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.judul_laporan}'

class CompareReport(models.Model):
    pilihan_1 = models.CharField(max_length=50, null=True)
    pilihan_2 = models.CharField(max_length=50, null=True)