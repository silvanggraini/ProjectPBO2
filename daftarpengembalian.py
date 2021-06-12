import wx
from wx.core import Panel
import ProjectUAS
import database

class dlgInsertPengembalian(ProjectUAS.dialogPengembalian):
    def __init__(self, parent, ID=-1):
        ProjectUAS.dialogPengembalian.__init__(self, parent)
        self.parent = parent 
        self.ID = ID

    def btnPengembalianOnButtonClick( self, event ):
        if self.tanggalPeminjaman.GetValue() == '' or self.inputNamaPeminjam.GetValue() == '' or self.inputIdMember.GetValue() == '' or self.inputJudulBuku.GetValue() == '' or self.tanggalPengembalian.GetValue() == '' or self.inputDenda.GetValue() == '':
            wx.MessageBox('Silahkan Isi Data yang Kosong', 'Information', wx.OK | wx.ICON_ERROR)
            return False
        else:
            wx.MessageBox('Data Berhasil Ditambahkan', 'Information', wx.OK | wx.ICON_INFORMATION)
            self.Destroy()
        print('simpan')
        while self.ID == -1:
            self.parent.insertDataPengembalian(self.tanggalPeminjaman.GetValue(), self.inputNamaPeminjam.GetValue(), 
			self.inputIdMember.GetValue(), self.inputJudulBuku.GetValue(), self.tanggalPengembalian.GetValue(),
            self.inputDenda.GetValue()
			)
            break

    def isiDataPengembalian(self,Tanggal, NamaPeminjam, IDMember, JudulBuku, TanggalPengembalian, Denda):
        self.tanggalPeminjaman.SetValue(Tanggal)
        self.inputNamaPeminjam.SetValue(NamaPeminjam)
        self.inputIdMember.SetValue(IDMember)
        self.inputJudulBuku.SetValue(JudulBuku)
        self.tanggalPengembalian.SetValue(TanggalPengembalian)
        self.inputDenda.SetValue(Denda)
        
class daftarPengembalian(ProjectUAS.framePengembalian):
    def __init__(self, parent):
        ProjectUAS.framePengembalian.__init__(self, parent)
        self.data1 = database.Pengembalian()
        self.initData()
        self.AddButtonDelete()

    def AddButtonDelete(self):		
        jmlKolom = self.m_grid42.GetNumberCols()
        self.m_grid42.AppendCols(1)
        colDelete = jmlKolom

        self.m_grid42.SetColLabelValue(colDelete, '')

        for row in range (self.m_grid42.GetNumberRows()):
            self.m_grid42.SetCellValue(row,colDelete,'Delete')
            self.m_grid42.SetCellBackgroundColour(row,colDelete,wx.RED)
            self.m_grid42.SetCellTextColour(row,colDelete,wx.WHITE)
            self.m_grid42.SetCellAlignment(row, colDelete, wx.ALIGN_CENTER_HORIZONTAL, wx.ALIGN_CENTER_VERTICAL)

    def initData(self):			
        n_cols = self.m_grid42.GetNumberCols()
        n_rows = self.m_grid42.GetNumberRows()
        if n_cols > 0:
            self.m_grid42.DeleteCols(0, n_cols, True)        
        if n_rows > 0:
            self.m_grid42.DeleteRows(0, n_rows, True)   

        koloms = ['Tanggal', 'Nama Peminjam', 'ID Member', 'Judul Buku', 'Tanggal Pengembalian', 'Denda']
        self.m_grid42.AppendCols(len(koloms))

        daftar = self.data1.getDaftarPengembalian()
        baris = 0

        self.lstIdPengembalian = []
        for col in range(len(koloms)):
            self.m_grid42.SetColLabelValue(col, koloms[col]) 
        for pengembalian_row in daftar:
            self.m_grid42.AppendRows(1)

            print(baris,'. ', pengembalian_row)
            ID, Tanggal, NamaPeminjam, IDMember, JudulBuku, Denda, TanggalPengembalian = pengembalian_row
            # self.m_grid42.SetCellValue(baris, 0, ID )
            self.m_grid42.SetCellValue(baris, 0, Tanggal )
            self.m_grid42.SetCellValue(baris, 1, NamaPeminjam)
            self.m_grid42.SetCellValue(baris, 2, IDMember )
            self.m_grid42.SetCellValue(baris, 3, JudulBuku)
            self.m_grid42.SetCellValue(baris, 4, Denda )
            self.m_grid42.SetCellValue(baris, 5, TanggalPengembalian )

            self.lstIdPengembalian.append(ID)	
            baris += 1

    def btnTambahPengembalianOnButtonClick(self, event):
        dlg = dlgInsertPengembalian(self)
        dlg.ShowModal()

    def m_grid42OnGridCmdSelectCell( self, event ):
        baris = event.GetRow()
        kolom = event.GetCol()

        print('baris: ', baris)
        print('kolom: ', kolom)

        while kolom == 6:
            dlg = wx.MessageDialog(self,'Apakah anda yakin akan menghapus data?', 'Informasi', style=wx.YES_NO )
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.data1.deleteDaftarPengembalian(self.lstIdPengembalian[baris])
                self.initData()
                self.AddButtonDelete()
            break

    def btnBackOnButtonClick(self, event):
        self.Destroy()  
        
    def insertDataPengembalian( self, Tanggal, NamaPeminjam, IDMember, JudulBuku, Denda, TanggalPengembalian ):
        self.data1.setDataPengembalian(Tanggal, NamaPeminjam, IDMember, JudulBuku, Denda, TanggalPengembalian)
        self.initData()
        self.AddButtonDelete()
            
