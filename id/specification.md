---
title: Apa yang harus kita minta? Panduan spesifikasi | SistemSehat
description: >-
  Tujuh prinsip dengan contoh untuk menulis spesifikasi alat kesehatan yang dapat dipenuhi
  beberapa produsen.
lang: id
layout: guide
order: 1
number: "1"
label: Spesifikasi
question: Apa yang harus kita minta?
summary: >-
  Spesifikasi menentukan alat apa yang tiba di fasilitas. Tujuh prinsip untuk menulis
  spesifikasi yang dapat dipenuhi beberapa produsen dan dapat dipakai klinisi.
icon: doc
lead: >-
  Spesifikasi menentukan alat apa yang tiba di fasilitas. Spesifikasi yang baik membuat beberapa
  produsen dapat bersaing memasok alat yang memenuhi kebutuhan klinis. Spesifikasi yang buruk
  meloloskan alat yang tidak berfungsi, atau hanya menyisakan satu penyedia yang bisa ikut.

rules:
  - number: "1.1"
    heading: Mulai dari kebutuhan klinis
    explanation: >-
      Sebelum menuliskan fitur apa pun, tuliskan dulu apa yang harus dilakukan alat itu, untuk
      pasien siapa, dan di fasilitas jenis apa. Alat untuk bangsal rumah sakit kabupaten dan
      alat untuk poskesdes bisa bernama sama, tetapi spesifikasinya bisa sangat berbeda.
    example: >-
      Untuk infant warmer: "Menjaga bayi baru lahir tetap hangat selama resusitasi dan beberapa
      jam pertama setelah lahir, di ruang bersalin puskesmas PONED."
    ask: >-
      Dapatkah klinisi yang akan memakai alat ini menjelaskan, dalam satu kalimat, mengapa
      setiap persyaratan diperlukan?

  - number: "1.2"
    heading: Jelaskan apa yang harus dilakukan alat, bukan mereknya
    explanation: >-
      Sebutkan rentang, akurasi, kapasitas, atau keluaran yang Anda perlukan. Jangan menyebut
      merek atau tipe. Jangan menyalin detail desain yang hanya dipakai satu produsen.
      Persyaratan yang disalin dari satu brosur biasanya hanya cocok untuk satu produk.
    example: >-
      Tulis "daya pemanas dikendalikan otomatis oleh sensor suhu kulit, dengan mode manual",
      bukan nama tipe infant warmer yang pernah Anda pakai.
    ask: Apakah lebih dari satu produsen dapat memenuhi persyaratan ini sebagaimana tertulis?

  - number: "1.3"
    heading: Pisahkan yang wajib dari yang sebaiknya ada
    explanation: >-
      Persyaratan wajib adalah sesuatu yang tanpanya alat menjadi tidak aman atau tidak berguna,
      karena penawaran yang tidak memenuhinya akan digugurkan. Selebihnya adalah hal yang
      sebaiknya ada. Jika metode evaluasi memungkinkan, beri nilai tambah untuk hal yang
      sebaiknya ada, alih-alih menggugurkan penawaran yang tidak memilikinya.
    example: >-
      Untuk infant warmer, alarm saat suhu keluar dari batas adalah wajib. Timbangan bayi bawaan
      adalah sebaiknya ada.
    ask: >-
      Jika sebuah penawaran tidak memenuhi baris ini, apakah Anda benar-benar ingin
      menggugurkannya?

  - number: "1.4"
    heading: Sebutkan standar yang tepat
    explanation: >-
      Peralatan listrik medis wajib memenuhi standar keselamatan umum IEC 60601-1. Banyak jenis
      alat juga punya standar khusus sendiri. Misalnya, IEC 60601-2-21 mengatur infant radiant
      warmer. Sebutkan standar yang berlaku dan mintalah bukti, seperti laporan uji, bukan
      sekadar pernyataan bahwa alat memenuhi standar.
    example: >-
      Lemah: "Memenuhi standar internasional." Kuat: "Memenuhi IEC 60601-1 dan IEC 60601-2-21.
      Lampirkan laporan uji."
    ask: Apakah setiap standar yang Anda sebutkan memang berlaku untuk jenis alat ini?

  - number: "1.5"
    heading: Pilih alat yang cocok dengan tempat pemakaiannya
    explanation: >-
      Alat harus tetap berfungsi di tempat ia dipakai. Perhatikan pasokan listrik dan iklimnya:
      panas, kelembapan, dan debu. Perhatikan juga perjalanan ke fasilitas terpencil, kemampuan
      petugas yang akan memakainya, dan siapa yang akan merawatnya.
    example: >-
      Analyzer laboratorium untuk puskesmas yang sering mati listrik mungkin memerlukan UPS, dan
      reagen yang bisa disimpan tanpa lemari pendingin.
    ask: >-
      Apakah alat ini tetap berfungsi di fasilitas yang sumber dayanya paling terbatas dalam
      daftar pengiriman?

  - number: "1.6"
    heading: Rinci semua yang harus menyertai alat
    explanation: >-
      Alat belum siap dipakai tanpa aksesorinya, persediaan awal bahan habis pakai, dan buku
      petunjuk yang bisa dibaca penggunanya. Masukkan semuanya, ditambah pelatihan, masa
      garansi, suku cadang, dan seberapa cepat penyedia harus datang saat alat rusak.
    example: >-
      Untuk analyzer laboratorium: reagen awal, bahan kontrol dan kalibrator, kertas printer,
      serta pelatihan untuk petugas laboratorium.
    ask: >-
      Pada hari alat tiba, apakah semua yang dibutuhkan untuk melayani pasien pertama sudah ada?

  - number: "1.7"
    heading: Pastikan setiap persyaratan bisa diperiksa
    explanation: >-
      Untuk setiap persyaratan, sebutkan bukti yang harus diserahkan peserta, dan cara Anda
      memeriksanya saat alat diserahterimakan. Persyaratan yang tidak bisa diperiksa tidak bisa
      ditegakkan.
    example: >-
      Persyaratan: pengendalian suhu dalam rentang yang Anda tetapkan. Bukti dalam penawaran:
      laporan uji. Pemeriksaan saat serah terima: ukur dengan termometer terkalibrasi saat uji
      terima.
    ask: >-
      Untuk setiap baris: dokumen apa yang membuktikannya, dan pemeriksaan apa yang
      memastikannya saat serah terima?

