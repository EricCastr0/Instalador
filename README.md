# Instalador de pastas personalizadas

Este é um simples instalador de aplicação desenvolvido em Python com a biblioteca Tkinter.

## Funcionalidades

- **Interface Gráfica Simples:** A aplicação possui uma janela simples para facilitar o processo de instalação.
- **Seleção de Destino:** O usuário pode escolher qualquer pasta em seu computador para a instalação dos arquivos.
- **Criação de Estrutura de Pastas:** O instalador cria a seguinte estrutura de pastas no local selecionado:
  ```
  [Pasta Selecionada]/
  └── INFOTEC SOFT/
      ├── INSTALADOR SISTEMA/
      ├── ACCESSO REMOTO/
      └── UTILITARIOS/
  ```
- **Feedback Visual:** A aplicação informa ao usuário quando a instalação é concluída com sucesso ou se ocorre algum erro.

## Como Executar

1.  Certifique-se de que você tem o Python instalado.
2.  Execute o arquivo `main.py`:
    ```bash
    python main.py
    ```
3.  A janela do instalador aparecerá.
4.  Clique em "Procurar..." para selecionar a pasta de destino.
5.  Clique em "Instalar" para criar a estrutura de pastas.

## Ícone

A aplicação utiliza um ícone customizado (`icon.ico`). Se o arquivo não for encontrado, um ícone padrão será utilizado.
