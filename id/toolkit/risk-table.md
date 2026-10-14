---
title: "Templat tabel risiko | SistemSehat"
description: "Tabel risiko alat kesehatan siap cetak: setiap bahaya, cedera yang dapat ditimbulkannya, dan cara mengendalikannya."
lang: id
layout: page
parent: toolkit.html
crumb: "Tabel risiko"
heading: "Tabel risiko"
lead: "Setiap bahaya, cedera yang dapat ditimbulkannya, dan cara Anda mengendalikannya. Menyertai [prinsip C.4](../design.html#rule-c-4). ISO 14971 menjelaskan proses lengkapnya."
note: "Cetak halaman ini, atau salin tabelnya ke dokumen Anda sendiri."
search:
  title: "Tabel risiko"
  text: "Tabel risiko alat kesehatan siap cetak: setiap bahaya, cedera yang dapat ditimbulkannya, dan cara mengendalikannya."
tables:
  risks:
    columns: ["No.", "Bahaya", "Cedera yang dapat ditimbulkan", "Kemungkinan (rendah, sedang, tinggi)", "Keparahan (rendah, sedang, tinggi)", "Pengendalian: desain, pelindung, atau peringatan", "Dibuktikan oleh uji apa"]
    rows:
      - ["1", "", "", "", "", "", ""]
      - ["2", "", "", "", "", "", ""]
      - ["3", "", "", "", "", "", ""]
      - ["4", "", "", "", "", "", ""]
      - ["5", "", "", "", "", "", ""]
      - ["6", "", "", "", "", "", ""]
      - ["7", "", "", "", "", "", ""]
      - ["8", "", "", "", "", "", ""]
---

## Cara memakainya

1. Daftar semua cara alat dapat mencederai pasien atau pengguna: panas, listrik, hasil ukur yang salah, kesalahan penggunaan.
2. Nilai seberapa mungkin dan seberapa parah setiap cedera.
3. Pilih pengendalian dengan urutan ini: ubah desain, tambahkan pelindung, lalu beri peringatan.
4. Untuk setiap pengendalian, sebutkan uji yang membuktikan bahwa pengendalian itu bekerja ([prinsip C.7](../design.html#rule-c-7)).
{: .steps}

## Contoh satu baris

Infant warmer bisa membuat bayi kepanasan (bahaya: panas berlebih; cedera: luka bakar). Pengendalian lewat desain: batasi daya pemanas. Pelindung: pemutus terpisah. Peringatan: alarm. Dibuktikan oleh: uji suhu dalam IEC 60601-2-21.

## Tabelnya

{% include table.html table=page.tables.risks %}
