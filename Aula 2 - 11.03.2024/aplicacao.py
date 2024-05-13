import customtkinter

# Configurar a aparência do aplicativo
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Configurar a nova janela
app = customtkinter.CTk()
app.geometry("400x240")
app.title("Minha Primeira Janela")

mensagem = customtkinter.CTkLabel(app, text="Seja Bem-vindo!")
mensagem.pack(padx=10, pady=10)

val1 = customtkinter.StringVar()
valor1 = customtkinter.CTkEntry(app, placeholder_text="Digite o seu Nome Completo", textvariable=val1)
valor1.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(app, text="Calcular", command=sum)
botao.pack(padx=10, pady=10)

# Iniciar a Janela
app.mainloop()