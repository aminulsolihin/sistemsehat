---
title: Bagaimana memakai sumber terbuka? Panduan sumber terbuka | SistemSehat
description: >-
  Tujuh prinsip dengan contoh untuk memakai dan membagikan perangkat keras dan lunak kesehatan sumber terbuka: lisensi, izin, bukti, dan data pasien.
lang: id
layout: guide
pillar: build
reviewed: 14 Oktober 2026
order: 8
number: "E"
label: Sumber terbuka
question: Bagaimana memakai dan membagikan teknologi sumber terbuka?
summary: >-
  Desain dan perangkat lunak terbuka dapat menghemat kerja bertahun-tahun, tetapi terbuka tidak
  berarti berizin atau aman. Tujuh prinsip untuk memakai dan membagikannya.
icon: share
lead: >-
  Perangkat keras dan lunak sumber terbuka memungkinkan siapa saja mempelajari, memakai, mengubah,
  dan membagikan sebuah desain. Dalam layanan kesehatan, kebebasan itu datang dengan kewajiban yang
  sama seperti alat lain: bukti, mutu, dan pihak yang bertanggung jawab.

rules:
  - number: "E.1"
    heading: Baca lisensinya sebelum memakai apa pun
    explanation: >-
      Lisensi menentukan apa yang boleh Anda lakukan dengan sebuah desain atau kode. Lisensi
      permisif, seperti MIT atau BSD, membolehkan Anda memakainya ulang hampir tanpa syarat. Lisensi
      resiprokal, seperti GNU GPL atau CERN-OHL-S, mewajibkan Anda membagikan perubahan dengan
      lisensi yang sama.
    example: >-
      SIMRS Khanza gratis dipakai, tetapi lisensinya melarang menjualnya. Open Source Initiative
      tidak menganggap lisensi dengan larangan seperti itu sebagai sumber terbuka.
    ask: Apa yang diwajibkan lisensinya jika Anda mengubah desain lalu menyebarkannya?

  - number: "E.2"
    heading: Desain terbuka bukan alat yang berizin
    explanation: >-
      Regulator menyetujui alat yang dibuat produsen yang bertanggung jawab, bukan berkas desain.
      Siapa pun yang memproduksi dan memasok alat di Indonesia memerlukan izin edar, sama seperti alat
      lain. Gratis atau terbuka tidak mengubah satu pun langkah di [Panduan D](to-market.html).
    example: >-
      Proyek OpenFlexure menyatakan bahwa mikroskopnya belum tersertifikasi sebagai alat kesehatan.
      Proyek itu juga mencatat bahwa sertifikat diberikan kepada produsen, bukan kepada desain.
    ask: Siapa yang akan tercatat sebagai produsen alat yang Anda buat dari desain ini?

  - number: "E.3"
    heading: Periksa buktinya, bukan antusiasmenya
    explanation: >-
      Proyek terbuka sering sudah terkenal sebelum teruji dengan baik. Menurut tinjauan tahun 2020 atas
      ventilator sumber terbuka, desain yang teruji tidak lengkap dokumentasinya, dan desain yang
      terdokumentasi hanya diuji seadanya atau tidak sama sekali. Mintalah laporan uji dan evaluasi
      yang diterbitkan, seperti untuk alat lain.
    example: >-
      Sebelum mengadaptasi desain ventilator terbuka, cari laporan uji terhadap standar ventilator,
      bukan hanya video yang menunjukkan alat itu bekerja.
    ask: Siapa yang menguji desain ini, terhadap standar apa, dan di mana hasilnya?

  - number: "E.4"
    heading: Periksa apakah proyeknya masih hidup
    explanation: >-
      Perangkat keras dan lunak perlu diperbaiki lama setelah rilis pertamanya. Lihat kapan versi
      terakhir keluar, berapa orang yang memeliharanya, dan bagaimana masalah keamanan dilaporkan dan
      diperbaiki. Proyek yang hanya dipelihara satu orang dapat berhenti kapan saja.
    example: >-
      Anda berencana memasang server citra terbuka di rumah sakit. Periksa dulu tanggal rilis
      terakhirnya, dan apakah ada perbaikan keamanan yang diterbitkan dalam setahun terakhir.
    ask: Jika besok ditemukan kerusakan serius, siapa yang akan memperbaikinya, dan bagaimana Anda akan mengetahuinya?

  - number: "E.5"
    heading: Pastikan alatnya bisa dibuat dari dokumennya
    explanation: >-
      Sebuah desain baru benar-benar terbuka jika orang lain dapat membuatnya. Cari berkas desain,
      daftar komponen, petunjuk perakitan dan kalibrasi, serta kode sumber firmware-nya. Bagian yang
      hilang biasanya berarti Anda tetap bergantung pada tim aslinya.
    example: >-
      Sebelum memilih sebuah desain, coba pesan setiap komponen dalam daftarnya dari pemasok di
      Indonesia.
    ask: Dapatkah teknisi di tim Anda membuat, mengalibrasi, dan memperbaiki satu unit hanya dari dokumen yang diterbitkan?

  - number: "E.6"
    heading: Lindungi data pasien
    explanation: >-
      Perangkat lunak yang menyimpan data pasien wajib memenuhi Undang-Undang Nomor 27 Tahun 2022
      tentang Pelindungan Data Pribadi, yang menggolongkan data kesehatan sebagai data sensitif.
      Fasilitas kesehatan juga wajib menyelenggarakan rekam medis elektronik yang terhubung dengan
      platform SATUSEHAT Kementerian Kesehatan. Periksa keduanya sebelum memilih perangkat lunak
      terbuka untuk rekam medis.
    example: >-
      Sebelum memakai sistem rekam medis terbuka, pastikan sistem itu mengatur siapa yang boleh
      melihat setiap rekam medis. Sistem itu juga harus mencatat setiap akses dan dapat bertukar
      data dengan SATUSEHAT.
    ask: Siapa yang dapat melihat data pasien di sistem ini, dan dapatkah Anda menunjukkan catatan siapa yang melihatnya?

  - number: "E.7"
    heading: Pilih lisensi saat membagikan karya sendiri
    explanation: >-
      Jika Anda menerbitkan sebuah desain, pilih lisensinya dengan sengaja. Untuk perangkat keras,
      CERN-OHL versi 2 punya varian resiprokal kuat, resiprokal lemah, dan permisif. Untuk perangkat
      lunak, pilihan utamanya antara lisensi resiprokal seperti GNU GPL dan lisensi permisif seperti
      MIT atau Apache 2.0.
    example: >-
      Tim yang ingin perusahaan membagikan perbaikan atas desain infant warmer-nya memilih
      CERN-OHL-S. Tim yang ingin desainnya dipakai seluas mungkin memilih CERN-OHL-P.
    ask: Apa yang Anda ingin orang lain boleh lakukan dengan desain Anda, dan apakah lisensinya menyatakan itu?

