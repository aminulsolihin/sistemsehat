---
title: Bagaimana merancang alat yang tepat? Panduan desain | SistemSehat
description: >-
  Tujuh prinsip dengan contoh untuk merancang alat kesehatan dari kebutuhan klinis: profil produk, tempat pemakaian, risiko, kegunaan, dan perangkat lunak.
lang: id
layout: guide
pillar: build
reviewed: 14 Oktober 2026
order: 6
number: "C"
label: Desain
question: Bagaimana merancang alat yang tepat?
summary: >-
  Banyak alat gagal karena memecahkan masalah yang keliru, atau mengabaikan tempat alat itu akan
  dipakai. Tujuh prinsip untuk merancang alat dari kebutuhan klinis.
icon: bulb
lead: >-
  Alat berhasil jika memecahkan masalah nyata, berfungsi di tempat ia dipakai, dan dapat dibuktikan
  aman. Prinsip ini berlaku baik Anda bekerja di universitas, rumah sakit, maupun perusahaan.

rules:
  - number: "C.1"
    heading: Mulai dari kebutuhan yang Anda lihat sendiri
    explanation: >-
      Amati pekerjaannya sebelum menciptakan apa pun. Luangkan waktu di tempat layanan diberikan, dan
      catat masalah yang Anda lihat, bukan solusinya. Pernyataan kebutuhan yang baik menyebut
      masalahnya, pasiennya, dan perubahan yang diinginkan, tanpa menyebut teknologi.
    example: >-
      Lemah: "Inkubator yang lebih murah." Lebih baik: "Cara menjaga bayi berat lahir rendah tetap
      hangat selama dirujuk dari puskesmas ke rumah sakit kabupaten."
    ask: Dapatkah Anda menyatakan kebutuhannya tanpa menyebut teknologi apa pun?

  - number: "C.2"
    heading: Tuliskan apa yang harus dicapai alat
    explanation: >-
      Profil produk target (TPP) memuat apa yang harus dilakukan produk jadi: tujuan penggunaan,
      pengguna, tempat pemakaian, kinerja, dan harga. WHO memberi dua nilai untuk setiap baris: batas
      minimum yang dapat diterima, dan hasil yang diharapkan. Sepakati profil ini dengan klinisi dan
      pembeli sebelum mulai merancang.
    example: >-
      Untuk penghangat transportasi bayi, batas minimumnya menjaga suhu kulit bayi dalam rentang aman
      selama perjalanan dua jam. Hasil yang diharapkan: empat jam dengan baterai. (Angka ilustrasi.)
    ask: Untuk setiap baris profil Anda, berapa nilai minimum yang dapat diterima, dan siapa yang menyepakatinya?

  - number: "C.3"
    heading: Rancang untuk tempat alat akan dipakai
    explanation: >-
      Cari tahu pasokan listrik, panas, kelembapan, dan debu di tempat alat akan bekerja, serta siapa
      yang akan memakai, membersihkan, dan memperbaikinya. Pembeli memeriksa hal yang sama saat
      menulis spesifikasi ([prinsip 1.5](specification.html#rule-1-5)). Alat yang membutuhkan apa yang
      tidak dimiliki fasilitas tidak akan dibeli, atau tidak akan dipakai.
    example: >-
      Jika puskesmas sering mati listrik, rancang alat agar bisa berjalan dengan baterai, dan pakai
      komponen yang dapat dibeli dan diganti sendiri oleh teknisi kabupaten.
    ask: Apakah alat Anda tetap berfungsi di fasilitas yang perlengkapannya paling terbatas yang ingin Anda layani?

  - number: "C.4"
    heading: Kelola risiko sejak sketsa pertama
    explanation: >-
      Daftar apa saja yang dapat mencederai pasien atau pengguna, seberapa mungkin terjadi, dan
      seberapa parah. Lalu hilangkan risikonya lewat desain, tambahkan pelindung, atau beri
      peringatan, dengan urutan itu. ISO 14971 menjelaskan prosesnya, dan regulator berharap melihat
      catatannya.
    example: >-
      Infant warmer bisa membuat bayi kepanasan. Desain: batasi daya pemanas. Pelindung: pemutus
      terpisah yang mati pada suhu tertentu. Peringatan: alarm dan label.
    ask: Untuk setiap bahaya yang Anda daftar, perubahan desain, pelindung, atau peringatan mana yang mengendalikannya?

  - number: "C.5"
    heading: Uji dengan pengguna nyata, sejak awal dan berulang
    explanation: >-
      Banyak masalah alat berupa kesalahan penggunaan: desainnya membuat pengguna yang lelah atau
      sibuk mudah keliru. IEC 62366-1 menjelaskan cara menemukan dan menghilangkannya. Biarkan
      perawat, bidan, atau teknisi mencoba purwarupa dalam kondisi yang mendekati nyata, dan amati
      tanpa membantu.
    example: >-
      Minta tiga bidan mengatur suhu dengan tangan bersarung, di ruangan redup, tanpa buku petunjuk.
      Catat setiap keraguan dan setiap tombol yang salah ditekan.
    ask: Kesalahan penggunaan apa yang Anda lihat saat pengujian, dan apa yang Anda ubah karenanya?

  - number: "C.6"
    heading: Perlakukan perangkat lunak sebagai bagian dari alat
    explanation: >-
      Perangkat lunak yang mengendalikan alat, atau yang membantu keputusan diagnosis atau terapi,
      biasanya diatur sebagai alat kesehatan. IEC 62304 menjelaskan cara mengembangkan dan
      memeliharanya. Rencanakan pembaruan, keamanan, dan pencatatan sejak awal.
    example: >-
      Aplikasi yang menghitung dosis obat dari berat badan anak adalah perangkat lunak alat kesehatan,
      walaupun berjalan di ponsel biasa.
    ask: Fungsi perangkat lunak Anda yang mana yang dapat mencederai pasien jika hasilnya salah?

  - number: "C.7"
    heading: Catat keputusan desain selama bekerja
    explanation: >-
      Simpan berkas desain: persyaratannya, cara setiap persyaratan diperiksa, dan alasan setiap
      keputusan. ISO 13485 menyebutnya pengendalian desain dan pengembangan. Menyusun ulang berkas
      ini belakangan memakan waktu, padahal pendaftaran alat ([Panduan D](to-market.html)) bergantung
      padanya.
    example: >-
      Untuk setiap persyaratan, simpan satu baris: persyaratannya, metode uji, hasilnya, tanggal, dan
      siapa yang memeriksa.
    ask: Dapatkah orang di luar tim Anda menelusuri setiap persyaratan sampai ke hasil ujinya?

tables:
  stages:
    columns:
      - Tahap
      - Yang harus Anda miliki
      - Standar dan alat bantu
    rows:
      - - Menemukan kebutuhan
        - Pernyataan kebutuhan yang disepakati dengan para pemberi layanan
        - Proses biodesign (identify, invent, implement)
      - - Menetapkan produk
        - Profil produk target dengan nilai minimum dan nilai yang diharapkan
        - Profil produk target WHO
      - - Merancang dan membuat purwarupa
        - Persyaratan, berkas risiko, dan berkas desain
        - ISO 14971, ISO 13485
      - - Menguji
        - Laporan uji bangku, uji kegunaan, dan uji keselamatan
        - IEC 60601-1, IEC 62366-1, IEC 62304
      - - Bersiap ke pasar
        - Bukti dan dokumen untuk pendaftaran
        - '[Panduan D](to-market.html)'
---

## Dari gagasan sampai alat

Apa yang perlu dimiliki di setiap tahap. Setiap tahap dibangun di atas tahap sebelumnya, dan kekurangan yang baru ditemukan belakangan paling mahal diperbaiki.

{% include table.html table=page.tables.stages %}

## Sumber

Berikut dokumen publik di balik panduan ini. Standarnya sendiri dijual oleh ISO dan IEC; halaman ringkasannya gratis.

- Stanford Byers Center for Biodesign, [proses biodesign](https://biodesign.stanford.edu/about-us/process.html): identify, invent, implement.
- Organisasi Kesehatan Dunia (WHO), [profil produk target](https://www.who.int/observatories/global-observatory-on-health-research-and-development/analyses-and-syntheses/target-product-profile/who-target-product-profiles): karakteristik minimum dan yang diharapkan.
- Organisasi Kesehatan Dunia (WHO), [kompendium teknologi kesehatan inovatif untuk tempat dengan sumber daya terbatas, 2024](https://www.who.int/publications/i/item/9789240095212).
- [ISO 14971:2019](https://www.iso.org/standard/72704.html), penerapan manajemen risiko pada alat kesehatan.
- [IEC 62366-1:2015](https://www.iso.org/standard/63179.html), penerapan rekayasa kegunaan pada alat kesehatan.
- [IEC 62304:2006](https://www.iso.org/standard/38421.html), proses siklus hidup perangkat lunak alat kesehatan.
- [ISO 13485:2016](https://www.iso.org/standard/59752.html), sistem manajemen mutu alat kesehatan.
