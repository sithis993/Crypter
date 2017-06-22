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

+ A Graphical User Interface for building Crypter. This will provide a significantly faster and more convenient method to customise the build and allow you to specify options such as the wallet address, ransom fee etc.

Updates not yet started, but planned for a future release include:

+ Integration within a Python-based Botnet. This will allow Crypter to be rapidly deployed to all infected machines. The Botnet is actively being developed.

Everyone is welcome to contribute ideas, improvements and fixes!

## Prerequisites
Before cloning the repository and attempting to build Crypter, you must first meet the following prerequisites. You'll then have all the tools required to produce the binary.

**Note:** You should install the software in the exact order shown in the table below, from top to bottom.

| Requirement | Supported Version (Tested) | Supported Version (Not tested) | Recommended Version |
| ----------- | ------------------ | ---------------------- | ----------- |
| Microsoft Windows | 7, 10 | 7, 8, 10, server 2K8 and above | 10 |
| Python | 2.7 | -- | 2.7 |
| Pyinstaller | 3.2.1, 3.2.2 | 3.2  | 3.2.1 |
| Microsoft VC++ for Python | 9.0 | -- | 9.0 |
| PyCrypto | 2.6.1 | -- | 2.6.1 |
| WxPython | 3.0 | -- | 3.0 |

The [UPX Packer](https://upx.github.io/) is an optional, but definitely recommended tool that you can also install for the purpose of building the binary. Whilst PyInstaller provides some great benefits, one inconvenience is that the produced file can sometimes be quite large. UPX will allow you to significantly reduce its size. For example, in some cases UPX can reduce a PyInstaller binary from 8MB to 5MB. The build process will run successfully without UPX, but if you'd like to take advantage of its functionality, simply place the UPX directory at build/upx394.

Finally, once the above software is installed you can build the Crypter binary. This is a very simple process which is detailed in the next section of this README.

## How can I build Crypter?
Providing you've met the above prerequisites, building Crypter is straightforward:

- Run the *Build.py* script in the *build* directory of this repository.
- Check the *bin* directory in the root of the repository for the produced binary.

A more detailed guide on building Crypter will be added to the repository's Wiki in the future.

## How does Crypter work?
Crypter's approach is fairly conventional. Once launched, it takes the following actions:

1. Checks to ensure that a version of Crypter is not already running
    - If a version is detected, a fake error is presented to the user stating that the file is corrupt
2. Checks if the machine has already been encrypted by an instance of Crypter
    - If already encrypted, the ransom GUI is presented to the user
    - Otherwise, continue with the encryption process
3. Generate the AES-256 bit encryption key and write it to key.txt
3. Search the target directories for files matching the types defined in Base.py
    - Currently, the main user directories (Documents, Pictures etc.) are the only locations searched
    - However, adding any additional directories is straightforward
4. Encrypt any matching files
5. Write the time of encryption to the registry (used for tracking remaining time to pay the ransom)
6. Presents the ransom GUI to the user

A more in-depth breakdown of these activities will be added to the repository's Wiki in the future.

## Why was Crypter created?
Given Crypter's malicious capabilities, as well as the disclaimer in this README, you may be wondering why Crypter was created. The primary goal of this project was to provide a proof-of-concept which demonstrated Python's capabilities as a language for malware development. Traditionally, compiled languages like C and C++ have been the chosen platforms of malware authors. Today however, a general advancement of platforms and tools has introduced attractive alternatives which extend these opportunities to other languages. 

As an incredibly popular, beginner-friendly language with an immense wealth of third party support, Python allows developers to quickly create powerful tools without the overhead of a lower-level language. These characteristics are likely responsible for the increase in Python-based malware pieces observed in recent years, and will also likely influence and impact future development trends in the area. Examples of such pieces include:

+ [PWOBot](http://researchcenter.paloaltonetworks.com/2016/04/unit42-python-based-pwobot-targets-european-organizations/)
+ [PyCL](https://www.bleepingcomputer.com/news/security/pycl-ransomware-delivered-via-rig-ek-in-distribution-test/)
+ [CryPy](http://www.zdnet.com/article/python-ransomware-encrypts-files-with-unique-keys-one-at-a-time/)
+ [HolyCrypt](https://www.bleepingcomputer.com/news/security/new-python-ransomware-called-holycrypt-discovered/)

Whilst similar projects do exist on GitHub, as of this writing few are actively supported, and none are a complete package. Crypter aims to build upon these by providing a *cryptolocker* style Python-based ransomware piece which can be easily compiled to a standalone executable format.
