import wx
import ProjectUAS
import database
# from home import home

class dlgInsertBuku(ProjectUAS.dialogDaftarBuku):
    def __init__(self, parent, ID=-1):
        ProjectUAS.dialogDaftarBuku.__init__(self, parent)
        self.parent = parent 
        self.ID = ID
        
    def btnSimpanDaftarBukuOnButtonClick( self, event ):
        if self.inputJudulBuku.GetValue() == '' or self.inputPengarang.GetValue() == '' or self.inputTahunTerbit.GetValue() == '' or self.inputKotaTerbit.GetValue() == '' or self.inputPenerbit.GetValue() == '' or self.inputJumlahBuku.GetValue() == '':
            wx.MessageBox('Silahkan Isi Data yang Kosong', 'Information', wx.OK | wx.ICON_ERROR)
            return False
        else:
            wx.MessageBox('Data Berhasil Ditambahkan', 'Information', wx.OK | wx.ICON_INFORMATION)
            self.Destroy()
        print('simpan')
        while self.ID == -1:
            self.parent.insertDataBuku(self.inputJudulBuku.GetValue(), self.inputPengarang.GetValue(), 
            self.inputTahunTerbit.GetValue(), self.inputKotaTerbit.GetValue(), self.inputPenerbit.GetValue(),
            self.inputJumlahBuku.GetValue())
            break

    def isiDataBuku(self,JudulBuku, NamaPengarang, TahunTerbit, KotaTerbit, NamaPenerbit, JumlahBuku):
        self.inputJudulBuku.SetValue(JudulBuku)
        self.inputPengarang.SetValue(NamaPengarang)
        self.inputTahunTerbit.SetValue(TahunTerbit)
        self.inputKotaTerbit.SetValue(KotaTerbit)
        self.inputPenerbit.SetValue(NamaPenerbit)
        self.inputJumlahBuku.SetValue(JumlahBuku)

class daftarBuku(ProjectUAS.frameDaftarBuku):
    def __init__(self, parent):
        ProjectUAS.frameDaftarBuku.__init__(self, parent)
        self.data5 = database.Buku()
        self.initData()
        self.AddButtonDelete()

    def AddButtonDelete(self):		
        jmlKolom = self.m_grid41.GetNumberCols()
        self.m_grid41.AppendCols(1)
        colDelete = jmlKolom

        self.m_grid41.SetColLabelValue(colDelete, '')

        for row in range (self.m_grid41.GetNumberRows()):
            self.m_grid41.SetCellValue(row,colDelete,'Delete')
            self.m_grid41.SetCellBackgroundColour(row,colDelete,wx.RED)
            self.m_grid41.SetCellTextColour(row,colDelete,wx.WHITE)
            self.m_grid41.SetCellAlignment(row, colDelete, wx.ALIGN_CENTER_HORIZONTAL, wx.ALIGN_CENTER_VERTICAL)

    def initData(self):			
        n_cols = self.m_grid41.GetNumberCols()
        n_rows = self.m_grid41.GetNumberRows()
        if n_cols > 0:
            self.m_grid41.DeleteCols(0, n_cols, True)        
        if n_rows > 0:
            self.m_grid41.DeleteRows(0, n_rows, True)   

            # t2.nama, t2.email, t1.nim, t1.tahun_masuk
        koloms = ['JudulBuku', 'NamaPengarang', 'TahunTerbit', 'KotaTerbit', 'NamaPenerbit', 'JumlahBuku']
        self.m_grid41.AppendCols(len(koloms))

        daftar = self.data5.getDataBuku()
        baris = 0
            # lstData = []
        self.lstIdBuku = []
        for col in range(len(koloms)):
            self.m_grid41.SetColLabelValue(col, koloms[col]) # mengubah nama kolom
        for buku_row in daftar:
            self.m_grid41.AppendRows(1)

            print(baris,'. ', buku_row)
            ID, JudulBuku, NamaPengarang, TahunTerbit, KotaTerbit, NamaPenerbit, JumlahBuku = buku_row
            
            # self.m_grid41.SetCellValue(baris, 0, ID )
            self.m_grid41.SetCellValue(baris, 0, JudulBuku )
            self.m_grid41.SetCellValue(baris, 1, NamaPengarang)
            self.m_grid41.SetCellValue(baris, 2, TahunTerbit )
            self.m_grid41.SetCellValue(baris, 3, KotaTerbit)
            self.m_grid41.SetCellValue(baris, 4, NamaPenerbit )
            self.m_grid41.SetCellValue(baris, 5, JumlahBuku )

            self.lstIdBuku.append(ID)	
            baris += 1

    def btnTambahBukuOnButtonClick(self,event):
        dlg = dlgInsertBuku(self)
        dlg.ShowModal()
        
    def m_grid41OnGridCmdSelectCell( self, event ):
        baris = event.GetRow()
        kolom = event.GetCol()

        print('baris: ', baris)
        print('kolom: ', kolom)

        while kolom == 6:
            dlg = wx.MessageDialog(self,'Apakah anda yakin akan menghapus data?', 'Informasi', style=wx.YES_NO )
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.data5.deleteDaftarBuku(self.lstIdBuku[baris])
                self.initData()
                self.AddButtonDelete()
            break
        
    def insertDataBuku( self,JudulBuku, NamaPengarang, TahunTerbit, KotaTerbit, NamaPenerbit, JumlahBuku ):
        self.data5.setDataBuku(JudulBuku, NamaPengarang, TahunTerbit, KotaTerbit, NamaPenerbit, JumlahBuku)
        self.initData()
        self.AddButtonDelete()

    def btnBackOnButtonClick( self, event ):
        # framehome = home(parent=None)
        # framehome.Show()
        self.Destroy()

# app=wx.App()
# Panel=daftarBuku(None)
# Panel.Show()
# app.MainLoop()
