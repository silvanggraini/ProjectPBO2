import wx
import ProjectUAS

class kasir(ProjectUAS.frameKasir):
    def __init__(self, parent):
        ProjectUAS.frameKasir.__init__(self, parent)
        # self.SetSize(parent.GetSize())

    def btnSimpanOnButtonClick( self, event ):
        idbuku = int(self.inputIdBuku.GetValue())
        tgltransaksi = self.tanggalTransaksi.GetValue()
        hrgbuku = int(self.inputHargaBuku.GetValue())
        jmlbuku = int(self.inputJumlahBuku.GetValue())

        totalHarga = hrgbuku * jmlbuku
        self.inputTotalPembayaran.SetValue(str(totalHarga))

    def btnKembalianOnButtonClick( self, event ):
        totalHarga = int(self.inputTotalPembayaran.GetValue())
        cash = int(self.inputCash.GetValue())
        cashback = cash - totalHarga
        self.inputKembalian.SetValue(str(cashback))

    def btnBackOnButtonClick( self, event ):
        self.Destroy()

