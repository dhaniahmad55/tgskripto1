import string

abjad = string.printable


key = int(input('Masukkan cipher key : '))


def encode(pesan, cipher_key):
    pesan = pesan.lower()
    hasilencode = ''
    for karakter in pesan:
        if karakter in abjad:
            indexlama = abjad.index(karakter)
            indexbaru = (indexlama + cipher_key) % len(abjad)
            abjadbaru = abjad[indexbaru]
            hasilencode = hasilencode + abjadbaru
        else:
            hasilencode = hasilencode + ' '
    return hasilencode


pesan = input('Masukkan kalimat yang ingin dienkripsi : ')
# ENKRIPSI
pesanhasil = encode(pesan, key)
print('Masukkan kalimat:', pesan)
print('Hasil enkripsi kalimat dengan key', key, 'adalah : ', pesanhasil)

# DEKRIPSI

pesanawal = encode(pesanhasil, -key)
print('hasil dienkripsi ulang kalimat key ',
      -key, 'adalah : ', pesanawal)
