# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Crypter Builder", pos = wx.DefaultPosition, size = wx.Size( 640,850 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1.SetMinSize( wx.Size( 640,850 ) ) 
		bSizer311 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel312 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer48 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer49 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.LoadConfigFileLabel = wx.StaticText( self.m_panel312, wx.ID_ANY, u"Load Config file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LoadConfigFileLabel.Wrap( -1 )
		self.LoadConfigFileLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		bSizer49.Add( self.LoadConfigFileLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.TOP, 5 )
		
		self.LoadFilePicker = wx.FilePickerCtrl( self.m_panel312, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		self.LoadFilePicker.SetToolTipString( u"Load an existing Builder configuration file." )
		
		bSizer49.Add( self.LoadFilePicker, 0, wx.ALL, 5 )
		
		
		bSizer48.Add( bSizer49, 0, wx.EXPAND, 5 )
		
		
		self.m_panel312.SetSizer( bSizer48 )
		self.m_panel312.Layout()
		bSizer48.Fit( self.m_panel312 )
		bSizer311.Add( self.m_panel312, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer311, 0, wx.EXPAND, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.ConfigScrollableWindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.ConfigScrollableWindow.SetScrollRate( 5, 5 )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.GuideScrollableWindow = wx.ScrolledWindow( self.ConfigScrollableWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.STATIC_BORDER|wx.VSCROLL )
		self.GuideScrollableWindow.SetScrollRate( 5, 5 )
		self.GuideScrollableWindow.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer44 = wx.BoxSizer( wx.VERTICAL )
		
		self.TitleLabel = wx.StaticText( self.GuideScrollableWindow, wx.ID_ANY, u"Crypter Builder", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.TitleLabel.Wrap( -1 )
		self.TitleLabel.SetFont( wx.Font( 22, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier" ) )
		self.TitleLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.TitleLabel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer44.Add( self.TitleLabel, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.SubtitleLabel = wx.StaticText( self.GuideScrollableWindow, wx.ID_ANY, u"Created by Sithis993", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.SubtitleLabel.Wrap( -1 )
		self.SubtitleLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier" ) )
		
		bSizer44.Add( self.SubtitleLabel, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.LogoBitmap = wx.StaticBitmap( self.GuideScrollableWindow, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.LogoBitmap, 0, wx.ALL|wx.EXPAND, 10 )
		
		self.QuickBuildTitleLabel = wx.StaticText( self.GuideScrollableWindow, wx.ID_ANY, u"Quick Build", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.QuickBuildTitleLabel.Wrap( 359 )
		self.QuickBuildTitleLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Courier" ) )
		
		bSizer44.Add( self.QuickBuildTitleLabel, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.QuickBuildDescriptionLabel = wx.StaticText( self.GuideScrollableWindow, wx.ID_ANY, u"To create the ransomware binary immediately, leave the fields below blank and click the BUILD button. This will produce the ransomware binary with the default settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.QuickBuildDescriptionLabel.Wrap( 359 )
		self.QuickBuildDescriptionLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier" ) )
		
		bSizer44.Add( self.QuickBuildDescriptionLabel, 0, wx.ALL|wx.EXPAND, 10 )
		
		self.CustomisingBuildTitleLabel = wx.StaticText( self.GuideScrollableWindow, wx.ID_ANY, u"Customising the ransomware", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CustomisingBuildTitleLabel.Wrap( 359 )
		self.CustomisingBuildTitleLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Courier" ) )
		
		bSizer44.Add( self.CustomisingBuildTitleLabel, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.CustomisingBuildDescriptionLabel = wx.StaticText( self.GuideScrollableWindow, wx.ID_ANY, u"The ransomware can be easily customised by adjusting any or all of the options below. For more information on each field, including a description and the expected input, hover the mouse cursor over the field's label or input box to view its tooltip. \nFields left blank will be set to the default configuration.\n\nTo see an example configuration, click the browse button at the top of the app and load the \"config_example.cfg\" file.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CustomisingBuildDescriptionLabel.Wrap( 340 )
		self.CustomisingBuildDescriptionLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier" ) )
		
		bSizer44.Add( self.CustomisingBuildDescriptionLabel, 0, wx.ALL, 10 )
		
		self.ManagingConfigurationsTitleLabel = wx.StaticText( self.GuideScrollableWindow, wx.ID_ANY, u"Managing Configurations", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ManagingConfigurationsTitleLabel.Wrap( 359 )
		self.ManagingConfigurationsTitleLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Courier" ) )
		
		bSizer44.Add( self.ManagingConfigurationsTitleLabel, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.ManagingConfigurationsDescriptionLabel = wx.StaticText( self.GuideScrollableWindow, wx.ID_ANY, u"Optionally, if you'd like to save your ransomware configuration click the Save button at the bottom of this form. Existing configurations can be loaded by clicking the Load button at the top of the interface.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ManagingConfigurationsDescriptionLabel.Wrap( 340 )
		self.ManagingConfigurationsDescriptionLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier" ) )
		
		bSizer44.Add( self.ManagingConfigurationsDescriptionLabel, 0, wx.ALL, 10 )
		
		
		self.GuideScrollableWindow.SetSizer( bSizer44 )
		self.GuideScrollableWindow.Layout()
		bSizer44.Fit( self.GuideScrollableWindow )
		bSizer2.Add( self.GuideScrollableWindow, 6, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline6 = wx.StaticLine( self.ConfigScrollableWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel31 = wx.Panel( self.ConfigScrollableWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		LanguageSettingsSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel31, wx.ID_ANY, u"Language" ), wx.HORIZONTAL )
		
		bSizer202 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.BuilderLanguageLabel = wx.StaticText( LanguageSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Builder Language", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BuilderLanguageLabel.Wrap( -1 )
		self.BuilderLanguageLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.BuilderLanguageLabel.SetToolTipString( u"The language of this GUI. Defaults to English." )
		
		bSizer202.Add( self.BuilderLanguageLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer202.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		BuilderLanguageChoiceChoices = [ u"English" ]
		self.BuilderLanguageChoice = wx.Choice( LanguageSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, BuilderLanguageChoiceChoices, 0 )
		self.BuilderLanguageChoice.SetSelection( 0 )
		self.BuilderLanguageChoice.SetToolTipString( u"The language of this GUI. Defaults to English." )
		
		bSizer202.Add( self.BuilderLanguageChoice, 0, wx.ALL, 5 )
		
		
		LanguageSettingsSizer.Add( bSizer202, 1, 0, 5 )
		
		
		self.m_panel31.SetSizer( LanguageSettingsSizer )
		self.m_panel31.Layout()
		LanguageSettingsSizer.Fit( self.m_panel31 )
		bSizer31.Add( self.m_panel31, 1, wx.ALL, 5 )
		
		self.m_panel311 = wx.Panel( self.ConfigScrollableWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		DebugSettingsSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel311, wx.ID_ANY, u"Debug" ), wx.HORIZONTAL )
		
		bSizer2021 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.DebugLevelLabel = wx.StaticText( DebugSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Debug Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DebugLevelLabel.Wrap( -1 )
		self.DebugLevelLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.DebugLevelLabel.SetToolTipString( u"The debug level of the build process. Select a higher level to increase the verbosity of the build output shown in the console box below.\n\nDefaults to 1 which provides a small amount of debug information." )
		
		bSizer2021.Add( self.DebugLevelLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer2021.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		DebugLevelChoiceChoices = [ u"0 - Minimal", u"1 - Low", u"2 - Medium", u"3 - High" ]
		self.DebugLevelChoice = wx.Choice( DebugSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, DebugLevelChoiceChoices, 0 )
		self.DebugLevelChoice.SetSelection( 1 )
		self.DebugLevelChoice.SetToolTipString( u"The debug level of the build process. Select a higher level to increase the verbosity of the build output shown in the console box below.\n\nDefaults to 1 which provides a small amount of debug information." )
		
		bSizer2021.Add( self.DebugLevelChoice, 0, wx.ALL, 5 )
		
		
		DebugSettingsSizer.Add( bSizer2021, 1, 0, 5 )
		
		
		self.m_panel311.SetSizer( DebugSettingsSizer )
		self.m_panel311.Layout()
		DebugSettingsSizer.Fit( self.m_panel311 )
		bSizer31.Add( self.m_panel311, 1, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer31, 0, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel41 = wx.Panel( self.ConfigScrollableWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel41.SetToolTipString( u"The path to the UPX Packer directory. If left blank, UPX will not be utilised and the executable will not be packed.\n\nIt is recommended that UPX is used as this can reduce the Crypter executable size by several Megabytes." )
		
		BinarySettingsSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel41, wx.ID_ANY, u"Binary Settings" ), wx.VERTICAL )
		
		bSizer391 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer41111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer20321211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.PyinstallerAesKeyLabel = wx.StaticText( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, u"Pyinstaller AES Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PyinstallerAesKeyLabel.Wrap( -1 )
		self.PyinstallerAesKeyLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.PyinstallerAesKeyLabel.SetToolTipString( u"The AES key used by Pyinstaller to encrypt the ransomware script files. This field is optional, but provides Crypter with a layer of obfuscation by making it more difficult to reverse engineer. Leave this field blank if you don't want to use this functionality." )
		
		bSizer20321211.Add( self.PyinstallerAesKeyLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer20321211.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.PyInstallerAesKeyTextCtrl = wx.TextCtrl( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PyInstallerAesKeyTextCtrl.SetToolTipString( u"The AES key used by Pyinstaller to encrypt the ransomware script files. This field is optional, but provides Crypter with a layer of obfuscation by making it more difficult to reverse engineer. Leave this field blank if you don't want to use this functionality." )
		
		bSizer20321211.Add( self.PyInstallerAesKeyTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer41111.Add( bSizer20321211, 1, wx.EXPAND, 5 )
		
		bSizer203211111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.IconLabel = wx.StaticText( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, u"File Icon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.IconLabel.Wrap( -1 )
		self.IconLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.IconLabel.SetToolTipString( u"The icon (.ico) file to use for the Crypter executable. If left blank PyInstaller will use its own icon." )
		
		bSizer203211111.Add( self.IconLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer203211111.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.IconFilePicker = wx.FilePickerCtrl( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.ico", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_SMALL )
		self.IconFilePicker.SetToolTipString( u"The icon (.ico) file to use for the Crypter executable. If left blank PyInstaller will use its own icon." )
		
		bSizer203211111.Add( self.IconFilePicker, 0, wx.ALL, 5 )
		
		
		bSizer41111.Add( bSizer203211111, 1, wx.EXPAND, 5 )
		
		
		bSizer391.Add( bSizer41111, 1, wx.EXPAND, 5 )
		
		bSizer411111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2032111111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.UpxDirLabel = wx.StaticText( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, u"UPX Packer Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.UpxDirLabel.Wrap( -1 )
		self.UpxDirLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.UpxDirLabel.SetToolTipString( u"The path to the UPX Packer directory. If left blank, UPX will not be utilised and the executable will not be packed.\n\nIt is recommended that UPX is used as this can reduce the Crypter executable size by several Megabytes." )
		
		bSizer2032111111.Add( self.UpxDirLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer2032111111.AddSpacer( ( 0, 0), 1, wx.ALIGN_LEFT|wx.EXPAND, 5 )
		
		self.UpxDirPicker = wx.DirPickerCtrl( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select UPX Directory", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		self.UpxDirPicker.SetToolTipString( u"The path to the UPX Packer directory. If left blank, UPX will not be utilised and the executable will not be packed.\n\nIt is recommended that UPX is used as this can reduce the Crypter executable size by several Megabytes." )
		
		bSizer2032111111.Add( self.UpxDirPicker, 0, wx.ALL, 5 )
		
		
		bSizer411111.Add( bSizer2032111111, 1, wx.EXPAND, 5 )
		
		bSizer2032111112 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer2032111112.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer411111.Add( bSizer2032111112, 1, wx.EXPAND, 5 )
		
		
		bSizer391.Add( bSizer411111, 1, wx.EXPAND, 5 )
		
		
		BinarySettingsSizer.Add( bSizer391, 0, wx.EXPAND, 5 )
		
		
		self.m_panel41.SetSizer( BinarySettingsSizer )
		self.m_panel41.Layout()
		BinarySettingsSizer.Fit( self.m_panel41 )
		bSizer12.Add( self.m_panel41, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel4 = wx.Panel( self.ConfigScrollableWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		RansomwareSettingsSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Ransomware Settings" ), wx.VERTICAL )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer412 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer203213 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.EncryptAttachedDrivesCheckbox = wx.CheckBox( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Encrypt Attached Drives", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptAttachedDrivesCheckbox.SetToolTipString( u"If ticked, all drives attached to the machine will be encrypted. This includes mapped network drives, as well as external and internal hard disks, but excludes C:." )
		
		bSizer203213.Add( self.EncryptAttachedDrivesCheckbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer412.Add( bSizer203213, 2, wx.EXPAND, 5 )
		
		
		bSizer412.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer2032131 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.EncryptUserHomeCheckbox = wx.CheckBox( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Encrypt User Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptUserHomeCheckbox.SetToolTipString( u"If ticked, all files and folders in the victim's home directory (such as Downloads, Documents and Pictures) will be encrypted." )
		
		bSizer2032131.Add( self.EncryptUserHomeCheckbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer412.Add( bSizer2032131, 2, wx.EXPAND, 5 )
		
		
		bSizer39.Add( bSizer412, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticline7 = wx.StaticLine( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer39.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer20321 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.EncryptedFileExtensionLabel = wx.StaticText( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Encrypted File Extension", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptedFileExtensionLabel.Wrap( -1 )
		self.EncryptedFileExtensionLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.EncryptedFileExtensionLabel.SetToolTipString( u"The file extension to use for encrypted files. If left blank, files encrypted by Crypter will be given a .locked extension" )
		
		bSizer20321.Add( self.EncryptedFileExtensionLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer20321.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.EncryptedFileExtensionTextCtrl = wx.TextCtrl( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptedFileExtensionTextCtrl.SetToolTipString( u"The file extension to use for encrypted files. If left blank, files encrypted by Crypter will be given a .locked extension" )
		
		bSizer20321.Add( self.EncryptedFileExtensionTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer20321, 1, wx.EXPAND, 5 )
		
		bSizer203211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.WalletAddressLabel = wx.StaticText( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Wallet Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WalletAddressLabel.Wrap( -1 )
		self.WalletAddressLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.WalletAddressLabel.SetToolTipString( u"The Bitcoin wallet address that the victim should pay the ransom to. This will be displayed in the Crypter GUI. Defaults to the bitcoin wallet of Crypter's author ;-)" )
		
		bSizer203211.Add( self.WalletAddressLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer203211.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.WalletAddressTextCtrl = wx.TextCtrl( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WalletAddressTextCtrl.SetToolTipString( u"The Bitcoin wallet address that the victim should pay the ransom to. This will be displayed in the Crypter GUI. Defaults to the bitcoin wallet of Crypter's author ;-)" )
		
		bSizer203211.Add( self.WalletAddressTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer203211, 1, wx.EXPAND, 5 )
		
		
		bSizer39.Add( bSizer41, 1, wx.EXPAND, 5 )
		
		bSizer411 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer203212 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.BitcoinFeeLabel = wx.StaticText( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Bitcoin Fee", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BitcoinFeeLabel.Wrap( -1 )
		self.BitcoinFeeLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.BitcoinFeeLabel.SetToolTipString( u"The Bitcoin Fee that you want to victim to pay. This amount will be shown in the GUI. Defaults to 1.0" )
		
		bSizer203212.Add( self.BitcoinFeeLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer203212.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.BitcoinFeeTextCtrl = wx.TextCtrl( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BitcoinFeeTextCtrl.SetToolTipString( u"The Bitcoin Fee that you want to victim to pay. This amount will be shown in the GUI. Defaults to 1.0" )
		
		bSizer203212.Add( self.BitcoinFeeTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer411.Add( bSizer203212, 1, wx.EXPAND, 5 )
		
		bSizer2032111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.KeyDestructionTimeLabel = wx.StaticText( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Key Destruction Time (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KeyDestructionTimeLabel.Wrap( -1 )
		self.KeyDestructionTimeLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.KeyDestructionTimeLabel.SetToolTipString( u"The time in seconds before the victim's decryption key is destroyed. Once the timer runs out, the victim will no longer be able to decrypt their files. Defaults to 259200 (72 hours)." )
		
		bSizer2032111.Add( self.KeyDestructionTimeLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer2032111.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.KeyDestructionTimeTextCtrl = wx.TextCtrl( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KeyDestructionTimeTextCtrl.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.KeyDestructionTimeTextCtrl.SetToolTipString( u"The time in seconds before the victim's decryption key is destroyed. Once the timer runs out, the victim will no longer be able to decrypt their files. Defaults to 259200 (72 hours)." )
		
		bSizer2032111.Add( self.KeyDestructionTimeTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer411.Add( bSizer2032111, 1, wx.EXPAND, 5 )
		
		
		bSizer39.Add( bSizer411, 1, wx.EXPAND, 5 )
		
		bSizer4111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2032121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.MaxFileSizeLabel = wx.StaticText( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Max File Size to Encrypt (MB)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MaxFileSizeLabel.Wrap( -1 )
		self.MaxFileSizeLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.MaxFileSizeLabel.SetToolTipString( u"The maximum size, in Megabytes, of a file that Crypter should encrypt. Any file that exceeds this limit will not be encrypted. Defaults to 512." )
		
		bSizer2032121.Add( self.MaxFileSizeLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer2032121.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.MaxFileSizeTextCtrl = wx.TextCtrl( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MaxFileSizeTextCtrl.SetToolTipString( u"The maximum size, in Megabytes, of a file that Crypter should encrypt. Any file that exceeds this limit will not be encrypted. Defaults to 512." )
		
		bSizer2032121.Add( self.MaxFileSizeTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer4111.Add( bSizer2032121, 1, wx.EXPAND, 5 )
		
		bSizer20321111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.FiletypesToEncryptLabel = wx.StaticText( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Filetypes to Encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FiletypesToEncryptLabel.Wrap( -1 )
		self.FiletypesToEncryptLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.FiletypesToEncryptLabel.SetToolTipString( u"A comma separated list of filetypes to encrypt. Files with these extensions will be encrypted. Leave this field blank to use the default set of common filetypes." )
		
		bSizer20321111.Add( self.FiletypesToEncryptLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer20321111.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.FiletypesToEncryptTextCtrl = wx.TextCtrl( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FiletypesToEncryptTextCtrl.SetToolTipString( u"A comma separated list of filetypes to encrypt. Files with these extensions will be encrypted. Leave this field blank to use the default set of common filetypes." )
		
		bSizer20321111.Add( self.FiletypesToEncryptTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer4111.Add( bSizer20321111, 1, wx.EXPAND, 5 )
		
		
		bSizer39.Add( bSizer4111, 1, wx.EXPAND, 5 )
		
		RansomMessageSizer = wx.StaticBoxSizer( wx.StaticBox( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Ransom Message" ), wx.VERTICAL )
		
		self.RansomMessageTextCtrl = wx.TextCtrl( RansomMessageSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.RansomMessageTextCtrl.SetToolTipString( u"The ransom message to display in the Crypter GUI. Leave this text box blank to use the default ransom message." )
		
		RansomMessageSizer.Add( self.RansomMessageTextCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer39.Add( RansomMessageSizer, 4, wx.EXPAND, 5 )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer39.Add( bSizer40, 1, wx.EXPAND, 5 )
		
		self.m_staticline61 = wx.StaticLine( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer39.Add( self.m_staticline61, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		RansomwareSettingsSizer.Add( bSizer39, 1, wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( RansomwareSettingsSizer )
		self.m_panel4.Layout()
		RansomwareSettingsSizer.Fit( self.m_panel4 )
		bSizer12.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer12, 0, wx.EXPAND, 5 )
		
		bSizer50 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.SaveConfigurationLabel = wx.StaticText( self.ConfigScrollableWindow, wx.ID_ANY, u"Save configuration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SaveConfigurationLabel.Wrap( -1 )
		self.SaveConfigurationLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		bSizer50.Add( self.SaveConfigurationLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.SaveFilePicker = wx.FilePickerCtrl( self.ConfigScrollableWindow, wx.ID_ANY, wx.EmptyString, u"Save Configuration", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE )
		self.SaveFilePicker.SetToolTipString( u"Save your configuration to a builder configuration file." )
		
		bSizer50.Add( self.SaveFilePicker, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer50, 1, wx.EXPAND, 5 )
		
		
		self.ConfigScrollableWindow.SetSizer( bSizer2 )
		self.ConfigScrollableWindow.Layout()
		bSizer2.Fit( self.ConfigScrollableWindow )
		bSizer1.Add( self.ConfigScrollableWindow, 8, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4112 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4112.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer172 = wx.BoxSizer( wx.VERTICAL )
		
		self.BuildProgressGauge = wx.Gauge( self.m_panel4112, wx.ID_ANY, 99, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.BuildProgressGauge.SetValue( 0 ) 
		bSizer172.Add( self.BuildProgressGauge, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel4112.SetSizer( bSizer172 )
		self.m_panel4112.Layout()
		bSizer172.Fit( self.m_panel4112 )
		bSizer1.Add( self.m_panel4112, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline211 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline211, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel411 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel411.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		ConsoleBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel411, wx.ID_ANY, u"Console" ), wx.VERTICAL )
		
		self.ConsoleTextCtrl = wx.TextCtrl( ConsoleBoxSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		self.ConsoleTextCtrl.SetForegroundColour( wx.Colour( 24, 249, 0 ) )
		self.ConsoleTextCtrl.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		ConsoleBoxSizer.Add( self.ConsoleTextCtrl, 1, wx.ALL|wx.EXPAND, 4 )
		
		
		bSizer17.Add( ConsoleBoxSizer, 1, wx.EXPAND, 5 )
		
		
		self.m_panel411.SetSizer( bSizer17 )
		self.m_panel411.Layout()
		bSizer17.Fit( self.m_panel411 )
		bSizer1.Add( self.m_panel411, 4, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4111 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.DOUBLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel4111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer171 = wx.BoxSizer( wx.VERTICAL )
		
		self.BuildButton = wx.Button( self.m_panel4111, wx.ID_ANY, u"BUILD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BuildButton.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer171.Add( self.BuildButton, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel4111.SetSizer( bSizer171 )
		self.m_panel4111.Layout()
		bSizer171.Fit( self.m_panel4111 )
		bSizer1.Add( self.m_panel4111, 1, wx.ALL|wx.EXPAND, 10 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.StatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class EncryptFiletypesDialog
###########################################################################

class EncryptFiletypesDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Encryptable Filetypes", pos = wx.DefaultPosition, size = wx.Size( 400,500 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer30.SetMinSize( wx.Size( 400,500 ) ) 
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Select the filetypes to encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Arial" ) )
		
		bSizer30.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 20 )
		
		self.SelectAllCheckbox = wx.CheckBox( self, wx.ID_ANY, u"Select All", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SelectAllCheckbox.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		bSizer30.Add( self.SelectAllCheckbox, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		FiletypesSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		DocumentFilesSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Document Files" ), wx.VERTICAL )
		
		bSizer54 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer332 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox52 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"DOCX", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer332.Add( self.m_checkBox52, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox42 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"DOC", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer332.Add( self.m_checkBox42, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox32 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer332.Add( self.m_checkBox32, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox22 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer332.Add( self.m_checkBox22, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer54.Add( bSizer332, 1, wx.EXPAND, 5 )
		
		bSizer331 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox51 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer331.Add( self.m_checkBox51, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox41 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer331.Add( self.m_checkBox41, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox31 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer331.Add( self.m_checkBox31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox21 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer331.Add( self.m_checkBox21, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer54.Add( bSizer331, 1, wx.EXPAND, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox5 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_checkBox5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox4 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_checkBox4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox3 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_checkBox3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_checkBox2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer54.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		
		DocumentFilesSizer.Add( bSizer54, 1, wx.EXPAND, 5 )
		
		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer57.AddSpacer( ( 0, 0), 2, wx.EXPAND, 5 )
		
		self.m_checkBox50 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Select All", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox50.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
		
		bSizer57.Add( self.m_checkBox50, 0, wx.ALL, 10 )
		
		
		DocumentFilesSizer.Add( bSizer57, 0, 0, 5 )
		
		
		bSizer32.Add( DocumentFilesSizer, 1, wx.EXPAND, 5 )
		
		ImageFileszSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Image Files" ), wx.VERTICAL )
		
		
		bSizer32.Add( ImageFileszSizer, 1, wx.EXPAND, 5 )
		
		VideoFilesSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Video Files" ), wx.VERTICAL )
		
		
		bSizer32.Add( VideoFilesSizer, 1, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizer32 )
		self.m_scrolledWindow1.Layout()
		bSizer32.Fit( self.m_scrolledWindow1 )
		FiletypesSizer.Add( self.m_scrolledWindow1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer30.Add( FiletypesSizer, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer30 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

