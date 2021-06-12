import ProjectUAS
import wx
import sqlite
from home import home

class utama (ProjectUAS.Mainframe):
    def __init__(self, parent):
        ProjectUAS.Mainframe.__init__(self, parent)
        self.con = sqlite.connection

    def btnLoginOnButtonClick( self, event):
        Cursor = self.con.cursor()
        Cursor.execute("SELECT Username, Password FROM login")
        cek = Cursor.fetchall()
        username = self.inputUsername.GetValue()
        password = self.inputPassword.GetValue()
        for (Username, Password) in cek:
            if Username == username and Password == password:
                wx.MessageBox('Login Berhasil', 'Information', wx.OK | wx.ICON_INFORMATION)
                framehome = home(parent=None)
                framehome.Show()
                self.Destroy()
                return True
            else:
                wx.MessageBox('Login gagal', 'Mistake', wx.OK | wx.ICON_ERROR)
                return False

