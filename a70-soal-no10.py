def hitungbayarclaim(nilai):
    if nilai <= 500:
        return 0
    elif nilai >= 2000:
        return nilai
    else:
        deductible = nilai - 500
        return deductible

klaim = [400, 1000, 2500]
bayar = 0

for i in klaim:
    payment = hitungbayarclaim(i)
    bayar += payment

print("Total pembayaran klaim:", bayar)
