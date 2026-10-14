---
# Kajian alat. Salin file ini ke id/dossiers/NAMA-ALAT.md, dengan nama file yang sama seperti versi
# bahasa Inggris di dossiers/. Ganti setiap kata berhuruf KAPITAL.
# Pertahankan setiap baris tabel spesifikasi; tulis "tidak berlaku" jika suatu bagian tidak relevan.
title: Kajian NAMA ALAT | SistemSehat
description: RINGKASAN SATU KALIMAT TENTANG KAJIAN INI.
lang: id
layout: page
crumb: NAMA ALAT
heading: NAMA ALAT
lead: Satu atau dua kalimat. Apa fungsi alat ini, di mana dipakai, dan untuk siapa kajian ini ditulis.
note: Versi 1.0, terbit TANGGAL. Semua sumber bersifat publik dan tercantum di bagian akhir.
tables:
  glance:
    columns: [Butir, Untuk alat ini]
    rows:
      - [Nama generik dan kode nomenklatur, "NAMA, KODE GMDN ATAU EMDN"]
      - [Tingkat layanan, TEMPAT ALAT INI SEHARUSNYA DIPAKAI]
      - [Kelas risiko di Indonesia, "A, B, C, ATAU D"]
      - [Standar yang berlaku, STANDAR DAN EDISINYA]
  specification:
    columns: [Bagian, Persyaratan, Cara memeriksa]
    rows:
      - ["Nama, kategori, dan kode", TEKS, BUKTI]
      - ["Tujuan penggunaan", TEKS, BUKTI]
      - ["Karakteristik teknis", TEKS, BUKTI]
      - ["Karakteristik fisik", TEKS, BUKTI]
      - ["Kebutuhan utilitas", TEKS, BUKTI]
      - ["Aksesori, bahan habis pakai, dan suku cadang", TEKS, BUKTI]
      - ["Kemasan", TEKS, BUKTI]
      - ["Persyaratan lingkungan", TEKS, BUKTI]
      - ["Pelatihan, pemasangan, dan penggunaan", TEKS, BUKTI]
      - ["Garansi dan pemeliharaan", TEKS, BUKTI]
      - ["Dokumentasi", TEKS, BUKTI]
      - ["Penghapusan", TEKS, BUKTI]
      - ["Keselamatan dan standar", TEKS, BUKTI]
  prices:
    columns: [Sumber, Harga, Tanggal, Yang tercakup]
    rows:
      - ["[NAMA SUMBER](URL)", HARGA DAN MATA UANG, TANGGAL, CAKUPAN]
---

## Sekilas

{% include table.html table=page.tables.glance %}

## 1. Apa yang harus kita minta?

Kebutuhan klinisnya dalam dua atau tiga kalimat. Lalu spesifikasi acuan, mengikuti tiga belas bagian templat WHO. Pertahankan setiap bagian, dan tulis "tidak berlaku" jika suatu bagian tidak relevan.

{% include table.html table=page.tables.specification %}

## 2. Berapa harga yang wajar?

{% include table.html table=page.tables.prices %}

Mengapa harga-harga ini berbeda.

## 3. Bagaimana membelinya tanpa tender gagal?

Cara membagi paket, cara menilai penawaran, dan pertanyaan yang biasa diajukan peserta tentang alat ini.

## Sumber

- [JUDUL DOKUMEN](URL), penerbit, tanggal. Dibaca pada TANGGAL.

## Koreksi

Belum ada.
