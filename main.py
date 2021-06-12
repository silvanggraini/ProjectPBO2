import wx
from login import utama

class MainApp(wx.App):
    def OnInit(self):
        self.frame = utama(None)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MainApp()
    app.MainLoop()