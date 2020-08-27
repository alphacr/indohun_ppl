from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['negara', 'provinsi', 'provinsi_selain_indonesia', 'nama_lengkap_laboratorium', 'akronim_laboratorium', 'alamat_lengkap',
                  'kab_kota']

class SplitUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['kode_pos', 'posisi_lintang', 'posisi_bujur', 'nomor_telepon', 'fax', 'website', 'afiliasi_laboratorium',
                  'administrasi_laboratorium', 'aktivitas_laboratorium', 'tambahan_info']