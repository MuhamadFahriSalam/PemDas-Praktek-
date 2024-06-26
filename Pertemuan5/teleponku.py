from datetime import datetime
import random
currentDate = datetime.now()

def nameMonth(month):
    indonesian_months = {
        1: "JANUARI",
        2: "FEBRUARI",
        3: "MARET",
        4: "APRIL",
        5: "MEI",
        6: "JUNI",
        7: "JULI",
        8: "AGUSTUS",
        9: "SEPTEMBER",
        10: "OKTOBER",
        11: "NOVEMBER",
        12: "DESEMBER"
    }
    return indonesian_months[month]

nama = input("Masukkan nama?")
tagihanList = []

tglbayar = datetime(currentDate.year, currentDate.month, currentDate.day, currentDate.hour, currentDate.minute)
notransaksi = random.randint(10000000000, 99999999999)

keluar = False
while(keluar == False):
    tagihan = int(input("Masukkan tagihan?"))
    if (tagihan == 0):
        keluar = True
        break
    tagihanList.append(tagihan)

print('{:^100}'.format('BUKTI PEMBAYARAN TAGIHAN TELEPONE'))
print()
print('{:25}'.format('TGL BAYAR')+
      '{:25}'.format(f': {tglbayar}'))
print('{:25}'.format('No. JASTEL')+
      '{:25}'.format(f': {nameMonth(currentDate.month)} {currentDate.year}')+
      '{:25}'.format(''))
print('{:25}'.format('Nama')+
      '{:25}'.format(f': {nama}'))
print('{:25}'.format('TAGIHAN/DATEL')+
      '{:25}'.format(f': {currentDate.strftime("%m/%d%y")}'))
print('{:25}'.format('NO. TRANSAKSI')+
      '{:25}'.format(f': {notransaksi}'))


print("")
print('Tagihan Telepone Anda')
for tagihan in tagihanList:
    print('Rp'+'{:.>25d}'.format(tagihan))

