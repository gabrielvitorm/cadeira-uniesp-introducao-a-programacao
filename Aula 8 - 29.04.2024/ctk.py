import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("400x240")
app.title("Minha Primeira Janela")

mensagem = customtkinter.CTkLabel(app, text="Digite 2 números para somar!")
mensagem.pack(padx=10, pady=10)

val1 = customtkinter.StringVar()
valor1 = customtkinter.CTkEntry(app, placeholder_text="Digite um número", textvariable=val1)
valor1.pack(padx=10, pady=10)

val2 = customtkinter.StringVar()
valor2 = customtkinter.CTkEntry(app, placeholder_text="Digite outro número", textvariable=val2)
valor2.pack(padx=10, pady=10)

resultado_label = customtkinter.CTkLabel(app, text="Resultado =", font=('Arial', 24))
resultado_label.pack(padx=10, pady=10)

def somar():
    resultado = int(val1.get()) + int(val2.get())
    resultado_label.configure(text=f"Resultado: {resultado}")  # Correção aqui

botao = customtkinter.CTkButton(app, text="Calcular", command=somar)
botao.pack(padx=10, pady=10)

app.mainloop()
