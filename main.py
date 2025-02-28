import tkinter

def read_temp():
    return "25°C"

def open_door():
    door_state_value.config(text="Ouverte", fg="yellow")

def close_door():
    door_state_value.config(text="Fermée", fg="yellow")

def activate_test_mode():
    test_mode_value.config(text="Activé", fg="yellow")

def deactivate_test_mode():
    test_mode_value.config(text="Désactivé", fg="yellow")

window = tkinter.Tk()
window.title("Système de Surveillance")
window.geometry("350x250")
window.configure(bg="#2C2F33")

menu_title = tkinter.Label(window, text="Système de Surveillance", font=("Arial", 16, "bold"), fg="white", bg="#2C2F33")
menu_title.grid(row=0, column=0, columnspan=2, pady=10, padx=50)

temperature_title = tkinter.Label(window, text="Température:", font=("Arial", 12), fg="white", bg="#2C2F33")
temperature_title.grid(row=1, column=0, sticky="w", padx=10, pady=5)
temperature_value = tkinter.Label(window, text=read_temp(), font=("Arial", 12, "bold"), fg="red", bg="#2C2F33")
temperature_value.grid(row=1, column=1, sticky="w", padx=10)

door_state_title = tkinter.Label(window, text="État de la porte:", font=("Arial", 12), fg="white", bg="#2C2F33")
door_state_title.grid(row=2, column=0, sticky="w", padx=10, pady=5)
door_state_value = tkinter.Label(window, text="Fermée", font=("Arial", 12, "bold"), fg="yellow", bg="#2C2F33")
door_state_value.grid(row=2, column=1, sticky="w", padx=10)

test_mode_label = tkinter.Label(window, text="Mode Test:", font=("Arial", 12), fg="white", bg="#2C2F33")
test_mode_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
test_mode_value = tkinter.Label(window, text="Désactivé", font=("Arial", 12, "bold"), fg="yellow", bg="#2C2F33")
test_mode_value.grid(row=3, column=1, sticky="w", padx=10)

window.mainloop()
