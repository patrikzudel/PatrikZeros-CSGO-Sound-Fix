import customtkinter as ctk
import json

# set default values

class SettingsGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Settings")
        self.toplevel_window = None
        default_values = {}
        try:
            with open("settings.txt", "r") as f:
                default_values = json.load(f)
        except:
            default_values = {"deathVolume": 0.20, "bombExplosionVolume": 0.20, "flashVolume": 0}

        self.deathVolume_label = ctk.CTkLabel(
            master=self, text=f"Volume when dead: {int(default_values['deathVolume']*100)}%")
        self.deathVolume_label.grid(
            row=1, column=0, padx=10, pady=5, sticky="w")
        def slider_deathVolume(value):
            text = f"Volume when dead: {int(value)}%"
            self.deathVolume_label.configure(text=text)
            print(text)
        self.deathVolume_entry = ctk.CTkSlider(master=self, from_=0, to=100, number_of_steps=100, command=slider_deathVolume)
        self.deathVolume_entry.set(default_values["deathVolume"]*100)
        self.deathVolume_entry.grid(
            row=1, column=1, padx=10, pady=5, sticky="e")

        self.bombExplosionVolume_label = ctk.CTkLabel(
            master=self, text=f"Volume when bomb explodes: {int(default_values['bombExplosionVolume']*100)}%")
        self.bombExplosionVolume_label.grid(
            row=2, column=0, padx=10, pady=5, sticky="w")
        def slider_bombExplosionVolume(value):
            text = f"Volume when bomb explodes: {int(value)}%"
            self.bombExplosionVolume_label.configure(text=text)
            print(text)
        self.bombExplosionVolume_entry = ctk.CTkSlider(master=self, from_=0, to=100, number_of_steps=100, command=slider_bombExplosionVolume)
        self.bombExplosionVolume_entry.set(default_values["bombExplosionVolume"]*100)
        self.bombExplosionVolume_entry.grid(
            row=2, column=1, padx=10, pady=5, sticky="e")

        self.flashVolume_label = ctk.CTkLabel(
            master=self, text=f"Volume when flashed: {int(default_values['flashVolume']*100)}%")
        self.flashVolume_label.grid(
            row=3, column=0, padx=10, pady=5, sticky="w")
        def slider_flashVolume(value):
            text = f"Volume when flashed: {int(value)}%"
            self.flashVolume_label.configure(text=text)
            print(text)
        self.flashVolume_entry = ctk.CTkSlider(master=self, from_=0, to=100, number_of_steps=100, command=slider_flashVolume)
        self.flashVolume_entry.set(default_values["flashVolume"]*100)
        self.flashVolume_entry.grid(
            row=3, column=1, padx=10, pady=5, sticky="e")

        # create a save button that calls the save_settings() function
        self.save_button = ctk.CTkButton(
            master=self, text="Save", command=self.save_settings)
        self.save_button.grid(row=20, columnspan=2, padx=10, pady=10)

        # create a label for status messages
        self.status_label = ctk.CTkLabel(master=self, text="")
        self.status_label.grid(row=21, columnspan=2)

    def clear_status_message(self):
        # clear the status message after a timeout period
        self.status_label.configure(text="")

    def save_settings(self):
        # get the user-inputted values for each setting
        deathVolume = float(self.deathVolume_entry.get()/100)
        bombeExplosionVolume = float(self.bombExplosionVolume_entry.get()/100)
        flashVolume = float(self.flashVolume_entry.get()/100)

        # create a dictionary of the user-inputted settings
        settings_dict = {"deathVolume": deathVolume, "bombExplosionVolume": bombeExplosionVolume, "flashVolume": flashVolume}

        # save the settings to a JSON file
        with open("settings.txt", "w") as f:
            json.dump(settings_dict, f)

        # show a message to the user indicating the settings were saved
        # ctk.messagebox.showinfo(title="Settings", message="Settings saved successfully!")
        self.status_label.configure(text="Settings saved!")
        self.after(3000, self.clear_status_message)


if __name__ == "__main__":
    settings_gui = SettingsGUI()
    settings_gui.mainloop()
