nama   = 'Hanifa Aulia Kamal'
nim    = 2310433024
shift  = '2'
print('Nama     : '+ nama)
print('NIM      : ', nim)
print('Shift    : '+ shift)
#program untuk memesan tiket bus
print('\n==========================')
print(" Bus PT.ANS Lintas Sumatera ")
print('\n==========================')

medan = 350000
pekanbaru = 300000
padang = 250000
palembang = 400000
lampung = 350000
aceh = 400000

print ("Bus PT. ANS Lintas Sumatera")
print ("Tujuan :")
print ("1. Banda Aceh : Rp.", aceh) 
print ("2. Medan      : Rp.", medan)
print ("3. Padang     : Rp.", padang)
print ("4. Pekanbaru  : Rp.", pekanbaru)
print ("5. lampung    : Rp.", lampung)
print ("6. Palembang  : Rp.", palembang)

tujuan=str (input("Tujuan yang dipilih: "))


if tujuan == "1":
  harga = 350000
elif tujuan == "2":
  harga = 300000
elif tujuan == "3":
  harga = 250000
elif tujuan == "4":
  harga = 400000
elif tujuan == "5":
  harga = 350000
elif tujuan == "6": 
  harga =400000
  
  print (" ")
  
ekonomi=10000
bisnis=20000
first= 30000
  
print ("Kelas (biaya tambahan) :")
print ("1. Ekonomi Class  : Rp." ,ekonomi)
print ("2. Bisnis Class   : Rp." ,bisnis)
print ("3. First Class    : Rp." ,first)
kelas=str (input("kelas yang dipilih: "))

if kelas =="1":
  biaya=10000
else:
  if kelas =="2":
    biaya=20000
  else :
    if kelas =="3":
       biaya=30000
  
jumlah=int (input("Jumlah : "))

total=(jumlah)* (harga + biaya)

if jumlah < 3:
  diskon = 0
elif jumlah == 3:
  diskon= 0.05* total
elif jumlah > 3:
  diskon= 0.05* total
elif jumlah < 5:
  diskon= 0.05* total
elif jumlah == 5: 
  diskon= 0.05* total

else :
  if jumlah > 5:
    diskon =0.1*total
    
totalakhir = total-diskon

print (" ")
print ("Tujuan               : Aceh ")
print ("Kelas                : First Class" )
print ("Jumlah Tiket.        : 4")
print ("Total                : Rp." ,total)
print ("Diskon               : Rp." ,diskon)
print ("Total Setelah Diskon : Rp." ,totalakhir)
print (" ")