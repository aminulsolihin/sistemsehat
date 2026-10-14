"""Indonesian content for SistemSehat. Pages here are written to docs/id/ with the same file names as English,
so the language switch can link each page to its counterpart. Rule numbers, anchors, checklist ids and
glossary ids match content_en.py. Writing rules are in WRITING-GUIDE.md.
"""
from engine import (begin, clause, reviewed, keypoints, related, pager, guide_card, tool_card, table,
                    checklist_groups, glossary_list, library_group, S)

REVIEWED = "11 Oktober 2026"

GUIDES = [
    ("specification.html", "1", "Spesifikasi", "Apa yang harus kita minta?",
     "Spesifikasi menentukan alat apa yang tiba di fasilitas. Tujuh prinsip untuk menulis spesifikasi yang dapat dipenuhi beberapa produsen dan dapat dipakai klinisi.", "doc"),
    ("pricing.html", "2", "Harga", "Berapa harga yang wajar?",
     "Harga tidak banyak berarti sebelum Anda tahu apa saja yang tercakup di dalamnya. Enam prinsip untuk menyusun harga acuan yang dapat Anda jelaskan dan pertanggungjawabkan.", "tag"),
    ("process.html", "3", "Proses", "Bagaimana membelinya tanpa tender gagal?",
     "Cara membagi paket, menilai penawaran, dan menetapkan batas waktu sudah menentukan hasil sebelum penawaran dibuka. Tujuh prinsip untuk menjalankan tender.", "route"),
    ("regulation.html", "A", "Regulasi", "Apa yang wajib dipenuhi sebuah alat?",
     "Izin edar, kelas risiko, sertifikat mutu, standar, TKDN, dan kalibrasi. Delapan prinsip untuk memeriksa dokumennya.", "shield"),
    ("technology.html", "B", "Teknologi", "Bagaimana menilai teknologinya?",
     "Cara kerjanya, bukti yang mendukungnya, riwayat pemakaiannya, dan kesesuaiannya dengan fasilitas Anda. Tujuh prinsip untuk menilai alat yang tidak Anda rancang sendiri.", "monitor"),
]

MAIN_NAV = [
    ("guides.html", "Panduan"),
    ("dossiers.html", "Kajian alat"),
    ("checklist.html", "Daftar periksa"),
    ("glossary.html", "Glosarium"),
    ("library.html", "Sumber rujukan"),
    ("about.html", "Tentang"),
]

PAGE_LABELS = {
    "guides.html": "Panduan",
    "dossiers.html": "Kajian alat",
    "checklist.html": "Daftar periksa",
    "glossary.html": "Glosarium",
    "library.html": "Sumber rujukan",
    "about.html": "Tentang",
    "search.html": "Pencarian",
}

UI = {
    "skip": "Langsung ke konten utama",
    "nav_label": "Menu utama",
    "crumbs_label": "Jejak halaman",
    "home": "Beranda",
    "guides_label": "Panduan",
    "tabs_label": "Rangkaian panduan",
    "f_guides_label": "Semua panduan",
    "og_alt": "SistemSehat: Minta alat yang tepat. Bayar harga yang wajar. Jalankan tender yang berhasil.",
    "search_label": "Cari di situs ini",
    "search_placeholder": "Cari prinsip dan istilah",
    "search": "Cari",
    "menu": "Menu",
    "lang_label": "Bahasa",
    "footer_about": "Inisiatif independen dan nonkomersial. Tidak terkait dengan atau didukung oleh lembaga pemerintah, pemberi pinjaman, atau produsen mana pun.",
    "f_tools": "Alat bantu",
    "f_about": "Tentang",
    "f_about_label": "Tentang situs ini",
    "f_about_site": "Tentang SistemSehat",
    "f_independent": "Cara menjaga independensi",
    "f_dossiers": "Kajian alat",
    "legal": "Panduan di sini bersifat umum dan tidak menggantikan aturan pengadaan yang berlaku di instansi Anda.",
    "test": "Tanyakan",
    "example": "Contoh",
    "check_count": "{n} dari {total} dicentang",
    "check_note": "Centang disimpan di peramban ini saja.",
    "check_clear": "Hapus semua centang",
    "last_reviewed": "Terakhir ditinjau {date}",
    "n_rules": "{n} prinsip",
    "reading_time": "Sekitar {n} menit membaca",
    "checklist_for_guide": "Daftar periksa panduan ini",
    "key_points": "{n} prinsip dalam panduan ini",
    "related": "Terkait",
    "rel_checklist": "{n} pertanyaan dari panduan ini, untuk dicentang atau dicetak",
    "rel_glossary": "Penjelasan istilah dan singkatan yang dipakai di sini",
    "rel_library": "Dokumen publik di balik panduan",
    "rel_dossiers": "Ketiga pertanyaan dijawab untuk satu alat",
    "prev_guide": "Panduan sebelumnya",
    "next_guide": "Panduan berikutnya",
    "finished": "Sudah selesai membaca panduan?",
    "open_checklist": "Buka daftar periksa",
    "pager_label": "Panduan lain",
    "guide_more": "Panduan {label_lower}",
    "library_headers": ["Sumber", "Penerbit", "Gunakan untuk"],
    "k_guide": "Panduan",
    "k_rule": "Prinsip {label_lower}",
    "k_page": "Halaman",
}

begin("id", UI, GUIDES, MAIN_NAV, PAGE_LABELS, REVIEWED)

IN_PREP = '<span class="status">Sedang disusun</span>'

STATUS_TABLE = table(
    ["Bidang", "Kajian", "Status"],
    [
        ["Perawatan bayi baru lahir", "Satu alat", IN_PREP],
        ["Laboratorium layanan primer", "Dua analyzer", IN_PREP],
    ],
)

# the thirteen sections of the WHO technical specification template
WHO_SECTIONS = [
    ("Nama, kategori, dan kode", "Nama generik dan kode dari sistem penamaan yang diakui, seperti GMDN, agar setiap peserta memahami alat yang sama"),
    ("Tujuan penggunaan", "Tujuan klinis, tingkat layanan, dan unit tempat alat akan dipakai"),
    ("Karakteristik teknis", "Apa yang harus dicapai alat, apa yang ditampilkannya, dan pengaturan yang dapat diubah pengguna"),
    ("Karakteristik fisik", "Komponen, mobilitas, dan bahan"),
    ("Kebutuhan utilitas", "Pasokan listrik, air, atau gas yang dibutuhkan alat"),
    ("Aksesori, bahan habis pakai, dan suku cadang", "Apa yang harus datang bersama alat, dan apa yang akan dihabiskannya"),
    ("Kemasan", "Sterilitas saat tiba, masa simpan, pengangkutan, penyimpanan, dan pelabelan"),
    ("Persyaratan lingkungan", "Kondisi yang harus ditahan alat di tempat ia bekerja"),
    ("Pelatihan, pemasangan, dan penggunaan", "Persiapan lokasi, pengesahan saat uji fungsi, dan pelatihan pengguna"),
    ("Garansi dan pemeliharaan", "Masa garansi, jenis kontrak layanan, suku cadang setelah garansi, dan pembaruan"),
    ("Dokumentasi", "Buku petunjuk dan dokumen lain yang harus diserahkan"),
    ("Penghapusan", "Perkiraan umur pakai alat"),
    ("Keselamatan dan standar", "Kelas risiko, izin edar, dan standar yang berlaku"),
]

# ------------------------------------------------------------------ Beranda

home = f"""    <section class="hero">
      <div class="wrap hero-grid">
        <div>
          <h1>
            <span>Minta alat yang tepat.</span>
            <span>Bayar harga yang wajar.</span>
            <span>Jalankan tender yang berhasil.</span>
          </h1>
          <p class="hero-lead">SistemSehat adalah panduan gratis dan independen untuk membeli alat kesehatan bagi fasilitas kesehatan pemerintah di Indonesia. Isinya: apa yang harus diminta, berapa harga yang wajar, dan bagaimana menjalankan tendernya.</p>
          <form class="search search-large" action="search.html" method="get" role="search" aria-label="Cari di panduan">
            <label for="hero-search">Cari di panduan</label>
            <div class="search-row">
              <input id="hero-search" type="search" name="q" placeholder="Contoh: kalibrasi">
              <button type="submit">Cari</button>
            </div>
          </form>
          <p class="hero-actions">
            <a class="button" href="guides.html">Jelajahi panduan</a>
            <a class="button button-quiet" href="checklist.html">Buka daftar periksa</a>
          </p>
        </div>

        <aside class="plate" aria-label="SistemSehat sekilas">
          <p class="plate-name">SistemSehat</p>
          <dl>
            <div><dt>Tujuan</dt><dd>Panduan menyusun spesifikasi, menentukan harga, dan membeli alat kesehatan</dd></div>
            <div><dt>Untuk</dt><dd>Pejabat pengadaan, klinisi, dan petugas teknis di dinas kesehatan dan rumah sakit pemerintah di Indonesia</dd></div>
            <div><dt>Sumber</dt><dd>Hanya dokumen publik, masing-masing dikutip</dd></div>
            <div><dt>Dana</dt><dd>Tidak menerima dana dari produsen atau distributor</dd></div>
            <div><dt>Status</dt><dd>Panduan sudah terbit. Kajian alat sedang disusun.</dd></div>
          </dl>
        </aside>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <div class="section-head">
          <h2>Cara memakai situs ini</h2>
        </div>
        <ol class="howto">
          <li>
            <h3>Temukan tugas Anda</h3>
            <p>Pilih pekerjaan yang sedang Anda lakukan dari daftar di bawah, atau buka panduan yang sesuai.</p>
          </li>
          <li>
            <h3>Baca prinsipnya</h3>
            <p>Setiap prinsip menjelaskan apa yang harus dilakukan, memberi contoh, dan ditutup dengan satu pertanyaan untuk Anda jawab.</p>
          </li>
          <li>
            <h3>Pakai daftar periksa</h3>
            <p>Bawa ke-35 pertanyaan ke rapat perencanaan atau saat memeriksa dokumen, di layar atau dicetak.</p>
          </li>
        </ol>

        <div class="section-head section-head-sub">
          <h2>Apa yang perlu Anda lakukan?</h2>
        </div>
        <ul class="tasks">
          <li><a href="specification.html">Menulis spesifikasi teknis</a></li>
          <li><a href="pricing.html">Menyusun HPS atau anggaran yang bisa dijelaskan</a></li>
          <li><a href="regulation.html">Memeriksa dokumen penawaran</a></li>
          <li><a href="process.html#rule-3-7">Mengulang tender yang gagal</a></li>
          <li><a href="technology.html#rule-b-7">Menilai teknologi baru yang ditawarkan penyedia</a></li>
          <li><a href="checklist.html">Mendapatkan daftar periksa untuk rapat</a></li>
        </ul>
      </div>
    </section>

    <section class="band band-tint">
      <div class="wrap">
        <div class="section-head">
          <h2>Tiga pertanyaan yang harus dijawab setiap pembelian</h2>
          <a class="all-link" href="guides.html">Semua panduan</a>
        </div>
        <p class="band-lead">Jawablah sesuai urutan ini. Jawaban yang lemah pada satu pertanyaan tidak bisa diperbaiki oleh pertanyaan berikutnya.</p>
        <ul class="cards cards-3">
{guide_card(GUIDES[0])}
{guide_card(GUIDES[1])}
{guide_card(GUIDES[2])}
        </ul>

        <div class="section-head section-head-sub">
          <h2>Dua panduan yang mendukung ketiganya</h2>
        </div>
        <p class="band-lead">Seperti lampiran dokumen pemilihan, keduanya memberi latar belakang yang dibutuhkan ketiga jawaban itu.</p>
        <ul class="cards cards-2">
{guide_card(GUIDES[3])}
{guide_card(GUIDES[4])}
        </ul>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <div class="section-head">
          <h2>Alat bantu</h2>
        </div>
        <ul class="cards cards-3">
{tool_card("checklist.html", "Daftar periksa", "Semua 35 pertanyaan dari panduan. Centang di layar atau cetak dalam dua halaman.", "check")}
{tool_card("glossary.html", "Glosarium", "Istilah pengadaan dan singkatan, dengan penjelasan singkat.", "book")}
{tool_card("library.html", "Sumber rujukan", "Dokumen publik di balik panduan: spesifikasi, harga, proses, dan bukti.", "shelf")}
        </ul>
      </div>
    </section>

    <section class="band band-tint">
      <div class="wrap two-col">
        <div>
          <div class="section-head">
            <h2>Kajian alat</h2>
            <a class="all-link" href="dossiers.html">Tentang kajian alat</a>
          </div>
          <p>Kajian alat adalah laporan singkat tentang satu alat. Kajian menjawab ketiga pertanyaan untuk alat itu: spesifikasi acuan, kisaran harga acuan, dan pelajaran untuk menjalankan pengadaannya. Tiga kajian pertama sedang ditulis.</p>
{STATUS_TABLE}
        </div>
        <div>
          <div class="section-head">
            <h2>Kabar terbaru</h2>
          </div>
          <ul class="updates">
            <li><span class="update-meta">Oktober 2026<span class="update-type">Panduan</span></span><a href="guides.html">Setiap prinsip kini dilengkapi contoh</a></li>
            <li><span class="update-meta">Oktober 2026<span class="update-type">Situs</span></span><a href="guides.html">Situs kini tersedia dalam bahasa Indonesia</a></li>
            <li><span class="update-meta">Oktober 2026<span class="update-type">Panduan</span></span><a href="guides.html">Lima panduan terbit, dengan 35 prinsip</a></li>
            <li><span class="update-meta">Oktober 2026<span class="update-type">Kajian</span></span><a href="dossiers.html">Tiga kajian alat pertama sedang disusun</a></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="band">
      <div class="wrap">
        <div class="section-head">
          <h2>Cara situs ini menjaga independensi</h2>
          <a class="all-link" href="about.html#how">Cara kerjanya</a>
        </div>
        <ul class="rules">
          <li>
            <h3>Hanya sumber publik</h3>
            <p>Setiap angka dan persyaratan berasal dari dokumen yang dapat diunduh siapa saja, dan masing-masing dikutip.</p>
          </li>
          <li>
            <h3>Tanpa uang dari penjual</h3>
            <p>Tidak ada dana, hadiah, atau konten bersponsor dari produsen maupun distributor.</p>
          </li>
          <li>
            <h3>Bukan tender yang sedang berjalan</h3>
            <p>Tidak ada yang diterbitkan tentang tender yang masih dalam tahap evaluasi.</p>
          </li>
          <li>
            <h3>Koreksi secara terbuka</h3>
            <p>Jika ada yang keliru atau sudah tidak berlaku, akan diperbaiki dan perubahannya dicatat di halaman itu.</p>
          </li>
        </ul>
      </div>
    </section>"""