tables:
  rewrite:
    columns:
      - Yang sering tertulis
      - Masalahnya
      - Lebih baik
    rows:
      - - '"Merek X atau setara"'
        - Menyebut produk, dan tidak menjelaskan arti "setara".
        - Sebutkan apa yang harus dicapai alat, beserta rentang dan akurasi yang diperlukan.
      - - '"Layar berkualitas tinggi"'
        - Tidak bisa diperiksa, jadi tidak bisa ditegakkan.
        - >-
          "Layar menampilkan nilai yang diatur dan nilai yang terukur, terbaca dari jarak satu
          meter."
      - - '"Wajib layar sentuh"'
        - Pilihan desain, bukan kebutuhan klinis.
        - >-
          "Kontrol dapat dipakai dengan tangan bersarung dan dibersihkan dengan disinfektan
          standar."
      - - '"Memenuhi standar internasional"'
        - Tidak menyebut standar yang mana, atau bukti apa yang diperlukan.
        - >-
          "Memenuhi IEC 60601-1 dan standar khusus untuk jenis alat ini. Laporan uji
          dilampirkan."
  sections:
    columns:
      - Bagian
      - Yang ditulis
    rows:
      - - Nama, kategori, dan kode
        - >-
          Nama generik dan kode dari sistem penamaan yang diakui, seperti GMDN, agar setiap
          peserta memahami alat yang sama
      - - Tujuan penggunaan
        - Tujuan klinis, tingkat layanan, dan unit tempat alat akan dipakai
      - - Karakteristik teknis
        - >-
          Apa yang harus dicapai alat, apa yang ditampilkannya, dan pengaturan yang dapat diubah
          pengguna
      - - Karakteristik fisik
        - Komponen, mobilitas, dan bahan
      - - Kebutuhan utilitas
        - Pasokan listrik, air, atau gas yang dibutuhkan alat
      - - Aksesori, bahan habis pakai, dan suku cadang
        - Apa yang harus datang bersama alat, dan apa yang akan dihabiskannya
      - - Kemasan
        - Sterilitas saat tiba, masa simpan, pengangkutan, penyimpanan, dan pelabelan
      - - Persyaratan lingkungan
        - Kondisi yang harus ditahan alat di tempat ia bekerja
      - - Pelatihan, pemasangan, dan penggunaan
        - Persiapan lokasi, pengesahan saat uji fungsi, dan pelatihan pengguna
      - - Garansi dan pemeliharaan
        - Masa garansi, jenis kontrak layanan, suku cadang setelah garansi, dan pembaruan
      - - Dokumentasi
        - Buku petunjuk dan dokumen lain yang harus diserahkan
      - - Penghapusan
        - Perkiraan umur pakai alat
      - - Keselamatan dan standar
        - Kelas risiko, izin edar, dan standar yang berlaku
---

## Menulis ulang persyaratan

Empat baris yang sering muncul dalam spesifikasi, dan cara menulis masing-masing dengan lebih baik. Contoh-contohnya bersifat ilustratif.

{% include table.html table=page.tables.rewrite %}

## Spesifikasi lengkap, bagian demi bagian

Organisasi Kesehatan Dunia (WHO) menerbitkan [templat spesifikasi teknis](https://www.who.int/publications/m/item/user-guide-who-technical-specification-for-medical-devices) berisi lima puluh isian dalam tiga belas bagian. Jika Anda memakai bagian yang sama setiap kali, tidak ada yang terlewat, dan dua spesifikasi dapat dibandingkan baris demi baris.

{% include table.html table=page.tables.sections %}
