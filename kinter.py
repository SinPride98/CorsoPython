#kinter
#ci/cd metodoogia ricerca
import customtkinter as tk

def button_event():
    print("button pressed")
def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())
def combobox_callback(choice):
    print("combobox dropdown clicked:", choice)
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)
def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())
def segmented_button_callback(value):
    print("segmented button clicked:", value)
def slider_event(value):
    print(value)
def switch_event():
    print("switch toggled, current value:", switch_var.get())


tk.set_default_color_theme("dark-blue")
app=tk.CTk()
app.title("la mia finestra")
app.geometry("700x900")

button = tk.CTkButton(app, text="CTkButton", command=button_event)
button.pack(pady=20)  

check_var = tk.StringVar(value="on")
#check_var2 = tk.StringVar(value="on")
checkbox = tk.CTkCheckBox(app, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
"""checkbox2 = tk.CTkCheckBox(app, text="CTkCheckBox2", command=checkbox_event,
                                     variable=check_var2, onvalue="on", offvalue="off")"""
checkbox.pack(pady=20)
#checkbox2.pack(pady=20)

combobox_var = tk.StringVar(value="option 2")
combobox = tk.CTkComboBox(app, values=["option 1", "option 2"],
                                     command=combobox_callback, variable=combobox_var)
combobox_var.set("option 2")

combobox.pack(pady=20)

entry = tk.CTkEntry(app, placeholder_text="CTkEntry")
entry.pack(pady=20)

label = tk.CTkLabel(app, text="CTkLabel", fg_color="transparent")
label.pack(pady=20)

optionmenu_var = tk.StringVar(value="option 2")
optionmenu = tk.CTkOptionMenu(app,values=["option 1", "option 2"],
                                         command=optionmenu_callback,
                                         variable=optionmenu_var)
optionmenu.pack(pady=20)

progressbar = tk.CTkProgressBar(app, orientation="horizontal")
progressbar.pack(pady=20)

radio_var = tk.IntVar(value=0)
radiobutton_1 = tk.CTkRadioButton(app, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value=1)
radiobutton_2 = tk.CTkRadioButton(app, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value=2)

radiobutton_1.pack(pady=20)
radiobutton_2.pack(pady=20)

segemented_button_var = tk.StringVar(value="Value 1")
segemented_button = tk.CTkSegmentedButton(app, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback,
                                                     variable=segemented_button_var)
segemented_button.pack(pady=20)

slider = tk.CTkSlider(app, from_=0, to=100, command=slider_event)
slider.pack(pady=20)

switch_var = tk.StringVar(value="on")
switch = tk.CTkSwitch(app, text="CTkSwitch", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")
switch.pack(pady=20)


"""tabview = tk.CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

tabview.add("tab 1")  # add tab at the end
tabview.add("tab 2")  # add tab at the end
tabview.set("tab 2")  # set currently visible tab

button = tk.CTkButton(master=tabview.tab("tab 1"))
button.pack(padx=20, pady=20)"""

textbox = tk.CTkTextbox(app)

textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
textbox.delete("0.0", "end")  # delete all text
#textbox.configure(state="disabled")   configure textbox to be read-only
textbox.pack(pady=20)

app.mainloop()

