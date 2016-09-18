## SITHIS: Crypt
## For encryption and decryption of data and Keys
## author mls

# Import libs
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import random
import os
import sys

######################
## Symmetric Crypto ##
######################
class SymmetricCrypto():
  # Class to provide an object for symmetric cryptography interaction

  def __init__(self, key=None):
    # Init object
    self.block_size = 16
    self.pad = lambda s: s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)
    self.unpad = lambda s : s[0:-ord(s[-1])]

    # Attempt to load key and generate one if not available
    if not key:
      self.load_symmetric_key()
    else:
      self.key = key

  def load_symmetric_key(self):
      # Function to load a local symmetric key if one is present

      if os.path.isfile("key.txt"):
        fh = open("key.txt", "r")
        self.key = fh.read()
        fh.close()
      else:
        self.key = self.generate_key()

  def generate_key(self):
    # Function to generate a random key for encryption

    key = ''.join(random.choice('0123456789ABCDEF') for i in range(32))
    # DEV - Write to file
    fh = open("key.txt", "w")
    fh.write(key)
    fh.close()

    return key

  def process_file(self, file, action):
      # Function to process the provided file ready for encryption/decryption

      # Open file and read contents
      try:
        fh = open(file, "rb")
        contents = fh.read()
        fh.close()
      except IOError:
        file_details = {'error': True}
        return file_details

      # Process file details
      file_details = {'full_path': file,
                           'full_filename': file.split("\\")[-1],
                           'extension' : str(file.split("\\")[-1]).split(".")[1],
                           'filename' : str(file.split("\\")[-1]).split(".")[0],
                           'contents' : contents
                           }

      # Specify file state depending on action
      if action == "encrypt":
        file_details['state'] = "unencrypted"
      elif action == "decrypt":
        file_details['state'] = "encrypted"
        # Try to decide, if not possible then file is not encrypted
        try:
          file_details['hex'] = contents.decode("hex")
        except TypeError:
          file_details['error'] = True
          return file_details

      # Error Checking
      file_details['error'] = False

      # Return dict
      return file_details


  def decrypt_file(self, file):
    # Function to decrypt a dataset

    # Get file details and process content. Check for errors
    file_details = self.process_file(file, "decrypt")
    if file_details['error']:
      return
    ciphertext = file_details['hex']

    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = AES.new(self.key, AES.MODE_CBC, iv)
    cleartext = self.unpad(cipher.decrypt(ciphertext))

    # Write decrypted version
    try:
      fh = open("%s" % file_details['full_path'], "wb")
    except IOError:
      return
    fh.write(cleartext)
    fh.close()

    # Update state
    file_details['state'] = "unencrypted"


  def encrypt_file(self, file):
    # Function to encrypt a dataset

    # Get file details and process content
    file_details = self.process_file(file, "encrypt")
    if file_details['error']:
      return False

    # Attempt padding
    #try:
    to_encrypt = self.pad(file_details['contents'])
    #except MemoryError:
    #  return False

    iv = Random.new().read(AES.block_size)
    cipher = AES.new(self.key, AES.MODE_CBC, iv)
    try:
      ciphertext = (iv + cipher.encrypt(to_encrypt)).encode("hex")
    except MemoryError:
      return False

    # Write encrypted version
    try:
      fh = open("%s" % file_details['full_path'], "wb")
    except IOError:
      return False
    fh.write(ciphertext)
    fh.close()

    # Update state
    file_details['state'] = "encrypted"
    return True


########################
## GenerateKeys Class ##
########################
class GenerateKeys():
  # Class to generate asymmetric keys for symmetric key encryption, via RSA

  def __init__(self):
    # Init object and define vars
    self.local_public_key = ""
    self.local_private_key = ""
    self.key_length = 2048

    # Generate Keys
    rsa_handle = RSA.generate(self.key_length)
    self.local_private_key = rsa_handle.exportKey('PEM')
    self.local_public_key = rsa_handle.publickey()
    self.local_public_key = self.local_public_key.exportKey('PEM')

###################
## Encrypt Class ##
###################
class EncryptKey():
  # Class to create Encrypt object for symmetric key

  def __init__(self, recipient_public_key, sym_key):
    # Init object
    self.recipient_public_key = recipient_public_key
    self.key_to_encrypt = str(sym_key)

    # Encrypt the data
    self.encrypted_key = self.encrypt_key()

  def encrypt_key(self):
    # Function to encrypt the provided symmetric key

    rsa_handle = RSA.importKey(self.recipient_public_key)
    key = rsa_handle.encrypt(self.key_to_encrypt, 1)

    return key


###################
## Decrypt Class ##
###################
class DecryptKey():
  # Class to create Decrypt object for symmetric key

  def __init__(self, private_key, sym_key, phrase):
    # Init object
    self.private_key = private_key
    self.key_to_decrypt = sym_key
    self.phrase = phrase

    # Decrypt the data
    self.decrypted_key = self.decrypt_key()

  def decrypt_key(self):
    # Function to decrypt the provided symmetric key

    rsa_handle = RSA.importKey(self.private_key, self.phrase)
    key = rsa_handle.decrypt(self.key_to_decrypt)

    return key

# TEST
if __name__ == "__main__":
  pass
  # Sym test
  #test = SymmetricCrypto()
  #test.encrypt_file("C:\\Users\\Sithis\\development\\experimental\\crypto\\test.txt")
  #test.decrypt_file("C:\\Users\\Sithis\\development\\experimental\\crypto\\test.txt")


  # PKI Test
  #test = GenerateKeys()
  #encrypt_test = EncryptKey(test.local_public_key, "C3C9BF85E96BC3489996280489C1EE24")
  #decrypt_test = DecryptKey(test.local_private_key, encrypt_test.encrypted_key, None)
  #print(encrypt_test.encrypted_key)
  #print(decrypt_test.decrypted_key)

