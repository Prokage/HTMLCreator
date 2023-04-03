import tkinter as tk
from tkinter import filedialog, colorchooser

class HTMLGeneratorGUI:
    
    def __init__(self, master):
        self.master = master
        self.master.title("HTML Generator")
        
        # Logo selection
        self.logo_path = ""
        self.logo_label = tk.Label(self.master, text="Logo:")
        self.logo_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.logo_button = tk.Button(self.master, text="Choose Logo", command=self.select_logo)
        self.logo_button.grid(row=0, column=1, padx=5, pady=5, sticky="e")
        
        # Header customization
        self.header_label = tk.Label(self.master, text="Header:")
        self.header_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.header_options = ["About Us", "Contact Us", "Services", "Portfolio"]
        self.header_var = tk.StringVar()
        self.header_var.set(self.header_options[0])
        self.header_dropdown = tk.OptionMenu(self.master, self.header_var, *self.header_options)
        self.header_dropdown.grid(row=0, column=3, padx=5, pady=5, sticky="e")
        
        # Section content
        self.section_label = tk.Label(self.master, text="Section Content:")
        self.section_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.section_text = tk.Text(self.master, width=50, height=10)
        self.section_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        
        # Background color
        self.background_label = tk.Label(self.master, text="Background Color:")
        self.background_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.background_var = tk.StringVar()
        self.background_var.set("#ffffff")
        self.background_entry = tk.Entry(self.master, textvariable=self.background_var)
        self.background_entry.grid(row=3, column=1, padx=5, pady=5, sticky="e")
        self.background_button = tk.Button(self.master, text="Select Color", command=self.select_background_color)
        self.background_button.grid(row=3, column=2, padx=5, pady=5, sticky="w")
        
        # Font color
        self.font_label = tk.Label(self.master, text="Font Color:")
        self.font_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.font_var = tk.StringVar()
        self.font_var.set("#000000")
        self.font_entry = tk.Entry(self.master, textvariable=self.font_var)
        self.font_entry.grid(row=4, column=1, padx=5, pady=5, sticky="e")
        self.font_button = tk.Button(self.master, text="Select Color", command=self.select_font_color)
        self.font_button.grid(row=4, column=2, padx=5, pady=5, sticky="w")
        
        # Generate HTML button
        self.generate_button = tk.Button(self.master, text="Generate HTML", command=self.generate_html)
        self.generate_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)
        
    def select_logo(self):
        self.logo_path = filedialog.askopenfilename(filetypes=(("PNG files", ".png"), ("JPEG files", ".jpg;*.jpeg")))
    def select_background_color(self):
        color = colorchooser.askcolor(title="Choose background color")
        self.background_var.set(color[1])
    
    def select_font_color(self):
        color = colorchooser.askcolor(title="Choose font color")
        self.font_var.set(color[1])
        
    def generate_html(self):
        html = "<!DOCTYPE html>\n<html>\n<head>\n"
        html += '<meta charset="UTF-8">\n'
        html += '<title>Generated HTML</title>\n'
        html += '<style>\n'
        html += 'body {background-color: ' + self.background_var.get() + '; color: ' + self.font_var.get() + ';}\n'
        html += 'h1 {text-align: center;}\n'
        html += 'img {display: block; margin: auto; max-width: 100%;}\n'
        html += '</style>\n'
        html += '</head>\n<body>\n'
        if self.logo_path:
            html += '<img src="' + self.logo_path + '">\n'
        html += '<h1>' + self.header_var.get() + '</h1>\n'
        html += '<p>' + self.section_text.get("1.0", "end-1c") + '</p>\n'
        html += '</body>\n</html>'
        
        with open("generated.html", "w") as f:
            f.write(html)
        
        self.master.destroy()

root = tk.Tk()
html_gen_gui = HTMLGeneratorGUI(root)
root.mainloop()



