#!/usr/bin/env python
# coding: utf-8

# In[43]:


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def calculate_max_stocks(*args):
    try:
        funds = float(funds_var.get())
        price_a = float(price_a_var.get())
        price_b = float(price_b_var.get())
        split_a = float(split_a_var.get())
        split_b = 100 - split_a

        funds_a = funds * (split_a / 100)
        funds_b = funds * (split_b / 100)

        max_shares_a = funds_a // price_a
        max_shares_b = funds_b // price_b

        remaining_funds_a = funds_a - (max_shares_a * price_a)
        remaining_funds_b = funds_b - (max_shares_b * price_b)

        additional_funds_a = price_a - remaining_funds_a if remaining_funds_a < price_a else 0
        additional_funds_b = price_b - remaining_funds_b if remaining_funds_b < price_b else 0

        total_allocated_a = max_shares_a * price_a
        total_allocated_b = max_shares_b * price_b

        total_allocated = total_allocated_a + total_allocated_b
        expected_max_funds = funds * 1.10  # Adding a 10% buffer

        result_a.set(f"Max shares of Stock A: {int(max_shares_a)}")
        result_b.set(f"Max shares of Stock B: {int(max_shares_b)}")
        additional_a.set(f"Additional funds for one more share of Stock A: {additional_funds_a:.2f}€")
        additional_b.set(f"Additional funds for one more share of Stock B: {additional_funds_b:.2f}€")
        total_allocation.set(f"Total Allocated Funds: {total_allocated:.2f}€")
        expected_range.set(f"Expected Funds Range (with 10% buffer): {funds:.2f}€ - {expected_max_funds:.2f}€")
        
        split_a_label.set(f"{split_a:.1f}%")
        split_b_label.set(f"{split_b:.1f}%")
    except ValueError as e:
        result_a.set("Max shares of Stock A: 0")
        result_b.set("Max shares of Stock B: 0")
        additional_a.set("Additional funds for one more share of Stock A: 0.00€")
        additional_b.set("Additional funds for one more share of Stock B: 0.00€")
        total_allocation.set("Total Allocated Funds: 0.00€")
        expected_range.set("Expected Funds Range (with 10% buffer): 0.00€ - 0.00€")

def update_entry_from_slider(value):
    split_a_var.set(f"{float(value):.1f}")
    split_b_var.set(f"{100 - float(value):.1f}")
    calculate_max_stocks()

def update_slider_from_entry_a(*args):
    try:
        value = float(split_a_var.get())
        slider_a.set(value)
        split_b_var.set(f"{100 - value:.1f}")
        calculate_max_stocks()
    except ValueError:
        pass

def update_slider_from_entry_b(*args):
    try:
        value = float(split_b_var.get())
        slider_a.set(100 - value)
        split_a_var.set(f"{100 - value:.1f}")
        calculate_max_stocks()
    except ValueError:
        pass

def toggle_mode():
    if style.theme_use() == 'dark':
        style.theme_use('light')
        root.configure(background='#f0f0f0')
        toggle_button.config(image=light_on_icon, bg='#f0f0f0', activebackground='#f0f0f0')
    else:
        style.theme_use('dark')
        root.configure(background='#333333')
        toggle_button.config(image=light_off_icon, bg='#333333', activebackground='#333333')

# Create the main window
root = tk.Tk()
root.title("Stock Split Calculator")
root.resizable(False, False)  # Disable window resizing

# Set the window icon
root.iconbitmap('bullish.ico')  # Update with the path to your .ico file

# Load the lightbulb icons
light_off_img = Image.open('light-off.png').resize((32, 32), Image.ANTIALIAS)
light_on_img = Image.open('light-on.png').resize((32, 32), Image.ANTIALIAS)

light_off_icon = ImageTk.PhotoImage(light_off_img)
light_on_icon = ImageTk.PhotoImage(light_on_img)

# Create variables for user input
funds_var = tk.StringVar()
price_a_var = tk.StringVar()
price_b_var = tk.StringVar()
split_a_var = tk.StringVar(value="88")
split_b_var = tk.StringVar(value="12")
split_a_label = tk.StringVar()
split_b_label = tk.StringVar()

# Create variables for results
result_a = tk.StringVar(value="Max shares of Stock A: 0")
result_b = tk.StringVar(value="Max shares of Stock B: 0")
additional_a = tk.StringVar(value="Additional funds for one more share of Stock A: 0.00€")
additional_b = tk.StringVar(value="Additional funds for one more share of Stock B: 0.00€")
total_allocation = tk.StringVar(value="Total Allocated Funds: 0.00€")
expected_range = tk.StringVar(value="Expected Funds Range (with 10% buffer): 0.00€ - 0.00€")

