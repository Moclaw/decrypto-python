import base64
import io
from Crypto.Cipher import AES
import argparse


def AESDecrypt(plainText, key):
    key = key.encode('utf-8')
    plainText = base64.b64decode(plainText)
    iv = plainText[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plainText = cipher.decrypt(plainText[AES.block_size:])
    plainText = plainText.decode('utf-8')
    plainText = plainText.rstrip('\0')
    return plainText


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="put secret key in to config.ini",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     )

    parser.add_argument("-p", "--password", action="store",
                        help="password before encryption")
    args = parser.parse_args()
    key = ''
    with open('config.ini', 'r') as f:
        key = f.read()

    encryptedText = args.password
    plainText = AESDecrypt(encryptedText, key)
    print('Password: '+plainText)
