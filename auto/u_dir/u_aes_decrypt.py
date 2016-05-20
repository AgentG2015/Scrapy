import os
import codecs
import json

from Crypto.Cipher import AES

def pkcs5_unpad(s):
    """
    unpadding according to PKCS #5

    @param s: string to unpad
    @type s: string

    @rtype: string
    """
    return s[0:-ord(s[-1])]

try:
    encryped_file_ext = '.html'
    output_file_ext = '.unitypackage'
    chunksize = 40960

    encryped_list = [os.path.splitext(f)[0] for f in os.listdir('.') if os.path.splitext(f)[1] == encryped_file_ext]

    for input_file in encryped_list:
        json_file = [f for f in os.listdir('.') if os.path.splitext(f)[1] != encryped_file_ext and input_file in os.path.splitext(f)[0]][0]
        with codecs.open(json_file, 'r', 'utf-8') as f:
            j = json.loads(f.read())
            keyIV = j['download']['key']
            output_file = j['download']['filename_safe_package_name'] + output_file_ext

        key = keyIV[:64].decode('hex')
        iv = keyIV[64:].decode('hex')
        cipher = AES.new(key, AES.MODE_CBC, iv)

        with open(input_file + encryped_file_ext, 'rb') as input_f, open(output_file, 'wb') as output_f:
            while True:
                chunk = input_f.read(chunksize)
                if chunk:
                    if len(chunk) != chunksize:
                        output_f.write(pkcs5_unpad(cipher.decrypt(chunk)))
                    else:
                        output_f.write(cipher.decrypt(chunk))
                else:
                    break

        # now delete
        os.remove(input_file + encryped_file_ext)
        os.remove(json_file)
except Exception as e:
    raw_input('Exception: ' + str(e))