# ------------------------------------------------------------------ Spesifikasi

spec_clauses = "\n".join([
    clause("1.1", "Mulai dari kebutuhan klinis",
           ["Sebelum menuliskan fitur apa pun, tuliskan dulu apa yang harus dilakukan alat itu, untuk pasien siapa, dan di fasilitas jenis apa. Alat untuk bangsal rumah sakit kabupaten dan alat untuk poskesdes bisa bernama sama, tetapi spesifikasinya bisa sangat berbeda."],
           "Dapatkah klinisi yang akan memakai alat ini menjelaskan, dalam satu kalimat, mengapa setiap persyaratan diperlukan?",
           "Untuk infant warmer: &ldquo;Menjaga bayi baru lahir tetap hangat selama resusitasi dan beberapa jam pertama setelah lahir, di ruang bersalin puskesmas PONED.&rdquo;"),
    clause("1.2", "Jelaskan apa yang harus dilakukan alat, bukan mereknya",
           ["Sebutkan rentang, akurasi, kapasitas, atau keluaran yang Anda perlukan. Jangan menyebut merek atau tipe. Jangan menyalin detail desain yang hanya dipakai satu produsen. Persyaratan yang disalin dari satu brosur biasanya hanya cocok untuk satu produk."],
           "Apakah lebih dari satu produsen dapat memenuhi persyaratan ini sebagaimana tertulis?",
           "Tulis &ldquo;daya pemanas dikendalikan otomatis oleh sensor suhu kulit, dengan mode manual&rdquo;, bukan nama tipe infant warmer yang pernah Anda pakai."),
    clause("1.3", "Pisahkan yang wajib dari yang sebaiknya ada",
           ["Persyaratan wajib adalah sesuatu yang tanpanya alat menjadi tidak aman atau tidak berguna, karena penawaran yang tidak memenuhinya akan digugurkan. Selebihnya adalah hal yang sebaiknya ada. Jika metode evaluasi memungkinkan, beri nilai tambah untuk hal yang sebaiknya ada, alih-alih menggugurkan penawaran yang tidak memilikinya."],
           "Jika sebuah penawaran tidak memenuhi baris ini, apakah Anda benar-benar ingin menggugurkannya?",
           "Untuk infant warmer, alarm saat suhu keluar dari batas adalah wajib. Timbangan bayi bawaan adalah sebaiknya ada."),
    clause("1.4", "Sebutkan standar yang tepat",
           ["Peralatan listrik medis wajib memenuhi standar keselamatan umum IEC 60601-1. Banyak jenis alat juga punya standar khusus sendiri. Misalnya, IEC 60601-2-21 mengatur infant radiant warmer. Sebutkan standar yang berlaku dan mintalah bukti, seperti laporan uji, bukan sekadar pernyataan bahwa alat memenuhi standar."],
           "Apakah setiap standar yang Anda sebutkan memang berlaku untuk jenis alat ini?",
           "Lemah: &ldquo;Memenuhi standar internasional.&rdquo; Kuat: &ldquo;Memenuhi IEC 60601-1 dan IEC 60601-2-21. Lampirkan laporan uji.&rdquo;"),
    clause("1.5", "Pilih alat yang cocok dengan tempat pemakaiannya",
           ["Alat harus tetap berfungsi di tempat ia dipakai. Perhatikan pasokan listrik dan iklimnya: panas, kelembapan, dan debu. Perhatikan juga perjalanan ke fasilitas terpencil, kemampuan petugas yang akan memakainya, dan siapa yang akan merawatnya."],
           "Apakah alat ini tetap berfungsi di fasilitas yang sumber dayanya paling terbatas dalam daftar pengiriman?",
           "Analyzer laboratorium untuk puskesmas yang sering mati listrik mungkin memerlukan UPS, dan reagen yang bisa disimpan tanpa lemari pendingin."),
    clause("1.6", "Rinci semua yang harus menyertai alat",
           ["Alat belum siap dipakai tanpa aksesorinya, persediaan awal bahan habis pakai, dan buku petunjuk yang bisa dibaca penggunanya. Masukkan semuanya, ditambah pelatihan, masa garansi, suku cadang, dan seberapa cepat penyedia harus datang saat alat rusak."],
           "Pada hari alat tiba, apakah semua yang dibutuhkan untuk melayani pasien pertama sudah ada?",
           "Untuk analyzer laboratorium: reagen awal, bahan kontrol dan kalibrator, kertas printer, serta pelatihan untuk petugas laboratorium."),
    clause("1.7", "Pastikan setiap persyaratan bisa diperiksa",
           ["Untuk setiap persyaratan, sebutkan bukti yang harus diserahkan peserta, dan cara Anda memeriksanya saat alat diserahterimakan. Persyaratan yang tidak bisa diperiksa tidak bisa ditegakkan."],
           "Untuk setiap baris: dokumen apa yang membuktikannya, dan pemeriksaan apa yang memastikannya saat serah terima?",
           "Persyaratan: pengendalian suhu dalam rentang yang Anda tetapkan. Bukti dalam penawaran: laporan uji. Pemeriksaan saat serah terima: ukur dengan termometer terkalibrasi saat uji terima."),
])

spec_rewrite = table(
    ["Yang sering tertulis", "Masalahnya", "Lebih baik"],
    [
        ["&ldquo;Merek X atau setara&rdquo;", "Menyebut produk, dan tidak menjelaskan arti &ldquo;setara&rdquo;.", "Sebutkan apa yang harus dicapai alat, beserta rentang dan akurasi yang diperlukan."],
        ["&ldquo;Layar berkualitas tinggi&rdquo;", "Tidak bisa diperiksa, jadi tidak bisa ditegakkan.", "&ldquo;Layar menampilkan nilai yang diatur dan nilai yang terukur, terbaca dari jarak satu meter.&rdquo;"],
        ["&ldquo;Wajib layar sentuh&rdquo;", "Pilihan desain, bukan kebutuhan klinis.", "&ldquo;Kontrol dapat dipakai dengan tangan bersarung dan dibersihkan dengan disinfektan standar.&rdquo;"],
        ["&ldquo;Memenuhi standar internasional&rdquo;", "Tidak menyebut standar yang mana, atau bukti apa yang diperlukan.", "&ldquo;Memenuhi IEC 60601-1 dan standar khusus untuk jenis alat ini. Laporan uji dilampirkan.&rdquo;"],
    ],
)

spec_sections = table(["Bagian", "Yang ditulis"], [list(s) for s in WHO_SECTIONS])

spec = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Apa yang harus kita minta?</h1>
        <p class="lead">Spesifikasi menentukan alat apa yang tiba di fasilitas. Spesifikasi yang baik membuat beberapa produsen dapat bersaing memasok alat yang memenuhi kebutuhan klinis. Spesifikasi yang buruk meloloskan alat yang tidak berfungsi, atau hanya menyisakan satu penyedia yang bisa ikut.</p>
{reviewed('guide-1')}
      </header>

{keypoints('1')}
      <div class="clauses">
{spec_clauses}
      </div>

      <h2 class="section-title">Menulis ulang persyaratan</h2>
      <p class="section-lead">Empat baris yang sering muncul dalam spesifikasi, dan cara menulis masing-masing dengan lebih baik. Contoh-contohnya bersifat ilustratif.</p>
{spec_rewrite}

      <h2 class="section-title">Spesifikasi lengkap, bagian demi bagian</h2>
      <p class="section-lead">Organisasi Kesehatan Dunia (WHO) menerbitkan <a href="https://www.who.int/publications/m/item/user-guide-who-technical-specification-for-medical-devices">templat spesifikasi teknis</a> berisi lima puluh isian dalam tiga belas bagian. Jika Anda memakai bagian yang sama setiap kali, tidak ada yang terlewat, dan dua spesifikasi dapat dibandingkan baris demi baris.</p>
{spec_sections}

