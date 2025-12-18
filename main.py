
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class InstallerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Instalador INFOTEC SOFT")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        try:
            self.root.iconbitmap("icon.ico")
        except tk.TclError:
            print("Ícone 'icon.ico' não encontrado. Usando o ícone padrão.")
            print("Para adicionar um ícone, coloque um arquivo 'icon.ico' no mesmo diretório do script.")

        self.destination_path = tk.StringVar()


        self.setup_ui()

    def setup_ui(self):
        # Frame principal
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Rótulo e entrada para o caminho de destino
        dest_label = tk.Label(main_frame, text="Selecione a pasta de destino:")
        dest_label.pack(anchor=tk.W)

        dest_frame = tk.Frame(main_frame)
        dest_frame.pack(fill=tk.X, pady=5)

        dest_entry = tk.Entry(dest_frame, textvariable=self.destination_path, state="readonly")
        dest_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        browse_button = tk.Button(dest_frame, text="Procurar...", command=self.browse_folder)
        browse_button.pack(side=tk.RIGHT, padx=(5, 0))

        # Botão de instalação
        install_button = tk.Button(main_frame, text="Instalar", command=self.install)
        install_button.pack(pady=20)

        # Rótulo de status
        self.status_label = tk.Label(main_frame, text="", fg="green")
        self.status_label.pack(anchor=tk.W)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.destination_path.set(folder_selected)
            self.status_label.config(text="")

    def install(self):
        dest_path = self.destination_path.get()
        if not dest_path:
            messagebox.showerror("Erro", "Por favor, selecione uma pasta de destino.")
            return

        try:
            base_dir = os.path.join(dest_path, "INFOTEC SOFT")
            os.makedirs(base_dir, exist_ok=True)

            sub_dirs = ["INSTALADOR SISTEMA", "ACCESSO REMOTO", "UTILITARIOS"]
            for sub_dir in sub_dirs:
                os.makedirs(os.path.join(base_dir, sub_dir), exist_ok=True)

            self.status_label.config(text=f"Pastas criadas com sucesso em: {base_dir}", fg="green")
            messagebox.showinfo("Sucesso", "Instalação concluída com sucesso!")
            self.root.after(3000, self.clear_status)

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a instalação: {e}")

    def clear_status(self):
        self.destination_path.set("")
        self.status_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = InstallerApp(root)
    root.mainloop()
