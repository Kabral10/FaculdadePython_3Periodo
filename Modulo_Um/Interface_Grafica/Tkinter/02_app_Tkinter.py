import tkinter as tk

def submit():
    # Recupera os dados do campo de entrada
    nome = nome_entry.get()
    email = email_entry.get()

    #Imprime os dados no console
    print(f'Nome: {nome}')
    print(f'Email: {email}')

#Cria a janela principal
root = tk.Tk()
root.title('Formulario de inscrição')

#Cria um frame para conter widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

#Campo de entrada para nome
nome_label = tk.Label(frame, text='Nome :')
nome_label.grid(row=0, column=0)

nome_entry = tk.Entry(frame)
nome_entry.grid(row=0, column=1)

#Campo de entrada para email
email_label = tk.Label(frame, text='Email :')
email_label.grid(row=1, column=0)

email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)

#Botão de submit
submit_button = tk.Button(frame, text='Submit', command=submit)
submit_button.grid(row=2, columnspan=2, pady=10)

#Inicializão
root.mainloop()