{related('1')}
{pager('specification.html')}
    </div>"""

# ------------------------------------------------------------------ Harga

price_clauses = "\n".join([
    clause("2.1", "Sepakati cakupan harga sebelum membandingkan",
           ["Dua harga untuk alat yang sama bisa berbeda beberapa kali lipat dan keduanya tetap wajar, karena mencakup hal yang berbeda. Yang satu mungkin hanya alatnya saat keluar dari pabrik. Yang lain mungkin sudah termasuk pengiriman, pemasangan, dan layanan selama bertahun-tahun. Tuliskan apa yang tercakup dalam setiap harga sebelum membandingkannya."],
           "Untuk setiap harga yang Anda pegang, dapatkah Anda merinci apa yang termasuk dan apa yang tidak?",
           "Penawaran A: Rp150 juta, hanya analyzer. Penawaran B: Rp290 juta, termasuk pengiriman, pemasangan, pelatihan, dan reagen dua tahun. Penawaran B bisa jadi lebih baik. (Angka ilustratif.)"),
    clause("2.2", "Hitung biaya selama seluruh umur pakai",
           ["Harga beli hanyalah sebagian dari biaya. Tambahkan pengiriman dan pemasangan, bahan habis pakai dan reagen, pemeliharaan dan suku cadang, pelatihan, serta penghapusan di akhir masa pakai. Untuk analyzer laboratorium, biaya reagen selama bertahun-tahun bisa melebihi harga alatnya."],
           "Berapa biaya alat ini setiap tahun setelah dipakai, dan siapa yang akan membayarnya?",
           "Puskesmas yang menjalankan 20 tes sehari, 250 hari setahun, memakai reagen untuk 25.000 tes dalam lima tahun. Kalikan dengan biaya reagen per tes untuk melihat biaya sebenarnya."),
    clause("2.3", "Gunakan harga yang bisa ditelusuri sumbernya",
           ["Susun harga acuan dari sumber yang bisa diperiksa siapa saja. Katalog internasional seperti <a href=\"https://supply.unicef.org/\">UNICEF Supply Catalogue</a> menerbitkan harga indikatif. Katalog elektronik nasional, <a href=\"https://katalog.inaproc.id/\">INAPROC Katalog Elektronik</a>, memuat penawaran dalam negeri. Nilai HPS dalam pengumuman tender, dan pengumuman pemenang, menunjukkan berapa yang diperkirakan dan dibayar pembeli lain. <a href=\"https://www.theglobalfund.org/en/sourcing-management/procurement-tools\">Global Fund</a> memberi contoh yang baik cara menyajikan harga acuan dan waktu pengiriman per kategori produk."],
           "Dapatkah orang lain menelusuri setiap angka dalam perkiraan Anda sampai ke sumbernya?",
           "Catat setiap harga seperti ini: sumber, nama barang, harga, mata uang, tanggal Anda membacanya, dan apa saja yang tercakup."),
    clause("2.4", "Bandingkan harga dengan dasar yang sama",
           ["Konversikan semua harga ke satu mata uang, dengan kurs pada satu tanggal yang disebutkan. Catat jumlah unit yang menjadi dasar setiap harga, tempat barang diserahkan, dan apakah pajak serta bea masuk sudah termasuk. Satu unit yang diambil di gudang dan seribu unit yang dikirim ke fasilitas terpencil tidak akan memiliki harga satuan yang sama."],
           "Apakah semua harga memakai mata uang yang sama, dari tanggal yang sama, dan untuk tempat penyerahan yang sama?",
           "Konversikan harga dalam dolar Amerika Serikat dengan kurs JISDOR Bank Indonesia pada hari Anda menyusun perkiraan, dan tuliskan tanggal itu di samping angkanya."),
    clause("2.5", "Jelaskan mengapa harga berbeda; jangan dirata-rata",
           ["Jika dua harga yang dapat dipercaya berjauhan, penyebabnya biasanya cakupan, jumlah, tingkat spesifikasi, atau layanan purnajual. Cari tahu yang mana. Rata-rata dari harga yang mencakup hal berbeda tidak berarti apa-apa."],
           "Untuk harga tertinggi dan terendah yang Anda pegang, dapatkah Anda menjelaskan mengapa keduanya berbeda?",
           "Dua harga infant warmer berbeda tiga kali lipat. Yang lebih mahal sudah termasuk unit resusitasi dan kontrak layanan lima tahun. Bandingkan setelah keduanya dikeluarkan."),
    clause("2.6", "Periksa apakah Anda akan terikat pada satu pemasok",
           ["Sebagian alat hanya bisa dipakai dengan reagen, bahan habis pakai, atau perangkat lunak dari produsennya sendiri. Harga beli yang rendah lalu bisa diikuti biaya operasional yang tinggi selama bertahun-tahun. Mintalah biaya per tes atau per pemakaian, dan berapa lama harga itu dijamin."],
           "Setelah pembelian, apakah bahan yang dipakai alat ini bisa dibeli dari lebih dari satu pemasok?",
           "Analyzer &ldquo;tertutup&rdquo; hanya menerima kemasan reagen dari produsennya. Analyzer &ldquo;terbuka&rdquo; bisa memakai reagen dari pemasok lain, sehingga biaya per tes biasanya lebih rendah."),
])

price_layers = table(
    ["Bagian harga", "Yang ditambahkan", "Tanyakan kepada penjual"],
    [
        ["Alat", "Peralatan beserta aksesori standarnya", "Aksesori dan bahan habis pakai awal apa saja yang termasuk?"],
        ["Ongkos angkut dan asuransi", "Pengangkutan sampai ke Indonesia atau ke gudang pusat", "Harga ini berlaku sampai tempat mana?"],
        ["Pengiriman ke fasilitas", "Perjalanan terakhir, yang bisa paling mahal untuk fasilitas terpencil", "Apakah pengiriman ke setiap fasilitas dalam daftar sudah termasuk?"],
        ["Pemasangan dan uji fungsi", "Pemasangan, pengujian, dan serah terima alat yang berfungsi", "Siapa yang memasang, dan kapan alat dianggap diterima?"],
        ["Pelatihan", "Mengajari pengguna mengoperasikan alat dan teknisi merawatnya", "Berapa orang, berapa lama, dan di mana?"],
        ["Garansi dan pemeliharaan", "Perbaikan, suku cadang, dan servis rutin untuk jangka waktu tertentu", "Berapa lama jaminannya, dan seberapa cepat penyedia harus datang?"],
        ["Bahan habis pakai dan reagen", "Yang dihabiskan alat saat beroperasi", "Berapa biaya per tes atau per pemakaian, dan berapa lama harganya dijamin?"],
    ],
)

pricing = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Berapa harga yang wajar?</h1>
        <p class="lead">Harga tidak banyak berarti sebelum Anda tahu apa saja yang tercakup di dalamnya. Harga acuan yang baik menyebutkan cakupannya dan asal setiap angkanya, sehingga Anda dapat menjelaskannya baris demi baris.</p>
{reviewed('guide-2')}
      </header>

{keypoints('2')}
      <div class="clauses">
{price_clauses}
      </div>

      <h2 class="section-title">Apa saja yang dapat tercakup dalam harga</h2>
      <p class="section-lead">Setiap bagian menambah biaya. Sebelum membandingkan dua harga, cari tahu bagian mana saja yang dicakup masing-masing.</p>
{price_layers}

{related('2')}
{pager('pricing.html')}
    </div>"""

# ------------------------------------------------------------------ Proses

proc_clauses = "\n".join([
    clause("3.1", "Atur ukuran paket agar beberapa penyedia bisa ikut",
           ["Paket adalah bagian tender yang ditawar dan dikontrakkan tersendiri. Paket dapat dibagi per jenis alat, per wilayah, atau keduanya. Ukurannya menentukan siapa yang bisa ikut. Paket yang terlalu besar menyingkirkan penyedia kecil yang sebenarnya mampu. Paket yang terlalu kecil membuat kontrak menjadi banyak dan bisa menaikkan harga."],
           "Untuk setiap paket, dapatkah Anda menyebut beberapa penyedia yang sanggup mengirim seluruh jumlahnya ke setiap lokasi?",
           "Daripada satu paket nasional berisi 200 infant warmer, lima paket per wilayah berisi sekitar 40 unit memberi kesempatan kepada distributor daerah untuk ikut."),
    clause("3.2", "Tentukan tender nasional atau internasional dengan sengaja",
           ["Tender nasional cocok untuk alat yang dapat dibuat atau dipasok penyedia dalam negeri dalam jumlah yang dibutuhkan. Tender internasional mendatangkan lebih banyak peserta jika mereka tidak mampu. Pilihan ini memengaruhi bahasa, mata uang, jadwal, dan syarat pengiriman seluruh tender."],
           "Apakah Anda tahu siapa yang membuat alat ini, dan di mana, sebelum memutuskan siapa yang boleh ikut?",
           "Sebelum memutuskan, cari di Info Alkes alat jenis ini yang bernomor izin edar AKD, artinya dibuat di Indonesia."),
    clause("3.3", "Beri tahu peserta cara penawaran dinilai",
           ["Peserta perlu tahu aturannya sebelum menawar. Kontrak diberikan kepada penawaran dengan harga terendah yang memenuhi semua persyaratan, atau penawaran dinilai dari mutu sekaligus harga (sistem nilai). Cantumkan kriteria dan bobotnya dalam dokumen pemilihan."],
           "Dapatkah peserta mengetahui cara pemenang dipilih hanya dari dokumen pemilihan?",
           "&ldquo;Harga 70%, waktu tanggap layanan 20%, rencana pelatihan 10%.&rdquo; (Bobot ilustratif.)"),
    clause("3.4", "Beri peserta waktu yang cukup dan jawaban yang jelas",
           ["Tiga hal membantu penyedia yang baik menyiapkan penawaran yang benar. Adakan rapat pemberian penjelasan. Bagikan jawaban tertulis kepada semua peserta. Terbitkan adendum resmi setiap kali dokumen berubah. Setelah adendum terakhir, sisakan waktu yang cukup bagi peserta untuk menanggapinya."],
           "Setelah adendum terakhir, berapa hari kerja yang tersisa bagi peserta?",
           "Jika adendum mengubah persyaratan teknis dua hari sebelum batas akhir, mundurkan batas akhirnya."),
    clause("3.5", "Belajar dari pertanyaan peserta",
           ["Pertanyaan peserta menunjukkan bagian dokumen yang lemah. Jika beberapa peserta menanyakan persyaratan yang sama, persyaratan itu tidak jelas atau lebih sempit dari yang dimaksud. Perbaiki sebelum penawaran ditutup, bukan setelah dibuka."],
           "Persyaratan mana yang paling banyak ditanyakan, dan apa yang Anda ubah karenanya?",
           "Jika tiga peserta bertanya apakah infant warmer wajib memiliki timbangan bawaan, persyaratannya tidak jelas atau terlalu sempit."),
    clause("3.6", "Rencanakan apa yang terjadi setelah kontrak ditandatangani",
           ["Penandatanganan kontrak adalah separuh jalan, bukan akhir. Rencanakan pengiriman, pemasangan, uji terima, pelatihan pengguna, dan garansi sejak awal. Tentukan siapa yang merawat alat setelah garansi berakhir."],
           "Siapa yang bertanggung jawab atas alat ini pada tahun setelah garansi berakhir?",
           "Tuliskan siapa yang menyimpan catatan servis, siapa yang menghubungi penyedia saat infant warmer rusak, dan siapa yang menganggarkan suku cadang setelah garansi habis."),
    clause("3.7", "Jika tender gagal, cari penyebabnya sebelum mengulang",
           ["Terlalu sedikit penawaran, tidak ada penawaran yang memenuhi syarat, dan harga di atas HPS adalah tiga kegagalan berbeda dengan penyebab yang berbeda. Mengulang tender yang sama tanpa mencari penyebabnya biasanya memberi hasil yang sama."],
           "Sebelum tender ulang: apa tepatnya yang gagal, dan bagian dokumen mana yang sudah Anda ubah?",
           "Tidak ada penawaran yang memenuhi syarat karena tidak satu pun memiliki laporan uji untuk standar khusus. Sebelum tender ulang, pastikan ada penyedia yang bisa memberikannya."),
])