# Trace the variables for real-time updates
funds_var.trace_add("write", calculate_max_stocks)
price_a_var.trace_add("write", calculate_max_stocks)
price_b_var.trace_add("write", calculate_max_stocks)
split_a_var.trace_add("write", update_slider_from_entry_a)
split_b_var.trace_add("write", update_slider_from_entry_b)

# Create and configure styles
style = ttk.Style()
style.theme_create('dark', parent='clam', settings={
    '.': {
        'configure': {
            'background': '#333333',
            'foreground': '#ffffff',
            'fieldbackground': '#555555',
            'font': ('Arial', 10),
        }
    },
    'TLabel': {
        'configure': {
            'background': '#333333',
            'foreground': '#ffffff',
        }
    },
    'TEntry': {
        'configure': {
            'background': '#555555',
            'foreground': '#ffffff',
        }
    },
    'TButton': {
        'configure': {
            'background': '#444444',
            'foreground': '#ffffff',
        }
    },
    'Horizontal.TScale': {
        'configure': {
            'background': '#333333',
        }
    },
})

style.theme_create('light', parent='clam', settings={
    '.': {
        'configure': {
            'background': '#f0f0f0',
            'foreground': '#000000',
            'fieldbackground': '#ffffff',
            'font': ('Arial', 10),
        }
    },
    'TLabel': {
        'configure': {
            'background': '#f0f0f0',
            'foreground': '#000000',
        }
    },
    'TEntry': {
        'configure': {
            'background': '#ffffff',
            'foreground': '#000000',
        }
    },
    'TButton': {
        'configure': {
            'background': '#e0e0e0',
            'foreground': '#000000',
        }
    },
    'Horizontal.TScale': {
        'configure': {
            'background': '#f0f0f0',
        }
    },
})

style.theme_use('dark')
root.configure(background='#333333')  # Set initial background color

# Create and arrange widgets in the window!
ttk.Label(root, text="Total Funds:").grid(column=0, row=0, padx=5, pady=5, sticky="W")
ttk.Entry(root, textvariable=funds_var).grid(column=1, row=0, padx=5, pady=5)

ttk.Label(root, text="Price of Stock A:").grid(column=0, row=1, padx=5, pady=5, sticky="W")
ttk.Entry(root, textvariable=price_a_var).grid(column=1, row=1, padx=5, pady=5)

ttk.Label(root, text="Price of Stock B:").grid(column=0, row=2, padx=5, pady=5, sticky="W")
ttk.Entry(root, textvariable=price_b_var).grid(column=1, row=2, padx=5, pady=5)

ttk.Label(root, text="Split: ").grid(column=0, row=3, padx=5, pady=5, sticky="W")
ttk.Entry(root, textvariable=split_a_var, width=5).grid(column=0, row=3, padx=5, pady=5, sticky="E")
slider_a = ttk.Scale(root, from_=0, to_=100, orient="horizontal", command=update_entry_from_slider, length=200)
slider_a.set(88)
slider_a.grid(column=1, row=3, padx=5, pady=5)
ttk.Entry(root, textvariable=split_b_var, width=5).grid(column=2, row=3, padx=5, pady=5, sticky="W")

# Results
ttk.Label(root, textvariable=result_a).grid(column=0, row=4, columnspan=3, padx=5, pady=5)
ttk.Label(root, textvariable=result_b).grid(column=0, row=5, columnspan=3, padx=5, pady=5)
ttk.Label(root, textvariable=additional_a).grid(column=0, row=6, columnspan=3, padx=5, pady=5)
ttk.Label(root, textvariable=additional_b).grid(column=0, row=7, columnspan=3, padx=5, pady=5)
ttk.Label(root, textvariable=total_allocation).grid(column=0, row=8, columnspan=3, padx=5, pady=5)
ttk.Label(root, textvariable=expected_range).grid(column=0, row=9, columnspan=3, padx=5, pady=5)

# Toggle button with lightbulb icon
toggle_button = tk.Button(root, image=light_off_icon, command=toggle_mode, bd=0, bg='#333333', activebackground='#333333')
toggle_button.grid(column=2, row=0, padx=5, pady=5, sticky="E")

# Start the Tkinter event loop
root.mainloop()

