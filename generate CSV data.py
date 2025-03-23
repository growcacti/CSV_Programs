import tkinter as tk
from tkinter import filedialog
import csv
import random

class CSVGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random CSV Generator")

        # --- Widgets ---
        tk.Label(root, text="Rows:").grid(row=0, column=0, sticky="e")
        self.rows_entry = tk.Entry(root)
        self.rows_entry.grid(row=0, column=1)

        tk.Label(root, text="Columns:").grid(row=1, column=0, sticky="e")
        self.cols_entry = tk.Entry(root)
        self.cols_entry.grid(row=1, column=1)

        self.number_type = tk.StringVar(value="float")
        tk.Radiobutton(root, text="Float", variable=self.number_type, value="float").grid(row=2, column=0)
        tk.Radiobutton(root, text="Integer", variable=self.number_type, value="int").grid(row=2, column=1)

        self.generate_button = tk.Button(root, text="Generate CSV", command=self.generate_csv)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.save_button = tk.Button(root, text="Save to File", command=self.save_csv)
        self.save_button.grid(row=4, column=0, columnspan=2)

        self.text_widget = tk.Text(root, width=60, height=20)
        self.text_widget.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # --- Data ---
        self.generated_data = []

    def generate_csv(self):
        try:
            rows = int(self.rows_entry.get())
            cols = int(self.cols_entry.get())
            data = []

            for _ in range(rows):
                row = []
                for _ in range(cols):
                    if self.number_type.get() == "float":
                        value = round(random.uniform(0, 100), 2)
                    else:
                        value = random.randint(0, 100)
                    row.append(value)
                data.append(row)

            self.generated_data = data
            self.display_data(data)

        except ValueError:
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, "Please enter valid integers for rows and columns.\n")

    def display_data(self, data):
        self.text_widget.delete("1.0", tk.END)
        for row in data:
            self.text_widget.insert(tk.END, ','.join(map(str, row)) + "\n")

    def save_csv(self):
        if not self.generated_data:
            self.text_widget.insert(tk.END, "\nNo data to save!\n")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(self.generated_data)
            self.text_widget.insert(tk.END, f"\nSaved to: {file_path}\n")

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CSVGeneratorApp(root)
    root.mainloop()
