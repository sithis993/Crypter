# Crypter

Welcome to Crypter! a ransomware piece written entirely in Python and compiled to a Windows executable using [PyInstaller](http://www.pyinstaller.org/). This README will provide you with all of the information necessary to understand, build and use this software.

**Please note that by making use of this repository you accept and agree with the disclaimer section of this README.**


 ![Crypter GUI](sample_images/crypter_gui.PNG)
 
 
 ## Disclaimer - IMPORTANT
Crypter is intended for educational and research purposes only. This software should not be used within any system or network for which you do not have permission, nor should it be used for any illegal or illicit purposes. The author takes no responsibility for any damages that may be caused by the software in this repository. 

Once compiled, Crypter WILL encrypt the files on the computer on which it is executed. Whilst this repository provides you with access to the source code of Crypter (enabling you to decrypt any encrypted files), bugs and other issues could, in theory, interrupt or prevent a successful decryption. 

Consequently, a permanent and irreversible loss of data could occur. To avoid any potential damage, you should only run Crypter on a test machine created for this purpose.

Once again, **the author accepts no responsibility for any damages that may occur, and by downloading this software you accept and agree to this disclaimer.**

## Roadmap
Crypter is an ongoing project with a number of updates, changes and improvements planned for the future. Updates actively under development include:

+ A Graphical User Interface for building Crypter. This will provide a significantly faster and more convenient method to customise the build and allow you to specify options such as the wallet address, ransom fee etc. (See issue [#6](/../../issues/6))

Updates not yet started, but planned for a future release include:

+ Integration within a Python-based Botnet. This will allow Crypter to be rapidly deployed to all infected machines. The Botnet is actively being developed.

Everyone is welcome to contribute ideas, improvements and fixes!

## Repository Structure
If you're unsure of the components that make up this repository, the following explanation should give you some insight:
```
Crypter
| -- Crypter (The actual ransomware code)
| -- build (The build code and configuration used to produce the PyInstaller binary)
| -- gui (The GUI project files. These can be viewed and edited using wxFormBuilder
| -- sample_images (Simply contains sample images used in this README)
```

## Prerequisites
Before cloning the repository and attempting to build Crypter, you must first meet the following prerequisites. You'll then have all the tools required to produce the binary.

**Note:** You should install the software in the exact order shown in the table below, from top to bottom.

| Requirement | Supported Version (Tested) | Supported Version (Not tested) | Recommended Version |
| ----------- | ------------------ | ---------------------- | ----------- |
| Microsoft Windows | 7, 10 | 7, 8, 10, server 2K8 and above | 10 |
| Python | 2.7.13 (x86) | -- | [2.7.13 (x86)](https://www.python.org/downloads/release/python-2713/) |
| Pyinstaller | 3.1.1, 3.2.1 |  3.2 | [3.1.1](https://github.com/pyinstaller/pyinstaller/releases/tag/v3.1.1) |
| Microsoft VC++ for Python | 9.0 | -- | [9.0](https://www.microsoft.com/en-gb/download/details.aspx?id=44266) |
| PyCrypto | 2.6.1 | -- | 2.6.1 (install via Pip) |
| WxPython | 3.0 | -- | [3.0](https://wxpython.org/download.php#msw) |
| \*UPX | 3.94w | -- | [3.94w](https://github.com/upx/upx/releases/tag/v3.94) |

\*The [UPX Packer](https://upx.github.io/) is an optional, but highly recommended tool that you can also install for the purpose of building Crypter. UPX will allow you to significantly reduce the size of the binary that PyInstaller produces. For example, in some cases UPX can reduce a PyInstaller binary from 8MB to 5MB. The build process will run successfully without UPX, but if you'd like to take advantage of its functionality, simply place the UPX directory at build/upx394.

Finally, once the above software is installed you can build the Crypter binary. This is a very simple process which is detailed in the next section of this README.

## How can I build Crypter?
Providing you've met the above prerequisites, building Crypter is straightforward:

- Run the *Build.py* script in the *build* directory of this repository.
- Check the *bin* directory (created during the build) in the root of the repository for the produced binary.

A more detailed guide on building Crypter will be added to the repository's Wiki in the future.

## How does Crypter work?
Crypter's approach is fairly conventional, but the lack of a CnC component does result in different behaviour. Rather than sending the key to a remote server, Crypter instead writes it to a local file so that the files can be easily decrypted. Once executed, the following steps are taken:

1. Generates an AES-256 bit key and writes it to key.txt in the current directory
    - You can use this key in the Crypter GUI to decrypt your files
2. Searches the following directories for files with the extensions defined in Base.py:
    - [USER_HOME_DIR]\Desktop
    - [USER_HOME_DIR]\Documents
    - [USER_HOME_DIR]\Downloads
    - [USER_HOME_DIR]\Music
    - [USER_HOME_DIR]\Pictures
    - [USER_HOME_DIR]\Videos    
3. Encrypts all matching files
4. Opens the Crypter GUI and displays the ransom note

A more in-depth breakdown of these activities will be added to the repository's Wiki in the future.

## Why was Crypter created?
Given Crypter's malicious capabilities, as well as the disclaimer in this README, you may be wondering why Crypter was created. The primary goal of this project was to provide a proof-of-concept which demonstrated Python's capabilities as a language for malware development. Traditionally, compiled languages like C and C++ have been the chosen platforms of malware authors. Today however, a general advancement of platforms and tools has introduced attractive alternatives which extend these opportunities to other languages. 

As an incredibly popular, beginner-friendly language with an immense wealth of third party support, Python allows developers to quickly create powerful tools without the overhead of a lower-level language. These characteristics are likely responsible for the increase in Python-based malware pieces observed in recent years, and will also likely influence and impact future development trends in the area. Examples of such pieces include:

+ [PWOBot](http://researchcenter.paloaltonetworks.com/2016/04/unit42-python-based-pwobot-targets-european-organizations/)
+ [PyCL](https://www.bleepingcomputer.com/news/security/pycl-ransomware-delivered-via-rig-ek-in-distribution-test/)
+ [CryPy](http://www.zdnet.com/article/python-ransomware-encrypts-files-with-unique-keys-one-at-a-time/)
+ [HolyCrypt](https://www.bleepingcomputer.com/news/security/new-python-ransomware-called-holycrypt-discovered/)

Whilst similar projects do exist on GitHub, few are structured in the same way. Crypter aims to expand upon these by providing a *cryptolocker* style Python-based ransomware piece, which can be easily compiled to a standalone executable format.
