class DaftarNilaiMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah(self, nama, nilai):
        self.data_mahasiswa.append({'nama': nama, 'nilai': nilai})
        print(f"Data {nama} berhasil ditambahkan!")

    def tampilkan(self):
        print("\nDaftar Nilai Mahasiswa:")
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
        else:
            for i, data in enumerate(self.data_mahasiswa, start=1):
                print(f"{i}. Nama: {data['nama']}, Nilai: {data['nilai']}")

    def hapus(self, nama):
        for data in self.data_mahasiswa:
            if data['nama'].lower() == nama.lower():
                self.data_mahasiswa.remove(data)
                print(f"Data {nama} berhasil dihapus!")
                return
        print(f"Data {nama} tidak ditemukan!")

    def ubah(self, nama, nilai_baru):
        for data in self.data_mahasiswa:
            if data['nama'].lower() == nama.lower():
                data['nilai'] = nilai_baru
                print(f"Data {nama} berhasil diubah menjadi Nilai: {nilai_baru}")
                return
        print(f"Data {nama} tidak ditemukan!")


if __name__ == "__main__":
    daftar_nilai = DaftarNilaiMahasiswa()

    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            nama = input("Masukkan Nama Mahasiswa: ")
            nilai = float(input("Masukkan Nilai Mahasiswa: "))
            daftar_nilai.tambah(nama, nilai)
        
        elif pilihan == '2':
            daftar_nilai.tampilkan()
        
        elif pilihan == '3':
            nama = input("Masukkan Nama Mahasiswa yang akan dihapus: ")
            daftar_nilai.hapus(nama)
        
        elif pilihan == '4':
            nama = input("Masukkan Nama Mahasiswa yang akan diubah: ")
            nilai_baru = float(input("Masukkan Nilai Baru: "))
            daftar_nilai.ubah(nama, nilai_baru)
        
        elif pilihan == '5':
            print("Program selesai. Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid! Silakan pilih menu 1-5.")
