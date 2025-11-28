# 🎬 CineVerse – Movie Ticket Booking System

CineVerse is a simple Python + Tkinter application connected with MySQL.  
It allows users to browse movies, book tickets, and view bookings through a clean dark-themed UI.

This is a beginner-friendly DBMS project and easy to run.

---

## 📁 How to Add Images

1. Create a folder named **images** in the project.
2. Add your character images inside it:
   - spiderman.png
   - ironman.png
3. Make sure the structure looks like this:

CineVerse/
│ movie_dashboard_main.py
│ config.py
│ README.md
└── images/
      spiderman.png
      ironman.png

The app will automatically load these images when you open the Home Page.

---

## ▶️ How to Run the Project

1. Install required libraries: pip install pillow mysql-connector-python

2. Create the database using MySQL Workbench  
   (Run the SQL file or copy the SQL setup code from this repo.)

3. Open **config.py** and update your MySQL username and password.

4. Run the application: python movie_dashboard_main.py


---

## 🧭 How to Use the Application

### 🏠 Home Page  
- Shows the main welcome screen with cinematic UI.  
- Click the card **"Check Movies"** to see the movie list.

### 🎞 Movies Page  
- Shows all movies stored in the database.  
- Use the search bar to filter movies by name.

### 🎟 Book Ticket  
- Select a movie  
- Enter your name  
- Enter number of seats  
- Click **Confirm Booking**  
- Your latest bookings will appear below.

### 📋 View Bookings  
- Shows all bookings stored in the database.  
- Displays movie name, customer, seats, and date.

---

## 👨‍🏫 Credits
Developed by **Swaroop**, **Abhishek**, and **Kuldeep**  
as part of our DBMS mini project.

---

## 📌 Notes
- You can replace Spider-Man and Iron Man images with any PNG you like.  
- Make sure your images are named correctly and placed inside the **images** folder.  
- The database must be created before running the app.








