# ------------------------------------------------------------
#  CineVerse - Movie Ticket Booking System (Final Fixed)
#  Backend: MySQL   |  Frontend: Tkinter (Dark Mode)
#  Team: Swaroop, Abhishek, Kuldeep
# ------------------------------------------------------------

import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from config import get_connection

# ---------------- THEME COLORS ----------------
BG = "#0D0D0D"
CARD_BG = "#1E1E1E"
ACCENT = "#E50914"
TEXT = "#FFFFFF"
TEXT_FADE = "#AAAAAA"

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("CineVerse - Movie Ticket Booking System")
root.geometry("1100x650")
root.minsize(950, 550)
root.config(bg=BG)

# ---------------- NAVIGATION BAR ----------------
nav_bar = tk.Frame(root, bg="#161616", height=60)
nav_bar.pack(fill="x", side="top")

title_label = tk.Label(nav_bar, text="CineVerse - Movie Ticket Booking",
                       bg="#161616", fg="white", font=("Segoe UI Semibold", 20))
title_label.pack(side="left", padx=20)

nav_buttons_frame = tk.Frame(nav_bar, bg="#161616")
nav_buttons_frame.pack(side="right", padx=20)

# ---------------- CONTENT FRAME ----------------
content_frame = tk.Frame(root, bg=BG)
content_frame.pack(fill="both", expand=True)

def clear_content():
    for w in content_frame.winfo_children():
        w.destroy()

# ============================================================
#                        HOME PAGE
# ============================================================
def home_page():
    clear_content()

    base_path = os.path.dirname(os.path.abspath(__file__))

    # Spider-Man (upright)
    try:
        spiderman_path = os.path.join(base_path, "images", "spiderman.png")
        spider_img = Image.open(spiderman_path).resize((380, 380))
        spider_photo = ImageTk.PhotoImage(spider_img)
        spider_label = tk.Label(content_frame, image=spider_photo, bg=BG)
        spider_label.image = spider_photo
        spider_label.place(relx=0.72, rely=-0.03)
    except Exception as e:
        print("⚠️ Spider-Man image missing or failed to load:", e)

    # Iron Man
    try:
        ironman_path = os.path.join(base_path, "images", "ironman.png")
        iron_img = Image.open(ironman_path).resize((280, 380))
        iron_photo = ImageTk.PhotoImage(iron_img)
        iron_label = tk.Label(content_frame, image=iron_photo, bg=BG)
        iron_label.image = iron_photo
        iron_label.place(relx=0.03, rely=0.35)
    except Exception as e:
        print("⚠️ Iron Man image missing or failed to load:", e)

    # Title and subtitle
    tk.Label(content_frame, text="Welcome to CineVerse",
             bg=BG, fg=TEXT, font=("Segoe UI Semibold", 28)).pack(pady=(50, 10))
    tk.Label(content_frame, text="Your One-Stop Platform to Explore and Book Movies Instantly",
             bg=BG, fg="#B0B0B0", font=("Segoe UI", 12)).pack()

    # Main feature card
    card = tk.Frame(content_frame, bg=CARD_BG, padx=35, pady=35)
    card.pack(pady=60)
    tk.Label(card, text="Check Movies", bg=CARD_BG, fg=ACCENT,
             font=("Segoe UI Semibold", 22)).pack(pady=(0, 8))
    tk.Label(card, text="Explore the latest movies now showing in theaters near you!",
             bg=CARD_BG, fg=TEXT_FADE, font=("Segoe UI", 11)).pack(pady=(0, 15))

    def on_enter(e): card.config(bg="#292929")
    def on_leave(e): card.config(bg=CARD_BG)
    card.bind("<Enter>", on_enter)
    card.bind("<Leave>", on_leave)
    card.bind("<Button-1>", lambda e: movies_page())

    footer = tk.Label(content_frame,
                      text="Made with ❤️ by Swaroop, Abhishek, Kuldeep",
                      bg=BG, fg="#888", font=("Segoe UI", 10, "italic"))
    footer.pack(side="bottom", pady=15)
    footer.bind("<Enter>", lambda e: footer.config(fg=ACCENT))
    footer.bind("<Leave>", lambda e: footer.config(fg="#888"))

