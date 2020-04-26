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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Crypter", pos = wx.DefaultPosition, size = wx.Size( 940,800 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.Colour( 177, 7, 14 ) )

		MainSizer = wx.BoxSizer( wx.VERTICAL )

		self.HeaderPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		HeaderSizer = wx.BoxSizer( wx.VERTICAL )

		self.TitleLabel = wx.StaticText( self.HeaderPanel, wx.ID_ANY, u"CRYPTER", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TitleLabel.Wrap( -1 )

		self.TitleLabel.SetFont( wx.Font( 48, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True, "Courier New" ) )
		self.TitleLabel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

		HeaderSizer.Add( self.TitleLabel, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )

		self.FlashingMessageText = wx.StaticText( self.HeaderPanel, wx.ID_ANY, u"YOUR FILES HAVE BEEN ENCRYPTED!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FlashingMessageText.Wrap( -1 )

		self.FlashingMessageText.SetFont( wx.Font( 18, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier New" ) )
		self.FlashingMessageText.SetForegroundColour( wx.Colour( 255, 255, 0 ) )

		HeaderSizer.Add( self.FlashingMessageText, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.HeaderPanel.SetSizer( HeaderSizer )
		self.HeaderPanel.Layout()
		HeaderSizer.Fit( self.HeaderPanel )
		MainSizer.Add( self.HeaderPanel, 1, wx.ALL|wx.EXPAND, 5 )

		self.BodyPanel = wx.Panel( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.TAB_TRAVERSAL )
		BodySizer = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel81 = wx.Panel( self.BodyPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer192 = wx.BoxSizer( wx.VERTICAL )

		self.LockBitmap = wx.StaticBitmap( self.m_panel81, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer192.Add( self.LockBitmap, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 7 )


		self.m_panel81.SetSizer( bSizer192 )
		self.m_panel81.Layout()
		bSizer192.Fit( self.m_panel81 )
		bSizer20.Add( self.m_panel81, 0, wx.EXPAND |wx.ALL, 0 )

		self.m_panel8 = wx.Panel( self.BodyPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.BORDER_RAISED )
		bSizer191 = wx.BoxSizer( wx.VERTICAL )

		self.TimeRemainingLabel = wx.StaticText( self.m_panel8, wx.ID_ANY, u"TIME REMAINING", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TimeRemainingLabel.Wrap( -1 )

		self.TimeRemainingLabel.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier New" ) )
		self.TimeRemainingLabel.SetForegroundColour( wx.Colour( 255, 255, 0 ) )

		bSizer191.Add( self.TimeRemainingLabel, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )

		self.TimeRemainingTime = wx.StaticText( self.m_panel8, wx.ID_ANY, u"00:00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TimeRemainingTime.Wrap( -1 )

		self.TimeRemainingTime.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier New" ) )
		self.TimeRemainingTime.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer191.Add( self.TimeRemainingTime, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel8.SetSizer( bSizer191 )
		self.m_panel8.Layout()
		bSizer191.Fit( self.m_panel8 )
		bSizer20.Add( self.m_panel8, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer17.Add( bSizer20, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.RansomMessageText = wx.TextCtrl( self.BodyPanel, wx.ID_ANY, u"The important files on your computer have been encrypted with military grade AES-256 bit encryption.\n\nYour documents, videos, images and other forms of data are now inaccessible, and cannot be unlocked without the decryption key. This key is currently being stored on a remote server.\n\nTo acquire this key, transfer the Bitcoin fee to the Bitcoin wallet address before the time runs out.\n\nIf you fail to take action within this time window, the decryption key will be destoyed and access to your files will be permanently lost.\n\nFor more information on what Bitcoin is, and to learn where you can buy Bitcoins, click the Bitcoin button directly below the timer.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.RansomMessageText.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier New" ) )

		bSizer18.Add( self.RansomMessageText, 3, wx.ALL|wx.EXPAND, 7 )


		bSizer17.Add( bSizer18, 1, wx.EXPAND, 5 )


		bSizer15.Add( bSizer17, 1, 0, 5 )


		BodySizer.Add( bSizer15, 1, wx.EXPAND, 5 )


		self.BodyPanel.SetSizer( BodySizer )
		self.BodyPanel.Layout()
		BodySizer.Fit( self.BodyPanel )
		MainSizer.Add( self.BodyPanel, 2, wx.ALL|wx.EXPAND, 20 )

		self.FooterPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel9 = wx.Panel( self.FooterPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.BitcoinButton = wx.BitmapButton( self.m_panel9, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		bSizer22.Add( self.BitcoinButton, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		self.m_panel9.SetSizer( bSizer22 )
		self.m_panel9.Layout()
		bSizer22.Fit( self.m_panel9 )
		bSizer181.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.FooterPanel, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_panel10 = wx.Panel( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer221 = wx.BoxSizer( wx.VERTICAL )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.WalletAddressLabel = wx.StaticText( self.m_panel10, wx.ID_ANY, u"WALLET ADDRESS:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WalletAddressLabel.Wrap( -1 )

		self.WalletAddressLabel.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier New" ) )
		self.WalletAddressLabel.SetForegroundColour( wx.Colour( 255, 255, 0 ) )

		bSizer13.Add( self.WalletAddressLabel, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.WalletAddressString = wx.StaticText( self.m_panel10, wx.ID_ANY, u"1BoatSLRHtKNngkdXEeobR76b53LETtpyT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WalletAddressString.Wrap( -1 )

		self.WalletAddressString.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier New" ) )
		self.WalletAddressString.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer13.Add( self.WalletAddressString, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer221.Add( bSizer13, 0, wx.EXPAND, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.BitcoinFeeLabel = wx.StaticText( self.m_panel10, wx.ID_ANY, u"BITCOIN FEE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BitcoinFeeLabel.Wrap( -1 )

		self.BitcoinFeeLabel.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier New" ) )
		self.BitcoinFeeLabel.SetForegroundColour( wx.Colour( 255, 255, 0 ) )

		bSizer14.Add( self.BitcoinFeeLabel, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.BitcoinFeeString = wx.StaticText( self.m_panel10, wx.ID_ANY, u"1.50", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BitcoinFeeString.Wrap( -1 )

		self.BitcoinFeeString.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier New" ) )
		self.BitcoinFeeString.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer14.Add( self.BitcoinFeeString, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer221.Add( bSizer14, 0, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer19.SetMinSize( wx.Size( -1,40 ) )

		bSizer19.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer19.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.ViewEncryptedFilesButton = wx.Button( self.m_panel10, wx.ID_ANY, u"View Encrypted Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.ViewEncryptedFilesButton, 1, wx.ALL|wx.EXPAND, 5 )

		self.EnterDecryptionKeyButton = wx.Button( self.m_panel10, wx.ID_ANY, u"Enter Decryption Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.EnterDecryptionKeyButton, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer221.Add( bSizer19, 2, wx.ALIGN_RIGHT|wx.EXPAND, 5 )


		self.m_panel10.SetSizer( bSizer221 )
		self.m_panel10.Layout()
		bSizer221.Fit( self.m_panel10 )
		sbSizer2.Add( self.m_panel10, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer181.Add( sbSizer2, 3, wx.EXPAND, 5 )


		self.FooterPanel.SetSizer( bSizer181 )
		self.FooterPanel.Layout()
		bSizer181.Fit( self.FooterPanel )
		MainSizer.Add( self.FooterPanel, 1, wx.ALL|wx.EXPAND, 20 )


		self.SetSizer( MainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class ViewEncryptedFilesDialog
###########################################################################

class ViewEncryptedFilesDialog ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Encrypted Files", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		BodySizer = wx.BoxSizer( wx.VERTICAL )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		TextCtrlSizer = wx.BoxSizer( wx.VERTICAL )

		self.EncryptedFilesTextCtrl = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
		TextCtrlSizer.Add( self.EncryptedFilesTextCtrl, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel4.SetSizer( TextCtrlSizer )
		self.m_panel4.Layout()
		TextCtrlSizer.Fit( self.m_panel4 )
		BodySizer.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( BodySizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class EnterDecryptionKeyDialog
###########################################################################

class EnterDecryptionKeyDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Decrypt Files", pos = wx.DefaultPosition, size = wx.Size( 500,200 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		MainSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel6, wx.ID_ANY, u"AES Decryption Key" ), wx.VERTICAL )


		MainSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		MainSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer13.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.DecryptionKeyTextCtrl = wx.TextCtrl( MainSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		self.DecryptionKeyTextCtrl.SetMaxLength( 32 )
		bSizer13.Add( self.DecryptionKeyTextCtrl, 0, wx.ALL, 5 )


		bSizer13.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		MainSizer.Add( bSizer13, 1, wx.EXPAND, 5 )


		MainSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		OkCancelSizer = wx.StdDialogButtonSizer()
		self.OkCancelSizerOK = wx.Button( MainSizer.GetStaticBox(), wx.ID_OK )
		OkCancelSizer.AddButton( self.OkCancelSizerOK )
		self.OkCancelSizerCancel = wx.Button( MainSizer.GetStaticBox(), wx.ID_CANCEL )
		OkCancelSizer.AddButton( self.OkCancelSizerCancel )
		OkCancelSizer.Realize();

		MainSizer.Add( OkCancelSizer, 1, wx.EXPAND, 5 )

		self.StatusText = wx.StaticText( MainSizer.GetStaticBox(), wx.ID_ANY, u"Waiting for input", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.StatusText.Wrap( -1 )

		MainSizer.Add( self.StatusText, 0, wx.ALL, 5 )

		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )

		self.DecryptionGauge = wx.Gauge( MainSizer.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.DecryptionGauge.SetValue( 0 )
		bSizer121.Add( self.DecryptionGauge, 0, wx.ALL, 5 )


		bSizer121.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.EncryptedFilesNumberLabel = wx.StaticText( MainSizer.GetStaticBox(), wx.ID_ANY, u"Encrypted Files: 0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptedFilesNumberLabel.Wrap( -1 )

		bSizer121.Add( self.EncryptedFilesNumberLabel, 0, wx.ALL, 5 )


		MainSizer.Add( bSizer121, 1, wx.EXPAND, 5 )


		self.m_panel6.SetSizer( MainSizer )
		self.m_panel6.Layout()
		MainSizer.Fit( self.m_panel6 )
		bSizer12.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


