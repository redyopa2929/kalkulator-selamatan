# Kalkulator Selamatan Orang Meninggal — Hitung 3, 7, 40, 100 hingga 1000 Hari Adat Jawa (Python)

**Kalkulator selamatan orang meninggal** ini adalah aplikasi Python sederhana untuk mengetahui tanggal nelung dina (3 hari), mitung dina (7 hari), matang puluh (40 hari), nyatus (100 hari), mendhak pisan, mendhak pindho, sampai nyewu (1.000 hari). Cukup masukkan tanggal wafat. Dalam hitungan detik Anda mendapat tabel lengkap berisi tanggal Masehi, hari dan pasaran Jawa, serta berapa hari lagi menuju setiap acara. Tool ini juga menjelaskan **cara menghitung selamatan orang meninggal adat Jawa** secara manual, sehingga keluarga bisa mencocokkan hasilnya dengan hitungan sesepuh.

> 🛠️ Tool gratis & open source ini adalah karya **[JoinBareng](https://joinbareng.com)** — platform patungan langganan premium di Indonesia.

Saat keluarga sedang berduka, urusan menghitung hari tahlilan sering terasa membingungkan. Ada yang menghitung 40 hari dari hari setelah wafat, ada yang dari hari wafat itu sendiri. Ada pula yang lupa bahwa wafat setelah maghrib sudah terhitung hari berikutnya. Kalkulator ini membantu supaya hitungan konsisten dan mudah dicek ulang.

## Daftar Isi

- [Apa Itu Selamatan Orang Meninggal](#apa-itu-selamatan-orang-meninggal)
- [Fitur](#fitur)
- [Cara Install dan Menjalankan](#cara-install-dan-menjalankan)
- [Cara Pakai dan Contoh Output](#cara-pakai-dan-contoh-output)
- [Cara Menghitung Selamatan Orang Meninggal Adat Jawa](#cara-menghitung-selamatan-orang-meninggal-adat-jawa)
- [Wafat Setelah Maghrib](#wafat-setelah-maghrib)
- [Tabel Referensi Cepat](#tabel-referensi-cepat)
- [Perbedaan Praktik Antardaerah](#perbedaan-praktik-antardaerah)
- [Tips dan Kesalahan Umum](#tips-dan-kesalahan-umum)
- [FAQ](#faq)
- [Metodologi, Pengujian, dan Sumber](#metodologi-pengujian-dan-sumber)
- [Tentang Pembuat](#tentang-pembuat)
- [Disclaimer](#disclaimer)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)
- [Dukung Proyek Ini](#dukung-proyek-ini)
- [Tools Lainnya dari Seri Ini](#tools-lainnya-dari-seri-ini)

## Apa Itu Selamatan Orang Meninggal

Selamatan (slametan) kematian adalah tradisi masyarakat Jawa untuk mendoakan anggota keluarga yang telah wafat. Kegiatannya biasanya berupa kenduri, pembacaan doa, dan tahlilan bersama tetangga serta kerabat. Antropolog Clifford Geertz dalam *The Religion of Java* (1960) mencatat bahwa slametan kematian digelar pada hari wafat, lalu diulang pada hari ke-3, ke-7, ke-40, ke-100, peringatan tahun pertama dan kedua, serta hari ke-1.000.

Urutan yang dikenal luas adalah sebagai berikut:

1. **Geblag atau surtanah**: hari wafat dan pemakaman.
2. **Nelung dina**: hari ke-3.
3. **Mitung dina**: hari ke-7.
4. **Matang puluh**: hari ke-40.
5. **Nyatus**: hari ke-100.
6. **Mendhak pisan**: peringatan tahun pertama (setahun Jawa).
7. **Mendhak pindho**: peringatan tahun kedua.
8. **Nyewu**: hari ke-1.000, biasanya menjadi peringatan terakhir dan paling besar.

Tradisi ini dijalankan secara berbeda-beda. Ada keluarga yang menggelar kenduri besar, ada yang cukup tahlilan sederhana, ada pula yang memilih bersedekah tanpa acara. Sebagian kalangan juga tidak menjalankannya dengan alasan pemahaman keagamaan. Repo ini tidak menilai mana yang lebih benar. Kalkulator selamatan orang meninggal ini hanya membantu keluarga yang memang ingin menjalankan tradisi agar hitungan harinya tepat.

## Fitur

Berikut kemampuan kalkulator selamatan orang meninggal ini:

- Menghitung delapan tahap selamatan sekaligus dari satu tanggal wafat.
- Menampilkan nama acara dalam bahasa Jawa dan Indonesia, hari ke-, tanggal Masehi lengkap (contoh "Jumat, 17 Agustus 1945"), serta hari dan pasaran.
- Menyertakan nama rumus mnemonik (lusarlu, tusaro, masarma, rosarma, patsarpat, jisarlu, nemsarma) supaya mudah dicocokkan dengan hitungan sesepuh.
- Menghitung sisa hari ("3 hari lagi") atau hari yang sudah lewat dibanding hari ini atau tanggal pilihan Anda.
- Opsi `--setelah-maghrib` untuk wafat setelah matahari terbenam.
- Mode interaktif berbahasa Indonesia: jalankan tanpa argumen, lalu jawab pertanyaannya.
- Hanya memakai standard library Python 3.8+, tanpa internet dan tanpa install paket tambahan.

## Cara Install dan Menjalankan

Pastikan Python 3.8 atau lebih baru sudah terpasang. Di Windows, gunakan `python` jika perintah `python3` tidak dikenali.

```bash
git clone https://github.com/redyopa2929/kalkulator-selamatan.git
cd kalkulator-selamatan
python3 selamatan.py
```

Perintah terakhir membuka mode interaktif. Untuk langsung menghitung, tambahkan tanggal wafat dengan format `DD-MM-YYYY`.

## Cara Pakai dan Contoh Output

### Contoh 1: perhitungan orang meninggal dari tanggal wafat

Misalkan seseorang wafat pada siang hari, Selasa 15 September 2026. Opsi `--pembanding` dipakai agar contoh ini bisa diulang persis. Tanpa opsi itu, pembandingnya adalah tanggal hari ini.

```text
$ python3 selamatan.py 15-09-2026 --pembanding 21-10-2026
Tanggal wafat       : Selasa, 15 September 2026 (Selasa Kliwon)
Hari ke-1 hitungan  : Selasa, 15 September 2026 (Selasa Kliwon)
Dibanding tanggal   : Rabu, 21 Oktober 2026

+--------------------------+----------+---------------------------+----------------+-----------+---------------------+
| Acara                    | Hari ke- | Tanggal Masehi            | Hari + pasaran | Rumus     | Keterangan          |
+--------------------------+----------+---------------------------+----------------+-----------+---------------------+
| Geblag (hari wafat)      |        1 | Selasa, 15 September 2026 | Selasa Kliwon  | -         | sudah lewat 36 hari |
| Nelung dina (3 hari)     |        3 | Kamis, 17 September 2026  | Kamis Pahing   | lusarlu   | sudah lewat 34 hari |
| Mitung dina (7 hari)     |        7 | Senin, 21 September 2026  | Senin Legi     | tusaro    | sudah lewat 30 hari |
| Matang puluh (40 hari)   |       40 | Sabtu, 24 Oktober 2026    | Sabtu Wage     | masarma   | 3 hari lagi         |
| Nyatus (100 hari)        |      100 | Rabu, 23 Desember 2026    | Rabu Wage      | rosarma   | 63 hari lagi        |
| Mendhak pisan (1 tahun)  |      354 | Jumat, 3 September 2027   | Jumat Pon      | patsarpat | 317 hari lagi       |
| Mendhak pindho (2 tahun) |      708 | Selasa, 22 Agustus 2028   | Selasa Pahing  | jisarlu   | 671 hari lagi       |
| Nyewu (1.000 hari)       |    1.000 | Minggu, 10 Juni 2029      | Minggu Wage    | nemsarma  | 963 hari lagi       |
+--------------------------+----------+---------------------------+----------------+-----------+---------------------+
Catatan: banyak keluarga menggelar acara pada malam sebelumnya (setelah
maghrib), misalnya acara hari Sabtu digelar Jumat malam (malam Sabtu),
karena dalam hitungan Jawa hari baru dimulai saat matahari terbenam.
Hasil ini panduan; konfirmasikan dengan sesepuh atau tokoh adat setempat.
```

### Contoh 2: wafat setelah maghrib

Kasus yang sama, tetapi wafat pukul 19.00. Semua tanggal bergeser satu hari karena hari ke-1 dihitung mulai Rabu Legi.

```text
$ python3 selamatan.py 15-09-2026 --setelah-maghrib --pembanding 21-10-2026
Tanggal wafat       : Selasa, 15 September 2026 (Selasa Kliwon)
Waktu wafat         : setelah maghrib -> hitungan Jawa sudah masuk hari berikutnya
Hari ke-1 hitungan  : Rabu, 16 September 2026 (Rabu Legi)
Dibanding tanggal   : Rabu, 21 Oktober 2026

+--------------------------+----------+---------------------------+----------------+-----------+---------------------+
| Acara                    | Hari ke- | Tanggal Masehi            | Hari + pasaran | Rumus     | Keterangan          |
+--------------------------+----------+---------------------------+----------------+-----------+---------------------+
| Geblag (hari wafat)      |        1 | Rabu, 16 September 2026   | Rabu Legi      | -         | sudah lewat 35 hari |
| Nelung dina (3 hari)     |        3 | Jumat, 18 September 2026  | Jumat Pon      | lusarlu   | sudah lewat 33 hari |
| Mitung dina (7 hari)     |        7 | Selasa, 22 September 2026 | Selasa Pahing  | tusaro    | sudah lewat 29 hari |
| Matang puluh (40 hari)   |       40 | Minggu, 25 Oktober 2026   | Minggu Kliwon  | masarma   | 4 hari lagi         |
| Nyatus (100 hari)        |      100 | Kamis, 24 Desember 2026   | Kamis Kliwon   | rosarma   | 64 hari lagi        |
| Mendhak pisan (1 tahun)  |      354 | Sabtu, 4 September 2027   | Sabtu Wage     | patsarpat | 318 hari lagi       |
| Mendhak pindho (2 tahun) |      708 | Rabu, 23 Agustus 2028     | Rabu Pon       | jisarlu   | 672 hari lagi       |
| Nyewu (1.000 hari)       |    1.000 | Senin, 11 Juni 2029       | Senin Kliwon   | nemsarma  | 964 hari lagi       |
+--------------------------+----------+---------------------------+----------------+-----------+---------------------+
Catatan: banyak keluarga menggelar acara pada malam sebelumnya (setelah
maghrib), misalnya acara hari Sabtu digelar Jumat malam (malam Sabtu),
karena dalam hitungan Jawa hari baru dimulai saat matahari terbenam.
Hasil ini panduan; konfirmasikan dengan sesepuh atau tokoh adat setempat.
```

### Contoh 3: mode interaktif

```text
$ python3 selamatan.py
=== Kalkulator Selamatan Orang Meninggal (Adat Jawa) ===
Hari wafat dihitung sebagai hari ke-1. Ketik Ctrl+C untuk keluar.

Tanggal wafat (DD-MM-YYYY): 15-09-2026
Nama almarhum/almarhumah (boleh dikosongkan):
Apakah wafat setelah maghrib? (y/T): y

Tanggal wafat       : Selasa, 15 September 2026 (Selasa Kliwon)
Waktu wafat         : setelah maghrib -> hitungan Jawa sudah masuk hari berikutnya
Hari ke-1 hitungan  : Rabu, 16 September 2026 (Rabu Legi)
...
```

Opsi lain: `--nama "..."` menambahkan nama almarhum di judul laporan, dan `--help` menampilkan bantuan. Format tanggal yang diterima adalah `DD-MM-YYYY`, `DD/MM/YYYY`, `DD.MM.YYYY`, dan `YYYY-MM-DD`. Jika tanggal tidak valid, misalnya 31 Februari, program menampilkan pesan error dan keluar dengan kode 2.

## Cara Menghitung Selamatan Orang Meninggal Adat Jawa

### Prinsip dasar: hari wafat adalah hari ke-1

Kunci seluruh hitungan adalah satu aturan: **hari wafat (geblag) dihitung sebagai hari pertama**. Karena itu hari ke-40 bukan "tanggal wafat + 40 hari", melainkan "tanggal wafat + 39 hari". Artikel detikJateng tentang hitungan 1.000 hari memakai cara yang sama, yakni menambahkan 999 hari dari hari wafat.

Kalender Jawa memiliki dua siklus yang berjalan bersamaan. Ada siklus tujuh hari (Senin sampai Minggu) dan siklus lima pasaran (Legi, Pahing, Pon, Wage, Kliwon). Kombinasi keduanya disebut weton dan berulang setiap 35 hari. Rumus mnemonik orang Jawa sebenarnya adalah cara cepat membaca posisi hari dan pasaran tanpa menghitung puluhan hari satu per satu.

### Rumus mudah menghitung selamatan orang meninggal

Setiap rumus terdiri atas dua bagian: urutan **dina** (hari) dan urutan **pasaran**. Keduanya dihitung dari hari dan pasaran wafat sebagai urutan pertama.

| Acara | Hari ke- | Rumus | Arti rumus | Tambah hari dari tanggal wafat |
|---|---|---|---|---|
| Nelung dina | 3 | lusarlu | dina katelu, pasaran katelu | +2 |
| Mitung dina | 7 | tusaro | dina kapitu, pasaran kaloro | +6 |
| Matang puluh | 40 | masarma | dina kalima, pasaran kalima | +39 |
| Nyatus | 100 | rosarma | dina kaloro, pasaran kalima | +99 |
| Mendhak pisan | 354 | patsarpat | dina kapat, pasaran kapat | +353 |
| Mendhak pindho | 708 | jisarlu | dina kasiji, pasaran katelu | +707 |
| Nyewu | 1.000 | nemsarma | dina kanem, pasaran kalima | +999 |

Rumus nelung dina, mitung dina, matang puluh, nyatus, dan nyewu muncul dengan nama yang sama di beberapa media (lihat bagian sumber). Untuk mendhak pindho, aturannya (hari pertama, pasaran ketiga, 708 hari) tercatat di Kapanlagi, tetapi namanya ditulis berbeda di sana. Di tool ini kami menyingkatnya "jisarlu" (siji–pasaran–telu) mengikuti pola penamaan rumus lain.

Mengapa rumus dan selisih hari selalu cocok? Ambil matang puluh. Selisih 39 hari sama dengan 5 minggu lebih 4 hari, jadi harinya maju 4 langkah, yaitu hari kelima jika hari wafat dihitung pertama. Selisih 39 juga sama dengan 7 putaran pasaran lebih 4, sehingga pasarannya ikut maju 4 langkah ke pasaran kelima. Itulah masarma. Unit test di repo ini memeriksa kecocokan tersebut untuk ke-35 kemungkinan weton wafat.

### Contoh hitung manual lengkap

Kita pakai data Contoh 1: wafat Selasa Kliwon, 15 September 2026, siang hari.

1. **Urutan hari** dimulai dari Selasa: Selasa (1), Rabu (2), Kamis (3), Jumat (4), Sabtu (5), Minggu (6), Senin (7).
2. **Urutan pasaran** dimulai dari Kliwon: Kliwon (1), Legi (2), Pahing (3), Pon (4), Wage (5).
3. **Nelung dina, lusarlu:** hari ke-3 adalah Kamis, pasaran ke-3 adalah Pahing. Hasilnya Kamis Pahing, 17 September 2026.
4. **Mitung dina, tusaro:** hari ke-7 adalah Senin, pasaran ke-2 adalah Legi. Hasilnya Senin Legi, 21 September 2026.
5. **Matang puluh, masarma:** hari ke-5 adalah Sabtu, pasaran ke-5 adalah Wage. Cari Sabtu Wage di sekitar 40 hari: 15 September ditambah 39 hari jatuh pada 24 Oktober 2026. Rinciannya, 15 hari tersisa di September lalu 24 hari di Oktober.
6. **Nyatus, rosarma:** hari ke-2 adalah Rabu, pasaran ke-5 adalah Wage. Tambah 99 hari: 15 (September) + 31 (Oktober) + 30 (November) + 23 (Desember) = 99, jadi Rabu Wage, 23 Desember 2026.
7. **Mendhak pisan, patsarpat:** hari ke-4 adalah Jumat, pasaran ke-4 adalah Pon. Tambah 353 hari, hasilnya Jumat Pon, 3 September 2027.
8. **Mendhak pindho, jisarlu:** hari ke-1 adalah Selasa, pasaran ke-3 adalah Pahing. Tambah 707 hari, hasilnya Selasa Pahing, 22 Agustus 2028.
9. **Nyewu, nemsarma:** hari ke-6 adalah Minggu, pasaran ke-5 adalah Wage. Tambah 999 hari, hasilnya Minggu Wage, 10 Juni 2029.

Semua hasil manual ini sama persis dengan output program di Contoh 1.

### Cara hitung 40 hari dan menghitung 100 hari orang meninggal

Untuk 40 hari, tambahkan 39 hari ke tanggal wafat. Untuk 100 hari, tambahkan 99 hari. Jika hasilnya tidak cocok dengan rumus masarma atau rosarma, biasanya hari wafat keliru dihitung sebagai hari ke-0.

### Kalkulator 1000 hari orang meninggal

Nyewu dihitung dengan menambahkan 999 hari. Karena 999 = 28 × 35 + 19, weton nyewu sama dengan weton wafat yang dimajukan 19 langkah. Contoh di detikJateng: wafat Jumat Kliwon, maka nyewu jatuh pada Rabu Wage. Program ini memberi hasil yang sama, dan kasus tersebut ikut diuji.

## Wafat Setelah Maghrib

Dalam kalender Jawa, pergantian hari terjadi saat matahari terbenam, sama seperti kalender Hijriah. Hal ini disebut dalam artikel Wikipedia *Javanese calendar* yang merujuk buku Eric Oey, *Java* (2001). detikJateng juga menyebutnya dengan mengutip book chapter *Astronomi Islam* karya Arwin Juli Rakhmadi Butar-Butar dan kawan-kawan.

Akibatnya, orang yang wafat hari Selasa pukul 19.00 dianggap wafat pada "malam Rabu", yaitu hari Rabu menurut hitungan Jawa. Artikel detikJateng tentang 1.000 hari menyatakan hal serupa: wafat setelah matahari terbenam sudah masuk hari selanjutnya. Opsi `--setelah-maghrib` menggeser hari ke-1 ke tanggal berikutnya, sehingga semua acara ikut bergeser satu hari.

Bagaimana jika wafat menjelang maghrib dan waktunya tidak pasti? Tanyakan kepada keluarga atau tokoh setempat, karena patokan yang dipakai bisa berbeda, misalnya azan maghrib di masjid terdekat.

## Tabel Referensi Cepat

Karena hari dan pasaran bergerak terpisah, tabel ini dibagi dua. Cari hari wafat di tabel pertama dan pasaran wafat di tabel kedua, lalu gabungkan hasilnya.

**Hari acara berdasarkan hari wafat**

| Hari wafat | Nelung dina | Mitung dina | Matang puluh | Nyatus | Mendhak pisan | Mendhak pindho | Nyewu |
|---|---|---|---|---|---|---|---|
| Senin | Rabu | Minggu | Jumat | Selasa | Kamis | Senin | Sabtu |
| Selasa | Kamis | Senin | Sabtu | Rabu | Jumat | Selasa | Minggu |
| Rabu | Jumat | Selasa | Minggu | Kamis | Sabtu | Rabu | Senin |
| Kamis | Sabtu | Rabu | Senin | Jumat | Minggu | Kamis | Selasa |
| Jumat | Minggu | Kamis | Selasa | Sabtu | Senin | Jumat | Rabu |
| Sabtu | Senin | Jumat | Rabu | Minggu | Selasa | Sabtu | Kamis |
| Minggu | Selasa | Sabtu | Kamis | Senin | Rabu | Minggu | Jumat |

**Pasaran acara berdasarkan pasaran wafat**

| Pasaran wafat | Nelung dina | Mitung dina | Matang puluh | Nyatus | Mendhak pisan | Mendhak pindho | Nyewu |
|---|---|---|---|---|---|---|---|
| Legi | Pon | Pahing | Kliwon | Kliwon | Wage | Pon | Kliwon |
| Pahing | Wage | Pon | Legi | Legi | Kliwon | Wage | Legi |
| Pon | Kliwon | Wage | Pahing | Pahing | Legi | Kliwon | Pahing |
| Wage | Legi | Kliwon | Pon | Pon | Pahing | Legi | Pon |
| Kliwon | Pahing | Legi | Wage | Wage | Pon | Pahing | Wage |

Contoh: wafat Senin Pon. Nyatus jatuh pada hari Selasa (tabel pertama) dengan pasaran Pahing (tabel kedua), jadi Selasa Pahing.

## Perbedaan Praktik Antardaerah

Hitungan di atas adalah aturan mnemonik yang paling sering dikutip. Meski begitu, praktik di lapangan tidak seragam, dan perbedaan berikut perlu Anda ketahui:

- **Mendhak dengan kalender Jawa.** Sebagian keluarga menggelar mendhak pada tanggal dan bulan Jawa yang sama setahun kemudian. Satu tahun Jawa berisi 354 atau 355 hari, sehingga hasilnya bisa selisih satu hari dari rumus patsarpat (hari ke-354). Untuk mendhak pindho, Mamikos dan Kapanlagi menyebut angka 708 hari.
- **Nyewu dengan hitungan bulan.** Ada yang mencari nyewu dengan menghitung bulan Jawa (sekitar 34 sampai 35 bulan setelah bulan wafat), lalu mencari hari yang cocok dengan rumus nemsarma.
- **Malam atau siang.** Banyak keluarga menggelar tahlilan pada malam sebelum tanggal hasil hitungan, karena malam itu sudah termasuk hari acara menurut hitungan Jawa. Contoh di Kapanlagi: untuk wafat Sabtu Pahing, mitung dina ditulis jatuh pada "Kamis malam Jumat", padahal hari ketujuh menurut rumus adalah Jumat. Ada juga yang menggelarnya siang hari pada tanggalnya.
- **Nama dan ejaan.** Nama acara dan rumus bisa berbeda antardaerah, misalnya mendhak, mendak, atau pendhak. Pasaran Pahing juga sering ditulis Paing.
- **Pandangan keagamaan.** Buya Yahya, seperti dikutip detikHikmah, menjelaskan bahwa doa dan sedekah untuk orang yang wafat adalah kebaikan. Penentuan hari-hari tertentu merupakan adat, dan sedekah tidak harus menunggu hari ketujuh atau keempat puluh. Kalangan lain memiliki pandangan berbeda. Kami menghormati semua pilihan tersebut.

Jika hasil kalkulator berbeda dengan hitungan sesepuh di kampung Anda, ikutilah kesepakatan keluarga dan tokoh setempat.

## Tips dan Kesalahan Umum

- **Menghitung hari wafat sebagai hari ke-0.** Ini kesalahan paling sering. Akibatnya semua acara mundur satu hari dan pasarannya tidak cocok dengan rumus.
- **Lupa waktu wafat.** Catat jam wafat. Jika setelah maghrib, gunakan `--setelah-maghrib`.
- **Mengira mendhak pisan sama dengan ulang tahun Masehi.** Mendhak memakai tahun Jawa (sekitar 354 hari), sehingga jatuh 12 hari lebih awal dari tanggal wafat di tahun Masehi berikutnya, atau 13 hari bila melewati 29 Februari.
- **Salah urutan pasaran.** Urutannya Legi, Pahing, Pon, Wage, Kliwon, lalu kembali ke Legi.
- **Tidak mengecek tahun kabisat.** Menghitung manual melewati Februari mudah meleset. Program memakai modul `datetime` Python yang sudah menangani tahun kabisat.
- **Mencetak hasil untuk undangan.** Tuliskan hari, pasaran, dan tanggal Masehi sekaligus, misalnya "Jumat Pon, 3 September 2027", agar tamu tidak bingung.

## FAQ

### Bagaimana cara menghitung selamatan orang meninggal adat Jawa dengan cepat?

Tambahkan 2, 6, 39, 99, 353, 707, dan 999 hari ke tanggal wafat untuk acara 3, 7, 40, 100 hari, mendhak pisan, mendhak pindho, dan 1.000 hari. Lalu cocokkan hari dan pasarannya dengan rumus lusarlu, tusaro, masarma, rosarma, patsarpat, jisarlu, dan nemsarma.

### Apakah ada aplikasi menghitung 1000 hari orang meninggal yang gratis?

Ada. Repo ini adalah kalkulator 1000 hari orang meninggal yang gratis dan open source. Programnya berjalan di komputer Anda sendiri tanpa internet dan tanpa iklan.

### Cara hitung 40 hari orang meninggal, apakah dari hari setelah wafat?

Bukan. Hari wafat dihitung sebagai hari pertama, sehingga hari ke-40 adalah tanggal wafat ditambah 39 hari. Rumus masarma (hari kelima, pasaran kelima) bisa dipakai untuk mengecek hasilnya.

### Bagaimana menghitung 100 hari orang meninggal?

Tambahkan 99 hari ke tanggal wafat. Hari jatuhnya selalu satu hari setelah hari wafat (Senin menjadi Selasa), dan pasarannya adalah pasaran kelima. Ini sesuai rumus rosarma.

### Apakah hitungan orang meninggal online ini sama dengan hitungan primbon?

Rumus yang dipakai adalah rumus mnemonik yang dikutip berbagai sumber tentang tradisi Jawa. Hasilnya bisa berbeda satu hari dengan hitungan yang memakai tanggal kalender Jawa, terutama untuk mendhak. Lihat bagian perbedaan praktik.

### Wafat setelah maghrib, hitungannya mulai kapan?

Mulai tanggal berikutnya, karena hari Jawa berganti saat matahari terbenam. Gunakan opsi `--setelah-maghrib` atau jawab "y" di mode interaktif.

### Apakah ini kalkulator kematian yang meramal umur?

Bukan. Istilah "kalkulator kematian" di sini hanya berarti alat hitung tanggal peringatan setelah seseorang wafat. Program ini tidak meramal apa pun.

### Bisakah dipakai untuk tanggal wafat puluhan tahun lalu?

Bisa. Program menghitung pasaran dengan selisih hari dari tanggal acuan, sehingga tanggal lama maupun tanggal yang akan datang tetap dihitung dengan benar, selama hasilnya tidak melewati tahun 9999.

## Metodologi, Pengujian, dan Sumber

**Cara program menghitung pasaran.** Pasaran ditentukan dari selisih hari terhadap tanggal acuan 17 Agustus 1945, yang merupakan Jumat Legi, lalu diambil sisa bagi 5. Acuan ini konsisten dengan awal kalender Jawa Sultan Agung, 1 Sura 1555 tahun Alip, yang jatuh pada Jumat Legi 8 Juli 1633. Selisih antara kedua tanggal habis dibagi 35, sehingga keduanya sama-sama Jumat Legi.

**Pengujian.** Repo ini memiliki 18 unit test yang semuanya lulus (`python3 -m unittest discover -s tests -v`). Beberapa di antaranya:

- Weton 17 Agustus 1945 dan 8 Juli 1633 harus Jumat Legi.
- Untuk ke-35 kemungkinan weton wafat, setiap acara harus jatuh pada urutan hari dan pasaran sesuai rumusnya.
- Contoh Akurat.co: wafat Senin Pon, 6 Februari 2023, menghasilkan Rabu Kliwon 8 Februari, Minggu Wage 12 Februari, Jumat Pahing 17 Maret, Selasa Pahing 16 Mei, dan nyewu 1 November 2025. Semua cocok, kecuali artikel menyebut nyewu "Rabu Legi", padahal 1 November 2025 adalah Sabtu Pahing.
- Contoh detikJateng (Jumat Kliwon, nyewu Rabu Wage), Mamikos (Jumat Kliwon, mitung dina Kamis Legi), dan Popbela (wafat 1 Januari 2025, 1.000 hari pada 27 September 2027).
- Pasaran 1, 3, dan 30 November 2025 dicocokkan dengan daftar weton detikJateng.
- Edge case: tahun kabisat (wafat 29 Februari 2024), opsi setelah maghrib, format tanggal salah, dan tanggal yang melewati tahun 9999.

**Sumber rujukan:**

- Geertz, Clifford. *The Religion of Java*. The Free Press, 1960, hlm. 58–72, sebagaimana dirangkum di [Wikipedia: Slametan](https://en.wikipedia.org/wiki/Slametan).
- [Wikipedia: Javanese calendar](https://en.wikipedia.org/wiki/Javanese_calendar), tentang Sultan Agung (1633) dan pergantian hari saat matahari terbenam (merujuk Oey, *Java*, 2001).
- [Wikipedia: 1633](https://en.wikipedia.org/wiki/1633), entri 8 Juli: epoch kalender Jawa 1 Sura 1555 = 1 Muharram 1043 H.
- Ulvia Nur Azizah, "[Cara Menghitung 1000 Hari Orang Meninggal Menurut Jawa dan Tradisinya](https://www.detik.com/jateng/budaya/d-8041779/cara-menghitung-1000-hari-orang-meninggal-menurut-jawa-dan-tradisinya)", detikJateng, 2 Agustus 2025.
- Kholida Qothrunnada, "[Cara Menghitung 1000 Hari Orang Meninggal dan Pendapat Ulama tentang Hal Ini](https://www.detik.com/hikmah/khazanah/d-7345752/cara-menghitung-1000-hari-orang-meninggal-dan-pendapat-ulama-tentang-hal-ini)", detikHikmah, 17 Mei 2024 (rumus nemsarma dari buku *Tradisi Cinandi di Banyuwangi* karya Poniman, serta pendapat Buya Yahya).
- Nur Umar Akashi, "[Hari Ini Malam Jumat Apa? Cek Weton Kalender Jawa Besok 24 Oktober 2025](https://www.detik.com/jateng/budaya/d-8174891/hari-ini-malam-jumat-apa-cek-weton-kalender-jawa-besok-24-oktober-2025)", detikJateng, 23 Oktober 2025.
- Sultan Tanjung, "[Inilah Cara Menghitung Selamatan dengan Tabel Hitungan Orang Meninggal](https://akurat.co/rahmah/787520/inilah-cara-menghitung-selamatan-dengan-tabel-hitungan-orang-meninggal-7-hari-hingga-1000-beserta-contohnya-dengan-akurat)", Akurat.co, 7 April 2025.
- Rizka Uzlifat, "[Cara Menghitung Selamatan Orang Meninggal dalam Tradisi Jawa](https://www.kapanlagi.com/feeds/cara-menghitung-selamatan-orang-meninggal-dalam-tradisi-jawa-1670a1534c.html)", Kapanlagi.com, 8 Februari 2026.
- Lailla, "[Cara Menghitung Selamatan Orang Meninggal](https://mamikos.com/info/cara-menghitung-selamatan-orang-meninggal-gnr/)", Mamikos, 9 Januari 2025.
- Nafi Khoiriyah, "[Cara Menghitung 1000 Hari Orang Meninggal untuk Selamatan](https://www.popbela.com/career/inspiration/cara-menghitung-1000-hari-orang-meninggal-00-m97rq-29dvjw)", Popbela, 31 Januari 2025.
- "[Di Tangan Walisongo, Angka-angka dalam Kalender Islam Jadi Hidup](https://nu.or.id/nasional/di-tangan-walisongo-angka-angka-dalam-kalender-islam-jadi-hidup-Z4lFs)", NU Online, 20 April 2015 (wawancara Agus Sunyoto: 40 hari disebut "dino limo pasaran limo").
- Anindya Milagsita, "[Daftar Weton Bulan November 2025 Lengkap](https://www.detik.com/jateng/budaya/d-8195804/daftar-weton-bulan-november-2025-lengkap-kalender-jawa-dan-jumlah-neptunya)", detikJateng, 5 November 2025.
- Rizky Kusumo, "[Makna Weton hingga Kisah Mistik Soekarno Pilih Proklamasi pada 17 Agustus](https://www.goodnewsfromindonesia.id/2021/08/17/makna-weton-hingga-kisah-mistik-soekarno-pilih-proklamasi-pada-17-agustus)", GNFI, 17 Agustus 2021 (kutipan "Hari Jumat ini Jumat Legi").

Sebagian besar rujukan rumus berasal dari media populer, bukan naskah primbon asli. Karena itu kami memverifikasi setiap contoh secara aritmetika dan mencatat contoh yang tidak konsisten, alih-alih menyalinnya begitu saja.

## Tentang Pembuat

Proyek ini adalah karya [JoinBareng](https://joinbareng.com) dan dikelola oleh [@redyopa2929](https://github.com/redyopa2929). JoinBareng adalah platform patungan langganan premium (Netflix, Spotify, YouTube Premium, ChatGPT, dll.) plus marketplace akun digital yang aman dan transparan. Seri tools ini dibuat untuk membantu kebutuhan hitung sehari-hari masyarakat Indonesia dengan kode yang terbuka dan bisa diperiksa siapa saja.

## Disclaimer

Hasil kalkulator selamatan orang meninggal ini adalah panduan, bukan ketetapan adat atau fatwa agama. Tradisi selamatan berbeda di setiap daerah, keluarga, dan komunitas. Selalu konfirmasikan tanggal acara dengan sesepuh, tokoh adat, atau tokoh agama setempat. Pembuat tidak bertanggung jawab atas keputusan yang diambil berdasarkan hasil program ini.

## Kontribusi

Menemukan perbedaan hitungan di daerah Anda, salah ketik, atau bug? Silakan buka laporan di [halaman Issues](https://github.com/redyopa2929/kalkulator-selamatan/issues). Pull request juga sangat diterima, terutama yang menambah test dengan sumber rujukan yang jelas. Jalankan `python3 -m unittest discover -s tests -v` sebelum mengirim perubahan.

## Lisensi

Dirilis dengan [Lisensi MIT](LICENSE). Anda bebas memakai, mengubah, dan membagikan kode ini dengan tetap mencantumkan pemberitahuan hak cipta.

## Dukung Proyek Ini

Jika kalkulator selamatan orang meninggal ini membantu keluarga Anda, beri ⭐ star pada repo ini agar lebih mudah ditemukan orang lain yang membutuhkan. Ingin hemat biaya langganan aplikasi premium untuk keluarga? Coba patungan di [JoinBareng](https://joinbareng.com).

## Tools Lainnya dari Seri Ini

- [Kalkulator Jadian](https://github.com/redyopa2929/kalkulator-jadian) — hitung lama hari jadian & anniversary
- [Kalkulator Jasmani Polri](https://github.com/redyopa2929/kalkulator-jasmani-polri) — hitung nilai kesamaptaan jasmani
- [Hitung WR ML](https://github.com/redyopa2929/hitung-wr-ml) — hitung win rate Mobile Legends
- [Tasbih Online](https://github.com/redyopa2929/tasbih-online) — tasbih digital penghitung dzikir
- [Terbilang Online](https://github.com/redyopa2929/terbilang-online) — ubah angka ke huruf / terbilang rupiah
- [Kalkulator Saham](https://github.com/redyopa2929/kalkulator-saham) — average down, compounding, ARA/ARB
- [Kalkulator Bangunan](https://github.com/redyopa2929/kalkulator-bangunan) — keramik, hebel, kubikasi, besi
- [Konversi Koordinat](https://github.com/redyopa2929/konversi-koordinat) — DMS, desimal, UTM
- [Cek Weton](https://github.com/redyopa2929/cek-weton) — cek weton & neptu dari tanggal lahir

---

Terakhir diperbarui: 21 Oktober 2026
