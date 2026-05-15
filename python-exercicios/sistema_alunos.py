import tkinter as tk
from tkinter import messagebox
import sqlite3
conexao = sqlite3.connect("alunos.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    matricula TEXT,
    av1 REAL,
    av2 REAL,
    media REAL,
    situacao TEXT
)
""")
conexao.commit()
def calcular_media(av1, av2):
    return(av1 + av2) / 2
def verificar_situacao(media):
    return "Aprovado" if media >= 7 else "Reprovado"
def cadastrar():
    nome = entrada_nome.get()
    matricula = entrada_matricula.get()
    try: 
        av1 = float(entrada_av1.get())
        av2 = float(entrada_av2.get())
    except:
        messagebox.showerror("Erro", "Digite notas válidas")
        return
    if nome == ""or matricula =="":
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return
    media = calcular_media(av1, av2)
    situacao = verificar_situacao(media)
    cursor.execute("""
    INSERT INTO alunos (nome, matricula, av1, av2, media, situacao)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, matricula, av1, av2, media, situacao))
    conexao.commit()
    messagebox.showinfo("Sucesso", "Aluno cadastrado!")
    limpar_campos()
def consultar():
    lista.delete(0, tk.END)
    matricula = entrada_busca.get()
    if matricula == "":
        messagebox.showwarning("Atenção", "Digite a matrícula!")
        return
    cursor.execute("""
    SELECT nome, matricula, av1, av2, media, situacao
    FROM alunos
    WHERE matricula = ?
    """, (matricula,))
    resultado = cursor.fetchone()
    if resultado:
        lista.insert(tk.END,
        f"{resultado[0]} | Mat: {resultado[1]} | AV1: {resultado[2]} | AV2: {resultado[3]} | Média: {resultado[4]:.2f} | {resultado[5]}")
    else:
        messagebox.showinfo("Resultado", "Aluno não encontrado!")
def listar_todos():
    lista.delete(0, tk.END)
    cursor.execute("SELECT nome, matricula, av1, av2, media, situacao FROM alunos")
    dados = cursor.fetchall()
    for aluno in dados:
        lista.insert(tk.END,
        f"{aluno[0]} | Mat: {aluno[1]} | Média: {aluno[4]:.2f} | {aluno[5]}")
def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_matricula.delete(0, tk.END)
    entrada_av1.delete(0, tk.END)
    entrada_av2.delete(0, tk.END)
def limpar_lista():
    lista.delete(0, tk.END)

janela = tk.Tk()
janela.title("Sistema de alunos")
janela.geometry("600x520")
tk.Label(janela, text="Nome").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()
tk.Label(janela, text="Matrícula").pack()
entrada_matricula = tk.Entry(janela)
entrada_matricula.pack()
tk.Label(janela, text="AV1").pack()
entrada_av1 = tk.Entry(janela)
entrada_av1.pack()
tk.Label(janela, text="AV2").pack()
entrada_av2 = tk.Entry(janela)
entrada_av2.pack()
tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=5)
tk.Label(janela, text="Buscar por matrícula").pack()
entrada_busca = tk.Entry(janela)
entrada_busca.pack()
tk.Button(janela, text="Consultar", command=consultar).pack(pady=5)
tk.Button(janela, text="Listar Todos", command=listar_todos).pack(pady=5)
tk.Button(janela, text="Limpar Lista", command=limpar_lista).pack(pady=5)
lista = tk.Listbox(janela, width=80)
lista.pack(pady=10)
janela.mainloop()
conexao.close()