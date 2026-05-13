import tkinter as tk
from tkinter import messagebox
import sqlite3
conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cpf TEXT,
    renda REAL
)
""")
conexao.commit()
def cadastrar():
    nome = entrada_nome.get()
    cpf = entrada_cpf.get()
    renda = entrada_renda.get()
    if nome ==""or cpf ==""or renda =="":
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return
    cursor.execute("INSERT INTO pessoas (nome, cpf, renda) VALUES (?, ?, ?)", (nome, cpf, float(renda)))
    conexao.commit()
    messagebox.showinfo("Sucesso", "Cadastro realizado!")
    entrada_nome.delete(0, tk.END)
    entrada_cpf.delete(0, tk.END)
    entrada_renda.delete(0, tk.END)
def listar():
    lista.delete(0, tk.END)
    cursor.execute("SELECT nome, cpf, renda FROM pessoas")
    dados = cursor.fetchall()
    for pessoa in dados:
        lista.insert(tk.END, f"Nome: {pessoa[0]} | CPF: {pessoa[1]} | renda: R$ {pessoa[2]:.2f}")

janela = tk.Tk()
janela.title("Cadastro de Pessoas")
janela.geometry("500x400")
tk.Label(janela, text="Nome").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()
tk.Label(janela, text="CPF").pack()
entrada_cpf = tk.Entry(janela)
entrada_cpf.pack()
tk.Label(janela, text="Renda").pack()
entrada_renda = tk.Entry(janela)
entrada_renda.pack()
tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=5)
tk.Button(janela, text="Listar", command=listar).pack(pady=5)
lista = tk.Listbox(janela, width=60)
lista.pack(pady=10)
janela.mainloop()
conexao.close()
