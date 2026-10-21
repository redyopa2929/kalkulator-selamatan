"""Unit test kalkulator selamatan. Jalankan: python3 -m unittest discover -s tests -v"""

import contextlib
import io
import os
import sys
import unittest
from datetime import date, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import selamatan as s  # noqa: E402


def cari_tanggal(hari: str, pasaran: str, mulai: date) -> date:
    """Tanggal pertama >= mulai dengan weton tertentu (helper test)."""
    d = mulai
    while s.weton(d) != f"{hari} {pasaran}":
        d += timedelta(days=1)
    return d


class TestPasaran(unittest.TestCase):
    def test_acuan_proklamasi_jumat_legi(self):
        self.assertEqual(s.weton(date(1945, 8, 17)), "Jumat Legi")

    def test_epoch_sultan_agung_jumat_legi(self):
        # 1 Sura 1555 Alip = Jumat Legi, 8 Juli 1633
        self.assertEqual(s.weton(date(1633, 7, 8)), "Jumat Legi")

    def test_siklus_pasaran_berurutan(self):
        mulai = date(1945, 8, 17)
        urut = [s.pasaran(mulai + timedelta(days=i)) for i in range(6)]
        self.assertEqual(urut, ["Legi", "Pahing", "Pon", "Wage", "Kliwon", "Legi"])

    def test_referensi_detik_november_2025(self):
        # detikJateng, 5 Nov 2025: daftar weton November 2025
        self.assertEqual(s.weton(date(2025, 11, 1)), "Sabtu Pahing")
        self.assertEqual(s.weton(date(2025, 11, 3)), "Senin Wage")
        self.assertEqual(s.weton(date(2025, 11, 30)), "Minggu Legi")


class TestRumusMnemonik(unittest.TestCase):
    def test_offset_cocok_dengan_rumus_untuk_35_kombinasi_weton(self):
        # Rumus (lusarlu, tusaro, dst.) harus berlaku untuk semua 35 weton wafat.
        for i in range(35):
            geblag = date(2026, 1, 1) + timedelta(days=i)
            for h in s.hitung_selamatan(geblag):
                with self.subTest(geblag=geblag, acara=h.acara.nama_jawa):
                    self.assertEqual(s.posisi_dina(geblag, h.tanggal), h.acara.dina_ke)
                    self.assertEqual(s.posisi_pasaran(geblag, h.tanggal), h.acara.pasaran_ke)

    def test_hari_ke_dan_offset(self):
        harapan = {
            "Geblag": 0, "Nelung dina": 2, "Mitung dina": 6,
            "Matang puluh": 39, "Nyatus": 99, "Mendhak pisan": 353,
            "Mendhak pindho": 707, "Nyewu": 999,
        }
        hasil = {a.nama_jawa: a.offset for a in s.DAFTAR_ACARA}
        self.assertEqual(hasil, harapan)


class TestContohSumber(unittest.TestCase):
    def test_contoh_akurat_senin_pon_6_februari_2023(self):
        hasil = {h.acara.hari_ke: h for h in s.hitung_selamatan(date(2023, 2, 6))}
        self.assertEqual(hasil[1].weton, "Senin Pon")
        self.assertEqual((hasil[3].tanggal, hasil[3].weton), (date(2023, 2, 8), "Rabu Kliwon"))
        self.assertEqual((hasil[7].tanggal, hasil[7].weton), (date(2023, 2, 12), "Minggu Wage"))
        self.assertEqual((hasil[40].tanggal, hasil[40].weton), (date(2023, 3, 17), "Jumat Pahing"))
        self.assertEqual((hasil[100].tanggal, hasil[100].weton), (date(2023, 5, 16), "Selasa Pahing"))
        self.assertEqual(hasil[1000].tanggal, date(2025, 11, 1))

    def test_contoh_detik_jumat_kliwon_nyewu_rabu_wage(self):
        geblag = cari_tanggal("Jumat", "Kliwon", date(2024, 1, 1))
        nyewu = s.hitung_selamatan(geblag)[-1]
        self.assertEqual(nyewu.weton, "Rabu Wage")

    def test_contoh_mamikos_jumat_kliwon_mitung_dina_kamis_legi(self):
        geblag = cari_tanggal("Jumat", "Kliwon", date(2024, 1, 1))
        mitung = s.hitung_selamatan(geblag)[2]
        self.assertEqual(mitung.weton, "Kamis Legi")

    def test_contoh_popbela_1_januari_2025_nyewu(self):
        self.assertEqual(s.hitung_selamatan(date(2025, 1, 1))[-1].tanggal, date(2027, 9, 27))


