letters='abcdefghijklmnopqrstuvwxyz'
num_letters=len(letters)

def encrypt(plaintext, key):
    ciphertext=''
    for letter in plaintext:
        letter=letter.lower()
        if not letter==' ':
            index=letters.find(letter)
            if index==-1:
                ciphertext+=letter
            else:
                new_index=index+key
                if new_index>=num_letters:
                    new_index-=num_letters
                ciphertext+=letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext=''
    for letter in ciphertext:
        letter=letter.lower()
        if not letter==' ':
            index=letters.find(letter)
            if index==-1:
                plaintext+=letter
            else:
                new_index=index-key
                if new_index<0:
                    new_index=num_letters
                plaintext+=letters[new_index]
    return plaintext



print()
print('*-*-*-* CEASAR CIPHER *-*-*-*')
print()

print('Select : (a) encrypt | (b) decrypt ')
user=input('(a)/(b): ').lower()
print()

if user=='a':
    print('encryption mode selected')
    print()
    key=int(input('Enter the key (1 to 26): '))
    text=input('Enter the text to encrypt: ')
    ciphertext=encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user=='b':
    print('decryption mode selected')
    print()
    key=int(input('Enter the key (1 to 26): '))
    text=input('Enter the text to decrypt: ')
    plaintext=decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')


