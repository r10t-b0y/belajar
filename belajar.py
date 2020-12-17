# Program pengisian biodata
import os
print "Selamat Datang Di Project Saya"
print "Calon Member Baru Wajib Intro"

# Input
nama = raw_input("Masukkan Nama Samaran Anda := ")
umur = int(input("Masukkan Usia Anda := "))
pk = raw_input("Masukkan Profesi Anda := ")
asal = raw_input("Masukkan Alamat Anda := ")
contact = int(input("Masukkan Nomer Anda {contoh 6285xxxxxxxxx}:= "))

# Output
print "Nama = ",nama,",","Usia = ",umur,",","Profesi = ",pk

# Jika tidak cukup umur
if(umur < 18):
    print "Maaf Usia Anda Masih Belum Mencukupi Syarat Untuk Masuk Grup Saya"
    sleep 5
    os.system("exit")

# Jika cukup umur
elif(umur >= 18):
    print "Selamat Anda Telah Mencukupi Syarat Untuk Masuk Grup Saya"
    print "Semoga Tidak Betah :V"
    print "Link Grup = "https://chat.whatsapp.com/ErrhWVMRczE5s8uT8LLkE2

# Jika polisi
if(pk = polisi):
    print "Maaf Anda Tidak Boleh Masuk Grup Kami"
    sleep 5
    os.system("exit")
