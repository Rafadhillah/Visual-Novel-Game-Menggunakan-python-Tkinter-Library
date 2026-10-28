import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import pygame
from cerita_data import CERITA_DATABASE, MASTER_ENDING


class VisualNovelApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Rifat Simulator : Jangan Terlambat ke Sekolah - Visual Novel")
        self.root.geometry("800x640")
        self.root.resizable(False, False)

        # Tema warna
        self.bg_color = "#161622"
        self.box_color = "#232336"
        self.text_color = "#ffffff"
        self.btn_color = "#4a4e69"
        self.btn_hover = "#6c757d"
        self.accent_color = "#ffcc00"

        self.root.configure(bg=self.bg_color)

        # ================= AUDIO =================

        self.audio_aktif = False
        self.sfx_klik = None

        self.folder_project = os.path.dirname(os.path.abspath(__file__))

        self.folder_sounds = os.path.join(self.folder_project,"sounds")

        self.file_bgm = os.path.join(self.folder_sounds,"bgm.mp3")

        self.file_klik = os.path.join(self.folder_sounds,"klik.mp3")

        try:
            pygame.mixer.init()

            if os.path.exists(self.file_klik):
                self.sfx_klik = pygame.mixer.Sound(
                    self.file_klik
                )

                self.sfx_klik.set_volume(0.7)

            self.audio_aktif = True

        except Exception as e:
            print("Audio tidak dapat dijalankan:", e)
            self.audio_aktif = False

        # ================= ENDING =================

        self.ending_terbuka = set()

        # ================= CONTAINER =================

        self.container = tk.Frame(
            root,
            bg=self.bg_color
        )

        self.container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        self.tampilkan_main_menu()

    # ================= AUDIO =================

    def mulai_bgm(self):
        if not self.audio_aktif:
            return

        try:
            if os.path.exists(self.file_bgm):

                pygame.mixer.music.load(
                    self.file_bgm
                )

                pygame.mixer.music.set_volume(
                    0.2
                )

                pygame.mixer.music.play(-1)

        except Exception as e:
            print("BGM error:", e)

    def stop_bgm(self):
        if not self.audio_aktif:
            return

        try:
            pygame.mixer.music.stop()

        except Exception as e:
            print("Gagal menghentikan BGM:", e)

    def suara_klik(self):
        if not self.audio_aktif:
            return

        try:
            if self.sfx_klik:
                self.sfx_klik.play()

        except Exception as e:
            print("SFX klik error:", e)

    def putar_sfx(self, nama_file):
        if not self.audio_aktif:
            return

        if not nama_file:
            return

        try:
            if not os.path.isabs(nama_file):
                nama_file = os.path.join(
                    self.folder_project,
                    nama_file
                )

            if not os.path.exists(nama_file):
                print(
                    "SFX tidak ditemukan:",
                    nama_file
                )
                return

            suara = pygame.mixer.Sound(
                nama_file
            )

            suara.set_volume(0.8)
            suara.play()

        except Exception as e:
            print("SFX error:", e)

    def klik_dan_muat(self, tujuan):
        self.suara_klik()
        self.muat_scene(tujuan)

    def klik_dan_jalankan(self, fungsi):
        self.suara_klik()
        fungsi()

    # ================= BERSIHKAN CONTAINER =================

    def bersihkan_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # ================= 1. MAIN MENU =================

    def tampilkan_main_menu(self):

        # Pastikan BGM mati ketika berada di menu
        self.stop_bgm()

        self.bersihkan_container()

        menu_frame = tk.Frame(
            self.container,
            bg=self.bg_color
        )

        menu_frame.pack(
            fill="both",
            expand=True
        )

        lbl_judul = tk.Label(
            menu_frame,
            text="Rifat Simulator \nJangan Terlambat ke Sekolah",
            bg=self.bg_color,
            fg=self.accent_color,
            font=("Arial", 26, "bold"),
            justify="center"
        )

        lbl_judul.pack(
            pady=90
        )

        btn_play = tk.Button(
            menu_frame,
            text="▶  MULAI PERMAINAN",
            bg="#2a9d8f",
            fg="white",
            font=("Arial", 12, "bold"),
            width=28,
            height=2,
            relief="flat",
            cursor="hand2",
            command=lambda: self.klik_dan_jalankan(
                self.mulai_game
            )
        )

        btn_play.pack(
            pady=10
        )

        btn_ending = tk.Button(
            menu_frame,
            text="🏆  DAFTAR ENDING",
            bg=self.btn_color,
            fg="white",
            font=("Arial", 12, "bold"),
            width=28,
            height=2,
            relief="flat",
            cursor="hand2",
            command=lambda: self.klik_dan_jalankan(
                self.tampilkan_daftar_ending
            )
        )

        btn_ending.pack(
            pady=10
        )

    # ================= 2. DAFTAR ENDING =================

    def tampilkan_daftar_ending(self):

        self.stop_bgm()

        self.bersihkan_container()

        frame_ending = tk.Frame(
            self.container,
            bg=self.bg_color
        )

        frame_ending.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            frame_ending,
            text="KOLEKSI ENDING",
            bg=self.bg_color,
            fg=self.accent_color,
            font=("Arial", 18, "bold")
        ).pack(
            pady=15
        )

        list_box_frame = tk.Frame(
            frame_ending,
            bg=self.box_color,
            bd=2,
            relief="groove"
        )

        list_box_frame.pack(
            fill="both",
            expand=True,
            pady=10,
            padx=10
        )

        for key, nama_ending in MASTER_ENDING.items():

            if key in self.ending_terbuka:

                teks_status = (
                    f"✔  {nama_ending} (TERBUKA)"
                )

                warna_teks = "#2a9d8f"

            else:

                teks_status = (
                    "❌  [ ????? ] — Belum Ditemukan"
                )

                warna_teks = "#777788"

            lbl_item = tk.Label(
                list_box_frame,
                text=teks_status,
                bg=self.box_color,
                fg=warna_teks,
                font=("Arial", 12, "bold"),
                anchor="w"
            )

            lbl_item.pack(
                fill="x",
                padx=25,
                pady=12
            )

        btn_kembali = tk.Button(
            frame_ending,
            text="◀  KEMBALI KE MENU UTAMA",
            bg=self.btn_color,
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=lambda: self.klik_dan_jalankan(
                self.tampilkan_main_menu
            )
        )

        btn_kembali.pack(
            pady=15
        )

    # ================= 3. GAMEPLAY UTAMA =================

    def mulai_game(self):

        # Nyalakan BGM ketika permainan dimulai
        self.mulai_bgm()

        self.bersihkan_container()

        game_frame = tk.Frame(
            self.container,
            bg=self.bg_color
        )

        game_frame.pack(
            fill="both",
            expand=True
        )

        # ================= GAMBAR =================

        self.canvas_visual = tk.Canvas(
            game_frame,
            width=760,
            height=360,
            bg="#111118",
            highlightthickness=2,
            highlightbackground="#33334d"
        )

        self.canvas_visual.pack(
            pady=(0, 6)
        )

        # ================= DIALOG =================

        self.dialog_frame = tk.Frame(
            game_frame,
            bg=self.box_color,
            bd=2,
            relief="groove"
        )

        self.dialog_frame.pack(
            fill="x",
            pady=(0, 6)
        )

        self.lbl_nama = tk.Label(
            self.dialog_frame,
            text="",
            bg=self.box_color,
            fg=self.accent_color,
            font=("Arial", 10, "bold")
        )

        self.lbl_nama.pack(
            anchor="w",
            padx=12,
            pady=2
        )

        self.lbl_teks = tk.Label(
            self.dialog_frame,
            text="",
            bg=self.box_color,
            fg=self.text_color,
            font=("Arial", 10),
            wraplength=720,
            justify="left",
            height=2
        )

        self.lbl_teks.pack(
            anchor="w",
            padx=12,
            pady=2
        )

        # ================= ACTION FRAME =================

        self.action_frame = tk.Frame(
            game_frame,
            bg=self.bg_color
        )

        self.action_frame.pack(
            fill="x"
        )

        # ================= TOMBOL LANJUT =================

        self.btn_lanjut = tk.Button(
            self.action_frame,
            text="LANJUT  ➔",
            bg="#2a9d8f",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            activebackground="#21867a",
            cursor="hand2",
            height=2
        )

        # ================= PILIHAN =================

        self.choice_frame = tk.Frame(
            self.action_frame,
            bg=self.bg_color
        )

        self.choice_frame.columnconfigure(
            0,
            weight=1,
            uniform="kolom"
        )

        self.choice_frame.columnconfigure(
            1,
            weight=1,
            uniform="kolom"
        )

        self.choice_frame.rowconfigure(
            0,
            weight=1
        )

        self.choice_frame.rowconfigure(
            1,
            weight=1
        )

        self.list_tombol = []

        posisi_grid = [
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1)
        ]

        for r, c in posisi_grid:

            btn = tk.Button(
                self.choice_frame,
                text="",
                bg=self.btn_color,
                fg=self.text_color,
                font=("Arial", 10, "bold"),
                relief="flat",
                activebackground=self.btn_hover,
                cursor="hand2",
                wraplength=350,
                height=2
            )

            btn.grid(
                row=r,
                column=c,
                sticky="nsew",
                padx=5,
                pady=3
            )

            self.list_tombol.append(btn)

        # ================= KEMBALI KE MENU =================

        btn_back_menu = tk.Button(
            game_frame,
            text="◀  KEMBALI KE MENU UTAMA",
            bg="#2c2c3e",
            fg="#aaaaaa",
            font=("Arial", 9, "bold"),
            relief="flat",
            cursor="hand2",
            activebackground=self.btn_hover,
            command=lambda: self.klik_dan_jalankan(
                self.tampilkan_main_menu
            )
        )

        btn_back_menu.pack(
            pady=(6, 0)
        )

        # Mulai dari scene pertama
        self.muat_scene("mulai")

    # ================= GAMBAR =================

    def ganti_gambar(
        self,
        nama_file,
        canvas_target
    ):

        if nama_file:

            if not os.path.isabs(nama_file):

                nama_file = os.path.join(
                    self.folder_project,
                    nama_file
                )

        if nama_file and os.path.exists(nama_file):

            try:

                img = Image.open(
                    nama_file
                )

                img = img.resize(
                    (760, 360),
                    Image.Resampling.LANCZOS
                )

                photo = ImageTk.PhotoImage(
                    img
                )

                canvas_target.image_ref = photo

                canvas_target.delete(
                    "all"
                )

                canvas_target.create_image(
                    0,
                    0,
                    anchor="nw",
                    image=photo
                )

            except Exception as e:

                print(
                    "Gagal memuat gambar:",
                    e
                )

                canvas_target.delete(
                    "all"
                )

                canvas_target.create_text(
                    380,
                    180,
                    text="[Gambar gagal dimuat]",
                    fill="#6c757d",
                    font=(
                        "Arial",
                        11,
                        "italic"
                    ),
                    justify="center"
                )

        else:

            canvas_target.delete(
                "all"
            )

            pesan = (
                f"[Gambar '{nama_file}' tidak ditemukan]"
                if nama_file
                else "[Tidak ada gambar]"
            )

            canvas_target.create_text(
                380,
                180,
                text=pesan,
                fill="#6c757d",
                font=(
                    "Arial",
                    11,
                    "italic"
                ),
                justify="center"
            )

    # ================= MUAT SCENE =================

    def muat_scene(
        self,
        nama_scene
    ):

        data = CERITA_DATABASE.get(
            nama_scene
        )

        if not data:

            messagebox.showerror(
                "Error",
                f"Scene '{nama_scene}' tidak ditemukan!"
            )

            return

        # ================= SFX SCENE =================

        if data.get("sfx"):

            self.putar_sfx(
                data.get("sfx")
            )

        # ================= ENDING =================

        if data.get("tipe") == "ending":

            # Matikan BGM ketika ending muncul
            self.stop_bgm()

            id_ending = data.get(
                "id_ending"
            )

            if id_ending:

                self.ending_terbuka.add(
                    id_ending
                )

            self.bersihkan_container()

            ending_frame = tk.Frame(
                self.container,
                bg=self.bg_color
            )

            ending_frame.pack(
                fill="both",
                expand=True
            )

            tk.Label(
                ending_frame,
                text=f"★ {data['judul']} ★",
                bg=self.bg_color,
                fg=self.accent_color,
                font=("Arial", 16, "bold")
            ).pack(
                pady=10
            )

            canvas_ending = tk.Canvas(
                ending_frame,
                width=760,
                height=260,
                bg="#111118",
                highlightthickness=2,
                highlightbackground="#33334d"
            )

            canvas_ending.pack(
                pady=8
            )

            self.ganti_gambar(
                data.get("gambar"),
                canvas_ending
            )

            lbl_pesan = tk.Label(
                ending_frame,
                text=data["pesan"],
                bg=self.box_color,
                fg=self.text_color,
                font=("Arial", 10),
                wraplength=720,
                justify="center",
                bd=2,
                relief="groove",
                padx=15,
                height=3
            )

            lbl_pesan.pack(
                fill="x",
                pady=8
            )

            # ================= MAIN DARI AWAL =================

            btn_ulang = tk.Button(
                ending_frame,
                text="🔄  MAIN DARI AWAL",
                bg="#2a9d8f",
                fg="white",
                font=("Arial", 10, "bold"),
                width=35,
                height=2,
                relief="flat",
                cursor="hand2",
                command=lambda: self.klik_dan_jalankan(
                    self.mulai_game
                )
            )

            btn_ulang.pack(
                pady=5
            )

            # ================= KEMBALI MENU =================

            btn_menu = tk.Button(
                ending_frame,
                text="🏠  KEMBALI KE MENU UTAMA",
                bg=self.btn_color,
                fg="white",
                font=("Arial", 10, "bold"),
                width=35,
                height=2,
                relief="flat",
                cursor="hand2",
                command=lambda: self.klik_dan_jalankan(
                    self.tampilkan_main_menu
                )
            )

            btn_menu.pack(
                pady=5
            )

            return

        # ================= SCENE CERITA BIASA =================

        self.lbl_nama.config(
            text=data.get(
                "nama",
                "Narator"
            )
        )

        self.lbl_teks.config(
            text=data.get(
                "teks",
                ""
            )
        )

        self.ganti_gambar(
            data.get("gambar"),
            self.canvas_visual
        )

        # ================= PILIHAN =================

        pilihan_tersedia = data.get(
            "pilihan",
            []
        )

        self.btn_lanjut.pack_forget()

        self.choice_frame.pack_forget()

        # ================= ADA PILIHAN =================

        if pilihan_tersedia:

            self.choice_frame.pack(
                fill="x",
                expand=True
            )

            for i, btn in enumerate(
                self.list_tombol
            ):

                if i < len(
                    pilihan_tersedia
                ):

                    pilihan_item = (
                        pilihan_tersedia[i]
                    )

                    btn.config(
                        text=pilihan_item["teks"],
                        state="normal",
                        command=lambda t=pilihan_item["tujuan"]:
                        self.klik_dan_muat(t)
                    )

                    if i < 2:

                        btn.grid(
                            row=0,
                            column=i,
                            sticky="nsew",
                            padx=5,
                            pady=3
                        )

                    else:

                        btn.grid(
                            row=1,
                            column=i - 2,
                            sticky="nsew",
                            padx=5,
                            pady=3
                        )

                else:

                    btn.grid_remove()

        # ================= TIDAK ADA PILIHAN =================

        else:

            tujuan_berikutnya = data.get(
                "tujuan"
            )

            if tujuan_berikutnya:

                self.btn_lanjut.config(
                    command=lambda t=tujuan_berikutnya:
                    self.klik_dan_muat(t)
                )

            else:

                self.btn_lanjut.config(
                    command=lambda:
                    self.klik_dan_jalankan(
                        self.tampilkan_main_menu
                    )
                )

            self.btn_lanjut.pack(
                fill="x",
                padx=5,
                pady=3
            )


# ================= JALANKAN PROGRAM =================

if __name__ == "__main__":

    root = tk.Tk()

    app = VisualNovelApp(
        root
    )

    # Pastikan BGM berhenti ketika window ditutup
    root.protocol(
        "WM_DELETE_WINDOW",
        lambda: (
            app.stop_bgm(),
            root.destroy()
        )
    )

    root.mainloop()