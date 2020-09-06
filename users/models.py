from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    negara_choices = (
        ('Indonesia', 'Indonesia'),
        ('Luar Negeri', 'Luar Negeri'),
    )
    negara = models.CharField(
        max_length=30, blank=False, null=True, choices=negara_choices)
    provinsi_choices = (
        ('Aceh', 'Aceh'),
        ('Sumatra Utara', 'Sumatra Utara'),
        ('Sumatra Barat', 'Sumatra Barat'),
        ('Riau', 'Riau'),
        ('Kepulauan Riau', 'Kepulauan Riau'),
        ('Jambi', 'Jambi'),
        ('Bengkulu', 'Bengkulu'),
        ('Sumatra Selatan', 'Sumatra Selatan'),
        ('Kepulauan Bangka Belitung', 'Kepulauan Bangka Belitung'),
        ('Lampung', 'Lampung'),
        ('Banten', 'Banten'),
        ('Jawa Barat', 'Jawa Barat'),
        ('Jakarta', 'Jakarta'),
        ('Jawa Tengah', 'Jawa Tengah'),
        ('Yogyakarta', 'Yogyakarta'),
        ('Jawa Timur', 'Jawa Timur'),
        ('Bali', 'Bali'),
        ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'),
        ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'),
        ('Kalimantan Barat', 'Kalimantan Barat'),
        ('Kalimantan Selatan', 'Kalimantan Selatan'),
        ('Kalimantan Tengah', 'Kalimantan Tengah'),
        ('Kalimantan Timur', 'Kalimantan Timur'),
        ('Kalimantan Utara', 'Kalimantan Utara'),
        ('Gorontalo', 'Gorontalo'),
        ('Sulawesi Barat', 'Sulawesi Barat'),
        ('Sulawesi Selatan', 'Sulawesi Selatan'),
        ('Sulawesi Tengah', 'Sulawesi Tengah'),
        ('Sulawesi Tenggara', 'Sulawesi Tenggara'),
        ('Sulawesi Utara', 'Sulawesi Utara'),
        ('Maluku', 'Maluku'),
        ('Maluku Utara', 'Maluku Utara'),
        ('Papua', 'Papua'),
        ('Papua Barat', 'Papua Barat'),
    )
    provinsi = models.CharField(
        max_length=50, blank=True, null=True, choices=provinsi_choices)
    provinsi_selain_indonesia = models.CharField(
        max_length=50, blank=True, null=True)
    nama_lengkap_laboratorium = models.CharField(
        max_length=100)
    akronim_laboratorium = models.CharField(max_length=100)
    alamat_lengkap = models.CharField(max_length=100)
    kab_kota = models.CharField(max_length=50)
    kode_pos = models.CharField(max_length=10, blank=True)
    posisi_lintang = models.CharField(max_length=100, blank=True)
    posisi_bujur = models.CharField(max_length=100, blank=True)
    nomor_telepon = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, blank=True)
    website = models.CharField(max_length=50, blank=True)
    afiliasi_choices = (
        ('Publik/Pemerintah', 'Publik/Pemerintah'),
        ('Privat', 'Privat'),
        ('Universitas', 'Universitas'),
        ('Industri', 'Industri'),
        ('Lainnya', 'Lainnya')
    )
    afiliasi_laboratorium = models.CharField(
        max_length=30, blank=True, null=True, choices=afiliasi_choices)
    administrasi_choices = (
        ('Provinsi', 'Provinsi'),
        ('Nasional', 'Nasional'),
        ('Regional', 'Regional'),
        ('Internasional', 'Internasional'),
        ('N/A', 'N/A'),
    )
    administrasi_laboratorium = models.CharField(
        max_length=30, blank=False, null=True, choices=administrasi_choices)
    aktivitas_choices = (
        ('Penelitian', 'Penelitian'),
        ('Diagnostik', 'Diagnostik'),
        ('Produksi Bahan Biologis', 'Produksi Bahan Biologis'),
        ('Lainnya', 'Lainnya'),
    )
    aktivitas_laboratorium = models.CharField(
        max_length=50, blank=True, null=True, choices=aktivitas_choices)
    tambahan_info = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.nama_lengkap_laboratorium}'