tables:
  licences:
    columns:
      - Lisensi
      - Jenis
      - Jika Anda menyebarkan versi yang diubah
      - Biasa dipakai untuk
    rows:
      - - MIT, BSD, Apache 2.0
        - Permisif
        - Pertahankan pemberitahuan aslinya. Versi Anda boleh memakai lisensi apa pun.
        - Perangkat lunak
      - - Mozilla Public License 2.0
        - Resiprokal lemah
        - Bagikan berkas yang diubah dengan lisensi yang sama. Berkas baru boleh memakai syarat lain.
        - Perangkat lunak
      - - GNU GPL versi 3
        - Resiprokal kuat
        - Bagikan kode sumber seluruh karya dengan lisensi GPL.
        - Perangkat lunak
      - - CERN-OHL-P versi 2
        - Permisif
        - Pertahankan pemberitahuan aslinya. Versi Anda boleh memakai lisensi apa pun.
        - Perangkat keras
      - - CERN-OHL-W versi 2
        - Resiprokal lemah
        - Bagikan perubahan atas desain yang dilisensikan. Bagian yang Anda tambahkan boleh memakai syarat lain.
        - Perangkat keras
      - - CERN-OHL-S versi 2
        - Resiprokal kuat
        - Bagikan seluruh desain yang diubah dengan lisensi yang sama.
        - Perangkat keras
      - - Creative Commons Attribution (CC BY)
        - Permisif
        - Cantumkan nama penulis aslinya.
        - Dokumentasi dan gambar
---

## Lisensi yang umum

Apa yang diminta setiap lisensi saat Anda menyebarkan versi yang diubah. Ini ringkasan: baca lisensinya sendiri sebelum Anda mengandalkannya.

{% include table.html table=page.tables.licences %}

## Contoh

Halaman [Inovasi](innovation.html#hardware) memuat perangkat keras dan lunak kesehatan sumber terbuka, beserta lisensinya dan apa kata dokumennya sendiri tentang pemakaian medis.

## Sumber

- CERN, [CERN Open Hardware Licence versi 2](https://ohwr.org/project/cernohl/wikis/Documents/CERN-OHL-version-2), dengan ketiga variannya.
- Open Source Initiative, [Open Source Definition dan daftar lisensi yang disetujui](https://opensource.org/licenses).
- Open Source Hardware Association, [sertifikasi perangkat keras sumber terbuka](https://certification.oshwa.org/).
- Joshua M. Pearce, [tinjauan ventilator sumber terbuka untuk COVID-19 dan pandemi berikutnya](https://f1000research.com/articles/9-218/v2), F1000Research, 2020.
- OpenFlexure, [alat kesehatan](https://openflexure.org/about/medical-devices): apa yang dapat dan tidak dapat diklaim oleh desain terbuka.
- [Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi](https://peraturan.bpk.go.id/Details/229798).
- [Peraturan Menteri Kesehatan Nomor 24 Tahun 2022 tentang Rekam Medis](https://peraturan.bpk.go.id/Details/245544).
