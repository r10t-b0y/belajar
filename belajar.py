# Program pengisian biodata
print "Selamat Datang Di Grup Saya"
print "Member Baru Wajib Intro"

# Input
nama = raw_input ("Masukkan Nama Samaran Anda := ")
umur = input ("Masukkan Usia Anda := ")
asal = raw_input ("Masukkan Alamat Anda := ")
contact = input ("Masukkan Nomer Anda {contoh 6285xxxxxxxxx}:= ")

# Output
print "Nama = ",nama,",","Usia = ",umur

# Jika tidak cukup umur
if(umur < 18):
    print "Maaf Usia Anda Masih Belum Mencukupi Syarat Untuk Masuk Grup Saya"
    quit()

# Jika cukup umur
if(umur >= 18):
    print "Selamat Anda Telah Mencukupi Syarat Untuk Masuk Grup Saya"
    print "Semoga Tidak Betah :V"
    print "Link Grup = https://chat.wahatsapp.com/AJU875H2J"
