import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Purple & Pink Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Purple and pink color scheme
        self.colors = {
            'bg': '#2D1B69',      # Dark purple background
            'display_bg': '#4A148C',  # Medium purple
            'display_text': '#000000', # Black text for better readability
            'button_bg': '#8E24AA',   # Purple buttons
            'button_hover': '#AB47BC', # Light purple hover
            'operator_bg': '#E91E63',  # Pink operators
            'operator_hover': '#F48FB1', # Light pink hover
            'equals_bg': '#9C27B0',    # Purple equals
            'equals_hover': '#BA68C8', # Light purple equals hover
            'clear_bg': '#AD1457',     # Dark pink clear
            'clear_hover': '#E91E63'   # Pink clear hover
        }
        
        # Configure root window
        self.root.configure(bg=self.colors['bg'])
        
        # Variables
        self.current = "0"
        self.total = 0
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
        
        self.create_display()
        self.create_buttons()
        
    def create_display(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg=self.colors['bg'])
        display_frame.pack(pady=20, padx=20, fill='x')
        
        # Display entry
        self.display = tk.Entry(
            display_frame,
            font=('Arial', 24, 'bold'),
            bg=self.colors['display_bg'],
            fg=self.colors['display_text'],
            bd=10,
            relief='flat',
            justify='right',
            state='readonly'
        )
        self.display.pack(fill='x', ipady=10)
        
        # Update display
        self.update_display()
        
    def create_buttons(self):
        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg=self.colors['bg'])
        buttons_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Button configuration
        button_config = {
            'font': ('Arial', 16, 'bold'),
            'bd': 3,
            'relief': 'raised',
            'width': 5,
            'height': 2
        }
        
        # Button layout
        buttons = [
            ['C', 'CE', '⌫', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                # Determine button color
                if text in ['C', 'CE']:
                    bg_color = self.colors['clear_bg']
                    hover_color = self.colors['clear_hover']
                elif text in ['+', '-', '*', '/']:
                    bg_color = self.colors['operator_bg']
                    hover_color = self.colors['operator_hover']
                elif text == '=':
                    bg_color = self.colors['equals_bg']
                    hover_color = self.colors['equals_hover']
                else:
                    bg_color = self.colors['button_bg']
                    hover_color = self.colors['button_hover']
                
                button = tk.Button(
                    buttons_frame,
                    text=text,
                    bg=bg_color,
                    fg='white',
                    activebackground=hover_color,
                    **button_config,
                    command=lambda t=text: self.button_click(t)
                )
                button.grid(row=i, column=j, padx=5, pady=5, sticky='nsew')
                
                # Configure grid weights
                buttons_frame.grid_rowconfigure(i, weight=1)
                buttons_frame.grid_columnconfigure(j, weight=1)
    
    def update_display(self):
        self.display.config(state='normal')
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current)
        self.display.config(state='readonly')
    
    def button_click(self, text):
        if text == 'C':
            self.current = "0"
            self.total = 0
            self.input_value = True
            self.check_sum = False
            self.op = ""
            self.result = False
        elif text == 'CE':
            self.current = "0"
            self.input_value = True
        elif text == '⌫':
            if len(self.current) > 1:
                self.current = self.current[:-1]
            else:
                self.current = "0"
        elif text == '±':
            if self.current != "0":
                if self.current.startswith('-'):
                    self.current = self.current[1:]
                else:
                    self.current = '-' + self.current
        elif text in ['+', '-', '*', '/']:
            if self.check_sum:
                self.calculate()
            else:
                self.total = float(self.current)
            self.op = text
            self.input_value = True
            self.check_sum = True
        elif text == '=':
            self.calculate()
        elif text == '.':
            if self.input_value:
                self.current = "0."
                self.input_value = False
            elif '.' not in self.current:
                self.current += '.'
        else:  # Numbers
            if self.input_value:
                self.current = text
                self.input_value = False
            else:
                if self.current == "0":
                    self.current = text
                else:
                    self.current += text
        
        self.update_display()
    
    def calculate(self):
        try:
            if self.op == '+':
                self.total += float(self.current)
            elif self.op == '-':
                self.total -= float(self.current)
            elif self.op == '*':
                self.total *= float(self.current)
            elif self.op == '/':
                if float(self.current) == 0:
                    self.current = "Error: Division by zero"
                    self.update_display()
                    return
                self.total /= float(self.current)
            
            # Format result
            if self.total == int(self.total):
                self.current = str(int(self.total))
            else:
                self.current = str(round(self.total, 10))
            
            self.input_value = True
            self.check_sum = False
            self.result = True
            
        except Exception as e:
            self.current = "Error"
            self.input_value = True
            self.check_sum = False
        
        self.update_display()

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