class TestEdgeCase(unittest.TestCase):
    def test_setelah_maghrib_menggeser_satu_hari(self):
        biasa = s.hitung_selamatan(date(2026, 10, 21))
        maghrib = s.hitung_selamatan(date(2026, 10, 21), setelah_maghrib=True)
        for a, b in zip(biasa, maghrib):
            self.assertEqual(b.tanggal - a.tanggal, timedelta(days=1))
        self.assertEqual(maghrib[0].tanggal, date(2026, 10, 22))

    def test_tahun_kabisat_29_februari(self):
        hasil = s.hitung_selamatan(date(2024, 2, 29))
        self.assertEqual(hasil[3].tanggal, date(2024, 4, 8))   # 40 hari
        self.assertEqual(hasil[-1].tanggal, date(2026, 11, 24))  # 1.000 hari

    def test_format_tanggal_dan_ribuan(self):
        self.assertEqual(s.format_tanggal(date(1945, 8, 17)), "Jumat, 17 Agustus 1945")
        self.assertEqual(s.format_ribuan(1000), "1.000")
        self.assertEqual(s.format_ribuan(1234567), "1.234.567")

    def test_keterangan_selisih(self):
        hari_ini = date(2026, 10, 21)
        self.assertEqual(s.keterangan_selisih(hari_ini, hari_ini), "hari ini")
        self.assertEqual(s.keterangan_selisih(date(2026, 10, 22), hari_ini), "besok")
        self.assertEqual(s.keterangan_selisih(date(2029, 7, 17), hari_ini), "1.000 hari lagi")
        self.assertEqual(s.keterangan_selisih(date(2026, 10, 11), hari_ini), "sudah lewat 10 hari")

    def test_parse_tanggal(self):
        self.assertEqual(s.parse_tanggal("17-08-1945"), date(1945, 8, 17))
        self.assertEqual(s.parse_tanggal("17/08/1945"), date(1945, 8, 17))
        self.assertEqual(s.parse_tanggal("1945-08-17"), date(1945, 8, 17))
        for salah in ("31-02-2025", "kemarin", "", "2025/13/01"):
            with self.subTest(salah=salah), self.assertRaises(ValueError):
                s.parse_tanggal(salah)


class TestCLI(unittest.TestCase):
    def jalankan(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            kode = s.main(list(argv))
        return kode, out.getvalue(), err.getvalue()

    def test_cli_sukses(self):
        kode, out, _ = self.jalankan("06-02-2023", "--pembanding", "21-10-2026")
        self.assertEqual(kode, 0)
        self.assertIn("Rabu, 8 Februari 2023", out)
        self.assertIn("Nyewu (1.000 hari)", out)

    def test_cli_tanggal_salah_exit_tidak_nol(self):
        kode, _, err = self.jalankan("32-13-2025")
        self.assertNotEqual(kode, 0)
        self.assertIn("tidak dikenali", err)

    def test_cli_overflow_tahun_9999(self):
        kode, _, err = self.jalankan("01-01-9999")
        self.assertNotEqual(kode, 0)
        self.assertIn("9999", err)


if __name__ == "__main__":
    unittest.main()
