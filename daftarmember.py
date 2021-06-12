import wx
from wx.core import Dialog
import ProjectUAS
import database

class dlgInsertMember(ProjectUAS.dialogMember):
    def __init__(self, parent, ID=-1):
        ProjectUAS.dialogMember.__init__(self, parent)
        self.parent = parent 
        self.ID = ID

    def btnSimpanMemberOnButtonClick( self, event ):
        if self.inputNamaMember.GetValue() == '' or self.inputAlamat.GetValue() == '' or self.inputNoHp.GetValue() == '':
            wx.MessageBox('Silahkan Isi Data yang Kosong', 'Information', wx.OK | wx.ICON_ERROR)
            return False
        else:
            wx.MessageBox('Data Berhasil Ditambahkan', 'Information', wx.OK | wx.ICON_INFORMATION)
            self.Destroy()
        print('simpan')
        while self.ID == -1:
            self.parent.insertDataMember(self.inputNamaMember.GetValue(), self.jenisKelamin.GetStringSelection(), 
            self.inputAlamat.GetValue(), self.inputNoHp.GetValue()
			)
            break
        
    def isiDataMember(self,Nama, JenisKelamin, Alamat, NoHP):
        self.inputNamaMember.SetValue(Nama)
        self.jenisKelamin.SetStringSelection(JenisKelamin)
        self.inputAlamat.SetValue(Alamat)
        self.inputNoHp.SetValue(NoHP) 


class daftarMember(ProjectUAS.frameMember):
    def __init__(self, parent):
        ProjectUAS.frameMember.__init__(self, parent)
        self.data2 = database.Member()
        self.initData()
        self.AddButtonDelete()

    def AddButtonDelete(self):		
        jmlKolom = self.m_grid422.GetNumberCols()
        self.m_grid422.AppendCols(1)
        colDelete = jmlKolom 

        self.m_grid422.SetColLabelValue(colDelete, '')

        for row in range (self.m_grid422.GetNumberRows()):
            self.m_grid422.SetCellValue(row,colDelete,'Delete')
            self.m_grid422.SetCellBackgroundColour(row,colDelete,wx.RED)
            self.m_grid422.SetCellTextColour(row,colDelete,wx.WHITE)
            self.m_grid422.SetCellAlignment(row, colDelete, wx.ALIGN_CENTER_HORIZONTAL, wx.ALIGN_CENTER_VERTICAL)

    def initData(self):			
        n_cols = self.m_grid422.GetNumberCols()
        n_rows = self.m_grid422.GetNumberRows()
        if n_cols > 0:
            self.m_grid422.DeleteCols(0, n_cols, True)        
        if n_rows > 0:
            self.m_grid422.DeleteRows(0, n_rows, True)   

            # t2.nama, t2.email, t1.nim, t1.tahun_masuk
        koloms = ['Nama', 'Jenis Kelamin', 'Alamat', 'No HP']
        self.m_grid422.AppendCols(len(koloms))

        daftar = self.data2.getDaftarMember()
        baris = 0
            # lstData = []
        self.lstIdMember = []
        for col in range(len(koloms)):
            self.m_grid422.SetColLabelValue(col, koloms[col]) # mengubah nama kolom
        for member_row in daftar:
            self.m_grid422.AppendRows(1)
                # tmp_data_baris = []
            print(baris,'. ', member_row)
            ID, Nama, JenisKelamin, Alamat, NoHP = member_row
            # self.m_grid422.SetCellValue(baris, 0, ID )
            self.m_grid422.SetCellValue(baris, 0, Nama )
            self.m_grid422.SetCellValue(baris, 1, JenisKelamin)
            self.m_grid422.SetCellValue(baris, 2, Alamat )
            self.m_grid422.SetCellValue(baris, 3, NoHP)
            self.lstIdMember.append(ID)	
            baris += 1
    
    def btnTambahMemberOnButtonClick(self,event):
        dlg = dlgInsertMember(self)
        dlg.ShowModal()

    def m_grid422OnGridCmdSelectCell( self, event ):
        baris = event.GetRow()
        kolom = event.GetCol()

        print('baris: ', baris)
        print('kolom: ', kolom)

        while kolom == 4:
            dlg = wx.MessageDialog(self,'Apakah anda yakin akan menghapus data?', 'Informasi', style=wx.YES_NO )
            retval = dlg.ShowModal()
            if retval == wx.ID_YES:
                print('hapus')
                self.data2.deleteDaftarMember(self.lstIdMember[baris])
                self.initData()
                self.AddButtonDelete()
            break

    def btnBackOnButtonClick(self, event):
        self.Destroy()
        
    def insertDataMember( self, Nama, JenisKelamin, Alamat, NoHP ):
        self.data2.setDataMember( Nama, JenisKelamin, Alamat, NoHP)
        self.initData()
        self.AddButtonDelete()
            

        

# app=wx.App()
# Panel=daftarMember(None)
# Panel.Show()
# app.MainLoop()
