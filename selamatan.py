#!/usr/bin/env python3
"""Kalkulator selamatan orang meninggal adat Jawa.

Menghitung tanggal geblag, nelung dina (3 hari), mitung dina (7 hari),
matang puluh (40 hari), nyatus (100 hari), mendhak pisan (1 tahun),
mendhak pindho (2 tahun), dan nyewu (1.000 hari) lengkap dengan hari,
pasaran Jawa, serta sisa hari dibanding hari ini.

Aturan: hari wafat (geblag) dihitung sebagai hari ke-1, sehingga
tanggal acara = tanggal geblag + (hari ke-N - 1). Hanya memakai
standard library Python 3.8+.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import List, Optional, Sequence

HARI = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")  # urutan date.weekday()
PASARAN = ("Legi", "Pahing", "Pon", "Wage", "Kliwon")
BULAN = (
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember",
)

# Tanggal acuan pasaran: 17 Agustus 1945 = Jumat Legi.
# Konsisten dengan epoch kalender Jawa Sultan Agung, 1 Sura 1555 = Jumat Legi 8 Juli 1633.
TANGGAL_ACUAN = date(1945, 8, 17)
INDEKS_PASARAN_ACUAN = 0  # Legi


@dataclass(frozen=True)
class Acara:
    """Satu tahap selamatan beserta rumus mnemoniknya."""

    nama_jawa: str
    nama_indonesia: str
    hari_ke: int        # hari ke-N, hari wafat = hari ke-1
    rumus: str          # nama rumus mnemonik
    dina_ke: int        # posisi hari (1-7) dihitung dari hari wafat = 1
    pasaran_ke: int     # posisi pasaran (1-5) dihitung dari pasaran wafat = 1

    @property
    def offset(self) -> int:
        return self.hari_ke - 1


DAFTAR_ACARA = (
    Acara("Geblag", "hari wafat", 1, "-", 1, 1),
    Acara("Nelung dina", "3 hari", 3, "lusarlu", 3, 3),
    Acara("Mitung dina", "7 hari", 7, "tusaro", 7, 2),
    Acara("Matang puluh", "40 hari", 40, "masarma", 5, 5),
    Acara("Nyatus", "100 hari", 100, "rosarma", 2, 5),
    Acara("Mendhak pisan", "1 tahun", 354, "patsarpat", 4, 4),
    Acara("Mendhak pindho", "2 tahun", 708, "jisarlu", 1, 3),
    Acara("Nyewu", "1.000 hari", 1000, "nemsarma", 6, 5),
)


@dataclass(frozen=True)
class HasilAcara:
    acara: Acara
    tanggal: date

    @property
    def weton(self) -> str:
        return weton(self.tanggal)


# ---------------------------------------------------------------- logika inti

def pasaran(tanggal: date) -> str:
    """Pasaran Jawa (Legi/Pahing/Pon/Wage/Kliwon) untuk tanggal Masehi."""
    selisih = (tanggal - TANGGAL_ACUAN).days
    return PASARAN[(INDEKS_PASARAN_ACUAN + selisih) % 5]


def nama_hari(tanggal: date) -> str:
    return HARI[tanggal.weekday()]


def weton(tanggal: date) -> str:
    """Gabungan hari dan pasaran, misalnya 'Jumat Legi'."""
    return f"{nama_hari(tanggal)} {pasaran(tanggal)}"


def format_ribuan(angka: int) -> str:
    """Format angka dengan titik ribuan ala Indonesia: 1000 -> '1.000'."""
    return f"{angka:,}".replace(",", ".")


def format_tanggal(tanggal: date) -> str:
    """Contoh: 'Jumat, 17 Agustus 1945'."""
    return f"{nama_hari(tanggal)}, {tanggal.day} {BULAN[tanggal.month - 1]} {tanggal.year}"


def posisi_dina(geblag: date, target: date) -> int:
    """Urutan hari (1-7) target, menghitung hari geblag sebagai ke-1."""
    return (target - geblag).days % 7 + 1


def posisi_pasaran(geblag: date, target: date) -> int:
    """Urutan pasaran (1-5) target, menghitung pasaran geblag sebagai ke-1."""
    return (target - geblag).days % 5 + 1


def tanggal_basis(tanggal_wafat: date, setelah_maghrib: bool = False) -> date:
    """Hari ke-1 hitungan. Wafat setelah maghrib = sudah masuk hari Jawa berikutnya."""
    return tanggal_wafat + timedelta(days=1) if setelah_maghrib else tanggal_wafat


def hitung_selamatan(tanggal_wafat: date, setelah_maghrib: bool = False) -> List[HasilAcara]:
    """Daftar seluruh tahap selamatan beserta tanggal Masehinya."""
    basis = tanggal_basis(tanggal_wafat, setelah_maghrib)
    return [HasilAcara(a, basis + timedelta(days=a.offset)) for a in DAFTAR_ACARA]


def keterangan_selisih(target: date, pembanding: date) -> str:
    """'hari ini', 'besok', 'N hari lagi', atau 'sudah lewat N hari'."""
    selisih = (target - pembanding).days
    if selisih == 0:
        return "hari ini"
    if selisih == 1:
        return "besok"
    if selisih > 0:
        return f"{format_ribuan(selisih)} hari lagi"
    return f"sudah lewat {format_ribuan(-selisih)} hari"


def parse_tanggal(teks: str) -> date:
    """Terima DD-MM-YYYY, DD/MM/YYYY, DD.MM.YYYY, atau YYYY-MM-DD."""
    teks = teks.strip()
    for fmt in ("%d-%m-%Y", "%d/%m/%Y", "%d.%m.%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(teks, fmt).date()
        except ValueError:
            continue
    raise ValueError(
        f"Tanggal '{teks}' tidak dikenali. Gunakan format DD-MM-YYYY, contoh 17-08-2025."
    )


# ---------------------------------------------------------------- tampilan

def _tabel(baris: Sequence[Sequence[str]], rata_kanan: Sequence[int] = ()) -> str:
    lebar = [max(len(r[i]) for r in baris) for i in range(len(baris[0]))]
    garis = "+-" + "-+-".join("-" * w for w in lebar) + "-+"
    hasil = [garis]
    for n, r in enumerate(baris):
        sel = [
            r[i].rjust(lebar[i]) if i in rata_kanan else r[i].ljust(lebar[i])
            for i in range(len(r))
        ]
        hasil.append("| " + " | ".join(sel) + " |")
        if n == 0:
            hasil.append(garis)
    hasil.append(garis)
    return "\n".join(hasil)


def render_laporan(
    tanggal_wafat: date,
    setelah_maghrib: bool,
    pembanding: date,
    nama: Optional[str] = None,
) -> str:
    hasil = hitung_selamatan(tanggal_wafat, setelah_maghrib)
    basis = hasil[0].tanggal
    kepala = []
    if nama:
        kepala.append(f"Almarhum/almarhumah : {nama}")
    kepala.append(f"Tanggal wafat       : {format_tanggal(tanggal_wafat)} ({weton(tanggal_wafat)})")
    if setelah_maghrib:
        kepala.append("Waktu wafat         : setelah maghrib -> hitungan Jawa sudah masuk hari berikutnya")
    kepala.append(f"Hari ke-1 hitungan  : {format_tanggal(basis)} ({weton(basis)})")
    kepala.append(f"Dibanding tanggal   : {format_tanggal(pembanding)}")

    baris = [["Acara", "Hari ke-", "Tanggal Masehi", "Hari + pasaran", "Rumus", "Keterangan"]]
    for h in hasil:
        baris.append([
            f"{h.acara.nama_jawa} ({h.acara.nama_indonesia})",
            format_ribuan(h.acara.hari_ke),
            format_tanggal(h.tanggal),
            h.weton,
            h.acara.rumus,
            keterangan_selisih(h.tanggal, pembanding),
        ])
    catatan = (
        "Catatan: banyak keluarga menggelar acara pada malam sebelumnya (setelah\n"
        "maghrib), misalnya acara hari Sabtu digelar Jumat malam (malam Sabtu),\n"
        "karena dalam hitungan Jawa hari baru dimulai saat matahari terbenam.\n"
        "Hasil ini panduan; konfirmasikan dengan sesepuh atau tokoh adat setempat."
    )
    return "\n".join(kepala) + "\n\n" + _tabel(baris, rata_kanan=(1,)) + "\n" + catatan


# ---------------------------------------------------------------- CLI

def _tanya_ya_tidak(pertanyaan: str) -> bool:
    jawab = input(pertanyaan).strip().lower()
    return jawab in ("y", "ya", "iya", "yes")


def mode_interaktif() -> int:
    print("=== Kalkulator Selamatan Orang Meninggal (Adat Jawa) ===")
    print("Hari wafat dihitung sebagai hari ke-1. Ketik Ctrl+C untuk keluar.\n")
    while True:
        teks = input("Tanggal wafat (DD-MM-YYYY): ")
        try:
            tanggal_wafat = parse_tanggal(teks)
            break
        except ValueError as err:
            print(f"  {err}")
    nama = input("Nama almarhum/almarhumah (boleh dikosongkan): ").strip() or None
    maghrib = _tanya_ya_tidak("Apakah wafat setelah maghrib? (y/T): ")
    print()
    print(render_laporan(tanggal_wafat, maghrib, date.today(), nama))
    return 0


def buat_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="selamatan.py",
        description=(
            "Kalkulator selamatan orang meninggal adat Jawa: 3, 7, 40, 100 hari, "
            "mendhak 1 & 2 tahun, dan nyewu (1.000 hari) lengkap dengan pasaran. "
            "Tanpa argumen akan masuk mode interaktif."
        ),
    )
    parser.add_argument("tanggal", help="tanggal wafat, format DD-MM-YYYY (contoh 17-08-2025)")
    parser.add_argument(
        "--setelah-maghrib", action="store_true",
        help="wafat setelah maghrib: hari ke-1 dihitung mulai tanggal berikutnya",
    )
    parser.add_argument(
        "--pembanding", metavar="TANGGAL",
        help="bandingkan dengan tanggal ini, bukan hari ini (format DD-MM-YYYY)",
    )
    parser.add_argument("--nama", help="nama almarhum/almarhumah (opsional, untuk judul)")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    try:
        if not argv:
            return mode_interaktif()
        args = buat_parser().parse_args(argv)
        try:
            tanggal_wafat = parse_tanggal(args.tanggal)
            pembanding = parse_tanggal(args.pembanding) if args.pembanding else date.today()
        except ValueError as err:
            print(f"Error: {err}", file=sys.stderr)
            return 2
        try:
            print(render_laporan(tanggal_wafat, args.setelah_maghrib, pembanding, args.nama))
        except OverflowError:
            print("Error: tanggal terlalu jauh, hasil hitungan melewati tahun 9999.", file=sys.stderr)
            return 2
        return 0
    except (KeyboardInterrupt, EOFError):
        print("\nDibatalkan. Sampai jumpa.")
        return 130


if __name__ == "__main__":
    sys.exit(main())