fail_table = table(
    ["Yang terjadi", "Penyebab umum", "Periksa lebih dulu"],
    [
        ["Penawaran terlalu sedikit, atau tidak ada", "Paket terlalu besar, jadwal terlalu singkat, atau penyedia tidak mengetahuinya.", "Ukuran paket dibandingkan kemampuan penyedia, jumlah hari yang diberikan, dan di mana pengumuman dimuat."],
        ["Ada penawaran, tetapi tidak satu pun memenuhi syarat", "Ada persyaratan yang tidak jelas, atau hanya satu produk yang bisa memenuhinya.", "Pertanyaan peserta saat pemberian penjelasan, dan persyaratan mana yang tidak dipenuhi tiap penawaran."],
        ["Harga di atas HPS", "HPS tidak memperhitungkan pengiriman, pemasangan, layanan, atau biaya lain yang dimasukkan peserta.", "Apa yang dicakup HPS, dibandingkan apa yang diminta dokumen pemilihan untuk dimasukkan peserta."],
    ],
)

roles_table = table(
    ["Peran", "Tugas yang lazim", "Panduan yang paling berguna"],
    [
        ["Pengguna klinis (dokter, bidan, perawat, petugas laboratorium)", "Menjelaskan kebutuhan klinis, dan memastikan spesifikasi masuk akal dalam praktik", '<a href="specification.html">Spesifikasi</a>'],
        ["Petugas teknik dan pemeliharaan (misalnya IPSRS di rumah sakit)", "Memeriksa persyaratan teknis, kebutuhan pemasangan, pemeliharaan, dan suku cadang", '<a href="specification.html">Spesifikasi</a> dan <a href="technology.html">Teknologi</a>'],
        ["PPK", "Menetapkan spesifikasi teknis dan HPS, menandatangani dan mengelola kontrak, serta menerima barang saat serah terima", '<a href="specification.html">Spesifikasi</a>, <a href="pricing.html">Harga</a>, dan <a href="regulation.html">Regulasi</a>'],
        ["Pokja Pemilihan", "Menyusun dokumen pemilihan, menjalankan tender, menjawab pertanyaan peserta, dan mengevaluasi penawaran", '<a href="process.html">Proses</a> dan <a href="regulation.html">Regulasi</a>'],
        ["Penyedia", "Mengajukan penawaran, lalu mengirim, memasang, melatih, dan memberi layanan sesuai kontrak", "&nbsp;"],
    ],
)

process = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Bagaimana membelinya tanpa tender gagal?</h1>
        <p class="lead">Banyak tender gagal karena keputusan yang diambil sebelum tender dibuka. Misalnya cara membagi paket, cara penawaran dinilai, dan berapa lama waktu yang diberikan kepada peserta.</p>
{reviewed('guide-3')}
      </header>

{keypoints('3')}
      <div class="clauses">
{proc_clauses}
      </div>

      <h2 class="section-title">Siapa melakukan apa dalam tender pemerintah</h2>
      <p class="section-lead">Peran yang lazim menurut Peraturan Presiden Nomor 16 Tahun 2018 tentang Pengadaan Barang/Jasa Pemerintah beserta perubahannya. Pembagian tugas di instansi Anda bisa berbeda. Pembelian melalui e-katalog biasanya ditangani PPK atau Pejabat Pengadaan, bukan Pokja.</p>
{roles_table}

      <h2 class="section-title">Ketika tender gagal</h2>
      <p class="section-lead">Tiga penyebab umum tender gagal, dan hal yang perlu diperiksa lebih dulu. Bisa lebih dari satu yang terjadi.</p>
{fail_table}

{related('3')}
{pager('process.html')}
    </div>"""

# ------------------------------------------------------------------ Regulasi dan standar

reg_clauses = "\n".join([
    clause("A.1", "Periksa izin edar lebih dulu",
           ["Alat kesehatan wajib memiliki izin edar dari Kementerian Kesehatan sebelum boleh dijual di Indonesia. Nomornya diawali AKD untuk alat buatan dalam negeri dan AKL untuk alat impor. Siapa pun dapat mencari produk di situs <a href=\"https://infoalkes.kemkes.go.id/\">Info Alkes</a> milik Kementerian."],
           "Apakah nomor dalam penawaran cocok dengan produk dan tipe yang persis sama di basis data publik, dan apakah masih berlaku?",
           "Cari produknya di Info Alkes, lalu pastikan produsen, tipe, dan nomor AKD atau AKL-nya sama dengan yang tertulis di penawaran."),
    clause("A.2", "Ketahui kelas risikonya",
           ["Alat kesehatan dibagi ke dalam empat kelas, dari A (risiko rendah) sampai D (risiko tinggi), mengikuti ASEAN Medical Device Directive. Alat kesehatan diagnostik in vitro (alat tes laboratorium) memakai empat huruf yang sama. Makin tinggi kelasnya, makin banyak bukti yang harus diserahkan produsen saat pendaftaran."],
           "Termasuk kelas apa alat ini, dan apakah dokumen dalam penawaran sesuai dengan kelas itu?",
           "Minta peserta menyebutkan kelas risiko alatnya, lalu periksa apakah dokumen pendaftaran dalam penawaran menunjukkan kelas yang sama."),
    clause("A.3", "Periksa siapa pembuatnya dan bagaimana mutunya dikendalikan",
           ["Pendaftaran biasanya mensyaratkan sertifikat ISO 13485 milik produsen yang diterbitkan lembaga terakreditasi. Alat buatan dalam negeri juga memerlukan sertifikat cara pembuatan alat kesehatan yang baik (CPAKB). Sertifikat ini menunjukkan bahwa pabrik bekerja dengan sistem yang terkendali, tetapi tidak membuktikan bahwa suatu alat tertentu berkinerja baik."],
           "Apakah sertifikat mutu produsen masih berlaku, dan apakah ruang lingkupnya mencakup produk ini?",
           "Sertifikat ISO 13485 yang hanya mencakup monitor pasien tidak mencakup infant warmer dari pabrik yang sama. Baca ruang lingkup yang tertulis pada sertifikatnya."),
    clause("A.4", "Periksa siapa penjualnya",
           ["Distributor wajib menerapkan cara distribusi alat kesehatan yang baik (CDAKB). Penjual juga sebaiknya memiliki surat penunjukan dari produsen. Surat ini paling penting setelah alat tiba, saat Anda membutuhkan suku cadang dan layanan."],
           "Dapatkah penjual menunjukkan surat penunjukan dari produsen, dan apakah surat itu mencakup layanan selama seluruh umur pakai alat?",
           "Surat penunjukan yang baik menyebutkan nama distributor, produk, dan masa berlakunya, serta ditandatangani produsen."),
    clause("A.5", "Minta standar beserta buktinya",
           ["Dengan standar, pembeli dan penjual sepakat tentang arti &ldquo;aman&rdquo;. Sebutkan standar yang berlaku untuk alat itu beserta edisinya, dan mintalah laporan ujinya. Tabel di bawah memuat standar yang paling sering disebut."],
           "Untuk setiap standar dalam penawaran: edisi berapa, diuji oleh siapa, dan pada tipe yang mana?",
           "&ldquo;Memenuhi IEC 60601-1&rdquo; adalah klaim. &ldquo;IEC 60601-1:2005+AMD1:2012+AMD2:2020, laporan uji nomor &hellip;, dari laboratorium &hellip;, untuk tipe &hellip;&rdquo; adalah bukti."),
    clause("A.6", "Periksa TKDN",
           ["Pembeli pemerintah wajib mengutamakan produk dalam negeri. Kandungan lokal disertifikasi dalam bentuk persentase, yaitu TKDN. Jika ada produk dalam negeri dengan TKDN yang mencukupi, produk impor tidak boleh dibeli sebagai gantinya. Aturan perhitungan dan sertifikasi TKDN berubah pada 2025, jadi periksa aturan yang berlaku sebelum mengandalkan suatu angka."],
           "Apakah ada produk dalam negeri yang memenuhi spesifikasi, dan berapa nilai pada sertifikat TKDN-nya?",
           "Sebelum menyimpulkan bahwa tidak ada produk dalam negeri yang memenuhi syarat, cari sertifikat TKDN produknya di basis data TKDN Kementerian Perindustrian."),
    clause("A.7", "Anggarkan kalibrasi setiap tahun",
           ["Setiap alat kesehatan yang dipakai di fasilitas pelayanan kesehatan wajib diuji atau dikalibrasi paling sedikit sekali setahun oleh institusi penguji yang berwenang. Ini biaya dan pekerjaan yang berulang setiap tahun, mulai tahun setelah alat diterima."],
           "Siapa yang akan mengalibrasi alat ini setiap tahun, dan apakah biayanya sudah dianggarkan?",
           "Jika tahun ini Anda membeli sepuluh infant warmer, anggaran tahun depan perlu memuat sepuluh kalibrasi."),
    clause("A.8", "Ketahui cara melaporkan masalah",
           ["Kementerian Kesehatan mengelola sistem pemantauan nasional alat kesehatan, yaitu e-Watch Alkes. Kementerian juga menerbitkan panduan pelaporan kejadian tidak diinginkan (KTD), yaitu kejadian ketika alat mencederai atau dapat mencederai pasien. Petugas yang tahu caranya melapor lebih cepat, dan laporan yang cepat melindungi pasien berikutnya."],
           "Jika besok alat ini mencederai pasien, siapa di fasilitas Anda yang akan melaporkannya, dan bagaimana caranya?",
           "Tunjuk satu orang di setiap fasilitas untuk melaporkan masalah alat, dan tempel langkah pelaporannya di dekat alat."),
])

standards_table = table(
    ["Standar", "Yang diatur", "Kapan disebutkan"],
    [
        ["IEC 60601-1", "Keselamatan dasar dan kinerja esensial peralatan listrik medis", "Setiap alat kesehatan yang memakai listrik PLN atau baterai"],
        ["IEC 60601-1-2", "Kompatibilitas elektromagnetik: alat tidak mengganggu peralatan lain, dan tidak terganggu olehnya", "Alat yang sama, terutama jika beberapa alat dipakai berdampingan"],
        ["Seri IEC 60601-2", 'Persyaratan tambahan untuk satu jenis alat. <a href="https://webstore.iec.ch/publication/64028">IEC 60601-2-21</a>, misalnya, mengatur infant radiant warmer', "Setiap kali ada standar khusus untuk jenis alat itu"],
        ['<a href="https://www.iso.org/standard/59752.html">ISO 13485</a>', "Sistem manajemen mutu produsen", "Sebagai bukti tentang produsen, bukan tentang alatnya"],
        ["ISO 14971", "Cara produsen menemukan dan mengendalikan risiko", "Untuk alat berisiko lebih tinggi, bersama analisis risikonya"],
        ["IEC 62304", "Cara perangkat lunak alat kesehatan dikembangkan dan dipelihara", "Setiap alat yang bergantung pada perangkat lunak"],
        ["IEC 62366-1", "Kebergunaan: desain yang mencegah kesalahan pengguna", "Alat yang keselamatannya bergantung pada cara pengguna mengoperasikannya"],
    ],
)

regulation = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Apa yang wajib dipenuhi sebuah alat?</h1>
        <p class="lead">Alat kesehatan harus memenuhi regulasi Indonesia sebelum boleh dijual atau dipakai, dan alat yang baik dibuat serta diuji menurut standar yang dipublikasikan. Mengetahui dokumen apa yang harus diminta adalah cara tercepat membedakan penawaran yang benar-benar memenuhi syarat dari yang hanya mengaku memenuhi.</p>
{reviewed('guide-a')}
      </header>

{keypoints('A')}
      <div class="clauses">
{reg_clauses}
      </div>

      <h2 class="section-title">Standar yang paling sering disebut</h2>
      <p class="section-lead">Standar diperbarui dari waktu ke waktu. Selalu sebutkan edisinya, dan periksa kepada penerbitnya edisi mana yang berlaku.</p>
{standards_table}

      <h2 class="section-title">Sumber</h2>
      <div class="prose">
        <p>Prinsip di halaman ini diperiksa pada 11 Oktober 2026. Regulasi bisa berubah, jadi pastikan teks terbarunya sebelum mengandalkannya.</p>
        <ul>
          <li><a href="https://jdih.kemkes.go.id/storage/documents/pdfs/2017permenkes062.pdf">Peraturan Menteri Kesehatan Nomor 62 Tahun 2017</a> tentang Izin Edar Alat Kesehatan, Alat Kesehatan Diagnostik In Vitro dan Perbekalan Kesehatan Rumah Tangga.</li>
          <li><a href="https://regalkes.kemkes.go.id/informasi_alkes/Indonesia%20Guideline%20for%20Evaluation%20of%20Medical%20Device%20and%20IVD%202020.pdf">Indonesia Guideline for Evaluation of Medical Device and IVD (2020)</a>, Kementerian Kesehatan.</li>
          <li><a href="https://regalkes.kemkes.go.id/informasi_alkes/TataCaraKlasifikasi1.pdf">Tata cara klasifikasi alat kesehatan berdasarkan risiko</a>, Kementerian Kesehatan.</li>
          <li><a href="https://farmalkes.kemkes.go.id/2024/07/bijak-memilih-dan-menggunakan-alkes-dan-pkrt/">Cara memeriksa nomor izin edar</a>, Direktorat Jenderal Kefarmasian dan Alat Kesehatan (2024).</li>
          <li><a href="https://farmalkes.kemkes.go.id/unduh/modul-cara-distribusi-alat-kesehatan-yang-baik/">Modul cara distribusi alat kesehatan yang baik</a>, merujuk Peraturan Menteri Kesehatan Nomor 4 Tahun 2014.</li>
          <li><a href="https://peraturan.bpk.go.id/Download/107180/Permenkes%20Nomor%2054%20Tahun%202015.pdf">Peraturan Menteri Kesehatan Nomor 54 Tahun 2015</a> tentang Pengujian dan Kalibrasi Alat Kesehatan.</li>
          <li><a href="https://bbt.kemenperin.go.id/blog/menperin:-regulasi-baru-tkdn-prioritaskan-produk-lokal-dan-pacu-investasi">Pernyataan Kementerian Perindustrian tentang aturan TKDN yang baru</a> (Oktober 2025).</li>
          <li><a href="https://farmalkes.kemkes.go.id/unduh/tata-cara-pelaporan-kejadian-tidak-diinginkan-ktd-alat-kesehatan/">Tata cara pelaporan kejadian tidak diinginkan (KTD) alat kesehatan</a>, Kementerian Kesehatan (2020).</li>
        </ul>
      </div>

{related('A')}
{pager('regulation.html')}
    </div>"""

