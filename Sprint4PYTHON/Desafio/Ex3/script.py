import hashlib

while True:
    str1ng = str(input('Digite palavras para realizar o mascaramento: '))
    my_hash = hashlib.sha1(str1ng.encode()).hexdigest()
    print(my_hash)