
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

class FileSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seletor de Arquivos de Instalação")
        self.root.geometry("600x500")

        self.categories = {
            "INSTALADOR SISTEMA": [],
            "ACESSO REMOTO": [],
            "UTILITARIOS": []
        }

        self.config_file = "config.json"
        self.load_config()
        self.setup_ui()

    def setup_ui(self):
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        for i, (category, files) in enumerate(self.categories.items()):
            frame = tk.LabelFrame(main_frame, text=category, padx=5, pady=5)
            frame.pack(fill=tk.X, pady=5)

            listbox = tk.Listbox(frame, height=4)
            listbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            for f in files:
                listbox.insert(tk.END, os.path.basename(f))

            btn_frame = tk.Frame(frame)
            btn_frame.pack(side=tk.RIGHT, padx=5)

            add_btn = tk.Button(btn_frame, text="Adicionar", command=lambda c=category, l=listbox: self.add_file(c, l))
            add_btn.pack(fill=tk.X, pady=2)

            remove_btn = tk.Button(btn_frame, text="Remover", command=lambda c=category, l=listbox: self.remove_file(c, l))
            remove_btn.pack(fill=tk.X, pady=2)

        save_button = tk.Button(main_frame, text="Salvar Configuração", command=self.save_config)
        save_button.pack(pady=20)

    def add_file(self, category, listbox):
        files_selected = filedialog.askopenfilenames(title=f"Selecione arquivos para {category}")
        if not files_selected:
            return

        for f in files_selected:
            if f not in self.categories[category]:
                self.categories[category].append(f)
                listbox.insert(tk.END, os.path.basename(f))
    
    def remove_file(self, category, listbox):
        selected_indices = listbox.curselection()
        if not selected_indices:
            return

        for index in reversed(selected_indices):
            del self.categories[category][index]
            listbox.delete(index)

    def save_config(self):
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(self.categories, f, indent=4)
            messagebox.showinfo("Sucesso", f"Configuração salva com sucesso em '{self.config_file}'")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar a configuração: {e}")

    def load_config(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    self.categories = json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                messagebox.showwarning("Aviso", f"Não foi possível carregar o arquivo de configuração '{self.config_file}': {e}\nUm novo arquivo será criado ao salvar.")
                self.categories = { "INSTALADOR SISTEMA": [], "ACESSO REMOTO": [], "UTILITARIOS": [] }


if __name__ == "__main__":
    root = tk.Tk()
    app = FileSelectorApp(root)
    root.mainloop()
