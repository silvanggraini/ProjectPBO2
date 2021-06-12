import wx
import ProjectUAS
from kasir import kasir
from daftarmember import daftarMember
from daftarPeminjaman import daftarPeminjaman
from daftarpengembalian import daftarPengembalian
from daftarTransaksi import daftarTransaksi
from daftarBuku import daftarBuku

class home(ProjectUAS.frameHome):
    def __init__(self, parent):
        ProjectUAS.frameHome.__init__(self, parent)

    def btnDaftarBukuOnButtonClick( self, event ):
        framebuku = daftarBuku(parent=None)
        framebuku.Show()
        self.Destroy()
        
    def btnPeminjamanOnButtonClick( self, event ):
        framepeminjaman = daftarPeminjaman(parent=None)
        framepeminjaman.Show()
        self.Destroy()
        
    def btnPengembalianOnButtonClick( self, event ):
        framepengembalian = daftarPengembalian(parent=None)
        framepengembalian.Show()
        self.Destroy()
        
    def btnKasirOnButtonClick( self, event ):
        framekasir = kasir(parent=None)
        framekasir.Show()
        self.Destroy()

    def btnMemberOnButtonClick( self, event ):
        framemember = daftarMember(parent=None)
        framemember.Show()
        self.Destroy()

    def btnTransaksiOnButtonClick( self, event ):
        frametransaksi = daftarTransaksi(parent=None)
        frametransaksi.Show()
        self.Destroy()

# app=wx.App()
# Panel=home(None)
# Panel.Show()
# app.MainLoop()     