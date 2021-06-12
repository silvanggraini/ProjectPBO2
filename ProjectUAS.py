# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class dialogTransaksi
###########################################################################

class dialogTransaksi ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 447,299 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Tambah Transaksi Penjualan Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		bSizer43.Add( self.m_staticText55, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		gSizer14 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"ID Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		gSizer14.Add( self.m_staticText49, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputIDBuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputIDBuku, 0, wx.ALL, 5 )

		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Tanggal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		gSizer14.Add( self.m_staticText50, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_datePicker6 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer14.Add( self.m_datePicker6, 0, wx.ALL, 5 )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Harga(Rp)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )

		gSizer14.Add( self.m_staticText61, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputHarga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputHarga, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Jumlah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		gSizer14.Add( self.m_staticText51, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputJumlah = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputJumlah, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"Total Harga(Rp)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		gSizer14.Add( self.m_staticText52, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputTotalHarga = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputTotalHarga, 0, wx.ALL, 5 )


		bSizer43.Add( gSizer14, 1, wx.EXPAND, 5 )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		self.btnSimpanTransaksi = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.btnSimpanTransaksi, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer43.Add( bSizer44, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer43 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnSimpanTransaksi.Bind( wx.EVT_BUTTON, self.btnSimpanTransaksiOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnSimpanTransaksiOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class dialogMember
###########################################################################

class dialogMember ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 411,249 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Tambah Member", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		bSizer43.Add( self.m_staticText55, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		gSizer14 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		gSizer14.Add( self.m_staticText49, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputNamaMember = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputNamaMember, 0, wx.ALL, 5 )

		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		gSizer14.Add( self.m_staticText50, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		jenisKelaminChoices = [ u"Laki Laki", u"Perempuan" ]
		self.jenisKelamin = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, jenisKelaminChoices, 0 )
		self.jenisKelamin.SetSelection( 0 )
		gSizer14.Add( self.jenisKelamin, 0, wx.ALL, 5 )

		self.IDMember = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.IDMember.Wrap( -1 )

		gSizer14.Add( self.IDMember, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputAlamat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputAlamat, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"No Hp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		gSizer14.Add( self.m_staticText52, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputNoHp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputNoHp, 0, wx.ALL, 5 )


		bSizer43.Add( gSizer14, 1, wx.EXPAND, 5 )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		self.btnSimpanMember = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.btnSimpanMember, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer43.Add( bSizer44, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer43 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnSimpanMember.Bind( wx.EVT_BUTTON, self.btnSimpanMemberOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnSimpanMemberOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class dialogPengembalian
###########################################################################

class dialogPengembalian ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 546,300 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Tambah Pengembalian Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		bSizer43.Add( self.m_staticText55, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		gSizer14 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Tanggal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		gSizer14.Add( self.m_staticText49, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.tanggalPeminjaman = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer14.Add( self.tanggalPeminjaman, 0, wx.ALL, 5 )

		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Nama Peminjam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		gSizer14.Add( self.m_staticText50, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputNamaPeminjam = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputNamaPeminjam, 0, wx.ALL, 5 )

		self.IDMember = wx.StaticText( self, wx.ID_ANY, u"ID Member", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.IDMember.Wrap( -1 )

		gSizer14.Add( self.IDMember, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputIdMember = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputIdMember, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"Judul Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		gSizer14.Add( self.m_staticText52, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputJudulBuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputJudulBuku, 0, wx.ALL, 5 )

		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Pengembalian", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		gSizer14.Add( self.m_staticText53, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.tanggalPengembalian = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer14.Add( self.tanggalPengembalian, 0, wx.ALL, 5 )

		self.inputDenda1 = wx.StaticText( self, wx.ID_ANY, u"Denda (Rp)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inputDenda1.Wrap( -1 )

		gSizer14.Add( self.inputDenda1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputDenda = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputDenda, 0, wx.ALL, 5 )


		bSizer43.Add( gSizer14, 1, wx.EXPAND, 5 )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		self.btnPengembalian = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.btnPengembalian, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer43.Add( bSizer44, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer43 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnPengembalian.Bind( wx.EVT_BUTTON, self.btnPengembalianOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnPengembalianOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class dialogPeminjaman
###########################################################################

class dialogPeminjaman ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 546,278 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Tambah Peminjaman Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		bSizer43.Add( self.m_staticText55, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		gSizer14 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Peminjaman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		gSizer14.Add( self.m_staticText49, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.tanggalPeminjaman = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer14.Add( self.tanggalPeminjaman, 0, wx.ALL, 5 )

		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Nama Peminjam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		gSizer14.Add( self.m_staticText50, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputNamaPeminjam = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputNamaPeminjam, 0, wx.ALL, 5 )

		self.IDMember = wx.StaticText( self, wx.ID_ANY, u"ID Member", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.IDMember.Wrap( -1 )

		gSizer14.Add( self.IDMember, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputIdMember = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputIdMember, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"Judul Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		gSizer14.Add( self.m_staticText52, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputJudulBuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputJudulBuku, 0, wx.ALL, 5 )

		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Tanggal Pengembalian", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		gSizer14.Add( self.m_staticText53, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.tanggalPengembalian = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer14.Add( self.tanggalPengembalian, 0, wx.ALL, 5 )


		bSizer43.Add( gSizer14, 1, wx.EXPAND, 5 )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		self.btnSimpanPeminjaman = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.btnSimpanPeminjaman, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer43.Add( bSizer44, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer43 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnSimpanPeminjaman.Bind( wx.EVT_BUTTON, self.btnSimpanPeminjamanOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnSimpanPeminjamanOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class dialogDaftarBuku
###########################################################################

class dialogDaftarBuku ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Daftar Buku", pos = wx.DefaultPosition, size = wx.Size( 528,326 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer43 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Tambah Daftar Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )

		bSizer43.Add( self.m_staticText55, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		gSizer14 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Judul Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		gSizer14.Add( self.m_staticText49, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputJudulBuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputJudulBuku, 0, wx.ALL, 5 )

		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Nama Pengarang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		gSizer14.Add( self.m_staticText50, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputPengarang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputPengarang, 0, wx.ALL, 5 )

		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"Tahun Terbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )

		gSizer14.Add( self.m_staticText51, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputTahunTerbit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputTahunTerbit, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"Kota Terbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )

		gSizer14.Add( self.m_staticText52, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputKotaTerbit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputKotaTerbit, 0, wx.ALL, 5 )

		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Nama Penerbit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )

		gSizer14.Add( self.m_staticText53, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputPenerbit = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputPenerbit, 0, wx.ALL, 5 )

		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"Jumlah Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )

		gSizer14.Add( self.m_staticText54, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.inputJumlahBuku = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer14.Add( self.inputJumlahBuku, 0, wx.ALL, 5 )


		bSizer43.Add( gSizer14, 1, wx.EXPAND, 5 )

		bSizer44 = wx.BoxSizer( wx.VERTICAL )

		self.btnSimpanDaftarBuku = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer44.Add( self.btnSimpanDaftarBuku, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer43.Add( bSizer44, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer43 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnSimpanDaftarBuku.Bind( wx.EVT_BUTTON, self.btnSimpanDaftarBukuOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnSimpanDaftarBukuOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Mainframe
###########################################################################

class Mainframe ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 624,297 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.panelLogin = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self.panelLogin, wx.ID_ANY, u"Selamat Datang ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer9.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_panel2 = wx.Panel( self.panelLogin, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText15 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		self.m_staticText15.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer4.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.inputUsername = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.inputUsername, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer4.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.inputPassword = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer4.Add( self.inputPassword, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.m_panel2.SetSizer( gSizer4 )
		self.m_panel2.Layout()
		gSizer4.Fit( self.m_panel2 )
		bSizer9.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.btnLogin = wx.Button( self.panelLogin, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnLogin.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer15.Add( self.btnLogin, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer9.Add( bSizer15, 1, wx.EXPAND, 5 )


		self.panelLogin.SetSizer( bSizer9 )
		self.panelLogin.Layout()
		bSizer9.Fit( self.panelLogin )
		bSizer1.Add( self.panelLogin, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.MainframeOnSize )
		self.btnLogin.Bind( wx.EVT_BUTTON, self.btnLoginOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def MainframeOnSize( self, event ):
		event.Skip()

	def btnLoginOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class frameDaftarBuku
###########################################################################

class frameDaftarBuku ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 814,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.panelDaftarBuku1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer221 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText271 = wx.StaticText( self.panelDaftarBuku1, wx.ID_ANY, u"Daftar Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText271.Wrap( -1 )

		self.m_staticText271.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer221.Add( self.m_staticText271, 0, wx.ALL, 5 )

		bSizer231 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_grid41 = wx.grid.Grid( self.panelDaftarBuku1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid41.CreateGrid( 5, 10 )
		self.m_grid41.EnableEditing( True )
		self.m_grid41.EnableGridLines( True )
		self.m_grid41.EnableDragGridSize( False )
		self.m_grid41.SetMargins( 0, 0 )

		# Columns
		self.m_grid41.EnableDragColMove( False )
		self.m_grid41.EnableDragColSize( True )
		self.m_grid41.SetColLabelSize( 30 )
		self.m_grid41.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid41.EnableDragRowSize( True )
		self.m_grid41.SetRowLabelSize( 80 )
		self.m_grid41.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid41.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer231.Add( self.m_grid41, 0, wx.ALL, 5 )

		self.btnTambahBuku = wx.Button( self.panelDaftarBuku1, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer231.Add( self.btnTambahBuku, 0, wx.ALL, 5 )


		bSizer221.Add( bSizer231, 1, wx.EXPAND, 5 )

		self.btnBack1 = wx.Button( self.panelDaftarBuku1, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer221.Add( self.btnBack1, 0, wx.ALL, 5 )


		self.panelDaftarBuku1.SetSizer( bSizer221 )
		self.panelDaftarBuku1.Layout()
		bSizer221.Fit( self.panelDaftarBuku1 )
		bSizer22.Add( self.panelDaftarBuku1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer22 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_grid41.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.m_grid41OnGridCmdSelectCell )
		self.btnTambahBuku.Bind( wx.EVT_BUTTON, self.btnTambahBukuOnButtonClick )
		self.btnBack1.Bind( wx.EVT_BUTTON, self.btnBackOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_grid41OnGridCmdSelectCell( self, event ):
		event.Skip()

	def btnTambahBukuOnButtonClick( self, event ):
		event.Skip()

	def btnBackOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class framePengembalian
###########################################################################

class framePengembalian ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 764,313 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer222 = wx.BoxSizer( wx.VERTICAL )

		self.panelPengembalian1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer68 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText272 = wx.StaticText( self.panelPengembalian1, wx.ID_ANY, u"Pengembalian Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText272.Wrap( -1 )

		self.m_staticText272.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer68.Add( self.m_staticText272, 0, wx.ALL, 5 )

		bSizer232 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_grid42 = wx.grid.Grid( self.panelPengembalian1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid42.CreateGrid( 5, 8 )
		self.m_grid42.EnableEditing( True )
		self.m_grid42.EnableGridLines( True )
		self.m_grid42.EnableDragGridSize( False )
		self.m_grid42.SetMargins( 0, 0 )

		# Columns
		self.m_grid42.EnableDragColMove( False )
		self.m_grid42.EnableDragColSize( True )
		self.m_grid42.SetColLabelSize( 30 )
		self.m_grid42.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid42.EnableDragRowSize( True )
		self.m_grid42.SetRowLabelSize( 80 )
		self.m_grid42.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid42.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer232.Add( self.m_grid42, 0, wx.ALL, 5 )

		self.btnTambahPengembalian = wx.Button( self.panelPengembalian1, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer232.Add( self.btnTambahPengembalian, 0, wx.ALL, 5 )


		bSizer68.Add( bSizer232, 1, wx.EXPAND, 5 )

		self.btnBack = wx.Button( self.panelPengembalian1, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer68.Add( self.btnBack, 0, wx.ALL, 5 )


		self.panelPengembalian1.SetSizer( bSizer68 )
		self.panelPengembalian1.Layout()
		bSizer68.Fit( self.panelPengembalian1 )
		bSizer222.Add( self.panelPengembalian1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer222 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_grid42.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.m_grid42OnGridCmdSelectCell )
		self.btnTambahPengembalian.Bind( wx.EVT_BUTTON, self.btnTambahPengembalianOnButtonClick )
		self.btnBack.Bind( wx.EVT_BUTTON, self.btnBackOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_grid42OnGridCmdSelectCell( self, event ):
		event.Skip()

	def btnTambahPengembalianOnButtonClick( self, event ):
		event.Skip()

	def btnBackOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class framePeminjaman
###########################################################################

class framePeminjaman ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 696,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer221 = wx.BoxSizer( wx.VERTICAL )

		self.panelPeminjaman1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2311 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText81 = wx.StaticText( self.panelPeminjaman1, wx.ID_ANY, u"Peminjaman Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		bSizer2311.Add( self.m_staticText81, 0, wx.ALL, 5 )

		bSizer54 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_grid4111 = wx.grid.Grid( self.panelPeminjaman1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid4111.CreateGrid( 5, 6 )
		self.m_grid4111.EnableEditing( True )
		self.m_grid4111.EnableGridLines( True )
		self.m_grid4111.EnableDragGridSize( False )
		self.m_grid4111.SetMargins( 0, 0 )

		# Columns
		self.m_grid4111.EnableDragColMove( False )
		self.m_grid4111.EnableDragColSize( True )
		self.m_grid4111.SetColLabelSize( 30 )
		self.m_grid4111.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid4111.EnableDragRowSize( True )
		self.m_grid4111.SetRowLabelSize( 80 )
		self.m_grid4111.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid4111.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer54.Add( self.m_grid4111, 0, wx.ALL, 5 )

		self.btnTambahPeminjaman = wx.Button( self.panelPeminjaman1, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer54.Add( self.btnTambahPeminjaman, 0, wx.ALL, 5 )


		bSizer2311.Add( bSizer54, 1, wx.EXPAND, 5 )

		self.btnBack = wx.Button( self.panelPeminjaman1, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2311.Add( self.btnBack, 0, wx.ALL, 5 )


		self.panelPeminjaman1.SetSizer( bSizer2311 )
		self.panelPeminjaman1.Layout()
		bSizer2311.Fit( self.panelPeminjaman1 )
		bSizer221.Add( self.panelPeminjaman1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer221 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_grid4111.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.m_grid4111OnGridCmdSelectCell )
		self.btnTambahPeminjaman.Bind( wx.EVT_BUTTON, self.btnTambahPeminjamanOnButtonClick )
		self.btnBack.Bind( wx.EVT_BUTTON, self.btnBackOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_grid4111OnGridCmdSelectCell( self, event ):
		event.Skip()

	def btnTambahPeminjamanOnButtonClick( self, event ):
		event.Skip()

	def btnBackOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class frameKasir
###########################################################################

class frameKasir ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,417 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer69 = wx.BoxSizer( wx.VERTICAL )

		self.panelKasir1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.panelKasir1, wx.ID_ANY, u"Masukan Data" ), wx.VERTICAL )

		gSizer13 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText34 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"ID Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		gSizer13.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.inputIdBuku = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.inputIdBuku, 0, wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Tanggal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		gSizer13.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.tanggalTransaksi = wx.adv.DatePickerCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer13.Add( self.tanggalTransaksi, 0, wx.ALL, 5 )

		self.m_staticText36 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Harga (Rp)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		gSizer13.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.inputHargaBuku = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.inputHargaBuku, 0, wx.ALL, 5 )

		self.m_staticText37 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Jumlah Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )

		gSizer13.Add( self.m_staticText37, 0, wx.ALL, 5 )

		self.inputJumlahBuku = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.inputJumlahBuku, 0, wx.ALL, 5 )

		self.btnSimpan = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.btnSimpan, 0, wx.ALL, 5 )


		sbSizer3.Add( gSizer13, 1, wx.EXPAND, 5 )


		bSizer32.Add( sbSizer3, 1, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText39 = wx.StaticText( self.panelKasir1, wx.ID_ANY, u"Total Pembayaran (Rp)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )

		fgSizer2.Add( self.m_staticText39, 0, wx.ALL, 5 )

		self.inputTotalPembayaran = wx.TextCtrl( self.panelKasir1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inputTotalPembayaran, 0, wx.ALL, 5 )

		self.m_staticText40 = wx.StaticText( self.panelKasir1, wx.ID_ANY, u"Cash (Rp)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )

		fgSizer2.Add( self.m_staticText40, 0, wx.ALL, 5 )

		self.inputCash = wx.TextCtrl( self.panelKasir1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inputCash, 0, wx.ALL, 5 )

		self.m_staticText41 = wx.StaticText( self.panelKasir1, wx.ID_ANY, u"Kembalian (Rp)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		fgSizer2.Add( self.m_staticText41, 0, wx.ALL, 5 )

		gSizer24 = wx.GridSizer( 0, 2, 0, 0 )

		self.inputKembalian = wx.TextCtrl( self.panelKasir1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer24.Add( self.inputKembalian, 0, wx.ALL, 5 )

		self.btnKembalian = wx.Button( self.panelKasir1, wx.ID_ANY, u"Kembalian", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer24.Add( self.btnKembalian, 0, wx.ALL, 5 )


		fgSizer2.Add( gSizer24, 1, wx.EXPAND, 5 )


		bSizer32.Add( fgSizer2, 1, wx.EXPAND, 5 )

		self.btnBack = wx.Button( self.panelKasir1, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.btnBack, 0, wx.ALL, 5 )


		self.panelKasir1.SetSizer( bSizer32 )
		self.panelKasir1.Layout()
		bSizer32.Fit( self.panelKasir1 )
		bSizer69.Add( self.panelKasir1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer69 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnSimpan.Bind( wx.EVT_BUTTON, self.btnSimpanOnButtonClick )
		self.btnKembalian.Bind( wx.EVT_BUTTON, self.btnKembalianOnButtonClick )
		self.btnBack.Bind( wx.EVT_BUTTON, self.btnBackOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnSimpanOnButtonClick( self, event ):
		event.Skip()

	def btnKembalianOnButtonClick( self, event ):
		event.Skip()

	def btnBackOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class frameMember
###########################################################################

class frameMember ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 710,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer71 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		panelMember1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2722 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Daftar Member", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2722.Wrap( -1 )

		self.m_staticText2722.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		panelMember1.Add( self.m_staticText2722, 0, wx.ALL, 5 )

		bSizer2322 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_grid422 = wx.grid.Grid( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid422.CreateGrid( 5, 6 )
		self.m_grid422.EnableEditing( True )
		self.m_grid422.EnableGridLines( True )
		self.m_grid422.EnableDragGridSize( False )
		self.m_grid422.SetMargins( 0, 0 )

		# Columns
		self.m_grid422.EnableDragColMove( False )
		self.m_grid422.EnableDragColSize( True )
		self.m_grid422.SetColLabelSize( 30 )
		self.m_grid422.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid422.EnableDragRowSize( True )
		self.m_grid422.SetRowLabelSize( 80 )
		self.m_grid422.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid422.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2322.Add( self.m_grid422, 0, wx.ALL, 5 )

		self.btnTambahMember = wx.Button( self.m_panel15, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2322.Add( self.btnTambahMember, 0, wx.ALL, 5 )


		panelMember1.Add( bSizer2322, 1, wx.EXPAND, 5 )

		self.btnBack = wx.Button( self.m_panel15, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		panelMember1.Add( self.btnBack, 0, wx.ALL, 5 )


		self.m_panel15.SetSizer( panelMember1 )
		self.m_panel15.Layout()
		panelMember1.Fit( self.m_panel15 )
		bSizer71.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer71 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_grid422.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.m_grid422OnGridCmdSelectCell )
		self.btnTambahMember.Bind( wx.EVT_BUTTON, self.btnTambahMemberOnButtonClick )
		self.btnBack.Bind( wx.EVT_BUTTON, self.btnBackOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_grid422OnGridCmdSelectCell( self, event ):
		event.Skip()

	def btnTambahMemberOnButtonClick( self, event ):
		event.Skip()

	def btnBackOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class frameTransaksi
###########################################################################

class frameTransaksi ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 841,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2211 = wx.BoxSizer( wx.VERTICAL )

		self.panelTransaksiPenjualan = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22111 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText27111 = wx.StaticText( self.panelTransaksiPenjualan, wx.ID_ANY, u"Transaksi Penjualan Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27111.Wrap( -1 )

		self.m_staticText27111.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer22111.Add( self.m_staticText27111, 0, wx.ALL, 5 )

		bSizer23111 = wx.BoxSizer( wx.HORIZONTAL )

		self.tabelTransaksi = wx.grid.Grid( self.panelTransaksiPenjualan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabelTransaksi.CreateGrid( 5, 8 )
		self.tabelTransaksi.EnableEditing( True )
		self.tabelTransaksi.EnableGridLines( True )
		self.tabelTransaksi.EnableDragGridSize( False )
		self.tabelTransaksi.SetMargins( 0, 0 )

		# Columns
		self.tabelTransaksi.EnableDragColMove( False )
		self.tabelTransaksi.EnableDragColSize( True )
		self.tabelTransaksi.SetColLabelSize( 30 )
		self.tabelTransaksi.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelTransaksi.EnableDragRowSize( True )
		self.tabelTransaksi.SetRowLabelSize( 80 )
		self.tabelTransaksi.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelTransaksi.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer23111.Add( self.tabelTransaksi, 0, wx.ALL, 5 )

		self.btnTambahTransaksi = wx.Button( self.panelTransaksiPenjualan, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23111.Add( self.btnTambahTransaksi, 0, wx.ALL, 5 )


		bSizer22111.Add( bSizer23111, 1, wx.EXPAND, 5 )

		self.btnBack1 = wx.Button( self.panelTransaksiPenjualan, wx.ID_ANY, u"Kembali", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22111.Add( self.btnBack1, 0, wx.ALL, 5 )


		self.panelTransaksiPenjualan.SetSizer( bSizer22111 )
		self.panelTransaksiPenjualan.Layout()
		bSizer22111.Fit( self.panelTransaksiPenjualan )
		bSizer2211.Add( self.panelTransaksiPenjualan, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2211 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.tabelTransaksi.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelTransaksiOnGridCmdSelectCell )
		self.btnTambahTransaksi.Bind( wx.EVT_BUTTON, self.btnTambahTransaksiOnButtonClick )
		self.btnBack1.Bind( wx.EVT_BUTTON, self.btnBackOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tabelTransaksiOnGridCmdSelectCell( self, event ):
		event.Skip()

	def btnTambahTransaksiOnButtonClick( self, event ):
		event.Skip()

	def btnBackOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class frameHome
###########################################################################

class frameHome ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.panelHome1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText171 = wx.StaticText( self.panelHome1, wx.ID_ANY, u"Sistem Informasi Penjualan dan Peminjaman Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )

		self.m_staticText171.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer35.Add( self.m_staticText171, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		gSizer81 = wx.GridSizer( 0, 2, 0, 0 )

		self.btnDaftarBuku1 = wx.Button( self.panelHome1, wx.ID_ANY, u"Daftar Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer81.Add( self.btnDaftarBuku1, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnPeminjaman1 = wx.Button( self.panelHome1, wx.ID_ANY, u"Peminjaman Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer81.Add( self.btnPeminjaman1, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnPengembalian1 = wx.Button( self.panelHome1, wx.ID_ANY, u"Pengembalian Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer81.Add( self.btnPengembalian1, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnKasir1 = wx.Button( self.panelHome1, wx.ID_ANY, u"Kasir Penjualan Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer81.Add( self.btnKasir1, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnMember1 = wx.Button( self.panelHome1, wx.ID_ANY, u"Member", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer81.Add( self.btnMember1, 0, wx.ALL|wx.EXPAND, 5 )

		self.btnTransaksi1 = wx.Button( self.panelHome1, wx.ID_ANY, u"Transaksi Penjualan Buku", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer81.Add( self.btnTransaksi1, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer35.Add( gSizer81, 1, wx.EXPAND, 5 )


		self.panelHome1.SetSizer( bSizer35 )
		self.panelHome1.Layout()
		bSizer35.Fit( self.panelHome1 )
		bSizer17.Add( self.panelHome1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer17 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnDaftarBuku1.Bind( wx.EVT_BUTTON, self.btnDaftarBukuOnButtonClick )
		self.btnPeminjaman1.Bind( wx.EVT_BUTTON, self.btnPeminjamanOnButtonClick )
		self.btnPengembalian1.Bind( wx.EVT_BUTTON, self.btnPengembalianOnButtonClick )
		self.btnKasir1.Bind( wx.EVT_BUTTON, self.btnKasirOnButtonClick )
		self.btnMember1.Bind( wx.EVT_BUTTON, self.btnMemberOnButtonClick )
		self.btnTransaksi1.Bind( wx.EVT_BUTTON, self.btnTransaksiOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnDaftarBukuOnButtonClick( self, event ):
		event.Skip()

	def btnPeminjamanOnButtonClick( self, event ):
		event.Skip()

	def btnPengembalianOnButtonClick( self, event ):
		event.Skip()

	def btnKasirOnButtonClick( self, event ):
		event.Skip()

	def btnMemberOnButtonClick( self, event ):
		event.Skip()

	def btnTransaksiOnButtonClick( self, event ):
		event.Skip()


