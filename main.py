import tkinter as tk
import mysql.connector

# Koneksi ke database MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="coba_bot"
)

def add_data():
    nama = nama_entry.get()
    alamat = alamat_entry.get()
    cursor = mydb.cursor()
    query = "INSERT INTO messages (message, pesan) VALUES (%s, %s)"
    values = (nama, alamat)
    cursor.execute(query, values)
    mydb.commit()
    show_data()
    nama_entry.delete(0, tk.END)
    alamat_entry.delete(0, tk.END)

def show_data():
    cursor = mydb.cursor()
    query = "SELECT * FROM messages"
    cursor.execute(query)
    result = cursor.fetchall()
    data_listbox.delete(0, tk.END)
    for row in result:
        data_listbox.insert(tk.END, row)



# Fungsi untuk mengambil jawaban dari database MySQL
def get_response(user_input):
    cursor = mydb.cursor()
    query = "SELECT * FROM messages WHERE message=%s"
    cursor.execute(query, (user_input,))
    result = cursor.fetchone()
    if result:
        return result[1]
    else:
        return "Maaf, saya tidak mengerti."

# Fungsi untuk menampilkan pesan di GUI
def send():
    user_input = input_field.get()
    chat_history.insert(tk.END, "Anda: " + user_input + "\n")
    chat_history.insert(tk.END, "Chatbot: " + get_response(user_input) + "\n")
    input_field.delete(0, tk.END)

# Membuat GUI
window = tk.Tk()
window.title("Chatbot helium01 ")
window.geometry("400x500")

nama_label = tk.Label(window, text="Chat:")
alamat_label = tk.Label(window, text="Pesan:")
nama_entry = tk.Entry(window)
alamat_entry = tk.Entry(window)
add_button = tk.Button(window, text="Tambah Data", command=add_data)
data_listbox = tk.Listbox(window)

# Membuat komponen GUI
chat_history = tk.Text(window)
input_field = tk.Entry(window)
send_button = tk.Button(window, text="Kirim", command=send)

# Menempatkan komponen GUI di window
chat_history.pack(pady=10)
input_field.pack(pady=10)
send_button.pack(pady=10)
nama_label.pack(pady=20)
nama_entry.pack(pady=15)
alamat_label.pack(pady=20)
alamat_entry.pack(pady=15)
add_button.pack(pady=20)

window.mainloop()