# ============================================================
#                      MOVIES PAGE
# ============================================================
def movies_page():
    clear_content()
    tk.Label(content_frame, text="Browse Movies",
             bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(pady=10)

    search_frame = tk.Frame(content_frame, bg=BG)
    search_frame.pack(pady=(5, 10))
    tk.Label(search_frame, text="Search:", bg=BG, fg="#CCCCCC",
             font=("Segoe UI", 11)).pack(side="left", padx=5)
    search_var = tk.StringVar()
    search_entry = tk.Entry(search_frame, textvariable=search_var,
                            bg=CARD_BG, fg=TEXT, relief="flat",
                            insertbackground="white", width=35)
    search_entry.pack(side="left", padx=5)

    container = tk.Frame(content_frame, bg=BG)
    container.pack(fill="both", expand=True, padx=20, pady=10)
    canvas = tk.Canvas(container, bg=BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=BG)
    scroll_frame.bind("<Configure>",
                      lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def fetch_and_display(keyword=""):
        for w in scroll_frame.winfo_children(): w.destroy()
        conn = get_connection()
        cur = conn.cursor()
        if keyword:
            cur.execute("SELECT title, genre, duration, release_date FROM movie WHERE title LIKE %s LIMIT 200",
                        (f"%{keyword}%",))
        else:
            cur.execute("SELECT title, genre, duration, release_date FROM movie LIMIT 200")
        data = cur.fetchall()
        conn.close()

        if not data:
            tk.Label(scroll_frame, text="No movies found.",
                     bg=BG, fg="#888", font=("Segoe UI", 11)).pack(pady=10)
            return

        header = tk.Label(scroll_frame,
                          text=f"{'Title':<35} {'Genre':<15} {'Duration':<10} {'Release Date':<12}",
                          bg=BG, fg=ACCENT, font=("Consolas", 12, "bold"))
        header.pack(anchor="w", padx=30)
        tk.Label(scroll_frame, text="-" * 80,
                 bg=BG, fg="#333").pack(anchor="w", padx=30)

        for m in data:
            line = f"{m[0]:<35} {m[1]:<15} {m[2]:<10} {m[3]}"
            tk.Label(scroll_frame, text=line, bg=BG, fg="#CCCCCC",
                     font=("Consolas", 11)).pack(anchor="w", padx=30, pady=2)

    def on_search(*args): fetch_and_display(search_var.get().strip())
    search_var.trace("w", on_search)
    fetch_and_display()

# ============================================================
#             BOOK TICKET PAGE
# ============================================================
def book_ticket_page():
    clear_content()
    tk.Label(content_frame, text="Book Your Ticket",
             bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(pady=20)

    form = tk.Frame(content_frame, bg=BG)
    form.pack(pady=10)

    tk.Label(form, text="Select Movie:", bg=BG, fg=TEXT_FADE,
             font=("Segoe UI", 11)).grid(row=0, column=0, sticky="e", pady=8, padx=10)
    tk.Label(form, text="Your Name:", bg=BG, fg=TEXT_FADE,
             font=("Segoe UI", 11)).grid(row=1, column=0, sticky="e", pady=8, padx=10)
    tk.Label(form, text="Seats to Book:", bg=BG, fg=TEXT_FADE,
             font=("Segoe UI", 11)).grid(row=2, column=0, sticky="e", pady=8, padx=10)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT title FROM movie ORDER BY title ASC LIMIT 500")
    movie_list = [r[0] for r in cur.fetchall()]
    conn.close()

    selected_movie = tk.StringVar()
    movie_dropdown = ttk.Combobox(form, textvariable=selected_movie,
                                  values=movie_list, width=40, state="readonly")
    movie_dropdown.grid(row=0, column=1, pady=8, padx=10)

    name_entry = tk.Entry(form, width=42, bg=CARD_BG, fg=TEXT,
                          insertbackground="white", relief="flat")
    name_entry.grid(row=1, column=1, pady=8, padx=10)

    seats_entry = tk.Entry(form, width=42, bg=CARD_BG, fg=TEXT,
                           insertbackground="white", relief="flat")
    seats_entry.grid(row=2, column=1, pady=8, padx=10)

    result_label = tk.Label(content_frame, bg=BG, fg="#00FF99", font=("Segoe UI", 10))
    result_label.pack(pady=5)

    recent_box = tk.Frame(content_frame, bg=BG)
    recent_box.pack(pady=5)

    def confirm_booking():
        movie = selected_movie.get()
        name = name_entry.get().strip()
        seats = seats_entry.get().strip()
        if not movie or not name or not seats:
            result_label.config(text="Please fill all fields.", fg="red")
            return
        try:
            seats = int(seats)
            if seats <= 0:
                raise ValueError
        except:
            result_label.config(text="Seats must be a positive number.", fg="red")
            return

        conn = get_connection()
        cur = conn.cursor()

        # find or create showtime
        cur.execute("SELECT s.show_id FROM showtime s JOIN movie m ON s.movie_id = m.movie_id WHERE m.title=%s LIMIT 1", (movie,))
        row = cur.fetchone()
        if row:
            show_id = row[0]
        else:
            cur.execute("SELECT movie_id FROM movie WHERE title=%s LIMIT 1", (movie,))
            mid_row = cur.fetchone()
            if mid_row:
                movie_id = mid_row[0]
                cur.execute("INSERT INTO showtime (movie_id, show_date, show_time, total_seats) VALUES (%s, CURDATE(), '18:00:00', 100)", (movie_id,))
                conn.commit()
                show_id = cur.lastrowid
            else:
                result_label.config(text="Movie not found in database.", fg="red")
                conn.close()
                return

        # insert booking
        cur.execute("INSERT INTO booking (show_id, customer_name, seats_booked, booking_date) VALUES (%s, %s, %s, CURDATE())",
                    (show_id, name, seats))
        conn.commit()
        result_label.config(text="Booking confirmed!", fg="#00FF99")
        show_latest_bookings(name)
        conn.close()

    def show_latest_bookings(name):
        for w in recent_box.winfo_children(): w.destroy()
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT m.title, b.seats_booked, b.booking_date
            FROM booking b
            JOIN showtime s ON b.show_id = s.show_id
            JOIN movie m ON s.movie_id = m.movie_id
            WHERE b.customer_name=%s
            ORDER BY b.booking_id DESC LIMIT 5;
        """, (name,))
        data = cur.fetchall()
        conn.close()
        if data:
            tk.Label(recent_box, text=f"Recent Bookings for {name}",
                     bg=BG, fg=ACCENT, font=("Segoe UI", 12, "bold")).pack(pady=10)
            for row in data:
                tk.Label(recent_box, text=f"{row[0]} | Seats: {row[1]} | Date: {row[2]}",
                         bg=BG, fg=TEXT_FADE, font=("Segoe UI", 10)).pack(pady=2)
        else:
            tk.Label(recent_box, text="No bookings found.",
                     bg=BG, fg="#888", font=("Segoe UI", 10)).pack(pady=6)

    tk.Button(form, text="Confirm Booking", bg=ACCENT, fg="white",
              activebackground="#B2060F", relief="flat",
              font=("Segoe UI", 10, "bold"), padx=12, pady=6,
              command=confirm_booking).grid(row=3, columnspan=2, pady=20)

# ============================================================
#                   VIEW BOOKINGS PAGE
# ============================================================
def view_bookings_page():
    clear_content()
    tk.Label(content_frame, text="All Bookings",
             bg=BG, fg=TEXT, font=("Segoe UI Semibold", 18)).pack(pady=20)

    container = tk.Frame(content_frame, bg=BG)
    container.pack(fill="both", expand=True, padx=20, pady=10)
    canvas = tk.Canvas(container, bg=BG, highlightthickness=0)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg=BG)
    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT b.customer_name, m.title, b.seats_booked, b.booking_date
        FROM booking b
        JOIN showtime s ON b.show_id = s.show_id
        JOIN movie m ON s.movie_id = m.movie_id
        ORDER BY b.booking_id DESC;
    """)
    data = cur.fetchall()
    conn.close()

    if not data:
        tk.Label(scroll_frame, text="No bookings yet.", bg=BG,
                 fg="#888", font=("Segoe UI", 11)).pack(pady=10)
        return

    tk.Label(scroll_frame, text=f"{'Name':<15} {'Movie':<25} {'Seats':<10} {'Date':<15}",
             bg=BG, fg=ACCENT, font=("Consolas", 12, "bold")).pack(anchor="w", padx=30)
    tk.Label(scroll_frame, text="-" * 80, bg=BG, fg="#333").pack(anchor="w", padx=30)

    for row in data:
        tk.Label(scroll_frame, text=f"{row[0]:<15} {row[1]:<25} {row[2]:<10} {row[3]}",
                 bg=BG, fg="#CCCCCC", font=("Consolas", 11)).pack(anchor="w", padx=30, pady=2)

# ============================================================
#                     NAVIGATION BUTTONS
# ============================================================
def create_nav_button(text, command):
    btn = tk.Label(nav_buttons_frame, text=text, bg="#161616", fg="#AAAAAA",
                   font=("Segoe UI", 10, "bold"), padx=10, pady=6, cursor="hand2")
    btn.pack(side="left", padx=8)
    btn.bind("<Enter>", lambda e: btn.config(bg=ACCENT, fg="white"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#161616", fg="#AAAAAA"))
    btn.bind("<Button-1>", lambda e: command())

create_nav_button("Home", home_page)
create_nav_button("Movies", movies_page)
create_nav_button("Book", book_ticket_page)
create_nav_button("Bookings", view_bookings_page)

# ============================================================
#                      DEFAULT PAGE
# ============================================================
home_page()
root.mainloop()