# ------------------------------------------------------------------ Teknologi dan riset

tech_clauses = "\n".join([
    clause("B.1", "Pahami cara kerjanya",
           ["Setiap alat mengukur atau menghasilkan sesuatu yang bersifat fisik, seperti panas, tekanan, cahaya, atau sinyal listrik. Dengan mengetahuinya, Anda tahu apa yang membatasi akurasinya, apa yang dibutuhkannya dari lingkungan sekitar, dan bagian apa yang biasanya rusak lebih dulu."],
           "Dapatkah Anda menjelaskan dalam dua kalimat bagaimana alat ini menjalankan tugasnya?",
           "Radiant warmer memanaskan bayi dari atas dengan panas inframerah, sehingga petugas bisa merawat bayi tanpa menyelimutinya. Karena itu alat ini memerlukan sensor suhu kulit untuk mengendalikan panasnya."),
    clause("B.2", "Pisahkan yang penting bagi pasien dari fitur tambahan",
           ["Teknologi inti menentukan seberapa baik alat bekerja bagi pasien. Fitur tambahan menambah kenyamanan, dan sering menambah harga. Dua alat dengan teknologi inti yang sama bisa berbeda jauh harganya karena layar, konektivitas, atau perangkat lunak yang tidak mengubah apa pun bagi pasien."],
           "Fitur mana dalam daftar itu yang mengubah hasil bagi pasien?",
           "Pada analyzer, metode pengukuran menentukan akurasi hasil. Layar sentuh yang lebih besar atau Wi-Fi tidak."),
    clause("B.3", "Tanyakan bukti di balik setiap klaim",
           ["Bobot bukti tidak sama. Laporan uji independen atau studi yang ditelaah sejawat lebih kuat daripada data produsen sendiri, dan keduanya lebih kuat daripada brosur. Izin edar menunjukkan bahwa alat boleh dijual, bukan bahwa alat itu pilihan yang tepat bagi Anda."],
           "Untuk klaim kinerja utamanya: siapa yang mengukurnya, dan apakah mereka independen dari penjual?",
           "Brosur menulis &ldquo;sangat akurat&rdquo;. Evaluasi independen melaporkan seberapa dekat hasilnya dengan metode rujukan, dan pada berapa sampel."),
    clause("B.4", "Periksa riwayat pemakaiannya",
           ["Cari tahu sudah berapa lama tipe itu dijual, di mana saja dipakai, dan apakah pernah ditarik atau disebut dalam pemberitahuan keselamatan. Fasilitas yang sudah memakainya adalah sumber informasi terbaik, dan biasanya mereka bersedia berbagi."],
           "Di mana tipe ini sudah dipakai, dan apa kata para penggunanya?",
           "Minta penjual menyebutkan tiga fasilitas yang sudah memakai tipe itu lebih dari setahun, lalu hubungi setidaknya satu di antaranya."),
    clause("B.5", "Sesuaikan teknologi dengan tingkat layanan",
           ["Alat paling canggih belum tentu pilihan terbaik untuk setiap fasilitas. WHO, UNFPA, dan UNICEF menerbitkan <a href=\"https://www.who.int/publications/i/item/9789241565028\">daftar bersama alat kesehatan prioritas</a> untuk kesehatan ibu, bayi baru lahir, dan anak. Daftar ini disusun menurut tingkat layanan. Platform <a href=\"https://medevis.who-healthtechnologies.org/\">MeDevIS</a> milik WHO memuat lebih dari 2.300 jenis alat beserta tingkat layanan yang sesuai. Di Indonesia, komite penilaian teknologi kesehatan yang dibentuk Kementerian Kesehatan pada 2014 menelaah bukti untuk teknologi yang dipertimbangkan masuk ke manfaat JKN."],
           "Apakah teknologi ini dirancang untuk fasilitas seperti milik Anda, dengan tenaga dan jumlah pasien seperti di tempat Anda?",
           "Analyzer kimia otomatis penuh mungkin cocok untuk laboratorium rumah sakit kabupaten. Puskesmas mungkin lebih terbantu oleh analyzer semi-otomatis yang lebih kecil, yang bisa dijalankan dan dirawat petugasnya sendiri."),
    clause("B.6", "Rencanakan seluruh umur pakainya",
           ["Alat dipakai bertahun-tahun setelah garansinya habis. Tanyakan berapa lama suku cadang akan tersedia. Tanyakan bagaimana perangkat lunak diperbarui dan siapa yang membayarnya. Tanyakan juga kapan produsen berencana menghentikan dukungan untuk tipe itu."],
           "Berapa tahun produsen menjanjikan suku cadang dan dukungan perangkat lunak?",
           "Minta peserta menyatakan secara tertulis sampai tahun berapa suku cadang tipe ini akan tersedia."),
    clause("B.7", "Hati-hati dengan teknologi baru",
           ["Teknologi baru bisa masuk pasar sebelum ada bukti bahwa ia bekerja dengan baik. Membeli terlalu awal berarti membayar untuk menemukan masalahnya. Untuk apa pun yang baru, carilah evaluasi oleh pihak selain produsen sebelum membelinya untuk satu kabupaten."],
           "Apakah teknologi ini sudah dievaluasi oleh pihak yang tidak mendapat untung dari penjualannya?",
           "Uji coba tes cepat yang baru di satu fasilitas dan bandingkan hasilnya dengan laboratorium, sebelum membelinya untuk semua puskesmas."),
])

evidence_table = table(
    ["Sumber", "Yang ada di sana", "Gunakan untuk"],
    [
        ['<a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a>', "Studi yang ditelaah sejawat tentang alat dan teknologi di baliknya", "Bukti independen tentang akurasi dan manfaat klinis"],
        ['<a href="https://medevis.who-healthtechnologies.org/">WHO MeDevIS</a>', "Lebih dari 2.300 jenis alat kesehatan, dengan tingkat layanan dan infrastruktur yang dibutuhkan masing-masing", "Memastikan alat cocok untuk jenis fasilitas Anda sebelum menulis spesifikasinya"],
        ['<a href="https://www.who.int/publications/i/item/9789241565028">Daftar antarlembaga WHO, UNFPA, dan UNICEF</a>', "Alat kesehatan prioritas untuk kesehatan ibu, bayi baru lahir, dan anak, menurut tingkat layanan", "Menentukan apakah suatu teknologi layak berada di jenis fasilitas Anda"],
        ['<a href="https://supply.unicef.org/">UNICEF Supply Catalogue</a>', "Spesifikasi teknis dan harga indikatif untuk alat yang dipasok UNICEF", "Spesifikasi acuan yang ditulis untuk tempat dengan sumber daya terbatas"],
        ['<a href="https://infoalkes.kemkes.go.id/">Info Alkes</a>', "Alat, produsen, dan distributor yang terdaftar di Indonesia", "Memastikan suatu tipe memiliki izin edar, dan siapa pemasoknya"],
        ['<a href="https://e-watch-alkes.kemkes.go.id/">e-Watch Alkes</a>', "Sistem pemantauan nasional alat kesehatan di Indonesia", "Melaporkan masalah pada alat"],
    ],
)

technology = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Bagaimana menilai teknologinya?</h1>
        <p class="lead">Anda tidak perlu merancang alat untuk bisa menilainya. Anda perlu tahu cara kerjanya, bukti apa yang mendukungnya, dan apakah alat itu cocok untuk tempat ia akan dipakai.</p>
{reviewed('guide-b')}
      </header>

