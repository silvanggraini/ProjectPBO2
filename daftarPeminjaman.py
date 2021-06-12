import wx
from wx.core import Panel
import ProjectUAS
import database

class dlgInsertPeminjaman(ProjectUAS.dialogPeminjaman):
    def __init__(self, parent, ID=-1):
        ProjectUAS.dialogPeminjaman.__init__(self, parent)
        self.parent = parent 
        self.ID = ID

    def btnSimpanPeminjamanOnButtonClick( self, event ):
        if self.tanggalPeminjaman.GetValue() == '' or self.tanggalPeminjaman.GetValue() == '' or self.inputNamaPeminjam.GetValue() == '' or self.inputIdMember.GetValue() == '' or self.inputJudulBuku.GetValue() == '' or self.tanggalPengembalian.GetValue() == '':
            wx.MessageBox('Silahkan Isi Data yang Kosong', 'Information', wx.OK | wx.ICON_ERROR)
            return False
        else:
            wx.MessageBox('Data Berhasil Ditambahkan', 'Information', wx.OK | wx.ICON_INFORMATION)
            self.Destroy()
        print('simpan')
        while self.ID == -1:
            self.parent.insertDataPeminjaman(self.tanggalPeminjaman.GetValue(), self.inputNamaPeminjam.GetValue(), 
			self.inputIdMember.GetValue(), self.inputJudulBuku.GetValue(), self.tanggalPengembalian.GetValue(),
			)
            break

    def isiDataPeminjaman(self,Tanggal, NamaPeminjam, IDMember, JudulBuku, TanggalPengembalian):
        self.tanggalPeminjaman.SetValue(Tanggal)
        self.inputNamaPeminjam.SetValue(NamaPeminjam)
        self.inputIdMember.SetValue(IDMember)
        self.inputJudulBuku.SetValue(JudulBuku)
        self.tanggalPengembalian.SetValue(TanggalPengembalian)

class daftarPeminjaman(ProjectUAS.framePeminjaman):
    def __init__(self, parent):
        ProjectUAS.framePeminjaman.__init__(self, parent)
        self.data3 = database.Peminjaman()
        self.initData()
        self.AddButtonDelete()

    def AddButtonDelete(self):		
        jmlKolom = self.m_grid4111.GetNumberCols()
        self.m_grid4111.AppendCols(1)
        colDelete = jmlKolom

        self.m_grid4111.SetColLabelValue(colDelete, '')

        for row in range (self.m_grid4111.GetNumberRows()):
            self.m_grid4111.SetCellValue(row,colDelete,'Delete')
            self.m_grid4111.SetCellBackgroundColour(row,colDelete,wx.RED)
            self.m_grid4111.SetCellTextColour(row,colDelete,wx.WHITE)
            self.m_grid4111.SetCellAlignment(row, colDelete, wx.ALIGN_CENTER_HORIZONTAL, wx.ALIGN_CENTER_VERTICAL)

    def initData(self):			
        n_cols = self.m_grid4111.GetNumberCols()
        n_rows = self.m_grid4111.GetNumberRows()
        if n_cols > 0:
            self.m_grid4111.DeleteCols(0, n_cols, True)        
        if n_rows > 0:
            self.m_grid4111.DeleteRows(0, n_rows, True)   

        koloms = ['Tanggal', 'Nama Peminjam', 'ID Member', 'Judul Buku', 'Tanggal Pengembalian']
        self.m_grid4111.AppendCols(len(koloms))

        daftar = self.data3.getDataPeminjaman()
        baris = 0
            # lstData = []
        self.lstIdPeminjaman = []
        for col in range(len(koloms)):
            self.m_grid4111.SetColLabelValue(col, koloms[col]) # mengubah nama kolom
        for peminjaman_row in daftar:
            self.m_grid4111.AppendRows(1)

            print(baris,'. ', peminjaman_row)
            ID, Tanggal, NamaPeminjam, IDMember, JudulBuku, TanggalPengembalian = peminjaman_row
            # self.m_grid4111.SetCellValue(baris, 0, ID )
            self.m_grid4111.SetCellValue(baris, 0, Tanggal )
            self.m_grid4111.SetCellValue(baris, 1, NamaPeminjam)
            self.m_grid4111.SetCellValue(baris, 2, IDMember )
            self.m_grid4111.SetCellValue(baris, 3, JudulBuku)
            self.m_grid4111.SetCellValue(baris, 4, TanggalPengembalian )

            self.lstIdPeminjaman.append(ID)	
            baris += 1

    def btnTambahPeminjamanOnButtonClick(self,event):
        dlg = dlgInsertPeminjaman(self)
        dlg.ShowModal()


    def m_grid4111OnGridCmdSelectCell( self, event ):
        baris = event.GetRow()
        kolom = event.GetCol()

        print('baris: ', baris)
        print('kolom: ', kolom)

        while kolom == 5:
            dlg = wx.MessageDialog(self,'Apakah anda yakin akan menghapus data?', 'Informasi', style=wx.YES_NO )
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.data3.deletePeminjaman(self.lstIdPeminjaman[baris])
                self.initData()
                self.AddButtonDelete()
            break

    def btnBackOnButtonClick(self, event):
        self.Destroy()      
        
    def insertDataPeminjaman( self, Tanggal, NamaPeminjam, IDMember, JudulBuku, TanggalPengembalian ):
        self.data3.setDataPeminjaman( Tanggal, NamaPeminjam, IDMember, JudulBuku, TanggalPengembalian)
        self.initData()
        self.AddButtonDelete()

