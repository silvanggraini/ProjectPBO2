import sqlite3

class Data:
	def __init__(self):
		self.connection = sqlite3.connect('data.sqlite3')
		self.cursor = self.connection.cursor()
	def executeQuery(self, query, retVal=False):
		self.cursor.execute(query)
		all_results = self.cursor.fetchall()
		self.connection.commit()
		if retVal:
			return all_results

class Pengembalian(Data):
	def setDataPengembalian(self, Tanggal, Nama_Peminjam, IDMember, JudulBuku, Denda, TanggalPengembalian):
		self.query = 'INSERT INTO `pengembalianBuku`(`Tanggal`, `Nama Peminjam`, `ID Member`, `Judul Buku`, `Tanggal Pengembalian`, `Denda`) values (\'%s\',\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
		self.query = self.query % (Tanggal, Nama_Peminjam, IDMember, JudulBuku, Denda, TanggalPengembalian)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def getDaftarPengembalian(self):
		self.query = 'SELECT `ID`, `Tanggal`, `Nama Peminjam`, `ID Member`, `Judul Buku`, `Tanggal Pengembalian`, `Denda` FROM `pengembalianBuku` WHERE 1' 
		print('self.query : ', self.query )
		daftar = self.executeQuery(self.query, True)
		return daftar
		
	def deleteDaftarPengembalian(self,ID):
		self.query = 'DELETE FROM pengembalianBuku where ID = %i' 
		self.query = self.query % (ID)
		print('self.query : ', self.query )
		self.executeQuery(self.query)

class Member(Data):
	def setDataMember(self, Nama, JenisKelamin, Alamat, NoHP):
		self.query = 'INSERT INTO `dataMember`( `Nama`, `Jenis Kelamin`, `Alamat`, `No HP`) values (\'%s\', \'%s\', \'%s\', \'%s\')' 
		self.query = self.query % (Nama, JenisKelamin, Alamat, NoHP)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def getDaftarMember(self):
		self.query = 'SELECT `ID`, `Nama`, `Jenis Kelamin`, `Alamat`, `No HP` FROM `dataMember` WHERE 1' 
		print('self.query : ', self.query )
		daftar = self.executeQuery(self.query, True)
		return daftar
		
	def deleteDaftarMember(self,ID):
		self.query = 'DELETE FROM dataMember where ID = %i' 
		self.query = self.query % (ID)
		print('self.query : ', self.query )
		self.executeQuery(self.query)

class Peminjaman(Data):
	def setDataPeminjaman(self, TanggalPeminjaman, NamaPeminjam, IDMember, JudulBuku, TanggalPengembalian):
		self.query = 'INSERT INTO `peminjamanBuku`( `Tanggal Peminjaman`, `Nama Peminjam`, `ID Member`, `Judul Buku`, `Tanggal Pengembalian`) values (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
		self.query = self.query % (TanggalPeminjaman, NamaPeminjam, IDMember, JudulBuku, TanggalPengembalian)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def getDataPeminjaman(self):
		self.query = 'SELECT `ID`, `Tanggal Peminjaman`, `Nama Peminjam`, `ID Member`, `Judul Buku`, `Tanggal Pengembalian` FROM `peminjamanBuku` WHERE 1' 
		print('self.query : ', self.query )
		daftar = self.executeQuery(self.query, True)
		return daftar
		
	def deletePeminjaman(self,ID):
		self.query = 'DELETE FROM peminjamanBuku where ID = %i' 
		self.query = self.query % (ID)
		print('self.query : ', self.query )
		self.executeQuery(self.query)

class Transaksi(Data):
	def setDataTransaksi(self,IDBuku, Tanggal, Harga, JumlahBuku, Total):
		self.query = 'INSERT INTO `dataTransaksi`(`ID Buku`, `Tanggal`, `Harga`, `Jumlah Buku`, `Total`) values (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
		self.query = self.query % (IDBuku, Tanggal, Harga, JumlahBuku, Total)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def getDataTransaksi(self):
		self.query = 'SELECT `ID`, `ID Buku`, `Tanggal`, `Harga`, `Jumlah Buku`, `Total` FROM `dataTransaksi` WHERE 1' 
		print('self.query : ', self.query )
		daftar = self.executeQuery(self.query, True)
		return daftar
		
	def deleteTransaksi(self,ID):
		self.query = 'DELETE FROM dataTransaksi where ID = %i' 
		self.query = self.query % (ID)
		print('self.query : ', self.query )
		self.executeQuery(self.query)

class Buku(Data):
	def setDataBuku(self, JudulBuku, NamaPengarang, TahunTerbit, KotaTerbit, NamaPenerbit, JumlahBuku):
		self.query = 'INSERT INTO `daftarBuku`(`Judul Buku`, `Nama Pengarang`, `Tahun Terbit`, `Kota Terbit`, `Nama Penerbit`, `Jumlah Buku`) values (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
		self.query = self.query % (JudulBuku, NamaPengarang, TahunTerbit, KotaTerbit, NamaPenerbit, JumlahBuku)
		print('self.query : ', self.query )
		self.executeQuery(self.query)
		
	def getDataBuku(self):
		self.query = 'SELECT `ID`, `Judul Buku`, `Nama Pengarang`, `Tahun Terbit`, `Kota Terbit`, `Nama Penerbit`, `Jumlah Buku` FROM `daftarBuku` WHERE 1' 
		print('self.query : ', self.query )
		daftar = self.executeQuery(self.query, True)
		return daftar
		
	def deleteDaftarBuku(self,ID):
		self.query = 'DELETE FROM daftarBuku where ID = %i' 
		self.query = self.query % (ID)
		print('self.query : ', self.query )
		self.executeQuery(self.query)

if __name__ == '__main__':
	data1=Pengembalian()
	daftar = data1.getDaftarPengembalian()
	baris = 1
	for data_row in daftar:
		print(baris,'. ', data_row)
		baris += 1
	data2=Member()
	daftar = data2.getDaftarMember()
	baris = 1
	for data_row in daftar:
		print(baris,'. ', data_row)
		baris += 1
	data3=Peminjaman()
	daftar = data3.getDataPeminjaman()
	baris = 1
	for data_row in daftar:
		print(baris,'. ', data_row)
		baris += 1
	data4=Transaksi()
	daftar = data4.getDataTransaksi()
	baris = 1
	for data_row in daftar:
		print(baris,'. ', data_row)
		baris += 1
	data5=Buku()
	daftar = data5.getDataBuku()
	baris = 1
	for data_row in daftar:
		print(baris,'. ', data_row)
		baris += 1