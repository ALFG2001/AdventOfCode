import hashlib

stringaHash = "     "
numero = 923329
while stringaHash[:6] != "000000":
    try:
        print(numero)
        stringa = f"bgvyzdsv{numero}".encode()
        result = hashlib.md5(stringa)
        stringaHash = result.hexdigest()
        print(stringaHash)

    finally:
        numero += 1