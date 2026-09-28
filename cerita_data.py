# ==========================================
# DATABASE CERITA: JANGAN TERLAMBAT KE SEKOLAH
# ==========================================

MASTER_ENDING = {
    "good": "GOOD ENDING — TEPAT WAKTU",
    "bad": "BAD ENDING — TERLAMBAT LAGI",
    "police": "POLICE ENDING — PERJALANAN BERAKHIR",
    "true": "TRUE ENDING — HARI YANG SALAH",
    "secret": "SECRET ENDING — BANGUN, RIFAT!"
}

CERITA_DATABASE = {
    # ================= BAGIAN 1: BANGUN KESIANGAN =================
    "mulai": {
        "nama": "Narator",
        "teks": "Kringg Kringg! Alarm berbunyi keras di pagi hari.",
        "gambar": "images/rifat_tidur.png",
        "tujuan": "mulai_2"
    },
    "mulai_2": {
        "nama": "Narator",
        "teks": "Rifat membuka mata dan melihat jam di samping tempat tidurnya menunjukkan pukul 07:10.",
        "gambar": "images/rifat_tidur.png",
        "tujuan": "mulai_3"
    },
    "mulai_3": {
        "nama": "Rifat",
        "teks": "“HAH?! Jam tujuh lewat?!”",
        "gambar": "images/jam_alarm.png",
        "tujuan": "mulai_4"
    },
    "mulai_4": {
        "nama": "Rifat",
        "teks": "“Gawat, aku harus segera bersiap secepat mungkin!”",
        "gambar": "images/rifat_panik.png",
        "pilihan": [
            {"teks": "Mandi terlebih dahulu", "tujuan": "mandi_1"},
            {"teks": "Tidak mandi dan langsung bersiap", "tujuan": "tidak_mandi_1"}
        ]
    },

    # ================= BAGIAN 2A: MANDI =================
    "mandi_1": {
        "nama": "Narator",
        "teks": "Rifat berlari terbirit-birit menuju kamar mandi.",
        "gambar": "images/kamar_mandi.png",
        "tujuan": "mandi_2"
    },
    "mandi_2": {
        "nama": "Narator",
        "teks": "Dia mandi dengan sangat cepat, lalu buru-buru memakai seragamnya.",
        "gambar": "images/ganti_baju.png",
        "tujuan": "mandi_3"
    },
    "mandi_3": {
        "nama": "Narator",
        "teks": "Setelah selesai, Rifat melirik jam dinding yang menunjukkan pukul 07:25.",
        "gambar": "images/jam_0725.png",
        "tujuan": "mandi_4"
    },
    "mandi_4": {
        "nama": "Rifat",
        "teks": "“Masih sempat... harusnya.”",
        "gambar": "images/rifat_lega.png",
        "tujuan": "mandi_5"
    },
    "mandi_5": {
        "nama": "Narator",
        "teks": "Rifat mengambil tasnya dan melewati ruang makan. Di atas meja, sarapan sudah tersaji.",
        "gambar": "images/meja_makan.png",
        "pilihan": [
            {"teks": "Sarapan sebentar", "tujuan": "sarapan_ya"},
            {"teks": "Tidak sarapan dan langsung berangkat", "tujuan": "sarapan_tidak"}
        ]
    },

    # ================= BAGIAN 2B: TIDAK MANDI =================
    "tidak_mandi_1": {
        "nama": "Narator",
        "teks": "Rifat memutuskan untuk langsung memakai seragam tanpa mandi demi menghemat waktu.",
        "gambar": "images/ganti_baju.png",
        "tujuan": "tidak_mandi_2"
    },
    "tidak_mandi_2": {
        "nama": "Rifat",
        "teks": "“Yang penting sampai sekolah dulu, urusan mandi belakangan!”",
        "gambar": "images/rifat_panik2.png",
        "tujuan": "tidak_mandi_3"
    },
    "tidak_mandi_3": {
        "nama": "Narator",
        "teks": "Dia menyambar tasnya dan bergegas keluar kamar, lalu melewati ruang makan. Di meja masih ada sarapan.",
        "gambar": "images/meja_makan.png",
        "pilihan": [
            {"teks": "Sarapan sebentar", "tujuan": "sarapan_ya"},
            {"teks": "Tidak sarapan dan langsung berangkat", "tujuan": "sarapan_tidak"}
        ]
    },

    # ================= BAGIAN 3: SARAPAN / TIDAK =================
    "sarapan_ya": {
        "nama": "Narator",
        "teks": "Rifat duduk sebentar dan memakan sarapannya dengan cepat.",
        "gambar": "images/makan.png",
        "tujuan": "sarapan_ya_2"
    },
    "sarapan_ya_2": {
        "nama": "Narator",
        "teks": "Saat melirik jam, waktu sudah menunjukkan pukul 07:30.",
        "gambar": "images/jam_0730.png",
        "tujuan": "sarapan_ya_3"
    },
    "sarapan_ya_3": {
        "nama": "Rifat",
        "teks": "“Waduh, gawat! Aku harus berangkat sekarang juga!”",
        "gambar": "images/rifat_panik3.png",
        "tujuan": "pilih_jalan"
    },
    "sarapan_tidak": {
        "nama": "Rifat",
        "teks": "“Nanti saja deh makannya di kantin sekolah.”",
        "gambar": "images/rifat_takmakan.png",
        "tujuan": "sarapan_tidak_2"
    },
    "sarapan_tidak_2": {
        "nama": "Narator",
        "teks": "Rifat langsung mengambil kunci motornya dan bergegas keluar rumah.",
        "gambar": "images/kunci_motor.png",
        "tujuan": "pilih_jalan"
    },

    # ================= BAGIAN 4: MEMILIH JALAN =================
    "pilih_jalan": {
        "nama": "Narator",
        "teks": "Rifat menyalakan motornya dan mulai menuju ke sekolah.",
        "gambar": "images/naik_motor.png",
        "tujuan": "pilih_jalan_2"
    },
    "pilih_jalan_2": {
        "nama": "Narator",
        "teks": "Di perjalanan rifat bertemu persimpangan antara jalan pintas dan jalan utama.",
        "gambar": "images/persimpangan.png",
        "tujuan": "pilih_jalan_3"
    },
    "pilih_jalan_3": {
        "nama": "Rifat",
        "teks": "“Kalau lewat jalan utama takut macet, tapi kalau lewat jalan pintas... entahlah.”",
        "gambar": "images/rifat_mikir.png",
        "pilihan": [
            {"teks": "Lewat jalan utama", "tujuan": "jalan_utama"},
            {"teks": "Lewat jalan pintas", "tujuan": "jalan_pintas"}
        ]
    },

    # ================= BAGIAN 4A: JALAN UTAMA =================
    "jalan_utama": {
        "nama": "Narator",
        "teks": "Rifat pun memilih untuk melewati jalan utama.",
        "gambar": "images/jalan_raya.png",
        "tujuan": "jalan_utama_2"
    },
    "jalan_utama_2": {
        "nama": "Narator",
        "teks": "Oh Nooo... Ternyata kondisi jalanan cukup padat dan dipenuhi kendaraan lain.",
        "gambar": "images/macet.png",
        "tujuan": "jalan_utama_3"
    },
    "jalan_utama_3": {
        "nama": "Narator",
        "teks": "Rifat melihat jam tangannya. Pukul 07:40.",
        "gambar": "images/jam_0740.png",
        "tujuan": "jalan_utama_4"
    },
    "jalan_utama_4": {
        "nama": "Rifat",
        "teks": "“Masih ada waktu dua puluh menit lagi, semoga terkejar.”",
        "gambar": "images/rifat_lega2.png",
        "tujuan": "jalan_utama_5"
    },
    "jalan_utama_5": {
        "nama": "Narator",
        "teks": "Tidak lama kemudian, Rifat tiba di sebuah lampu merah yang baru saja menyala merah.",
        "gambar": "images/lampu_merah.png",
        "pilihan": [
            {"teks": "Menunggu lampu hijau", "tujuan": "utama_menunggu"},
            {"teks": "Mencoba menerobos", "tujuan": "utama_menerobos"}
        ]
    },

    "utama_menunggu": {
        "nama": "Narator",
        "teks": "Rifat menghentikan motornya di belakang kendaraan lain dengan sabar.",
        "gambar": "images/tunggu_lampu.png",
        "tujuan": "utama_menunggu_2"
    },
    "utama_menunggu_2": {
        "nama": "Narator",
        "teks": "Beberapa saat kemudian, lampu berubah menjadi hijau.",
        "gambar": "images/lampu_hijau.png",
        "tujuan": "utama_menunggu_3"
    },
    "utama_menunggu_3": {
        "nama": "Narator",
        "teks": "Rifat melanjutkan perjalanannya dengan tertib dan aman hingga berhasil melewati jalan utama menuju sekolah.",
        "gambar": "images/naik_motor2.png",
        "tujuan": "cek_waktu_sekolah"
    },

    "utama_menerobos": {
        "nama": "Narator",
        "teks": "Rifat melihat situasi jalanan tampak agak kosong dan merasa tergoda untuk menerobos lampu merah.",
        "gambar": "images/lampu_merah.png",
        "tujuan": "utama_menerobos_2"
    },
    "utama_menerobos_2": {
        "nama": "Narator",
        "teks": "Namun secara tiba-tiba, muncul kendaraan dari arah lain dengan kecepatan tinggi!",
        "gambar": "images/hampir_tabrakan.png",
        "tujuan": "utama_menerobos_3"
    },
    "utama_menerobos_3": {
        "nama": "Narator",
        "teks": "Rifat langsung menarik rem dalam-dalam hingga ban motornya berdecit.",
        "gambar": "images/rem_mendadak.png",
        "tujuan": "utama_menerobos_4"
    },
    "utama_menerobos_4": {
        "nama": "Narator",
        "teks": "Nahasnya, di dekat persimpangan tersebut ada seorang polisi lalu lintas yang melihat seluruh kejadian itu.",
        "gambar": "images/polisi.png",
        "tujuan": "utama_menerobos_5"
    },
    "utama_menerobos_5": {
        "nama": "Narator",
        "teks": "Polisi tersebut meniup peluit dan memberikan isyarat keras agar Rifat segera menepi.",
        "gambar": "images/polisi_suruh_tepi.png",
        "pilihan": [
            {"teks": "Berhenti dan mengakui kesalahan", "tujuan": "police_ending"},
            {"teks": "Marah dan melawan polisi", "tujuan": "secret_ending"}
        ]
    },

    # ================= BAGIAN 4B: JALAN PINTAS =================
    "jalan_pintas": {
        "nama": "Narator",
        "teks": "Rifat memutuskan untuk mengambil jalur jalan pintas.",
        "gambar": "images/jalan_pintas.png",
        "tujuan": "jalan_pintas_2"
    },
    "jalan_pintas_2": {
        "nama": "Narator",
        "teks": "Pada awal perjalanan, suasana jalanan memang sangat sepi dan lancar.",
        "gambar": "images/jalan_sepi.png",
        "tujuan": "jalan_pintas_3"
    },
    "jalan_pintas_3": {
        "nama": "Rifat",
        "teks": "“Nah, bener kan dugaanku. Lewat sini jauh lebih cepat!”",
        "gambar": "images/rifat_senang.png",
        "tujuan": "jalan_pintas_4"
    },
    "jalan_pintas_4": {
        "nama": "Narator",
        "teks": "Namun beberapa menit kemudian, Rifat di hadapkan pada jalur yang rusak parah dan dipenuhi kendaraan truk besar.",
        "gambar": "images/jalan_rusak.png",
        "tujuan": "jalan_pintas_5"
    },
    "jalan_pintas_5": {
        "nama": "Narator",
        "teks": "Rifat mengecek jam tangannya. Waktu menunjukkan pukul 07:45.",
        "gambar": "images/jam_0745.png",
        "tujuan": "jalan_pintas_6"
    },
    "jalan_pintas_6": {
        "nama": "Rifat",
        "teks": "“Duh... malah macet total di sini! Sial banget.”",
        "gambar": "images/rifat_panik.png",
        "tujuan": "jalan_pintas_7"
    },
    "jalan_pintas_7": {
        "nama": "Narator",
        "teks": "Dengan susah payah, Rifat tetap meneruskan perjalanan hingga akhirnya bisa keluar kembali ke jalan utama.",
        "gambar": "images/naik_motor.png",
        "tujuan": "jalan_pintas_8"
    },
    "jalan_pintas_8": {
        "nama": "Narator",
        "teks": "Di depan terdapat persimpangan lampu merah yang sedang menyala merah.",
        "gambar": "images/lampu_merah.png",
        "pilihan": [
            {"teks": "Menunggu lampu hijau", "tujuan": "pintas_menunggu"},
            {"teks": "Menerobos lampu merah", "tujuan": "pintas_menerobos"}
        ]
    },

    "pintas_menunggu": {
        "nama": "Narator",
        "teks": "Rifat menghentikan motornya dengan sabar menunggu lampu berganti hijau.",
        "gambar": "images/tunggu_lampu.png",
        "tujuan": "pintas_menunggu_2"
    },
    "pintas_menunggu_2": {
        "nama": "Narator",
        "teks": "Lampu lalu lintas akhirnya menyala hijau.",
        "gambar": "images/lampu_hijau.png",
        "tujuan": "pintas_menunggu_3"
    },
    "pintas_menunggu_3": {
        "nama": "Narator",
        "teks": "Karena tadi sempat terjebak macet di jalan pintas, waktu berjalan begitu cepat.",
        "gambar": "images/naik_motor.png",
        "tujuan": "terlambat_awal"  # Otomatis masuk jalur terlambat karena sempat macet
    },

    "pintas_menerobos": {
        "nama": "Narator",
        "teks": "Karena panik sudah semakin siang, Rifat nekat menerobos lampu merah tersebut.",
        "gambar": "images/nekat_terobos.png",
        "tujuan": "pintas_menerobos_2"
    },
    "pintas_menerobos_2": {
        "nama": "Narator",
        "teks": "Sialnya, seorang polisi yang berjaga di pos dekat sana langsung memergokinya.",
        "gambar": "images/polisi.png",
        "tujuan": "pintas_menerobos_3"
    },
    "pintas_menerobos_3": {
        "nama": "Narator",
        "teks": "Polisi memberikan isyarat tegas agar Rifat segera menepikan kendaraannya.",
        "gambar": "images/polisi_suruh_tepi.png",
        "pilihan": [
            {"teks": "Berhenti dan mengakui kesalahan", "tujuan": "police_ending"},
            {"teks": "Marah dan melawan polisi", "tujuan": "secret_ending"}
        ]
    },

    # ================= POLICE ENDING =================
    "police_ending": {
        "nama": "Narator",
        "teks": "Rifat mematikan mesin motornya dan menepi ke pinggir jalan. Pak Polisi langsung menghampirinya.",
        "gambar": "images/tilang_1.png",
        "tujuan": "police_ending_2"
    },
    "police_ending_2": {
        "nama": "Polisi",
        "teks": "“KAMU TADI JELAS-JELAS MENEROBOS LAMPU MERAH YA?!”",
        "gambar": "images/tilang_marah.png",
        "tujuan": "police_ending_3"
    },
    "police_ending_3": {
        "nama": "Narator",
        "teks": "Rifat menundukkan kepalanya karena merasa bersalah.",
        "gambar": "images/rifat_nunduk.png",
        "tujuan": "police_ending_4"
    },
    "police_ending_4": {
        "nama": "Rifat",
        "teks": "“Iya, Pak. Saya ngaku salah... Saya benar-benar takut terlambat ke sekolah.”",
        "gambar": "images/rifat_nunduk.png",
        "tujuan": "police_ending_5"
    },
    "police_ending_5": {
        "nama": "Narator",
        "teks": "Pak Polisi dengan tegas menjelaskan pelanggaran Rifat serta menjatuhkan sanksi tilang.",
        "gambar": "images/tilang_proses.png",
        "tujuan": "police_ending_6"
    },
    "police_ending_6": {
        "nama": "Narator",
        "teks": "Kunci motor Rifat disita, membuatnya tidak bisa melanjutkan perjalanan ke sekolah.",
        "gambar": "images/motor_disita.png",
        "tujuan": "police_ending_7"
    },
    "police_ending_7": {
        "nama": "Narator",
        "teks": "Rifat melirik jam tangannya yang menunjukkan pukul 07:55.",
        "gambar": "images/jam_0755.png",
        "tujuan": "police_ending_8"
    },
    "police_ending_8": {
        "nama": "Rifat",
        "teks": "“Yah... Habis sudah riwayatku. Gimana caranya bisa sampai sekolah sekarang?”",
        "gambar": "images/rifat_menangis.png",
        "tipe": "ending",
        "id_ending": "police",
        "judul": "POLICE ENDING — PERJALANAN BERAKHIR",
        "pesan": "Rifat tertangkap basah melanggar lalu lintas, ditilang polisi, dan gagal total sampai di sekolah."
    },

    # ================= SECRET ENDING =================
    "secret_ending": {
        "nama": "Narator",
        "teks": "Rifat yang sudah dikuasai rasa panik bertindak di luar kendali.",
        "gambar": "images/rifat_marah.png",
        "tujuan": "secret_ending_2"
    },
    "secret_ending_2": {
        "nama": "Narator",
        "teks": "Ketika pak polisi menyuruhnya tetap tenang, Rifat malah membentak dan bersikap agresif.",
        "gambar": "images/ribut_polisi.png",
        "tujuan": "secret_ending_3"
    },
    "secret_ending_3": {
        "nama": "Narator",
        "teks": "Terjadi perdebatan dan keributan singkat di pinggir jalan raya tersebut.",
        "gambar": "images/ribut_polisi.png",
        "tujuan": "secret_ending_4"
    },
    "secret_ending_4": {
        "nama": "Narator",
        "teks": "Akhirnya, Rifat berhasil diamankan oleh petugas dan dibawa ke pos polisi terdekat.",
        "gambar": "images/kantor_polisi.png",
        "tujuan": "secret_ending_5"
    },
    "secret_ending_5": {
        "nama": "Narator",
        "teks": "Rifat duduk sendirian di dalam ruangan interogasi dengan tatapan kosong.",
        "gambar": "images/ruang_tunggu.png",
        "tujuan": "secret_ending_6"
    },
    "secret_ending_6": {
        "nama": "Rifat",
        "teks": "“Kenapa hidup gue bisa jadi kacau begini...”",
        "gambar": "images/rifat_menangis.png",
        "tujuan": "secret_ending_7"
    },
    "secret_ending_7": {
        "nama": "Narator",
        "teks": "Tiba-tiba, sayup-sayup terdengar suara seseorang memanggilnya dari kejauhan.",
        "gambar": "images/gelap.png",
        "tujuan": "secret_ending_8"
    },
    "secret_ending_8": {
        "nama": "Suara Misterius",
        "teks": "“Rifat! Bangun!”",
        "gambar": "images/gelap.png",
        "tujuan": "secret_ending_9"
    },
    "secret_ending_9": {
        "nama": "Narator",
        "teks": "Rifat terkesiap dan perlahan membuka kedua matanya.",
        "gambar": "images/rifat_tidur.png",
        "tujuan": "secret_ending_10"
    },
    "secret_ending_10": {
        "nama": "Narator",
        "teks": "Rifat terbangun di atas tempat tidurnya sendiri. Dia melirik jam dinding: 06:30.",
        "gambar": "images/jam_0630.png",
        "tujuan": "secret_ending_11"
    },
    "secret_ending_11": {
        "nama": "Rifat",
        "teks": "“Hah...? Jadi ini semua cuma mimpi?”",
        "gambar": "images/rifat_bingung.png",
        "tujuan": "secret_ending_12"
    },
    "secret_ending_12": {
        "nama": "Narator",
        "teks": "Dia melihat seragamnya masih tergantung rapi, lalu menghela napas panjang penuh rasa syukur.",
        "gambar": "images/seragam.png",
        "tipe": "ending",
        "id_ending": "secret",
        "judul": "SECRET ENDING — BANGUN, RIFAT!",
        "pesan": "Segala kekacauan di jalanan tadi ternyata hanyalah mimpi buruk Rifat karena tidur terlalu pulas."
    },

    # ================= CEK WAKTU SAMPAI DI SEKOLAH (OTOMATIS) =================
    "cek_waktu_sekolah": {
        "nama": "Narator",
        "teks": "Rifat mengendarai motornya dengan sisa-sisa tenaga hingga gerbang sekolah mulai tampak di depan mata.",
        "gambar": "images/gerbang_sekolah.png",
        "tujuan": "cek_waktu_sekolah_2"
    },
    "cek_waktu_sekolah_2": {
        "nama": "Narator",
        "teks": "Rifat melirik jam tangannya untuk melihat waktu kedatangannya...",
        "gambar": "images/lihat_jam.png",
        "tujuan": "tepat_waktu_awal"  # Otomatis Tepat Waktu karena lewat jalan utama secara tertib
    },

    # ================= JIKA TEPAT WAKTU (< 08:00) =================
    "tepat_waktu_awal": {
        "nama": "Narator",
        "teks": "Rifat melihat jam menunjukkan pukul 07:50.",
        "gambar": "images/jam_0750.png",
        "tujuan": "tepat_waktu_2"
    },
    "tepat_waktu_2": {
        "nama": "Rifat",
        "teks": "“Yes! Masih sempat! Aku tidak terlambat!”",
        "gambar": "images/rifat_senang.png",
        "tujuan": "tepat_waktu_3"
    },
    "tepat_waktu_3": {
        "nama": "Narator",
        "teks": "Rifat memarkirkan motornya dengan tenang dan berjalan menuju gedung sekolah.",
        "gambar": "images/parkir_motor.png",
        "tujuan": "tepat_waktu_4"
    },
    "tepat_waktu_4": {
        "nama": "Narator",
        "teks": "Namun sebelum melangkah masuk, dia dihadapkan pada situasi akhir.",
        "gambar": "images/koridor_sekolah.png",
        "pilihan": [
            {"teks": "Langsung masuk kelas", "tujuan": "pilih_masuk_kelas_tepat"},
            {"teks": "Duduk sebentar di depan kelas", "tujuan": "duduk_sebentar_tepat"}
        ]
    },

    "duduk_sebentar_tepat": {
        "nama": "Narator",
        "teks": "Rifat merasa lega luar biasa karena berhasil datang sebelum pelajaran dimulai.",
        "gambar": "images/koridor_sekolah.png",
        "tujuan": "duduk_sebentar_tepat_2"
    },
    "duduk_sebentar_tepat_2": {
        "nama": "Narator",
        "teks": "Dia duduk bersantai sejenak di bangku depan kelas.",
        "gambar": "images/duduk_santai.png",
        "tujuan": "duduk_sebentar_tepat_3"
    },
    "duduk_sebentar_tepat_3": {
        "nama": "Narator",
        "teks": "Beberapa menit kemudian, bel sekolah berbunyi menandakan jam pelajaran dimulai.",
        "gambar": "images/bel_sekolah.png",
        "tujuan": "duduk_sebentar_tepat_4"
    },
    "duduk_sebentar_tepat_4": {
        "nama": "Narator",
        "teks": "Rifat berdiri dengan tenang dan masuk ke dalam kelas untuk mengikuti pelajaran.",
        "gambar": "images/masuk_kelas.png",
        "tipe": "ending",
        "id_ending": "good",
        "judul": "GOOD ENDING — TEPAT WAKTU",
        "pesan": "Rifat berhasil tiba di sekolah sebelum jam 08:00 dan menjalani hari dengan lancar."
    },

    "pilih_masuk_kelas_tepat": {
        "nama": "Narator",
        "teks": "Rifat membuka pintu kelas dengan mantap.",
        "gambar": "images/buka_pintu.png",
        "tujuan": "pilih_masuk_kelas_tepat_2"
    },
    "pilih_masuk_kelas_tepat_2": {
        "nama": "Narator",
        "teks": "Namun... Suasana di dalam kelas terasa sangat sunyi senyap. Tidak ada siapa-siapa.",
        "gambar": "images/kelas_kosong.png",
        "tujuan": "pilih_masuk_kelas_tepat_3"
    },
    "pilih_masuk_kelas_tepat_3": {
        "nama": "Rifat",
        "teks": "“...Hah? Kok aneh banget?”",
        "gambar": "images/rifat_bingung.png",
        "tujuan": "pilih_masuk_kelas_tepat_4"
    },
    "pilih_masuk_kelas_tepat_4": {
        "nama": "Narator",
        "teks": "Dia memeriksa meja teman-temannya. Tidak ada tas, tidak ada siswa, bahkan meja guru pun kosong.",
        "gambar": "images/kelas_kosong.png",
        "tujuan": "pilih_masuk_kelas_tepat_5"
    },
    "pilih_masuk_kelas_tepat_5": {
        "nama": "Narator",
        "teks": "Lalu pandangan Rifat tertuju pada selembar kalender dinding yang tergantung di dekat papan tulis.",
        "gambar": "images/kalender.png",
        "tujuan": "pilih_masuk_kelas_tepat_6"
    },
    "pilih_masuk_kelas_tepat_6": {
        "nama": "Rifat",
        "teks": "“Tulisannya... Minggu, 27 September?!”",
        "gambar": "images/rifat_syok.png",
        "tujuan": "pilih_masuk_kelas_tepat_7"
    },
    "pilih_masuk_kelas_tepat_7": {
        "nama": "Narator",
        "teks": "Rifat memegang kepalanya sendiri dengan ekspresi tidak percaya.",
        "gambar": "images/rifat_pusing.png",
        "tujuan": "pilih_masuk_kelas_tepat_8"
    },
    "pilih_masuk_kelas_tepat_8": {
        "nama": "Rifat",
        "teks": "“Jadi dari tadi pagi gue buru-buru... padahal hari ini kan hari Minggu?!”",
        "gambar": "images/rifat_syok.png",
        "tipe": "ending",
        "id_ending": "true",
        "judul": "TRUE ENDING — HARI YANG SALAH",
        "pesan": "Rifat sukses sampai sekolah tepat waktu, namun ia baru sadar kalau hari itu adalah hari libur (Minggu)."
    },

    # ================= JIKA TERLAMBAT (> 08:00) =================
    "terlambat_awal": {
        "nama": "Narator",
        "teks": "Rifat melirik jam tangannya dan melihat angka sudah menunjukkan pukul 08:10.",
        "gambar": "images/jam_0810.png",
        "tujuan": "terlambat_2"
    },
    "terlambat_2": {
        "nama": "Rifat",
        "teks": "“Celaka... aku benar-benar terlambat.”",
        "gambar": "images/rifat_menangis.png",
        "tujuan": "terlambat_3"
    },
    "terlambat_3": {
        "nama": "Narator",
        "teks": "Rifat berlari terbirit-birit menuju ke ruang kelasnya.",
        "gambar": "images/lari_koridor.png",
        "tujuan": "terlambat_4"
    },
    "terlambat_4": {
        "nama": "Narator",
        "teks": "Saat pintu dibuka, guru killer sudah berdiri di dalam kelas dan semua mata menatap ke arahnya.",
        "gambar": "images/guru_marah.png",
        "tujuan": "terlambat_5"
    },
    "terlambat_5": {
        "nama": "Guru",
        "teks": "“Rifat! Kenapa kamu baru datang jam segini?!”",
        "gambar": "images/guru_marah.png",
        "tujuan": "terlambat_6"
    },
    "terlambat_6": {
        "nama": "Rifat",
        "teks": "“I-iya, Pak... Maaf saya kesiangan.”",
        "gambar": "images/rifat_nunduk.png",
        "tujuan": "terlambat_7"
    },
    "terlambat_7": {
        "nama": "Narator",
        "teks": "Guru memberikan hukuman disiplin karena keterlambatannya, dan Rifat hanya bisa pasrah.",
        "gambar": "images/hukuman.png",
        "tujuan": "terlambat_8"
    },
    "terlambat_8": {
        "nama": "Narator",
        "teks": "Rifat menjalani sisa jam pelajaran dengan perasaan malu bercampur lelah karena terlambat.",
        "gambar": "images/belajar_lesu.png",
        "tipe": "ending",
        "id_ending": "bad",
        "judul": "BAD ENDING — TERLAMBAT LAGI",
        "pesan": "Rifat terlambat datang ke sekolah dan harus menerima hukuman dari guru piket maupun wali kelas."
    }
}