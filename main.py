
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import json
import shutil

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
        self.config_file = "config.json"


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
            # 1. Criação da estrutura de pastas
            base_dir = os.path.join(dest_path, "INFOTEC SOFT")
            os.makedirs(base_dir, exist_ok=True)

            sub_dirs = ["INSTALADOR SISTEMA", "ACCESSO REMOTO", "UTILITARIOS"]
            dir_paths = {}
            for sub_dir in sub_dirs:
                path = os.path.join(base_dir, sub_dir)
                os.makedirs(path, exist_ok=True)
                dir_paths[sub_dir] = path
            
            self.status_label.config(text="Pastas criadas. Verificando arquivos...", fg="blue")
            self.root.update_idletasks()

            # 2. Cópia dos arquivos do config.json
            files_copied_status = self.copy_files_from_config(dir_paths)

            # 3. Finalização
            final_message = "Instalação concluída com sucesso!"
            if files_copied_status == "no_config":
                final_message = "Pastas criadas com sucesso!\n\n(Observação: Nenhum arquivo foi copiado pois 'config.json' não foi encontrado. Use o 'file_selector.py' para definir os arquivos.)"
            elif files_copied_status == "empty_config":
                 final_message = "Pastas criadas com sucesso!\n\n(Observação: Nenhum arquivo foi copiado pois a configuração está vazia.)"


            self.status_label.config(text=f"Instalação finalizada em: {base_dir}", fg="green")
            messagebox.showinfo("Sucesso", final_message)
            self.root.after(3000, self.clear_status)

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro durante a instalação: {e}")
            self.status_label.config(text="Ocorreu um erro.", fg="red")

    def copy_files_from_config(self, dir_paths):
        if not os.path.exists(self.config_file):
            messagebox.showinfo("Informação", f"Arquivo de configuração '{self.config_file}' não encontrado.\n\nApenas as pastas serão criadas. Use o 'file_selector.py' para configurar os arquivos a serem instalados.")
            return "no_config"

        with open(self.config_file, "r", encoding="utf-8") as f:
            try:
                config_data = json.load(f)
            except json.JSONDecodeError:
                messagebox.showwarning("Aviso", f"O arquivo '{self.config_file}' está corrompido ou mal formatado.")
                return "error"
        
        if not any(config_data.values()):
            return "empty_config"

        errors = []
        self.status_label.config(text="Copiando arquivos...", fg="blue")
        self.root.update_idletasks()

        for category, files in config_data.items():
            if category not in dir_paths:
                continue
            
            dest_dir = dir_paths[category]
            for src_file in files:
                if not os.path.exists(src_file):
                    errors.append(f"- {os.path.basename(src_file)} (Não encontrado)")
                    continue
                
                try:
                    shutil.copy(src_file, dest_dir)
                except Exception as e:
                    errors.append(f"- {os.path.basename(src_file)} (Erro ao copiar: {e})")
        
        if errors:
            error_message = "Alguns arquivos não puderam ser copiados:\n\n" + "\n".join(errors)
            messagebox.showwarning("Aviso de Cópia", error_message)

        return "copied"

    def clear_status(self):
        self.destination_path.set("")
        self.status_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = InstallerApp(root)
    root.mainloop()
