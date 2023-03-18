import tkinter as tk
from tkinter import ttk
import json

# Read the current settings from the file
def read_settings():
    with open("settings.txt", "r") as settings_file:
        settings = json.loads(settings_file.read().replace('\n', ''))
    return settings

# Save the current settings to the file
def save_settings(settings):
    with open("settings.txt", "w") as settings_file:
        json.dump(settings, settings_file, indent=4)

# Callback function for the Save button
def save_button_callback():
    settings["deathVolume"] = death_volume_slider.get()
    settings["bombExplosionVolume"] = bomb_volume_slider.get()
    settings["flashVolume"] = flash_volume_slider.get()
    save_settings(settings)

# Callback function for slider updates
def slider_update(*args):
    death_volume_value.set(round(death_volume_slider.get(), 2))
    bomb_volume_value.set(round(bomb_volume_slider.get(), 2))
    flash_volume_value.set(round(flash_volume_slider.get(), 2))

settings = read_settings()

# Create the main window
root = tk.Tk()
root.title("CSGO Volume Settings")
root.geometry("350x200")

# Create and configure the sliders
death_volume_slider = ttk.Scale(root, from_=0, to=1, value=settings["deathVolume"], orient="horizontal", command=slider_update)
death_volume_slider.grid(column=1, row=0)

bomb_volume_slider = ttk.Scale(root, from_=0, to=1, value=settings["bombExplosionVolume"], orient="horizontal", command=slider_update)
bomb_volume_slider.grid(column=1, row=1)

flash_volume_slider = ttk.Scale(root, from_=0, to=1, value=settings["flashVolume"], orient="horizontal", command=slider_update)
flash_volume_slider.grid(column=1, row=2)

# Create and configure the labels
death_volume_label = ttk.Label(root, text="Death Volume")
death_volume_label.grid(column=0, row=0)

bomb_volume_label = ttk.Label(root, text="Bomb Explosion Volume")
bomb_volume_label.grid(column=0, row=1)

flash_volume_label = ttk.Label(root, text="Flash Volume")
flash_volume_label.grid(column=0, row=2)

# Create and configure the value labels
death_volume_value = tk.StringVar()
death_volume_value.set(round(settings["deathVolume"], 2))
death_volume_value_label = ttk.Label(root, textvariable=death_volume_value)
death_volume_value_label.grid(column=2, row=0)

bomb_volume_value = tk.StringVar()
bomb_volume_value.set(round(settings["bombExplosionVolume"], 2))
bomb_volume_value_label = ttk.Label(root, textvariable=bomb_volume_value)
bomb_volume_value_label.grid(column=2, row=1)

flash_volume_value = tk.StringVar()
flash_volume_value.set(round(settings["flashVolume"], 2))
flash_volume_value_label = ttk.Label(root, textvariable=flash_volume_value)
flash_volume_value_label.grid(column=2, row=2)

# Create and configure the Save button
save_button = ttk.Button(root, text="Save", command=save_button_callback)
save_button.grid(column=1, row=3)

# Start the Tkinter event loop
root.mainloop()
