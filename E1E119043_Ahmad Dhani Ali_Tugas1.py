print ("Ahmad Dhani Ali")
print ("E1E119043")
def encript(plaintext, key):
    encoded = []

    for i in range(len(plaintext)):
        xor = ord(plaintext[i]) ^ ord(key[i % len(key)])
        encoded.append(chr(xor))

    return ''.join(encoded)

def decript(chipertext, key):
    return encript(chipertext, key)

def main():
    print("Pilih Menu: \n1. Enkripsi\n2. Dekripsi")
    pilihan = int(input("Pilihan: "))

    if pilihan == 1:
        plaintext = str(input("Masukkan plaintext: "))
        key = str(input("Masukkan key: "))

        print("Plaintext: ", plaintext)
        print("Enkripsi: ", encript(plaintext, key))
    elif pilihan == 2:
        chipertext = str(input("Masukkan chipertext: "))
        key = str(input("Masukkan key: "))

        print("Chipertext: ", chipertext)
        print("Dekripsi: ", decript(chipertext, key))
    else:
        exit()

main()
