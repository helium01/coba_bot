import tkinter as tk
import mysql.connector

# Koneksi ke database MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="coba_bot"
)

# Fungsi untuk menambah data
def add_data():
    nama = nama_entry.get()
    alamat = alamat_entry.get()
    cursor = mydb.cursor()
    query = "INSERT INTO messages (message, pesan) VALUES (%s, %s)"
    values = (nama, alamat)
    cursor.execute(query, values)
    mydb.commit()
    show_data()

# Fungsi untuk menampilkan data
def show_data():
    cursor = mydb.cursor()
    query = "SELECT * FROM messages"
    cursor.execute(query)
    result = cursor.fetchall()
    data_listbox.delete(0, tk.END)
    for row in result:
        data_listbox.insert(tk.END, row)

# Fungsi untuk memperbarui data
def update_data():
    selected_data = data_listbox.get(data_listbox.curselection())
    id = selected_data[0]
    nama = nama_entry.get()
    alamat = alamat_entry.get()
    cursor = mydb.cursor()
    query = "UPDATE messages SET nama=%s, alamat=%s,  WHERE id=%s"
    values = (nama, alamat)
    cursor.execute(query, values)
    mydb.commit()
    show_data()

# Fungsi untuk menghapus data
def delete_data():
    selected_data = data_listbox.get(data_listbox.curselection())
    id = selected_data[0]
    cursor = mydb.cursor()
    query = "DELETE FROM messages WHERE id=%s"
    cursor.execute(query, (id,))
    mydb.commit()
    show_data()

# Membuat GUI
window = tk.Tk()
window.title("Aplikasi CRUD")
window.geometry("400x500")

# Membuat komponen GUI
nama_label = tk.Label(window, text="Nama:")
alamat_label = tk.Label(window, text="Alamat:")
nama_entry = tk.Entry(window)
alamat_entry = tk.Entry(window)
add_button = tk.Button(window, text="Tambah Data", command=add_data)
update_button = tk.Button(window, text="Perbarui Data", command=update_data)
delete_button = tk.Button(window, text="Hapus Data", command=delete_data)
data_listbox = tk.Listbox(window)

# Menempatkan komponen GUI di window
nama_label.pack(pady=10)
nama_entry.pack(pady=5)
alamat_label.pack(pady=10)
alamat_entry.pack(pady=5)
add_button.pack(pady=10)
update_button.pack(pady=10)
delete_button.pack(pady=10)
data_listbox.pack(pady=10)

# Menampilkan data pada aplikasi
show_data()

window.mainloop()
