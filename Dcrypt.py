import hashlib

def decrypt(hash_value):
    with open('password_list.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if hashlib.md5(line.encode()).hexdigest() == hash_value:
                return line
    return "Password not found in the list."

def main(hash_value):
    password = decrypt(hash_value)
    print(f"The decrypted password is: {password}")

if __name__ == '__main__':
    main(input("Enter the hashed value: "))
