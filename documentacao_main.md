# Documentação Técnica - `main.py`

Este documento fornece uma análise técnica detalhada do código-fonte da aplicação "Instalador INFOTEC SOFT", contido no arquivo `main.py`.

## 1. Visão Geral

O `main.py` é um script Python que cria uma aplicação de desktop com interface gráfica (GUI) para um instalador simples. A função principal da aplicação é criar uma estrutura de diretórios pré-definida em um local escolhido pelo usuário. A interface foi construída utilizando a biblioteca padrão do Python, `Tkinter`.

## 2. Dependências

O script utiliza as seguintes bibliotecas e módulos:

-   `tkinter`: Biblioteca padrão do Python para a criação de interfaces gráficas.
    -   `tkinter.filedialog`: Submódulo para abrir caixas de diálogo de seleção de arquivo/diretório.
    -   `tkinter.messagebox`: Submódulo para exibir caixas de mensagem padrão (informação, erro).
-   `os`: Módulo padrão do Python para interagir com o sistema operacional, utilizado aqui para a criação de diretórios.

## 3. Estrutura do Código

O código é estruturado em uma classe principal, `InstallerApp`, que encapsula toda a lógica e os componentes da interface gráfica.

### 3.1. Classe `InstallerApp`

Esta classe gerencia a janela principal, seus widgets e todas as ações do usuário.

#### `__init__(self, root)`

-   **Descrição:** O construtor da classe. Inicializa a janela principal e as variáveis necessárias.
-   **Parâmetros:**
    -   `root`: A instância principal (raiz) do `tk.Tk()`.
-   **Ações:**
    1.  Define o título da janela como "Instalador INFOTEC SOFT".
    2.  Define as dimensões da janela para 400x250 pixels e a torna não redimensionável.
    3.  Tenta carregar o ícone `icon.ico`. Se o arquivo não for encontrado, uma mensagem de aviso é impressa no console.
    4.  Inicializa `self.destination_path` como uma `tk.StringVar`, que será vinculada ao campo de entrada de texto para armazenar o caminho de destino escolhido.
    5.  Chama o método `self.setup_ui()` para construir a interface.

#### `setup_ui(self)`

-   **Descrição:** Cria e organiza todos os widgets (componentes visuais) na janela principal.
-   **Ações:**
    1.  **Frame Principal:** Cria um `tk.Frame` que serve como contêiner para todos os outros widgets, com um preenchimento (padding) interno.
    2.  **Rótulo e Entrada de Texto:**
        -   Cria um `tk.Label` com o texto "Selecione a pasta de destino:".
        -   Cria um `tk.Entry` (campo de texto) desabilitado para edição (`state="readonly"`) que exibe o caminho selecionado. Ele é vinculado à variável `self.destination_path`.
    3.  **Botão "Procurar...":**
        -   Cria um `tk.Button` que, ao ser clicado, executa o método `self.browse_folder`.
    4.  **Botão "Instalar":**
        -   Cria um `tk.Button` principal que, ao ser clicado, executa o método `self.install`.
    5.  **Rótulo de Status:**
        -   Cria um `tk.Label` (`self.status_label`) para exibir mensagens de sucesso ou status ao usuário.

#### `browse_folder(self)`

-   **Descrição:** Abre uma caixa de diálogo para que o usuário possa selecionar uma pasta.
-   **Ações:**
    1.  Usa `filedialog.askdirectory()` para exibir a janela de seleção de pastas nativa do sistema operacional.
    2.  Se o usuário selecionar uma pasta, o caminho completo da pasta é armazenado na variável `self.destination_path` e o texto do rótulo de status é limpo.

#### `install(self)`

-   **Descrição:** Executa a lógica principal de "instalação" (criação de pastas).
-   **Ações:**
    1.  Verifica se um caminho de destino foi selecionado. Se não, exibe uma mensagem de erro com `messagebox.showerror`.
    2.  Se um caminho foi selecionado, entra em um bloco `try...except` para tratamento de erros.
    3.  Cria o diretório base: `[caminho_de_destino]/INFOTEC SOFT`.
    4.  Dentro do diretório base, cria os subdiretórios: "INSTALADOR SISTEMA", "ACCESSO REMOTO" e "UTILITARIOS".
    5.  Se a operação for bem-sucedida, atualiza o `self.status_label` com uma mensagem de sucesso e exibe uma caixa de diálogo informativa com `messagebox.showinfo`.
    6.  Agenda a execução do método `self.clear_status` para 3 segundos depois, a fim de limpar a interface.
    7.  Se ocorrer qualquer exceção (`Exception`), exibe uma mensagem de erro detalhada.

#### `clear_status(self)`

-   **Descrição:** Limpa o campo de texto do caminho de destino e a mensagem de status.
-   **Ações:**
    1.  Reseta a variável `self.destination_path` para uma string vazia.
    2.  Reseta o texto do `self.status_label` para uma string vazia.

### 3.2. Bloco de Execução Principal

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = InstallerApp(root)
    root.mainloop()
```

-   **Descrição:** Este é o ponto de entrada do script.
-   **Ações:**
    1.  Garante que o código dentro deste bloco só será executado quando o arquivo `main.py` for executado diretamente (e não quando for importado como um módulo).
    2.  Cria a janela raiz da aplicação com `root = tk.Tk()`.
    3.  Cria uma instância da classe `InstallerApp`, passando a janela raiz para ela.
    4.  Chama `root.mainloop()`, que inicia o loop de eventos da interface gráfica, fazendo com que a janela apareça na tela e responda às ações do usuário.
