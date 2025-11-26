from django.contrib import admin
from .models import Pemain

# Definisikan kelas Admin kustom untuk model Pemain
class PemainAdmin(admin.ModelAdmin):
    # KUNCI: Atribut list_display menentukan kolom-kolom yang akan ditampilkan
    # di halaman daftar (list) Django Admin. Ini harus selaras dengan field model Anda.
    list_display = (
        'name', 
        'age', 
        'country', 
        'position', 
        'player_number', 
        'salary',
        'id' # Opsional: menampilkan ID unik pemain
    )
    
    # Menambahkan filter di sidebar admin (berguna untuk navigasi cepat)
    list_filter = ('country', 'position')
    
    # Menambahkan kolom pencarian (search bar)
    search_fields = ('name', 'country', 'position')
    
    # Menentukan bidang yang akan menjadi link untuk mengedit objek
    list_display_links = ('name',)

# Daftarkan model Pemain dengan kelas Admin kustom
admin.site.register(Pemain, PemainAdmin)