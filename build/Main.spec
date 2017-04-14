# -*- mode: python -*-

block_cipher = pyi_crypto.PyiBlockCipher(key='0123456789ABCDEF')


a = Analysis(['..\\Crypter\\Main.py'],
             pathex=['.\\build'],
             binaries=[],
             datas=[("images/crypter.bmp", "."),
		    ("images/crypter_logo_small.bmp", "."),
		    ("images/encrypt_message.bmp", "."),
		    ("images/key_destruction.bmp", "."),
		    ("images/wallet_address.bmp", "."),
		    ("images/decrypt_message.bmp", ".")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Main',
          debug=False,
          strip=False,
          upx=True,
          console=False , uac_admin=True, icon='pdf.ico')