{keypoints('B')}
      <div class="clauses">
{tech_clauses}
      </div>

      <h2 class="section-title">Di mana mencari buktinya</h2>
      <p class="section-lead">Sumber publik yang layak diperiksa sebelum pembelian apa pun. Semuanya gratis.</p>
{evidence_table}

      <div class="prose">
        <h2>Catatan teknologi</h2>
        <p>Penjelasan singkat tentang cara kerja jenis alat tertentu akan diterbitkan bersama kajian alat. {IN_PREP}</p>
        <p>Sumber halaman ini: <a href="https://dara.ui.ac.id/research-output/0275fc74-f03e-4cc6-8a89-048e47c2f4a5">tulisan tentang penilaian teknologi kesehatan di Indonesia</a>, untuk komite yang dibentuk pada 2014. <a href="https://farmalkes.kemkes.go.id/unduh/tata-cara-pelaporan-kejadian-tidak-diinginkan-ktd-alat-kesehatan/">Halaman layanan alat kesehatan</a> Kementerian Kesehatan, untuk e&#8209;Watch Alkes.</p>
      </div>

{related('B')}
{pager('technology.html')}
    </div>"""

# ------------------------------------------------------------------ Kajian alat

dossier_parts = table(
    ["Bagian", "Pertanyaan yang dijawab", "Isinya"],
    [
        ['<a href="specification.html">Spesifikasi</a>', "Apa yang harus kita minta?", "Spesifikasi acuan yang tidak menyebut merek, persyaratan yang penting secara klinis, dan standar yang perlu disebutkan."],
        ['<a href="pricing.html">Harga</a>', "Berapa harga yang wajar?", "Harga acuan yang dipublikasikan, apa yang dicakup masing-masing, dan mengapa harganya berbeda."],
        ['<a href="process.html">Proses</a>', "Bagaimana membelinya tanpa tender gagal?", "Cara membagi paket, cara menilai penawaran, dan pertanyaan yang biasa diajukan peserta."],
    ],
)

dossiers = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Kajian alat</h1>
        <p class="lead">Kajian alat adalah laporan singkat tentang satu alat. Kajian menjawab ketiga pertanyaan untuk alat itu, dalam beberapa halaman, untuk tim yang harus membelinya.</p>
      </header>

      <div class="prose">
        <h2>Isi sebuah kajian</h2>
{dossier_parts}

        <h2>Cara kajian disusun</h2>
        <p>Setiap kajian mengikuti enam langkah yang sama, sehingga dua kajian mana pun dapat dibandingkan dan setiap klaim dapat ditelusuri.</p>
        <ol class="steps">
          <li>Sumber publik dikumpulkan, dan masing-masing dicatat beserta tautan dan tanggal dibacanya.</li>
          <li>Spesifikasi ditulis mengikuti <a href="specification.html">tiga belas bagian templat WHO</a>, sama untuk setiap alat.</li>
          <li>Harga acuan disusun dari angka yang dikutip, masing-masing dengan cakupannya.</li>
          <li>Draf diperiksa terhadap dua aturan penerbitan di bawah.</li>
          <li>Seseorang yang memakai alat itu dalam praktik klinis membacanya sebelum diterbitkan.</li>
          <li>Kajian diterbitkan dengan nomor versi dan tanggal, dan setiap koreksi dicatat di halamannya.</li>
        </ol>

        <h2>Sedang disusun</h2>
{STATUS_TABLE}

        <h2>Kapan kajian diterbitkan</h2>
        <p>Kajian hanya diterbitkan jika kedua hal ini terpenuhi:</p>
        <ul>
          <li>Seluruh isinya berasal dari dokumen publik, dan setiap sumber dikutip.</li>
          <li>Kajian itu tidak menyangkut tender yang masih dalam tahap evaluasi.</li>
        </ul>
        <p>Kajian tidak menilai merek atau merekomendasikan tipe tertentu. Kajian menjelaskan apa yang perlu diminta, apa yang dicakup harga yang wajar, dan cara menjalankan pengadaannya.</p>
      </div>
    </div>"""

# ------------------------------------------------------------------ Tentang

about = """    <div class="wrap">
      <header class="page-head">
        <h1>Tentang SistemSehat</h1>
        <p class="lead">SistemSehat menerbitkan panduan independen tentang pembelian alat kesehatan: spesifikasi teknis, harga, dan proses pengadaan, dengan latar belakang tentang regulasi, standar, dan teknologinya.</p>
      </header>

      <div class="prose">
        <h2>Untuk siapa situs ini</h2>
        <p>Untuk orang-orang di dinas kesehatan dan rumah sakit pemerintah di Indonesia yang terlibat dalam pembelian alat kesehatan:</p>
        <ul>
          <li>pejabat pengadaan, seperti PPK dan Pokja Pemilihan;</li>
          <li>klinisi yang membantu menulis spesifikasi dan memeriksa barang yang datang;</li>
          <li>petugas teknik dan pemeliharaan;</li>
          <li>perencana yang menyusun anggaran.</li>
        </ul>

        <h2>Mengapa situs ini ada</h2>
        <p>Tim-tim ini diminta menyusun spesifikasi dan harga untuk peralatan yang rumit, sering kali dengan sedikit bahan rujukan independen. Penyedia mengenal produknya secara rinci. Pembeli membutuhkan panduan yang sama cermatnya, dari pihak yang tidak menjual apa pun.</p>

        <h2>Mengapa namanya SistemSehat</h2>
        <p>Sistem kesehatan bergantung pada peralatannya, dan membeli alat yang tepat dengan harga yang wajar membantu menjaga sistem itu tetap sehat.</p>

        <h2>Siapa di baliknya</h2>
        <p>SistemSehat dimulai oleh Aminul Solihin, insinyur biomedis lulusan Institut Teknologi Bandung. Ia memimpin pengembangan tiga alat kesehatan dari purwarupa hingga ke pasar sebelum beralih ke pengadaan pemerintah.</p>

        <h2>Pengungkapan</h2>
        <p>Aminul bekerja di bidang pengadaan sektor publik di Indonesia. SistemSehat adalah inisiatif pribadi. Situs ini tidak terkait dengan atau didukung oleh pemberi kerjanya, lembaga pemerintah mana pun, atau pemberi pinjaman mana pun. Tidak ada isi situs ini yang mewakili pandangan mereka.</p>

        <h2 id="how">Cara kerjanya</h2>
        <ul>
          <li><strong>Hanya sumber publik.</strong> Setiap angka dan persyaratan berasal dari dokumen yang dapat diunduh siapa saja, dan masing-masing dikutip.</li>
          <li><strong>Tanpa uang dari penjual.</strong> Tidak ada dana, hadiah, atau konten bersponsor dari produsen maupun distributor.</li>
          <li><strong>Bukan tender yang sedang berjalan.</strong> Tidak ada yang diterbitkan tentang tender yang masih dalam tahap evaluasi.</li>
          <li><strong>Tanpa pemeringkatan merek.</strong> Panduan ini menjelaskan apa yang perlu diminta dan cara membelinya, bukan produk mana yang harus dipilih.</li>
          <li><strong>Koreksi secara terbuka.</strong> Jika ada yang keliru atau sudah tidak berlaku, akan diperbaiki dan perubahannya dicatat di halaman itu.</li>
        </ul>

        <h2>Status</h2>
        <p>SistemSehat adalah proyek yang sedang berjalan dan belum menjadi organisasi berbadan hukum. Tujuannya adalah menjadikannya lembaga nirlaba.</p>
        <!-- KONTAK: tambahkan satu baris berisi alamat email atau tautan LinkedIn sebelum situs ditayangkan. Samakan dengan versi bahasa Inggris. -->
      </div>
    </div>"""

# ------------------------------------------------------------------ Daftar periksa

