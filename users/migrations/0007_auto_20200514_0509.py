# Generated by Django 3.0.5 on 2020-05-14 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200514_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='provinsi',
            field=models.CharField(blank=True, choices=[('Aceh', 'Aceh'), ('Sumatra Utara', 'Sumatra Utara'), ('Sumatra Barat', 'Sumatra Barat'), ('Riau', 'Riau'), ('Kepulauan Riau', 'Kepulauan Riau'), ('Jambi', 'Jambi'), ('Bengkulu', 'Bengkulu'), ('Sumatra Selatan', 'Sumatra Selatan'), ('Kepulauan Bangka Belitung', 'Kepulauan Bangka Belitung'), ('Lampung', 'Lampung'), ('Banten', 'Banten'), ('Jawa Barat', 'Jawa Barat'), ('Jakarta', 'Jakarta'), ('Jawa Tengah', 'Jawa Tengah'), ('Yogyakarta', 'Yogyakarta'), ('Jawa Timur', 'Jawa Timur'), ('Bali', 'Bali'), ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'), ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'), ('Kalimantan Barat', 'Kalimantan Barat'), ('Kalimantan Selatan', 'Kalimantan Selatan'), ('Kalimantan Tengah', 'Kalimantan Tengah'), ('Kalimantan Timur', 'Kalimantan Timur'), ('Kalimantan Utara', 'Kalimantan Utara'), ('Gorontalo', 'Gorontalo'), ('Sulawesi Barat', 'Sulawesi Barat'), ('Sulawesi Selatan', 'Sulawesi Selatan'), ('Sulawesi Tengah', 'Sulawesi Tengah'), ('Sulawesi Tenggara', 'Sulawesi Tenggara'), ('Sulawesi Utara', 'Sulawesi Utara'), ('Maluku', 'Maluku'), ('Maluku Utara', 'Maluku Utara'), ('Papua', 'Papua'), ('Papua Barat', 'Papua Barat')], max_length=50, null=True),
        ),
    ]
