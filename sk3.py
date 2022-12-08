harga = int(input('daftar harga barang: '))

if harga >= 200000:
    print('bisa membeli sepeda motor')
elif harga >= 150000:
    print('bisa membeli mobil')
elif harga >= 100000:
    print('bisa membeli pesawat')
elif harga >= 80000:
    print('bisa membeli rumah')
else:
    print('maaf nabung lagi')    