checklist = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Daftar periksa</h1>
        <p class="lead">Semua pertanyaan &ldquo;Tanyakan&rdquo; dari kelima panduan, di satu tempat. Centang di layar, atau cetak daftarnya untuk rapat Anda.</p>
        <p class="reviewed">{len(S['registry'])} pertanyaan. Terakhir ditinjau {REVIEWED}. Di bawah setiap pertanyaan ada tautan ke prinsip asalnya.</p>
      </header>

      <div class="checklist">
{checklist_groups()}
      </div>
    </div>"""

# ------------------------------------------------------------------ Glosarium
# The ids match the English glossary, so a link to a term survives a language switch.

az, rows, n_terms = glossary_list([
    ("acceptance-test", "Uji terima", "Pemeriksaan saat alat diserahkan, untuk memastikan alat berfungsi dan sesuai kontrak sebelum pembeli menerimanya.", [r"(?i:\buji terima\b)"]),
    ("adverse-event", "Kejadian tidak diinginkan (KTD)", "Kejadian ketika alat mencederai, atau dapat mencederai, pasien atau pengguna.", [r"(?i:\bkejadian tidak diinginkan\b)", r"\bKTD\b"]),
    ("akd-and-akl", "AKD dan AKL", "Huruf awal nomor izin edar alat kesehatan di Indonesia. AKD berarti alat dibuat di dalam negeri; AKL berarti alat impor.", [r"\bAKD\b", r"\bAKL\b"]),
    ("alkes", "Alkes", "Singkatan dari alat kesehatan.", [r"\bAlkes\b"]),
    ("amendment", "Adendum", "Perubahan resmi atas dokumen pemilihan, disampaikan kepada semua peserta sebelum batas waktu penawaran.", [r"(?i:\badendum\b)"]),
    ("asean", "ASEAN", "Perhimpunan Bangsa-Bangsa Asia Tenggara. ASEAN Medical Device Directive menetapkan kelas risiko A sampai D yang diikuti Indonesia.", [r"\bASEAN\b"]),
    ("bidder", "Peserta", "Pelaku usaha yang mengajukan penawaran dalam tender.", [r"(?i:\bpeserta\b)"]),
    ("calibration", "Kalibrasi", "Pemeriksaan hasil ukur alat terhadap acuan yang diketahui, dan penyetelan bila perlu.", [r"(?i:\b(?:kalibrasi|dikalibrasi|mengalibrasi)\b)"]),
    ("cdakb", "CDAKB", "Cara Distribusi Alat Kesehatan yang Baik: pedoman yang wajib diterapkan distributor alat kesehatan di Indonesia.", [r"\bCDAKB\b"]),
    ("commissioning", "Uji fungsi", "Pengujian alat yang baru dipasang untuk memastikan alat berfungsi sebelum dipakai.", [r"(?i:\buji fungsi\b)"]),
    ("consumables", "Bahan habis pakai", "Barang yang dihabiskan alat saat dipakai, seperti reagen, sensor, filter, atau kertas.", [r"(?i:\bbahan habis pakai\b)"]),
    ("cpakb", "CPAKB", "Cara Pembuatan Alat Kesehatan yang Baik: pedoman produksi yang disertifikasi untuk produsen alat kesehatan di Indonesia.", [r"\bCPAKB\b"]),
    ("e-watch-alkes", "e-Watch Alkes", "Sistem pemantauan nasional alat kesehatan yang dikelola Kementerian Kesehatan. Masalah pada alat dilaporkan di sini.", [r"e(?:-|\u2011|&#8209;)Watch Alkes"]),
    ("ecri", "ECRI", "Organisasi nirlaba independen di Amerika Serikat yang menguji alat kesehatan dan melaporkan keselamatannya.", [r"\bECRI\b"]),
    ("emdn", "EMDN", "European Medical Device Nomenclature: sistem penamaan jenis alat kesehatan yang terutama dipakai di negara-negara Eropa.", [r"\bEMDN\b"]),
    ("gmdn", "GMDN", "Global Medical Device Nomenclature: sistem penamaan jenis alat kesehatan yang dipakai otoritas regulasi di banyak negara.", [r"\bGMDN\b"]),
    ("hps", "HPS", "Harga perkiraan sendiri: perkiraan harga yang disusun pembeli pemerintah sebelum tender, untuk menilai harga penawaran.", [r"\bHPS\b"]),
    ("hta", "HTA", 'Penilaian teknologi kesehatan (<em lang="en">health technology assessment</em>): telaah terstruktur atas hasil dan biaya suatu teknologi, untuk memutuskan apakah sistem kesehatan perlu membiayainya.', [r"\bHTA\b", r"(?i:\bpenilaian teknologi kesehatan\b)"]),
    ("iec", "IEC", "International Electrotechnical Commission. Lembaga ini menerbitkan standar keselamatan untuk peralatan listrik medis, seperti IEC 60601-1.", [r"\bIEC\b"]),
    ("inaproc-katalog-elektronik", "INAPROC Katalog Elektronik", "Katalog elektronik nasional untuk pengadaan pemerintah, dikelola LKPP.", [r"INAPROC Katalog Elektronik"]),
    ("info-alkes", "Info Alkes", "Basis data publik Kementerian Kesehatan tentang alat kesehatan, produsen, dan distributor yang terdaftar.", [r"\bInfo Alkes\b"]),
    ("ipsrs", "IPSRS", "Instalasi Pemeliharaan Sarana Rumah Sakit: unit rumah sakit yang merawat peralatan dan bangunan.", [r"\bIPSRS\b"]),
    ("iso", "ISO", "International Organization for Standardization. Lembaga ini menerbitkan standar seperti ISO 13485 tentang manajemen mutu produsen alat kesehatan.", [r"\bISO\b"]),
    ("ivd", "IVD", "Alat kesehatan diagnostik in vitro: alat untuk menguji sampel dari tubuh, seperti darah atau urine.", [r"\bIVD\b", r"(?i:\bdiagnostik in vitro\b)"]),
    ("izin-edar", "Izin edar", "Izin dari Kementerian Kesehatan yang wajib dimiliki alat kesehatan sebelum boleh dijual di Indonesia.", [r"(?i:\bizin edar\b)"]),
    ("jisdor", "JISDOR", "Jakarta Interbank Spot Dollar Rate: kurs referensi harian rupiah terhadap dolar Amerika Serikat yang diterbitkan Bank Indonesia.", [r"\bJISDOR\b"]),
    ("jkn", "JKN", "Jaminan Kesehatan Nasional, dikelola BPJS Kesehatan.", [r"\bJKN\b"]),
    ("lkpp", "LKPP", "Lembaga Kebijakan Pengadaan Barang/Jasa Pemerintah: lembaga yang menyusun kebijakan pengadaan pemerintah.", [r"\bLKPP\b"]),
    ("lot", "Paket", 'Bagian tender yang ditawar dan dikontrakkan tersendiri, sering kali satu jenis alat atau satu wilayah. Dalam dokumen berbahasa Inggris disebut <em lang="en">lot</em>.', [r"(?i:\bpaket\b)"]),
    ("model-specification", "Spesifikasi acuan", "Spesifikasi untuk satu jenis alat yang tidak menyebut merek, sebagai titik awal yang disesuaikan pembeli dengan kebutuhannya.", [r"(?i:\bspesifikasi acuan\b)"]),
    ("particular-standard", "Standar khusus", "Standar dalam seri IEC 60601-2 yang memuat persyaratan tambahan untuk satu jenis peralatan listrik medis.", [r"(?i:\bstandar khusus\b)"]),
    ("pokja-pemilihan", "Pokja Pemilihan", "Kelompok kerja yang menjalankan tender pemerintah: menyusun dokumen pemilihan, menjawab pertanyaan peserta, dan mengevaluasi penawaran.", [r"\bPokja Pemilihan\b", r"\bPokja\b"]),
    ("poned", "PONED", "Pelayanan Obstetri Neonatal Emergensi Dasar: layanan gawat darurat dasar untuk ibu dan bayi baru lahir, di puskesmas yang ditunjuk.", [r"\bPONED\b"]),
    ("ppk", "PPK", "Pejabat Pembuat Komitmen: pejabat yang menetapkan spesifikasi teknis dan HPS, serta menandatangani dan mengelola kontrak.", [r"\bPPK\b"]),
    ("pre-bid-meeting", "Pemberian penjelasan", "Rapat tempat pembeli menjelaskan tender dan menjawab pertanyaan calon peserta. Sering disebut <em>aanwijzing</em>.", [r"(?i:\bpemberian penjelasan\b)"]),
    ("puskesmas", "Puskesmas", "Pusat kesehatan masyarakat: fasilitas yang memberikan pelayanan kesehatan primer.", [r"(?i:\bpuskesmas\b)"]),
    ("rated-criteria", "Sistem nilai", "Metode evaluasi yang memberi skor pada mutu penawaran di samping harganya.", [r"(?i:\bsistem nilai\b)"]),
    ("reagent", "Reagen", "Bahan kimia yang dipakai analyzer laboratorium untuk menjalankan tes. Reagen dibeli berulang kali.", [r"(?i:\breagen\b)"]),
    ("reference-price", "Harga acuan", "Kisaran harga suatu alat yang disusun dari sumber yang dikutip, masing-masing dengan cakupannya, untuk menilai harga penawaran.", [r"(?i:\bharga acuan\b)"]),
    ("risk-class", "Kelas risiko", "Salah satu dari empat kelas, A sampai D, yang mengelompokkan alat kesehatan dari risiko rendah sampai tinggi.", [r"(?i:\bkelas risiko\b)"]),
    ("supplier", "Penyedia", "Pelaku usaha yang menjual dan mengirim barang dalam pengadaan pemerintah.", [r"(?i:\bpenyedia\b)"]),
    ("test-report", "Laporan uji", "Dokumen dari laboratorium penguji yang menunjukkan bahwa alat telah diuji terhadap suatu standar, beserta hasilnya.", [r"(?i:\blaporan uji\b)"]),
    ("tkdn", "TKDN", "Tingkat Komponen Dalam Negeri: persentase kandungan lokal suatu produk yang telah disertifikasi.", [r"\bTKDN\b"]),
    ("total-cost-of-ownership", "Biaya kepemilikan total", "Seluruh biaya alat selama masa pakainya: pembelian, pengiriman, pemasangan, bahan habis pakai, pemeliharaan, pelatihan, dan penghapusan.", [r"(?i:\bbiaya kepemilikan total\b)"]),
    ("umdns", "UMDNS", "Universal Medical Device Nomenclature System: sistem penamaan jenis alat kesehatan yang dikelola ECRI.", [r"\bUMDNS\b"]),
    ("unfpa", "UNFPA", "Dana Kependudukan Perserikatan Bangsa-Bangsa, badan yang menangani kesehatan seksual dan reproduksi.", [r"\bUNFPA\b"]),
    ("unicef", "UNICEF", "Dana Anak-Anak Perserikatan Bangsa-Bangsa. Lembaga ini membeli alat kesehatan untuk banyak negara dan menerbitkan spesifikasi serta harganya.", [r"\bUNICEF\b"]),
    ("ups", "UPS", "Uninterruptible power supply: unit baterai yang menjaga alat tetap menyala saat listrik padam.", [r"\bUPS\b"]),
    ("who", "WHO", "Organisasi Kesehatan Dunia, badan Perserikatan Bangsa-Bangsa untuk kesehatan.", [r"\bWHO\b", r"Organisasi Kesehatan Dunia"]),
])

glossary = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Glosarium</h1>
        <p class="lead">Istilah pengadaan dan singkatan yang dipakai di situs ini, dengan penjelasan singkat. Di dalam panduan, istilah yang bergaris bawah titik-titik tertaut ke penjelasannya di sini.</p>
        <p class="reviewed">{n_terms} istilah. Terakhir ditinjau {REVIEWED}.</p>
      </header>

      <div class="glossary-tools">
        <nav class="az" aria-label="Lompat ke huruf">
          <ul>{az}</ul>
        </nav>
        <div class="filter js-only">
          <label for="glossary-filter">Saring glosarium</label>
          <input id="glossary-filter" type="search" placeholder="Contoh: TKDN">
        </div>
      </div>
      <p id="glossary-count" class="reviewed" aria-live="polite"></p>

      <dl class="glossary">
{rows}
      </dl>
    </div>"""

# ------------------------------------------------------------------ Sumber rujukan (library.html)

WHO_ID = "Organisasi Kesehatan Dunia (WHO)"
KEMKES = "Kementerian Kesehatan"

library = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Sumber rujukan</h1>
        <p class="lead">Dokumen publik yang menjadi rujukan dan bahan belajar situs ini. Masing-masing unggul di satu bagian pekerjaan, dan semuanya gratis dibaca kecuali disebutkan lain. Sebagian besar berbahasa Inggris.</p>
        <p class="reviewed">Tautan diperiksa {REVIEWED}.</p>
      </header>

      <div class="prose library">
{library_group("Spesifikasi dan daftar alat", [
    ['<a href="https://www.who.int/publications/m/item/user-guide-who-technical-specification-for-medical-devices">Templat dan panduan pengguna spesifikasi teknis</a>', WHO_ID, "Templat berisi lima puluh isian dalam tiga belas bagian. Setiap kajian di sini memakai struktur ini."],
    ['<a href="https://medevis.who-healthtechnologies.org/">MeDevIS</a>', WHO_ID, "Lebih dari 2.300 jenis alat, dapat ditelusuri menurut tingkat layanan, unit layanan, dan jenisnya."],
    ['<a href="https://supply.unicef.org/">UNICEF Supply Catalogue</a>', "UNICEF", "Spesifikasi lengkap yang ditulis untuk tempat dengan sumber daya terbatas, dengan harga indikatif."],
    ['<a href="https://www.nhsrcindia.org/sites/default/files/2021-05/Technical%20Specifications%20of%20Medical%20Devices%20for%20Special%20Neonatal%20Care%20Unit.pdf">Spesifikasi teknis untuk unit perawatan neonatal khusus</a>', "National Health Systems Resource Centre, India", "Contoh kumpulan spesifikasi acuan nasional, disusun bersama klinisi, insinyur, dan produsen."],
    ['<a href="https://www.who.int/publications/i/item/9789241565028">Daftar alat kesehatan prioritas antarlembaga</a>', "WHO, UNFPA, dan UNICEF", "Alat apa yang sesuai untuk tingkat layanan mana, untuk kesehatan ibu, bayi baru lahir, dan anak."],
])}
{library_group("Harga", [
    ['<a href="https://www.theglobalfund.org/en/sourcing-management/procurement-tools">Alat bantu pengadaan dan harga acuan</a>', "The Global Fund", "Harga acuan dan waktu pengiriman per kategori produk, serta perkiraan biaya angkut, asuransi, dan pemeriksaan mutu."],
    ['<a href="https://katalog.inaproc.id/">INAPROC Katalog Elektronik</a>', "LKPP, Indonesia", "Penawaran dari penyedia dalam negeri di katalog elektronik nasional."],
])}
{library_group("Proses dan praktik", [
    ['<a href="https://www.open-contracting.org/what-is-open-contracting/health/">Open contracting for health</a>', "Open Contracting Partnership", "Panduan dan contoh dari berbagai negara tentang publikasi dan pemanfaatan data pengadaan kesehatan."],
    ['<a href="https://www.newborntoolkit.org/">Implementation Toolkit for Small and Sick Newborn Care</a>', "NEST360 dan UNICEF", "Panduan praktis yang disusun per tugas, termasuk bagian tentang peralatan dan perbekalan."],
])}
{library_group("Bukti dan keselamatan", [
    ['<a href="https://home.ecri.org/">ECRI</a>', "ECRI, organisasi nirlaba independen", "Evaluasi alat dan daftar tahunan bahaya teknologi kesehatan. Evaluasinya khusus untuk anggota."],
    ['<a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a>', "US National Library of Medicine", "Studi yang ditelaah sejawat tentang alat dan teknologi di baliknya."],
    ['<a href="https://infoalkes.kemkes.go.id/">Info Alkes</a>', KEMKES, "Memastikan alat memiliki izin edar di Indonesia, dan siapa pemasoknya."],
    ['<a href="https://e-watch-alkes.kemkes.go.id/">e-Watch Alkes</a>', KEMKES, "Sistem pemantauan nasional alat kesehatan."],
])}
      </div>
    </div>"""

# ------------------------------------------------------------------ Panduan

guide_cards_main = "\n".join(guide_card(g, "h2") for g in GUIDES[:3])
guide_cards_support = "\n".join(guide_card(g, "h2") for g in GUIDES[3:])

guides = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Panduan</h1>
        <p class="lead">Lima panduan dengan {len(S['registry'])} prinsip. Tiga mengikuti langkah pembelian. Dua memberi latar belakang yang dibutuhkan setiap pembelian.</p>
        <p class="reviewed">Setiap prinsip menjelaskan apa yang harus dilakukan, memberi contoh, dan ditutup dengan satu pertanyaan untuk Anda jawab.</p>
      </header>

      <div class="section-head">
        <h2 class="section-title">Tiga pertanyaan yang harus dijawab setiap pembelian</h2>
      </div>
      <ul class="cards cards-3">
{guide_cards_main}
      </ul>

      <div class="section-head section-head-sub">
        <h2 class="section-title">Dua panduan yang mendukung ketiganya</h2>
      </div>
      <ul class="cards cards-2">
{guide_cards_support}
      </ul>

      <section class="related related-spaced" aria-labelledby="related-title">
        <h2 id="related-title">Pakai panduan</h2>
        <ul class="link-list">
          <li><a href="checklist.html">Daftar periksa</a><span>Semua pertanyaan dari panduan, untuk dicentang atau dicetak</span></li>
          <li><a href="glossary.html">Glosarium</a><span>Penjelasan istilah dan singkatan yang dipakai di sini</span></li>
          <li><a href="library.html">Sumber rujukan</a><span>Dokumen publik di balik panduan</span></li>
          <li><a href="search.html">Pencarian</a><span>Cari prinsip atau istilah dengan kata kunci</span></li>
        </ul>
      </section>
    </div>"""

# ------------------------------------------------------------------ Pencarian

search = f"""    <div class="wrap">
      <header class="page-head">
        <h1>Pencarian</h1>
        <p class="lead">Cari di {len(S['registry'])} prinsip, glosarium, dan sumber rujukan.</p>
      </header>

      <form class="search search-large" action="search.html" method="get" role="search" aria-label="Pencarian baru">
        <label for="page-search">Cari</label>
        <div class="search-row">
          <input id="page-search" type="search" name="q">
          <button type="submit">Cari</button>
        </div>
      </form>

      <p id="search-status" class="reviewed" aria-live="polite"></p>
      <ol id="results" class="results"></ol>

      <noscript>
        <p>Pencarian memerlukan JavaScript. Tanpa JavaScript, telusuri <a href="guides.html">panduan</a>, <a href="checklist.html">daftar periksa</a>, atau <a href="glossary.html">glosarium</a>.</p>
      </noscript>

      <div id="search-help" class="prose">
        <h2>Coba cari</h2>
        <ul class="chips">
          <li><a href="search.html?q=kalibrasi">kalibrasi</a></li>
          <li><a href="search.html?q=garansi">garansi</a></li>
          <li><a href="search.html?q=paket">paket</a></li>
          <li><a href="search.html?q=TKDN">TKDN</a></li>
          <li><a href="search.html?q=HPS">HPS</a></li>
          <li><a href="search.html?q=reagen">reagen</a></li>
        </ul>
      </div>
    </div>"""

# ------------------------------------------------------------------ Templat kajian (tidak ikut diterbitkan)

def _template_rows():
    return "\n".join(
        f'              <tr><th scope="row">{name}</th><td data-label="Persyaratan">TEKS</td><td data-label="Cara memeriksa">BUKTI</td></tr>'
        for name, _ in WHO_SECTIONS)


template_rows = _template_rows()

template_body = f"""    <div class="wrap">
      <header class="page-head">
        <h1>NAMA ALAT</h1>
        <p class="lead">Satu atau dua kalimat: apa fungsi alat ini, di mana dipakai, dan untuk siapa kajian ini ditulis.</p>
        <p class="reviewed">Versi 1.0, terbit TANGGAL. Semua sumber bersifat publik dan tercantum di bagian akhir.</p>
      </header>

      <div class="prose">
        <h2>Sekilas</h2>
        <div class="table-wrap">
          <table>
            <thead>
              <tr><th scope="col">Butir</th><th scope="col">Untuk alat ini</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row">Nama generik dan kode nomenklatur</th><td data-label="Untuk alat ini">NAMA, KODE GMDN ATAU EMDN</td></tr>
              <tr><th scope="row">Tingkat layanan</th><td data-label="Untuk alat ini">TEMPAT ALAT INI SEHARUSNYA DIPAKAI</td></tr>
              <tr><th scope="row">Kelas risiko di Indonesia</th><td data-label="Untuk alat ini">A, B, C, ATAU D</td></tr>
              <tr><th scope="row">Standar yang berlaku</th><td data-label="Untuk alat ini">STANDAR DAN EDISINYA</td></tr>
            </tbody>
          </table>
        </div>

        <h2>1. Apa yang harus kita minta?</h2>
        <p>Kebutuhan klinisnya dalam dua atau tiga kalimat. Lalu spesifikasi acuan, mengikuti tiga belas bagian templat WHO. Pertahankan setiap bagian, dan tulis &ldquo;tidak berlaku&rdquo; jika suatu bagian tidak relevan.</p>
        <div class="table-wrap">
          <table>
            <thead>
              <tr><th scope="col">Bagian</th><th scope="col">Persyaratan</th><th scope="col">Cara memeriksa</th></tr>
            </thead>
            <tbody>
{template_rows}
            </tbody>
          </table>
        </div>

        <h2>2. Berapa harga yang wajar?</h2>
        <div class="table-wrap">
          <table>
            <thead>
              <tr><th scope="col">Sumber</th><th scope="col">Harga</th><th scope="col">Tanggal</th><th scope="col">Yang tercakup</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row"><a href="URL">NAMA SUMBER</a></th><td data-label="Harga">HARGA DAN MATA UANG</td><td data-label="Tanggal">TANGGAL</td><td data-label="Yang tercakup">CAKUPAN</td></tr>
            </tbody>
          </table>
        </div>
        <p>Mengapa harga-harga ini berbeda.</p>

        <h2>3. Bagaimana membelinya tanpa tender gagal?</h2>
        <p>Cara membagi paket, cara menilai penawaran, dan pertanyaan yang biasa diajukan peserta tentang alat ini.</p>

        <h2>Sumber</h2>
        <ul>
          <li><a href="URL">JUDUL DOKUMEN</a>, penerbit, tanggal. Dibaca pada TANGGAL.</li>
        </ul>

        <h2>Koreksi</h2>
        <p>Belum ada.</p>
      </div>
    </div>"""

PAGES = [
    ("index.html", "SistemSehat: panduan independen pembelian alat kesehatan",
     "Panduan gratis dan independen untuk menyusun spesifikasi, menentukan harga, dan membeli alat kesehatan bagi fasilitas kesehatan pemerintah.", home),
    ("guides.html", "Panduan | SistemSehat",
     "Lima panduan tentang spesifikasi, harga, dan pengadaan alat kesehatan, serta regulasi dan teknologi di baliknya.", guides),
    ("specification.html", "Apa yang harus kita minta? Panduan spesifikasi | SistemSehat",
     "Tujuh prinsip dengan contoh untuk menulis spesifikasi alat kesehatan yang dapat dipenuhi beberapa produsen.", spec),
    ("pricing.html", "Berapa harga yang wajar? Panduan harga | SistemSehat",
     "Enam prinsip dengan contoh untuk menyusun harga acuan alat kesehatan yang dapat dijelaskan dan dipertanggungjawabkan.", pricing),
    ("process.html", "Bagaimana membelinya tanpa tender gagal? Panduan proses | SistemSehat",
     "Tujuh prinsip dengan contoh untuk menjalankan tender alat kesehatan, dari membagi paket sampai mencari penyebab tender gagal.", process),
    ("regulation.html", "Apa yang wajib dipenuhi sebuah alat? Panduan regulasi | SistemSehat",
     "Delapan prinsip dengan contoh untuk memeriksa alat kesehatan terhadap regulasi Indonesia dan standar internasional.", regulation),
    ("technology.html", "Bagaimana menilai teknologinya? Panduan teknologi | SistemSehat",
     "Tujuh prinsip dengan contoh untuk menilai teknologi kesehatan dan bukti di baliknya.", technology),
    ("checklist.html", "Daftar periksa | SistemSehat",
     "Semua pertanyaan dari panduan SistemSehat dalam satu daftar periksa yang dapat dicentang atau dicetak.", checklist),
    ("glossary.html", "Glosarium | SistemSehat",
     "Istilah pengadaan dan singkatan yang dipakai di SistemSehat, dengan penjelasan singkat.", glossary),
    ("library.html", "Sumber rujukan | SistemSehat",
     "Dokumen publik tentang spesifikasi, harga, pengadaan, dan bukti alat kesehatan.", library),
    ("dossiers.html", "Kajian alat | SistemSehat",
     "Isi kajian alat SistemSehat, kajian yang sedang disusun, dan kapan sebuah kajian diterbitkan.", dossiers),
    ("about.html", "Tentang | SistemSehat",
     "Untuk siapa SistemSehat, siapa di baliknya, dan cara menjaga independensinya.", about),
    ("search.html", "Pencarian | SistemSehat",
     "Cari di prinsip, glosarium, dan sumber rujukan SistemSehat.", search),
]

INDEX_PAGES = [
    ("checklist.html", "Daftar periksa", "Semua pertanyaan dari kelima panduan, untuk dicentang di layar atau dicetak."),
    ("dossiers.html", "Kajian alat", "Isi sebuah kajian, cara menyusunnya, dan kapan diterbitkan."),
    ("about.html", "Tentang SistemSehat", "Untuk siapa situs ini, siapa di baliknya, dan cara menjaga independensinya."),
]

TEMPLATE = ("Kajian NAMA ALAT | SistemSehat", "RINGKASAN SATU KALIMAT TENTANG KAJIAN INI.",
            "NAMA ALAT", template_body, "dossier-template-id.html")
