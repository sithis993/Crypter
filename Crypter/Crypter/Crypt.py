'''
@summary: Generic High level encryption library
@author: MLS
'''

# Import libs
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Random import random
import os

# Import classes
from . import Base

######################
## Symmetric Crypto ##
######################
class SymmetricCrypto(Base.Base):
  # Class to provide an object for symmetric cryptography interaction

  def __init__(self, key=None):
    # Init object
    #self.pad = lambda s: s + (self.PADDING_BLOCK_SIZE - len(s) % self.PADDING_BLOCK_SIZE) * chr(self.PADDING_BLOCK_SIZE - len(s) % self.PADDING_BLOCK_SIZE)
    self.unpad = lambda s : s[0:-s[-1]]


  def pad(self, s):
    return s + bytes((self.PADDING_BLOCK_SIZE - len(s) % self.PADDING_BLOCK_SIZE) * chr(self.PADDING_BLOCK_SIZE - len(s) % self.PADDING_BLOCK_SIZE), encoding="utf-8")
      
  def init_keys(self, key=None):
      '''
      @summary: initialise the symmetric keys. Uses the provided key, or creates one
      @param key: If None provided, a new key is generated, otherwise the provided key is used
      '''
      
      if not key:
        print("Loading a key")
        self.load_symmetric_key()
      else:
        print("using existing key: %s" % key)
        self.key = key
      

  def load_symmetric_key(self):
      # Function to load a local symmetric key if one is present

      if os.path.isfile("key.txt"):
        fh = open("key.txt", "r")
        self.key = fh.read()
        fh.close()
        print("Key file already here. Using + " + self.key)
      else:
        print("No key file. Generating")
        self.key = self.generate_key()

  def generate_key(self):
    # Function to generate a random key for encryption
    print("writing out key to " + os.getcwd())

    key = ''.join(random.choice('0123456789ABCDEF') for i in range(32))
    # DEV - Write to file
    fh = open("key.txt", "w")
    fh.write(key)
    fh.close()

    return key

  def process_file(self, file, action, extension):
      '''
      @summary: Processes the specified file ready for encryption/decryption
      @param file: The absolute path to the target file
      @param extension: The extension of the encrypted file
      '''

      # Process file details
      try:
        file_details = {'full_path': file,
                        'full_filename': file.split("\\")[-1],
                        'extension' : str(file.split("\\")[-1]).split(".")[1],
                        'filename' : str(file.split("\\")[-1]).split(".")[0],
                        'locked_path': file + "." + extension
                        }
      except:
        file_details = {'full_path': file,
                        'full_filename': file.split("\\")[-1],
                        'extension' : None,
                        'filename' : str(file.split("\\")[-1]),
                        'locked_path': file + "." + extension
                        }

      # Specify file state depending on action
      if action == "encrypt":
        file_details['state'] = "unencrypted"
      elif action == "decrypt":
        file_details['state'] = "encrypted"

      # Error Checking
      file_details['error'] = False

      # Return dict
      return file_details


  def decrypt_file(self, file, decryption_key, extension):
    '''
    @summary: Decrypts the target file
    @param file: Absolute path to the file to decrypt
    @param extension: The extension that was added to the encrypted file
    '''

    # Get file details and check for errors
    file_details = self.process_file(file, "decrypt", extension)
    if file_details['error']:
      print("Some kind of error getting file details")
      return

    # Open file reading and writing handles
    try:
      fh_read = open(file_details["locked_path"], "rb")
      fh_write = open(file_details["full_path"], "wb")
    except IOError as io:
      print("Got IO Error below fh read and write: %s" % io)
      return False

    # Read blocks and decrypt
    while True:
      # 4118 for block size + iv + padding
      block = fh_read.read(self.BLOCK_SIZE_BYTES + 32)

      # Check that block is valid
      if not block:
        break

      ciphertext = block
      iv = ciphertext[:self.IV_SIZE]
      ciphertext = ciphertext[self.IV_SIZE:]
      cipher = AES.new(bytes(decryption_key, encoding="utf-8"), AES.MODE_CBC, iv)
      cleartext = self.unpad(cipher.decrypt(ciphertext))

      # Write decrypted block
      fh_write.write(cleartext)

    # Close file handle
    fh_write.close()
    fh_read.close()

    # Update state
    file_details['state'] = "unencrypted"

    return file_details["locked_path"]


  def encrypt_file(self, file, extension):
    '''
    @summary: Encrypts the target file
    @param file: Absolute path to the file to encrypt
    @param extension: The extension to add to the encrypted file
    '''

    # Get file details and process content
    file_details = self.process_file(file, "encrypt", extension)
    if file_details['error']:
      return False

    # Open file reading and writing handles
    try:
      fh_read = open(file_details["full_path"], "rb")
      fh_write = open(file_details["locked_path"], "wb")
    except IOError:
      return False

    # Read blocks and encrypt
    while True:
      block = fh_read.read(self.BLOCK_SIZE_BYTES)

      # Check block is valid
      if not block:
        break

      # Attempt padding
      to_encrypt = self.pad(block)


      iv = Random.new().read(AES.block_size)
      cipher = AES.new(bytes(self.key, encoding="utf-8"), AES.MODE_CBC, iv)
      try:
        # Create ciphertext. Length is now 4096 + 32 (block + iv + padding)
        ciphertext = (iv + cipher.encrypt(to_encrypt))
      except MemoryError:
        return False

      # Write encrypted block
      fh_write.write(ciphertext)

    # Close file handles
    fh_write.close()
    fh_read.close()

    # Update state
    file_details['state'] = "encrypted"
    return file_details['locked_path']


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

