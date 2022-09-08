from tkinter import * 
import customtkinter
from PIL import ImageTk, Image
from player import Player

root = customtkinter.CTk()

root.title('Monopoly Tax GUI')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
root.iconbitmap('/Users/german/Documents/Coding/Python projects/My coding projects/GUI/Tkinter/Monopoly/favicon.ico')
root.geometry("1380x600")
root.configure(bg='black')


#Player 1

def money_calc():
    player_1.money += int(player_1_entry_bank.get())
    player_1_money.configure(text=f"Bank: ${player_1.money}")
    player_1.ground += int(player_1_entry_ground.get())
    player_1_ground.configure(text=f"Ground: ${player_1.ground}")
    player_1.real_estate += int(player_1_entry_re.get())
    player_1_real_estate.configure(text=f"RE: ${player_1.real_estate}")
    
    player_1_entry_bank.delete(0, END)
    player_1_entry_ground.delete(0, END)
    player_1_entry_re.delete(0, END)

    player_1_entry_bank.insert(0, '0')
    player_1_entry_ground.insert(0, '0')
    player_1_entry_re.insert(0, '0')
    
def calculate_tax(): 
    player_1.calc_tax()
    player_1_money.configure(text=f"Bank: ${player_1.money}")
#Making the elements
player_1 = Player()

player_1_frame = customtkinter.CTkFrame(master=root,
                               width=500,
                               height=300,
                               corner_radius=10,
                               bg='black',
                               fg_color='#FEB139',
                               border_width=2, border_color="white")

player_1_label = customtkinter.CTkEntry(root, width=195,
                               height=40,
                               corner_radius=10,
                               fg_color='#0F3D3E',
                               text_font=('Times New Roman', 26),
                               justify=CENTER,
                               bg_color='#FEB139',
                               border_width=2, border_color="white"
                               )

