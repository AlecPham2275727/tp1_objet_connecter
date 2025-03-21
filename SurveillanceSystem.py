import tkinter
from HardwareController import HardwareController
from Status import Status

class SurveillanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Système de Surveillance")
        self.root.geometry("700x250")
        self.root.configure(bg="#2C2F33")
        self.root.resizable(False, False)

        self.hardware = HardwareController()

        self.create_widgets()
        self.update_temperature()
        self.deactivate_test_mode()

    def create_widgets(self):

        menu_title = tkinter.Label(self.root, text="Système de Surveillance", font=("Arial", 16, "bold"),
                                   fg="white", bg="#2C2F33")
        menu_title.grid(row=0, column=0, columnspan=2, pady=10, padx=50)

        tkinter.Label(self.root, text="Température:", font=("Arial", 12),
                      fg="white", bg="#2C2F33").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.temperature_value = tkinter.Label(self.root, text="", font=("Arial", 12, "bold"),
                                               fg="red", bg="#2C2F33")
        self.temperature_value.grid(row=1, column=1, sticky="w", padx=10)

        tkinter.Label(self.root, text="État de la porte:", font=("Arial", 12),
                      fg="white", bg="#2C2F33").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.door_state_value = tkinter.Label(self.root, text="Ouverte", font=("Arial", 12, "bold"),
                                              fg="yellow", bg="#2C2F33")
        self.door_state_value.grid(row=2, column=1, sticky="w", padx=10)

        tkinter.Label(self.root, text="Mode Test:", font=("Arial", 12),
                      fg="white", bg="#2C2F33").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.test_mode_value = tkinter.Label(self.root, text="Désactivé", font=("Arial", 12, "bold"),
                                             fg="yellow", bg="#2C2F33")
        self.test_mode_value.grid(row=3, column=1, sticky="w", padx=10)


        # SECTION: TEST
        self.test_mode_btn = tkinter.Button(self.root, text="Activer/Désactiver Test Mode", command=self.toggle_test_mode)
        self.test_mode_btn.grid(row=4, column=1, pady=1)

        tkinter.Label(self.root, text="Température:", font=("Arial", 12),
                      fg="white", bg="#2C2F33").grid(row=0, column=2, pady=10, padx=5)

        self.increase_temp_btn = tkinter.Button(self.root, text="+", command=self.increase_temp)
        self.increase_temp_btn.grid(row=1, column=2, pady=10, padx=5)

        self.decrease_temp_btn = tkinter.Button(self.root, text="-", command=self.decrease_temp)
        self.decrease_temp_btn.grid(row=2, column=2, pady=10, padx=5)

        tkinter.Label(self.root, text="Trappe:", font=("Arial", 12),
                      fg="white", bg="#2C2F33").grid(row=0, column=3, pady=10, padx=5)

        self.open_door_btn = tkinter.Button(self.root, text="Ouvrir", command=self.open_door)
        self.open_door_btn.grid(row=1, column=3, pady=10, padx=5)

        self.close_door_btn = tkinter.Button(self.root, text="Fermer", command=self.close_door)
        self.close_door_btn.grid(row=2, column=3, pady=10, padx=5)

        tkinter.Label(self.root, text="Alarme:", font=("Arial", 12),
                      fg="white", bg="#2C2F33").grid(row=0, column=4, pady=10, padx=5)

        self.activate_alarm_btn = tkinter.Button(self.root, text="Activer", command=self.activate_alarm)
        self.activate_alarm_btn.grid(row=1, column=4, pady=10, padx=5)

        self.deactivate_alarm_btn = tkinter.Button(self.root, text="Désactiver", command=self.deactivate_alarm)
        self.deactivate_alarm_btn.grid(row=2, column=4, pady=10, padx=5)

    def update_temperature(self):
        temp = self.hardware.current_temp
        self.temperature_value.config(text=f"{temp}°C")

        self.hardware.check_temperature(self.handle_alert)
    
        self.root.after(500, self.update_temperature)

    def handle_alert(self, status ):
        if status == Status.ALERT:
            self.door_state_value.config(text="Fermée", fg="red")
        else:
            self.door_state_value.config(text="Ouverte", fg="yellow")
    
    def toggle_test_mode(self):
        if self.hardware.is_test_mode:
            self.deactivate_test_mode()
        else:
            self.activate_test_mode()

    def activate_test_mode(self):
        self.hardware.activate_test_mode()
        self.test_mode_value.config(text="Activé", fg="yellow")
        self.increase_temp_btn.config(state="normal")
        self.decrease_temp_btn.config(state="normal")
        self.open_door_btn.config(state="normal")
        self.close_door_btn.config(state="normal")
        self.activate_alarm_btn.config(state="normal")
        self.deactivate_alarm_btn.config(state="normal")
        

    def deactivate_test_mode(self):
        self.hardware.deactivate_test_mode()
        self.test_mode_value.config(text="Désactivé", fg="yellow")
        self.increase_temp_btn.config(state="disabled")
        self.decrease_temp_btn.config(state="disabled")
        self.open_door_btn.config(state="disabled")
        self.close_door_btn.config(state="disabled")
        self.activate_alarm_btn.config(state="disabled")
        self.deactivate_alarm_btn.config(state="disabled")

    def increase_temp(self):
        self.hardware.increase_temp()

    def decrease_temp(self):
        self.hardware.decrease_temp()

    def open_door(self):
        self.hardware.open_door()
        self.handle_alert(Status.SAFE)
        
    def close_door(self):
        self.hardware.close_door()
        self.handle_alert(Status.ALERT)

    def activate_alarm(self):
        self.hardware.activate_alarm()

    def deactivate_alarm(self):
        self.hardware.deactivate_alarm()
