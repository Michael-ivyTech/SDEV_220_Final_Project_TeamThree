#developer : guemri ziad 
#last update : 9/25/2025
#task : front end 



import tkinter as tk
from tkinter import ttk, messagebox
import json
import datetime
import random
import threading
import time

class BakeryOrderingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Heyerly's Bakery Ordering System")
        self.root.geometry("800x600")
        self.root.configure(bg='#FFF8F0')
        
        # Load bakery items
        self.items = self.load_items()
        
        # Current order
        self.current_order = {}
        self.order_id = None
        
        # Create the main interface
        self.create_welcome_screen()
        
    def load_items(self):
        """Load bakery items from a JSON file or create default items"""
        try:
            with open('bakery_items.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Default items if file doesn't exist
            return {
                "Breads": [
                    {"name": "Sourdough", "price": 5.99, "description": "Artisan sourdough loaf"},
                    {"name": "Whole Wheat", "price": 4.99, "description": "Healthy whole wheat bread"},
                    {"name": "Baguette", "price": 3.99, "description": "French-style baguette"}
                ],
                "Pastries": [
                    {"name": "Croissant", "price": 2.99, "description": "Buttery flaky croissant"},
                    {"name": "Cinnamon Roll", "price": 3.49, "description": "Sweet cinnamon pastry"},
                    {"name": "Apple Turnover", "price": 3.99, "description": "Flaky pastry with apple filling"}
                ],
                "Cakes": [
                    {"name": "Chocolate Cake", "price": 24.99, "description": "Rich chocolate layer cake"},
                    {"name": "Cheesecake", "price": 29.99, "description": "New York style cheesecake"},
                    {"name": "Red Velvet", "price": 26.99, "description": "Classic red velvet cake"}
                ],
                "Cookies": [
                    {"name": "Chocolate Chip", "price": 1.50, "description": "Classic chocolate chip cookie"},
                    {"name": "Oatmeal Raisin", "price": 1.50, "description": "Hearty oatmeal cookie with raisins"},
                    {"name": "Sugar Cookie", "price": 1.25, "description": "Sweet sugar cookie"}
                ]
            }
    
    def create_welcome_screen(self):
        """Create the welcome screen"""
        self.clear_screen()
        
        # Welcome frame
        welcome_frame = tk.Frame(self.root, bg='#FFF8F0')
        welcome_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            welcome_frame, 
            text="Welcome to Heyerly's Bakery", 
            font=('Arial', 24, 'bold'),
            fg='#8B4513',  # SaddleBrown
            bg='#FFF8F0'
        )
        title_label.pack(pady=20)
        
        # Description
        desc_label = tk.Label(
            welcome_frame,
            text="Freshly baked goods made with love since 1985",
            font=('Arial', 14),
            fg='#8B4513',
            bg='#FFF8F0'
        )
        desc_label.pack(pady=10)
        
        # Start ordering button
        order_btn = tk.Button(
            welcome_frame,
            text="Start Ordering",
            font=('Arial', 16, 'bold'),
            bg='#D2B48C',  # Tan
            fg='white',
            command=self.create_order_screen,
            width=20,
            height=2
        )
        order_btn.pack(pady=30)
        
        # View menu button
        menu_btn = tk.Button(
            welcome_frame,
            text="View Menu",
            font=('Arial', 14),
            bg='#F5DEB3',  # Wheat
            fg='#8B4513',
            command=self.create_menu_screen,
            width=15,
            height=1
        )
        menu_btn.pack(pady=10)
    
    def create_menu_screen(self):
        """Create the menu screen"""
        self.clear_screen()
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#FFF8F0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="Heyerly's Bakery Menu", 
            font=('Arial', 24, 'bold'),
            fg='#8B4513',
            bg='#FFF8F0'
        )
        title_label.pack(pady=10)
        
        # Create notebook for categories
        notebook = ttk.Notebook(main_frame)
        notebook.pack(expand=True, fill='both', pady=10)
        
        # Style the notebook
        style = ttk.Style()
        style.configure('TNotebook', background='#FFF8F0')
        style.configure('TNotebook.Tab', font=('Arial', 12, 'bold'))
        
        # Create a tab for each category
        for category, items in self.items.items():
            category_frame = tk.Frame(notebook, bg='#FFF8F0')
            notebook.add(category_frame, text=category)
            
            # Create a scrollable frame for items
            canvas = tk.Canvas(category_frame, bg='#FFF8F0')
            scrollbar = ttk.Scrollbar(category_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas, bg='#FFF8F0')
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            # Add items to the scrollable frame
            for i, item in enumerate(items):
                item_frame = tk.Frame(scrollable_frame, bg='#FFF8F0', relief='ridge', bd=1)
                item_frame.pack(fill='x', padx=10, pady=5)
                
                # Item name and description
                name_label = tk.Label(
                    item_frame, 
                    text=f"{item['name']} - ${item['price']:.2f}",
                    font=('Arial', 14, 'bold'),
                    fg='#8B4513',
                    bg='#FFF8F0',
                    anchor='w'
                )
                name_label.pack(fill='x', padx=10, pady=(5, 0))
                
                desc_label = tk.Label(
                    item_frame,
                    text=item['description'],
                    font=('Arial', 10),
                    fg='#8B4513',
                    bg='#FFF8F0',
                    anchor='w'
                )
                desc_label.pack(fill='x', padx=10, pady=(0, 5))
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
        
        # Back button
        back_btn = tk.Button(
            main_frame,
            text="Back to Welcome",
            font=('Arial', 12),
            bg='#F5DEB3',
            fg='#8B4513',
            command=self.create_welcome_screen
        )
        back_btn.pack(pady=10)
    
    def create_order_screen(self):
        """Create the order screen"""
        self.clear_screen()
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#FFF8F0')
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="Place Your Order", 
            font=('Arial', 24, 'bold'),
            fg='#8B4513',
            bg='#FFF8F0'
        )
        title_label.pack(pady=10)
        
        # Create a frame for the order form
        order_frame = tk.Frame(main_frame, bg='#FFF8F0')
        order_frame.pack(fill='both', expand=True)
        
        # Left side - item selection
        left_frame = tk.Frame(order_frame, bg='#FFF8F0')
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        # Category selection
        category_label = tk.Label(
            left_frame,
            text="Select Category:",
            font=('Arial', 12, 'bold'),
            fg='#8B4513',
            bg='#FFF8F0'
        )
        category_label.pack(anchor='w', pady=(0, 5))
        
        self.category_var = tk.StringVar()
        category_combo = ttk.Combobox(
            left_frame, 
            textvariable=self.category_var,
            values=list(self.items.keys()),
            state='readonly'
        )
        category_combo.pack(fill='x', pady=(0, 10))
        category_combo.bind('<<ComboboxSelected>>', self.update_items_list)
        
        # Items listbox
        items_label = tk.Label(
            left_frame,
            text="Select Item:",
            font=('Arial', 12, 'bold'),
            fg='#8B4513',
            bg='#FFF8F0'
        )
        items_label.pack(anchor='w', pady=(10, 5))
        
        self.items_listbox = tk.Listbox(left_frame, height=10, font=('Arial', 11))
        self.items_listbox.pack(fill='both', expand=True, pady=(0, 10))
        
        # Quantity selection
        quantity_frame = tk.Frame(left_frame, bg='#FFF8F0')
        quantity_frame.pack(fill='x', pady=10)
        
        quantity_label = tk.Label(
            quantity_frame,
            text="Quantity:",
            font=('Arial', 12, 'bold'),
            fg='#8B4513',
            bg='#FFF8F0'
        )
        quantity_label.pack(side='left')
        
        self.quantity_var = tk.StringVar(value="1")
        quantity_spinbox = tk.Spinbox(
            quantity_frame,
            from_=1,
            to=20,
            textvariable=self.quantity_var,
            width=5,
            font=('Arial', 11)
        )
        quantity_spinbox.pack(side='left', padx=10)
        
        # Add to order button
        add_btn = tk.Button(
            left_frame,
            text="Add to Order",
            font=('Arial', 12, 'bold'),
            bg='#D2B48C',
            fg='white',
            command=self.add_to_order
        )
        add_btn.pack(fill='x', pady=10)
        
        # Right side - current order
        right_frame = tk.Frame(order_frame, bg='#FFF8F0')
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        current_order_label = tk.Label(
            right_frame,
            text="Current Order:",
            font=('Arial', 12, 'bold'),
            fg='#8B4513',
            bg='#FFF8F0'
        )
        current_order_label.pack(anchor='w', pady=(0, 5))
        
        # Order items frame with scrollbar
        order_items_frame = tk.Frame(right_frame, bg='#FFF8F0')
        order_items_frame.pack(fill='both', expand=True)
        
        self.order_text = tk.Text(
            order_items_frame,
            height=15,
            width=40,
            font=('Arial', 11),
            state='disabled'
        )
        self.order_text.pack(side='left', fill='both', expand=True)
        
        scrollbar = ttk.Scrollbar(order_items_frame, command=self.order_text.yview)
        scrollbar.pack(side='right', fill='y')
        self.order_text.config(yscrollcommand=scrollbar.set)
        
        # Total price
        self.total_label = tk.Label(
            right_frame,
            text="Total: $0.00",
            font=('Arial', 14, 'bold'),
            fg='#8B4513',
            bg='#FFF8F0'
        )
        self.total_label.pack(anchor='e', pady=10)
        
        # Buttons frame
        buttons_frame = tk.Frame(right_frame, bg='#FFF8F0')
        buttons_frame.pack(fill='x', pady=10)
        
        clear_btn = tk.Button(
            buttons_frame,
            text="Clear Order",
            font=('Arial', 12),
            bg='#F5DEB3',
            fg='#8B4513',
            command=self.clear_order
        )
        clear_btn.pack(side='left', padx=(0, 10))
        
        submit_btn = tk.Button(
            buttons_frame,
            text="Submit Order",
            font=('Arial', 12, 'bold'),
            bg='#8B4513',
            fg='white',
            command=self.submit_order
        )
        submit_btn.pack(side='right')
        
        # Back button
        back_btn = tk.Button(
            main_frame,
            text="Back to Welcome",
            font=('Arial', 12),
            bg='#F5DEB3',
            fg='#8B4513',
            command=self.create_welcome_screen
        )
        back_btn.pack(pady=10)
    
    def update_items_list(self, event=None):
        """Update the items list based on selected category"""
        category = self.category_var.get()
        if category in self.items:
            self.items_listbox.delete(0, tk.END)
            for item in self.items[category]:
                self.items_listbox.insert(tk.END, f"{item['name']} - ${item['price']:.2f}")
    
    def add_to_order(self):
        """Add selected item to the current order"""
        category = self.category_var.get()
        selection = self.items_listbox.curselection()
        
        if not category or not selection:
            messagebox.showwarning("Selection Error", "Please select a category and an item.")
            return
        
        try:
            quantity = int(self.quantity_var.get())
            if quantity <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Quantity Error", "Please enter a valid quantity.")
            return
        
        item_index = selection[0]
        item = self.items[category][item_index]
        item_name = item['name']
        
        # Add to current order
        if item_name in self.current_order:
            self.current_order[item_name]['quantity'] += quantity
        else:
            self.current_order[item_name] = {
                'price': item['price'],
                'quantity': quantity,
                'category': category
            }
        
        # Update order display
        self.update_order_display()
    
    def update_order_display(self):
        """Update the order display with current items and total"""
        self.order_text.config(state='normal')
        self.order_text.delete(1.0, tk.END)
        
        total = 0
        for item_name, details in self.current_order.items():
            item_total = details['price'] * details['quantity']
            total += item_total
            self.order_text.insert(tk.END, f"{item_name} x{details['quantity']} - ${item_total:.2f}\n")
        
        self.order_text.config(state='disabled')
        self.total_label.config(text=f"Total: ${total:.2f}")
    
    def clear_order(self):
        """Clear the current order"""
        self.current_order = {}
        self.update_order_display()
    
    def submit_order(self):
        """Submit the current order"""
        if not self.current_order:
            messagebox.showwarning("Order Error", "Your order is empty. Please add items before submitting.")
            return
        
        # Generate order ID
        self.order_id = f"HB{random.randint(1000, 9999)}"
        
        # Calculate total
        total = sum(details['price'] * details['quantity'] for details in self.current_order.values())
        
        # Show confirmation
        confirmation_msg = f"Order submitted successfully!\n\nOrder ID: {self.order_id}\nTotal: ${total:.2f}\n\nYou will be notified when your order is ready."
        messagebox.showinfo("Order Confirmation", confirmation_msg)
        
        # Simulate order processing (in a real system, this would connect to a backend)
        self.simulate_order_processing()
        
        # Clear order and return to welcome screen
        self.current_order = {}
        self.create_welcome_screen()
    
    def simulate_order_processing(self):
        """Simulate order processing in the background"""
        def process_order():
            # Simulate processing time (5-15 seconds)
            processing_time = random.randint(5, 15)
            time.sleep(processing_time)
            
            # Show notification
            self.root.after(0, self.show_order_ready_notification)
        
        # Start processing in a separate thread
        threading.Thread(target=process_order, daemon=True).start()
    
    def show_order_ready_notification(self):
        """Show notification that order is ready"""
        messagebox.showinfo(
            "Order Ready!", 
            f"Your order {self.order_id} is ready for pickup!\n\nThank you for choosing Heyerly's Bakery!"
        )
    
    def clear_screen(self):
        """Clear all widgets from the root window"""
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = BakeryOrderingSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()