player_1_money = customtkinter.CTkLabel(root, text=f"Bank: ${player_1.money}", width=130,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#FEB139')

player_1_ground = customtkinter.CTkLabel(root, text=f"Ground: ${player_1.ground}", width=130,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#FEB139')

player_1_real_estate = customtkinter.CTkLabel(root, text=f"RE: ${player_1.ground}", width=140,
                               height=40,
                               fg_color=("white", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#FEB139')

player_1_entry_bank = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#0F3D3E',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#FEB139',
                               border_width=2, border_color="white"
                            )

player_1_entry_ground = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#0F3D3E',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#E2DCC8',
                               border_width=2, border_color="white"
                            )

player_1_entry_re = customtkinter.CTkEntry(root, width=130,
                               height=40,
                               corner_radius=10,
                            fg_color='#0F3D3E',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#FEB139',
                               border_width=2, border_color="white"
                            )

player_1_button = customtkinter.CTkButton(root, command=money_calc, width=195,
                                 height=40,
                                 corner_radius=8,
                                 text="Add/Subtract Money",
                                 fg_color='#0F3D3E',
                                 text_font=('Times New Roman', 20),
                               bg_color='#FEB139',
                               hover_color='#3AB4F2',
                               border_width=2, border_color="white"
                                 )

player_1_button_tax = customtkinter.CTkButton(root, command=calculate_tax, width=195,
                                 height=40,
                                 corner_radius=8,
                                 text="Calculate Tax",
                                 fg_color='#0F3D3E',
                                 text_font=('Times New Roman', 20),
                               bg_color='#FEB139',
                               hover_color='#3AB4F2',
                               border_width=2, border_color="white"
                                 )

#insert default text in Entry Boxes
player_1_entry_bank.insert(0, '0')
player_1_entry_ground.insert(0, '0')
player_1_entry_re.insert(0, '0')
#Packing them on the screen
player_1_frame.grid(row=0, column=0, columnspan=4, rowspan=4, sticky='news')
player_1_label.grid(row=0, column=0, columnspan=4, )
player_1_money.grid(row=1, column=0, sticky='ew', padx=10)
player_1_ground.grid(row=1, column=1, sticky='ew', padx=10)
player_1_real_estate.grid(row=1, column=2, sticky='ew', padx=10)
player_1_entry_bank.grid(row=2, column=0, padx=10, sticky='ew', )
player_1_entry_ground.grid(row=2, column=1, padx=10, sticky='ew', )
player_1_entry_re.grid(row=2, column=2, padx=10, sticky='ew')
player_1_button.grid(row=3, column=0, columnspan=2, sticky='ew', padx=10)
player_1_button_tax.grid(row=3, column=2, columnspan=2, sticky='ew', padx=10)


#Player 2

def money_calc():
    player_2.money += int(player_2_entry_bank.get())
    player_2_money.configure(text=f"Bank: ${player_2.money}")
    player_2.ground += int(player_2_entry_ground.get())
    player_2_ground.configure(text=f"Ground: ${player_2.ground}")
    player_2.real_estate += int(player_2_entry_re.get())
    player_2_real_estate.configure(text=f"RE: ${player_2.real_estate}")
    
    player_2_entry_bank.delete(0, END)
    player_2_entry_ground.delete(0, END)
    player_2_entry_re.delete(0, END)

    player_2_entry_bank.insert(0, '0')
    player_2_entry_ground.insert(0, '0')
    player_2_entry_re.insert(0, '0')
    
def calculate_tax(): 
    player_2.calc_tax()
    player_2_money.configure(text=f"Bank: ${player_2.money}")
#Making the elements
player_2 = Player()

player_2_frame = customtkinter.CTkFrame(master=root,
                               width=500,
                               height=300,
                               corner_radius=10,
                               bg='white',
                               fg_color='#D61C4E',
                               border_width=2, border_color="white")

player_2_label = customtkinter.CTkEntry(root, width=195,
                               height=40,
                               corner_radius=10,
                               fg_color='#B2A4FF',
                               text_font=('Times New Roman', 26),
                               justify=CENTER,
                               bg_color='#D61C4E',
                               text_color='black',
                               border_width=2, border_color="black"
                               )

player_2_money = customtkinter.CTkLabel(root, text=f"Bank: ${player_2.money}", width=130,
                               height=40,
                               fg_color=("#100F0F", "#B2A4FF"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#D61C4E',
                               text_color='black',
                               )

player_2_ground = customtkinter.CTkLabel(root, text=f"Ground: ${player_2.ground}", width=130,
                               height=40,
                               fg_color=("#100F0F", "#B2A4FF"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#D61C4E',
                               text_color='black',
                               )

player_2_real_estate = customtkinter.CTkLabel(root, text=f"RE: ${player_2.ground}", width=140,
                               height=40,
                               fg_color=("white", "#B2A4FF"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#D61C4E',
                               text_color='black',
                               )

player_2_entry_bank = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#B2A4FF',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#D61C4E',
                               text_color='black',
                               border_width=2, border_color="black"
                            )

player_2_entry_ground = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#B2A4FF',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#D61C4E',
                               text_color='black',
                               border_width=2, border_color="black"
                            )

player_2_entry_re = customtkinter.CTkEntry(root, width=130,
                               height=40,
                               corner_radius=10,
                            fg_color='#B2A4FF',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#D61C4E',
                               text_color='black',
                               border_width=2, border_color="black"
                            )

player_2_button = customtkinter.CTkButton(root, command=money_calc, width=195,
                                 height=40,
                                 corner_radius=8,
                                 text="Add/Subtract Money",
                                 fg_color='#B2A4FF',
                                 text_font=('Times New Roman', 20),
                               bg_color='#D61C4E',
                               hover_color='#FFB4B4',
                               text_color='black',
                               border_width=2, border_color="black"
                                 )

player_2_button_tax = customtkinter.CTkButton(root, command=calculate_tax, width=195,
                                 height=40,
                                 corner_radius=8,
                                 text="Calculate Tax",
                                 fg_color='#B2A4FF',
                                 text_font=('Times New Roman', 20),
                               bg_color='#D61C4E',
                               hover_color='#FFB4B4',
                               text_color='black',
                               border_width=2, border_color="black"
                                 )

#insert default text in Entry Boxes
player_2_entry_bank.insert(0, '0')
player_2_entry_ground.insert(0, '0')
player_2_entry_re.insert(0, '0')
#Packing them on the screen
player_2_frame.grid(row=0, column=4, columnspan=4, rowspan=4, sticky='news')
player_2_label.grid(row=0, column=4, columnspan=4, )
player_2_money.grid(row=1, column=4, sticky='ew', padx=10)
player_2_ground.grid(row=1, column=5, sticky='ew', padx=10)
player_2_real_estate.grid(row=1, column=6, sticky='ew', padx=10)
player_2_entry_bank.grid(row=2, column=4, padx=10, sticky='ew', )
player_2_entry_ground.grid(row=2, column=5, padx=10, sticky='ew', )
player_2_entry_re.grid(row=2, column=6, padx=10, sticky='ew')
player_2_button.grid(row=3, column=4, columnspan=2, sticky='ew', padx=10)
player_2_button_tax.grid(row=3, column=6, columnspan=2, sticky='ew', padx=10)


#Player 3
def money_calc():
    player_3.money += int(player_3_entry_bank.get())
    player_3_money.configure(text=f"Bank: ${player_3.money}")
    player_3.ground += int(player_3_entry_ground.get())
    player_3_ground.configure(text=f"Ground: ${player_3.ground}")
    player_3.real_estate += int(player_3_entry_re.get())
    player_3_real_estate.configure(text=f"RE: ${player_3.real_estate}")
    
    player_3_entry_bank.delete(0, END)
    player_3_entry_ground.delete(0, END)
    player_3_entry_re.delete(0, END)

    player_3_entry_bank.insert(0, '0')
    player_3_entry_ground.insert(0, '0')
    player_3_entry_re.insert(0, '0')
    
def calculate_tax(): 
    player_3.calc_tax()
    player_3_money.configure(text=f"Bank: ${player_3.money}")
#Making the elements
player_3 = Player()

player_3_frame = customtkinter.CTkFrame(master=root,
                               width=500,
                               height=300,
                               corner_radius=10,
                               bg='white',
                               fg_color='#3FA796',
                               border_width=2, border_color="white")

player_3_label = customtkinter.CTkEntry(root, width=195,
                               height=40,
                               corner_radius=10,
                               fg_color='#FEC260',
                               text_font=('Times New Roman', 26),
                               justify=CENTER,
                               bg_color='#3FA796',
                               text_color='#2A0944',
                               border_width=2, border_color="#2A0944"
                               )

player_3_money = customtkinter.CTkLabel(root, text=f"Bank: ${player_3.money}", width=130,
                               height=40,
                               fg_color=("#100F0F", "#FEC260"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#3FA796',
                               text_color='#2A0944',
                               )

player_3_ground = customtkinter.CTkLabel(root, text=f"Ground: ${player_3.ground}", width=130,
                               height=40,
                               fg_color=("#100F0F", "#FEC260"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#3FA796',
                               text_color='#2A0944',
                               )

player_3_real_estate = customtkinter.CTkLabel(root, text=f"RE: ${player_3.ground}", width=140,
                               height=40,
                               fg_color=("white", "#FEC260"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#3FA796',
                               text_color='#2A0944',
                               )

player_3_entry_bank = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#FEC260',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#3FA796',
                               text_color='#2A0944',
                               border_width=2, border_color="#2A0944"
                            )

player_3_entry_ground = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#FEC260',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#3FA796',
                               text_color='#2A0944',
                               border_width=2, border_color="#2A0944"
                            )

player_3_entry_re = customtkinter.CTkEntry(root, width=130,
                               height=40,
                               corner_radius=10,
                            fg_color='#FEC260',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#3FA796',
                               text_color='#2A0944',
                               border_width=2, border_color="#2A0944"
                            )

player_3_button = customtkinter.CTkButton(root, command=money_calc, width=195,
                                 height=40,
                                 corner_radius=8,
                                 text="Add/Subtract Money",
                                 fg_color='#FEC260',
                                 text_font=('Times New Roman', 20),
                               bg_color='#3FA796',
                               hover_color='#A10035',
                               text_color='#2A0944',
                               border_width=2, border_color="#2A0944"
                                 )

player_3_button_tax = customtkinter.CTkButton(root, command=calculate_tax, width=195,
                                 height=40,
                                 corner_radius=8,
                                 text="Calculate Tax",
                                 fg_color='#FEC260',
                                 text_font=('Times New Roman', 20),
                               bg_color='#3FA796',
                               hover_color='#A10035',
                               text_color='#2A0944',
                               border_width=2, border_color="#2A0944"
                                 )

#insert default text in Entry Boxes
player_3_entry_bank.insert(0, '0')
player_3_entry_ground.insert(0, '0')
player_3_entry_re.insert(0, '0')

#Packing them on the screen
player_3_frame.grid(row=4, column=0, columnspan=4, rowspan=4, sticky='news',)
player_3_label.grid(row=4, column=0, columnspan=4, )
player_3_money.grid(row=5, column=0, sticky='ew', padx=10)
player_3_ground.grid(row=5, column=1, sticky='ew', padx=10)
player_3_real_estate.grid(row=5, column=2, sticky='ew', padx=10)
player_3_entry_bank.grid(row=6, column=0, padx=10, sticky='ew', )
player_3_entry_ground.grid(row=6, column=1, padx=10, sticky='ew', )
player_3_entry_re.grid(row=6, column=2, padx=10, sticky='ew')
player_3_button.grid(row=7, column=0, columnspan=2, sticky='ew', padx=10)
player_3_button_tax.grid(row=7, column=2, columnspan=2, sticky='ew', padx=10)


#Player 4


def money_calc():
    player_4.money += int(player_4_entry_bank.get())
    player_4_money.configure(text=f"Bank: ${player_4.money}")
    player_4.ground += int(player_4_entry_ground.get())
    player_4_ground.configure(text=f"Ground: ${player_4.ground}")
    player_4.real_estate += int(player_4_entry_re.get())
    player_4_real_estate.configure(text=f"RE: ${player_4.real_estate}")
    
    player_4_entry_bank.delete(0, END)
    player_4_entry_ground.delete(0, END)
    player_4_entry_re.delete(0, END)

    player_4_entry_bank.insert(0, '0')
    player_4_entry_ground.insert(0, '0')
    player_4_entry_re.insert(0, '0')
    
def calculate_tax(): 
    player_4.calc_tax()
    player_4_money.configure(text=f"Bank: ${player_4.money}")
#Making the elements
player_4 = Player()

player_4_frame = customtkinter.CTkFrame(master=root,
                               width=500,
                               height=300,
                               corner_radius=10,
                               bg='black',
                               fg_color='#31087B',
                               border_width=2, border_color="white")

player_4_label = customtkinter.CTkEntry(root, width=195,
                               height=40,
                               corner_radius=10,
                               fg_color='#FA2FB5',
                               text_font=('Times New Roman', 26),
                               justify=CENTER,
                               bg_color='#31087B',
                               text_color='white',
                               border_width=2, border_color="white"
                               )

player_4_money = customtkinter.CTkLabel(root, text=f"Bank: ${player_4.money}", width=130,
                               height=40,
                               fg_color=("#100720", "#FA2FB5"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#31087B',
                               text_color='white',
                               )

player_4_ground = customtkinter.CTkLabel(root, text=f"Ground: ${player_4.ground}", width=130,
                               height=40,
                               fg_color=("#100720", "#FA2FB5"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#31087B',
                               text_color='white',
                               )

player_4_real_estate = customtkinter.CTkLabel(root, text=f"RE: ${player_4.ground}", width=140,
                               height=40,
                               fg_color=("#100720", "#FA2FB5"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 20),
                               bg_color='#31087B',
                               text_color='white',
                               )

player_4_entry_bank = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#FA2FB5',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#31087B',
                               text_color='white',
                               border_width=2, border_color="white"
                            )

player_4_entry_ground = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                            fg_color='#FA2FB5',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#31087B',
                               text_color='white',
                               border_width=2, border_color="white"
                            )

player_4_entry_re = customtkinter.CTkEntry(root, width=130,
                               height=40,
                               corner_radius=10,
                            fg_color='#FA2FB5',
                            text_font=('Times New Roman', 20),
                            justify=CENTER,
                               bg_color='#31087B',
                               text_color='white',
                               border_width=2, border_color="white"
                            )

player_4_button = customtkinter.CTkButton(root, command=money_calc, width=195,
                                 height=40,
                                 corner_radius=8,
                                 text="Add/Subtract Money",
                                 fg_color='#FA2FB5',
                                 text_font=('Times New Roman', 20),
                               bg_color='#31087B',
                               hover_color='#FFC23C',
                               text_color='white',
                               border_width=2, border_color="white"
                                 )

player_4_button_tax = customtkinter.CTkButton(root, command=calculate_tax, width=195,
                                 height=40,
                                 corner_radius=8,
                                 text="Calculate Tax",
                                 fg_color='#FA2FB5',
                                 text_font=('Times New Roman', 20),
                               bg_color='#31087B',
                               hover_color='#FFC23C',
                               text_color='white',
                               border_width=2, border_color="white"
                                 )

#insert default text in Entry Boxes
player_4_entry_bank.insert(0, '0')
player_4_entry_ground.insert(0, '0')
player_4_entry_re.insert(0, '0')

#Packing them on the screen
player_4_frame.grid(row=4, column=4, columnspan=4, rowspan=4, sticky='news',)
player_4_label.grid(row=4, column=4, columnspan=4, )
player_4_money.grid(row=5, column=4, sticky='ew', padx=10)
player_4_ground.grid(row=5, column=5, sticky='ew', padx=10)
player_4_real_estate.grid(row=5, column=6, sticky='ew', padx=10)
player_4_entry_bank.grid(row=6, column=4, padx=10, sticky='ew', )
player_4_entry_ground.grid(row=6, column=5, padx=10, sticky='ew', )
player_4_entry_re.grid(row=6, column=6, padx=10, sticky='ew')
player_4_button.grid(row=7, column=4, columnspan=2, sticky='ew', padx=10)
player_4_button_tax.grid(row=7, column=6, columnspan=2, sticky='ew', padx=10)


#Trade Box



trade_frame = customtkinter.CTkFrame(master=root,
                               width=300,
                               height=600,
                               corner_radius=10,
                               bg='black',
                               fg_color='#3B44F6',
                               border_width=2, border_color="white")


trade_amount_entry = customtkinter.CTkEntry(root, width=85,
                               height=45,
                               corner_radius=8,
                            fg_color='#F7EC09',
                            text_font=('Times New Roman', 24),
                            justify=CENTER,
                               bg_color='#3B44F6',
                               text_color='black',
                               border_width=2, border_color="black"
                            )


def optionmenu_callback(choice):
    combobox.configure(values=[f"{player_1_label.get()}", f"{player_2_label.get()}", f"{player_3_label.get()}", f"{player_4_label.get()}"])
    trade_amount_entry.delete(0, END)
    trade_amount_entry.insert(0, '0')
    return choice
    
    
def optionmenu_callback2(choice):
    combobox2.configure(values=[f"{player_1_label.get()}", f"{player_2_label.get()}", f"{player_3_label.get()}", f"{player_4_label.get()}"])
    trade_amount_entry.delete(0, END)
    trade_amount_entry.insert(0, '0')
    return choice    


def trade():
    from_player_name = combobox.get()
    to_player_name = combobox2.get()
    if from_player_name == player_1_label.get():
        from_player = player_1
    elif from_player_name == player_2_label.get():
        from_player = player_2
    elif from_player_name == player_3_label.get():
        from_player = player_3
    elif from_player_name == player_4_label.get():
        from_player = player_4  
           
    if to_player_name == player_1_label.get():
        to_player = player_1    
    elif to_player_name == player_2_label.get():
        to_player = player_2    
    elif to_player_name == player_3_label.get():
        to_player = player_3    
    elif to_player_name == player_4_label.get():
        to_player = player_4          
    
    trade_amount = int(trade_amount_entry.get())
    
    trade_amount_entry.delete(0, END)
    trade_amount_entry.insert(0, '0')  
    
    from_player.money -= trade_amount
    to_player.money += trade_amount    
    
    player_1_money.configure(text=f"Bank: ${player_1.money}")
    player_2_money.configure(text=f"Bank: ${player_2.money}")
    player_3_money.configure(text=f"Bank: ${player_3.money}")
    player_4_money.configure(text=f"Bank: ${player_4.money}")
        
combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=["player_1", "player_2", "player_3", "player_4"],
                                       command=optionmenu_callback, 
                                       width=80,
                                        height=40,
                                        fg_color=("#570A57", "#F7EC09"),
                                        corner_radius=8, 
                                        text_font=('Times New Roman', 24),
                                        bg_color='#3B44F6',
                                        text_color='#2E0249',
                                        
                                        button_color='#F7EC09',
                                        button_hover_color='#A149FA',
                                        dropdown_text_font=('Times New Roman', 24),
                                                           
                                        )
combobox.grid(row=1, column=8, sticky='ew', padx=20, columnspan=2)
combobox.set("Player")  # set initial value


combobox2 = customtkinter.CTkOptionMenu(master=root,
                                       values=["player_1", "player_2", "player_3", "player_4"],
                                       command=optionmenu_callback2, 
                                       width=80,
                                        height=40,
                                        fg_color=("#570A57", "#F7EC09"),
                                        corner_radius=8, 
                                        text_font=('Times New Roman', 24),
                                        bg_color='#3B44F6',
                                        text_color='#2E0249',
                                        button_color='#F7EC09',
                                        button_hover_color='#A149FA',
                                        dropdown_text_font=('Times New Roman', 24),)
combobox2.grid(row=3, column=8, sticky='ew', padx=20, columnspan=2)
combobox2.set("Player")  # set initial value


from_label = customtkinter.CTkLabel(root, text="From:", width=80,
                               height=40,
                               fg_color=("#570A57", "#3EC70B"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='#3B44F6',
                               text_color='#570A57',
                               )
to_label = customtkinter.CTkLabel(root, text="To:", width=80,
                               height=40,
                               fg_color=("#570A57", "#3EC70B"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='#3B44F6',
                               text_color='#570A57',
                               )

trade_amount_label = customtkinter.CTkLabel(root, text="Amount:", width=80,
                               height=40,
                               fg_color=("#570A57", "#3EC70B"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='#3B44F6',
                               text_color='#570A57',
                               )


trade_button = customtkinter.CTkButton(root, command=trade, width=85,
                                 height=40,
                                 corner_radius=8,
                                 text="Trade",
                                 fg_color='#3EC70B',
                                 text_font=('Times New Roman', 24),
                               bg_color='#3B44F6',
                               hover_color='#A149FA',
                               text_color='black',
                               border_width=2, border_color="black"
                                 )


trade_frame.grid(row=0, column=8, columnspan=2, rowspan=8, sticky='news',)
from_label.grid(row=0, column=8, sticky='ew', padx=20, columnspan=2)
to_label.grid(row=2, column=8, sticky='ew', padx=20, columnspan=2)
trade_amount_label.grid(row=4, column=8, sticky='ew', padx=20, columnspan=2)
trade_amount_entry.grid(row=5, column=8, sticky='ew', padx=20, columnspan=2)
trade_button.grid(row=6, column=8, sticky='ew', padx=20, columnspan=2)

root.mainloop()