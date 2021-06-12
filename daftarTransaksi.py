import wx
from wx.core import Panel
import ProjectUAS
import database

class dlgInsertTransaksi(ProjectUAS.dialogTransaksi):
    def __init__(self, parent, ID =-1):
        ProjectUAS.dialogTransaksi.__init__(self, parent)
        self.parent = parent 
        self.ID = ID

    def btnSimpanTransaksiOnButtonClick( self, event ):
        if self.inputIDBuku.GetValue() == '' or self.m_datePicker6.GetValue() == '' or self.inputHarga.GetValue() == '' or self.inputJumlah.GetValue() == '' or self.inputTotalHarga.GetValue() == '':
            wx.MessageBox('Silahkan Isi Data yang Kosong', 'Information', wx.OK | wx.ICON_ERROR)
            return False
        else:
            wx.MessageBox('Data Berhasil Ditambahkan', 'Information', wx.OK | wx.ICON_INFORMATION)
            self.Destroy()
        print('simpan')
        while self.ID == -1:
            self.parent.insertDataTransaksi(self.inputIDBuku.GetValue(), self.m_datePicker6.GetValue(), 
			self.inputHarga.GetValue(), self.inputJumlah.GetValue(), self.inputTotalHarga.GetValue(),
			)
            break

    def isiDataTransaksi(self,IDBuku, Tanggal, Harga, JumlahBuku, Total):
        self.inputIDBuku.SetValue(IDBuku)
        self.m_datePicker6.SetValue(Tanggal)
        self.inputHarga.SetValue(Harga)
        self.inputJumlah.SetValue(JumlahBuku)
        self.inputTotalHarga.SetValue(Total)

class daftarTransaksi(ProjectUAS.frameTransaksi):
    def __init__(self, parent):
        ProjectUAS.frameTransaksi.__init__(self, parent)
        self.data4 = database.Transaksi()
        self.initData()
        self.AddButtonDelete()

    def AddButtonDelete(self):		
        jmlKolom = self.tabelTransaksi.GetNumberCols()
        self.tabelTransaksi.AppendCols(1)
        colDelete = jmlKolom
        
        self.tabelTransaksi.SetColLabelValue(colDelete, '')

        for row in range (self.tabelTransaksi.GetNumberRows()):
            self.tabelTransaksi.SetCellValue(row,colDelete,'Delete')
            self.tabelTransaksi.SetCellBackgroundColour(row,colDelete,wx.RED)
            self.tabelTransaksi.SetCellTextColour(row,colDelete,wx.WHITE)
            self.tabelTransaksi.SetCellAlignment(row, colDelete, wx.ALIGN_CENTER_HORIZONTAL, wx.ALIGN_CENTER_VERTICAL)

    def initData(self):			
        n_cols = self.tabelTransaksi.GetNumberCols()
        n_rows = self.tabelTransaksi.GetNumberRows()
        if n_cols > 0:
            self.tabelTransaksi.DeleteCols(0, n_cols, True)        
        if n_rows > 0:
            self.tabelTransaksi.DeleteRows(0, n_rows, True)   

            # t2.nama, t2.email, t1.nim, t1.tahun_masuk
        koloms = ['IDBuku', 'Tanggal', 'Harga', 'JumlahBuku', 'Total']
        self.tabelTransaksi.AppendCols(len(koloms))

        daftar = self.data4.getDataTransaksi()
        baris = 0
            # lstData = []
        self.lstIdTransaksi = []
        for col in range(len(koloms)):
            self.tabelTransaksi.SetColLabelValue(col, koloms[col]) # mengubah nama kolom
        for transaksi_row in daftar:
            self.tabelTransaksi.AppendRows(1)

            print(baris,'. ', transaksi_row)
            ID, IDBuku, Tanggal, Harga, JumlahBuku, Total = transaksi_row
            # self.tabelTransaksi.SetCellValue(baris, 0, IDTransaksi )
            self.tabelTransaksi.SetCellValue(baris, 0, IDBuku )
            self.tabelTransaksi.SetCellValue(baris, 1, Tanggal)
            self.tabelTransaksi.SetCellValue(baris, 2, Harga )
            self.tabelTransaksi.SetCellValue(baris, 3, JumlahBuku)
            self.tabelTransaksi.SetCellValue(baris, 4, Total )

            self.lstIdTransaksi.append(ID)	
            baris += 1

    def btnTambahTransaksiOnButtonClick(self,event):
        dlg = dlgInsertTransaksi(self)
        dlg.ShowModal()

    def tabelTransaksiOnGridCmdSelectCell( self, event ):
        baris = event.GetRow()
        kolom = event.GetCol()

        print('baris: ', baris)
        print('kolom: ', kolom)

        while kolom == 5:
            dlg = wx.MessageDialog(self,'Apakah anda yakin akan menghapus data?', 'Informasi', style=wx.YES_NO )
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.data4.deleteTransaksi(self.lstIdTransaksi[baris])
                self.initData()
                self.AddButtonDelete()
            break

    def btnBackOnButtonClick(self, event):
        self.Destroy() 
        
    def insertDataTransaksi( self, IDBuku, Tanggal, Harga, JumlahBuku, Total ):
        self.data4.setDataTransaksi(IDBuku, Tanggal, Harga, JumlahBuku, Total)
        self.initData()
        self.AddButtonDelete()


