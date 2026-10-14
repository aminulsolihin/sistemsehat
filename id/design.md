---
title: Bagaimana merancang alat yang tepat? Panduan desain | SistemSehat
description: >-
  Tujuh prinsip dengan contoh untuk mengubah konsep menjadi alat kesehatan yang aman dan mudah dipakai: risiko, kegunaan, uji, dan produksi.
lang: id
layout: guide
pillar: build
reviewed: 14 Oktober 2026
order: 7
number: "D"
label: Desain
question: Bagaimana merancang alat yang tepat?
summary: >-
  Gagasan yang baik tetap gagal jika alatnya tidak aman, sulit dipakai, atau tidak dapat diproduksi.
  Tujuh prinsip untuk mengubah konsep terpilih menjadi alat.
icon: pencil
lead: >-
  Setelah Anda punya kebutuhan dan konsep ([Panduan C](identify.html)), tugas berikutnya adalah
  membuat alat yang aman, mudah dipakai, dan dapat diproduksi, lalu membuktikannya. Prinsip ini
  berlaku baik Anda bekerja di universitas, rumah sakit, maupun perusahaan.

rules:
  - number: "D.1"
    heading: Rancang untuk tempat alat akan dipakai
    explanation: >-
      Cari tahu pasokan listrik, panas, kelembapan, dan debu di tempat alat akan bekerja,
      serta siapa yang akan memakai, membersihkan, dan memperbaikinya. Pembeli memeriksa
      hal yang sama saat menulis spesifikasi ([prinsip 1.5](specification.html#rule-1-5)).
      Alat yang membutuhkan apa yang tidak dimiliki fasilitas tidak akan dibeli, atau
      tidak akan dipakai.
    example: >-
      Jika puskesmas sering mati listrik, rancang alat agar bisa berjalan dengan baterai,
      dan pakai komponen yang dapat dibeli dan diganti sendiri oleh teknisi kabupaten.
    ask: >-
      Apakah alat Anda tetap berfungsi di fasilitas yang perlengkapannya paling terbatas
      yang ingin Anda layani?
  - number: "D.2"
    heading: Kelola risiko sejak sketsa pertama
    explanation: >-
      Daftar apa saja yang dapat mencederai pasien atau pengguna, seberapa mungkin
      terjadi, dan seberapa parah. Lalu hilangkan risikonya lewat desain, tambahkan
      pelindung, atau beri peringatan, dengan urutan itu. ISO 14971 menjelaskan prosesnya,
      dan regulator berharap melihat catatannya.
    example: >-
      Infant warmer bisa membuat bayi kepanasan. Desain: batasi daya pemanas. Pelindung:
      pemutus terpisah yang mati pada suhu tertentu. Peringatan: alarm dan label.
    ask: >-
      Untuk setiap bahaya yang Anda daftar, perubahan desain, pelindung, atau peringatan
      mana yang mengendalikannya?
  - number: "D.3"
    heading: Uji kegunaan dengan orang yang akan memakainya
    explanation: >-
      Banyak masalah alat berupa kesalahan penggunaan: desainnya membuat pengguna yang
      lelah atau sibuk mudah keliru. IEC 62366-1 menjelaskan cara menemukan dan
      menghilangkannya, diakhiri dengan uji atas desain akhir. Biarkan perawat, bidan,
      atau teknisi memakainya dalam kondisi yang mendekati nyata, dan amati tanpa
      membantu.
    example: >-
      Minta tiga bidan mengatur suhu dengan tangan bersarung, di ruangan redup, tanpa buku
      petunjuk. Catat setiap keraguan dan setiap tombol yang salah ditekan.
    ask: >-
      Kesalahan penggunaan apa yang Anda lihat saat pengujian, dan apa yang Anda ubah
      karenanya?
  - number: "D.4"
    heading: Perlakukan perangkat lunak sebagai bagian dari alat
    explanation: >-
      Perangkat lunak yang mengendalikan alat, atau yang membantu keputusan diagnosis atau
      terapi, biasanya diatur sebagai alat kesehatan. IEC 62304 menjelaskan cara
      mengembangkan dan memeliharanya. Rencanakan pembaruan, keamanan, dan pencatatan
      sejak awal.
    example: >-
      Aplikasi yang menghitung dosis obat dari berat badan anak adalah perangkat lunak
      alat kesehatan, walaupun berjalan di ponsel biasa.
    ask: >-
      Fungsi perangkat lunak Anda yang mana yang dapat mencederai pasien jika hasilnya
      salah?
  - number: "D.5"
    heading: Catat keputusan desain selama bekerja
    explanation: >-
      Simpan berkas desain: persyaratannya, cara setiap persyaratan diperiksa, dan alasan
      setiap keputusan. ISO 13485 menyebutnya pengendalian desain dan pengembangan.
      Menyusun ulang berkas ini belakangan memakan waktu, padahal pendaftaran alat
      ([Panduan E](to-market.html)) bergantung padanya.
    example: >-
      Untuk setiap persyaratan, simpan satu baris: persyaratannya, metode uji, hasilnya,
      tanggal, dan siapa yang memeriksa.
    ask: >-
      Dapatkah orang di luar tim Anda menelusuri setiap persyaratan sampai ke hasil
      ujinya?
  - number: "D.6"
    heading: Verifikasi desainnya, lalu validasi alatnya
    explanation: >-
      Verifikasi menunjukkan bahwa alat dibuat dengan benar: setiap persyaratan terpenuhi,
      dibuktikan dengan uji. Validasi menunjukkan bahwa alat yang dibuat memang tepat:
      memenuhi kebutuhan, dengan pengguna nyata, dalam kondisi yang mendekati nyata.
      Keduanya diperlukan sebelum Anda mengajukan pendaftaran.
    example: >-
      Verifikasi: uji bangku menunjukkan pemanas menjaga suhu yang diatur dalam batas
      toleransinya. Validasi: bidan memakai penghangat dalam simulasi rujukan dengan
      manekin bayi, lalu menilai apakah alat itu memenuhi kebutuhan.
    ask: >-
      Uji mana yang menunjukkan setiap persyaratan terpenuhi, dan uji mana yang
      menunjukkan alat memenuhi kebutuhan?
  - number: "D.7"
    heading: Rancang agar bisa diproduksi dan dipasok
    explanation: >-
      Purwarupa yang bisa dibuat seorang insinyur belum menjadi produk. Pilih komponen dan
      proses yang pasokannya dapat diandalkan, dalam jumlah dan biaya yang diizinkan
      kriteria kebutuhan Anda. Rencanakan siapa yang akan memproduksinya, dan dengan
      sistem mutu apa.
    example: >-
      Ganti rumah pemanas yang dibubut manual dengan cetakan, dan pastikan ada dua pemasok
      untuk setiap komponen penting, sebaiknya di Indonesia.
    ask: >-
      Dapatkah alat dibuat dalam jumlah dan biaya yang Anda perlukan, dari komponen yang
      dapat dibeli dengan andal?

tables:
  stages:
    columns:
      - Tahap
      - Yang harus Anda miliki
      - Tempat mencarinya
    rows:
      - - Menemukan dan memilih kebutuhan
        - Pernyataan kebutuhan dan kriteria kebutuhan yang disepakati dengan para pemberi layanan
        - '[Panduan C](identify.html), prinsip C.1 sampai C.4'
      - - Memilih konsep dan membuat purwarupa
        - Konsep yang disaring dengan kriteria, dan purwarupa yang menjawab pertanyaan Anda
        - '[Panduan C](identify.html), prinsip C.5 sampai C.7'
      - - Merancang
        - Persyaratan, berkas risiko, hasil uji kegunaan, dan berkas desain
        - Prinsip D.1 sampai D.5; ISO 14971, IEC 62366-1, IEC 62304, ISO 13485
      - - Verifikasi dan validasi
        - Laporan uji bangku, keselamatan, dan kegunaan, serta bukti bahwa alat memenuhi kebutuhan
        - Prinsip D.6; IEC 60601-1 dan standar khususnya
      - - Bersiap memproduksi dan menjual
        - Produsen dengan sistem mutu, pemasok, dan dokumen untuk pendaftaran
        - Prinsip D.7; [Panduan E](to-market.html)
---

## Dari gagasan sampai alat

Apa yang perlu dimiliki di setiap tahap. Setiap tahap dibangun di atas tahap sebelumnya, dan kekurangan yang baru ditemukan belakangan paling mahal diperbaiki.

{% include table.html table=page.tables.stages %}

## Sumber

Berikut dokumen publik di balik panduan ini. Standarnya sendiri dijual oleh ISO dan IEC; halaman ringkasannya gratis.

- Paul Yock, Stefanos Zenios, Josh Makower, dan kawan-kawan, *Biodesign: The Process of Innovating Medical Technologies*, edisi ke-2, Cambridge University Press, 2015. Lihat bab 4.5 (concept exploration and testing), 5.2 (R&D strategy), dan 5.5 (quality management).
- [ISO 14971:2019](https://www.iso.org/standard/72704.html), penerapan manajemen risiko pada alat kesehatan.
- [IEC 62366-1:2015](https://www.iso.org/standard/63179.html), penerapan rekayasa kegunaan pada alat kesehatan.
- [IEC 62304:2006](https://www.iso.org/standard/38421.html), proses siklus hidup perangkat lunak alat kesehatan.
- [ISO 13485:2016](https://www.iso.org/standard/59752.html), sistem manajemen mutu alat kesehatan.
- Organisasi Kesehatan Dunia (WHO), [kompendium teknologi kesehatan inovatif untuk tempat dengan sumber daya terbatas, 2024](https://www.who.int/publications/i/item/9789240095212).
