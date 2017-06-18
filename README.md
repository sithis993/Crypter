# Crypter

Welcome to Crypter, a ransomware piece written entirely in Python and compiled to Windows executable format using [PyInstaller](http://www.pyinstaller.org/). This README will provide you with all of the information necessary to understand, build and use this software.

**Please note that by making use of this repository you accept and agree with the disclaimer section of this README.**


 ![Crypter GUI](sample_images/crypter_gui.PNG)
 
 
 ## Disclaimer - IMPORTANT
Crypter is intended for educational and research purposes only. This software should not be used within any system or network for which you do not have permission, nor should it be used for any illegal or illicit purposes. The author takes no responsibility for any damages that may be caused by the software in this repository. 

Once compiled, Crypter WILL encrypt the files on the computer on which it is executed. Whilst this repository provides you with access to the source code of Crypter (enabling you to decrypt any encrypted files), bugs and other issues could, in theory, interrupt or prevent a successful decryption. 

Consequently, a permanent and irreversible loss of data could occur. To avoid any potential damage, you should only run Crypter on a test machine created for this purpose.

Once again, **the author accepts no responsibility for any damages that may occur, and by downloading this software you accept and agree to this disclaimer.**

## Roadmap
Crypter is an ongoing project with a number of updates, changes and improvements planned for the future. Updates actively under development include:

+ A Graphical User Interface for building Crypter. This will provide a significantly faster and more convenient method to customise the build and allow you to specify options such as the wallet address, ransom fee etc.

Updates not yet started, but planned for a future release include:

+ Integration within a Python-based Botnet. This will allow Crypter to be rapidly deployed to all infected machines. The Botnet is actively being developed.

## Prerequisites
Before cloning the repository and attempting to build Crypter, you must first meet the following prerequisities. You'll then have all of the tools required to produce the binary.

**Note:** You should install the software in the exact order shown in the table below, from top to bottom.

| Requirement | Supported (Tested) | Supported (Not tested) | Recommended |
| ----------- | ------------------ | ---------------------- | ----------- |
| Microsoft Windows | 7, 10 | 7, 8, 10, server 2K8 and above | 10 |
| Python | 2.7 | -- | 2.7 |
| Pyinstaller | 3.2.1, 3.2.2 | 3.2  | 3.2.1 |
| Microsoft VC++ for Python | 9.0 | -- | 9.0 |
| PyCrypto | 2.6.1 | -- | 2.6.1 |
| WxPython | 3.0 | -- | 3.0 |

Once the above software is installed, You can now build the Crypter binary. This is a very simple process which is detailed in the next section of this README.

## How can I build Crypter?
Instructions on building the executable

## How does Crypter work?
Brief overview of how Crypter ransomware works. 

## Why was Crypter created?
Given Crypter's malicious capabilities, as well as the disclaimer in this README, you may be wondering why Crypter was created. The primary goal of this project was to provide a proof-of-concept which demonstrated Python's capabilities as a language for malware development. Traditionally, compiled languages like C and C++ have been the chosen platforms of malware authors. Today however, a general advancement of platforms and tools has introduced attractive alternatives which extend these opportunities to other languages. 

As an incredibly popular, beginner-friendly language with an immense wealth of third party support, Python allows developers to quickly create powerful tools without the overhead of a lower-level language. These characteristics are likely responsible for the increase in Python-based malware pieces observed in recent years, and will also likely influence and impact future development trends in the area. Examples of such pieces include:

+ [PWOBot](http://researchcenter.paloaltonetworks.com/2016/04/unit42-python-based-pwobot-targets-european-organizations/)
+ [PyCL](https://www.bleepingcomputer.com/news/security/pycl-ransomware-delivered-via-rig-ek-in-distribution-test/)
+ [CryPy](http://www.zdnet.com/article/python-ransomware-encrypts-files-with-unique-keys-one-at-a-time/)
+ [HolyCrypt](https://www.bleepingcomputer.com/news/security/new-python-ransomware-called-holycrypt-discovered/)

Whilst similar projects do exist on GitHub, as of this writing few are actively supported, and none are a complete package. Crypter aims to build upon these by providing a *cryptolocker* style Python-based ransomware piece which can be easily compiled to a standalone executable format.
