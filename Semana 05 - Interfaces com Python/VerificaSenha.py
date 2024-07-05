import tkinter as tk

usersMap = dict()


# Funcao que carrega os dados dentro do dict
def loadUsers():
    for fileLine in open("users.csv", "r").readlines()[1:]:
        splitLine = fileLine.strip().split(",")
        usersMap.update({splitLine[0]: splitLine[1]})


# Funcao para configurar e definir a janela
def setWindow():
    window = tk.Tk()
    window.geometry("400x200")
    window.config(bg="#A569BD")
    window.title("Password checker")
    window.resizable(width=False, height=False)

    return window


# Funcao que checa se a senha bate com a do usuario digitado
def checkUser():
    username = str(usernameInput.get())
    password = str(passwordInput.get())

    checkResult.config(state="normal")
    if usersMap.get(username) == password:
        checkResult.insert(tk.END, "Password is correct")
        checkResult.config(state="disabled")
    else:
        checkResult.insert(tk.END, "Password is incorrect")
        checkResult.config(state="disabled")


# Cria a janela e carrega os usuarios
window = setWindow()
loadUsers()

# Configura os input e o label dos inputs
titleLabel = tk.Label(
    window,
    text="Check user password",
    font=("Noto Mono", 15),
    fg="white",
    bg="Black",
).pack()

usernameLabel = tk.Label(
    window,
    text="Enter the username: ",
    font=("Noto Mono", 10, "bold"),
    fg="white",
    bg="#A569BD",
).pack()
usernameInput = tk.Entry(window, font=("Noto Mono", 10))
usernameInput.pack()

passwordLabel = tk.Label(
    window,
    text="Enter the password: ",
    font=("Noto Mono", 10, "bold"),
    fg="white",
    bg="#A569BD",
).pack()
passwordInput = tk.Entry(window, font=("Noto Mono", 10))
passwordInput.pack()

submitButton = tk.Button(
    window, text="Check", font=("Noto Mono", 10), command=checkUser
).pack()

checkResult = tk.Text(window, state="disabled", width=25, height=0)
checkResult.pack()

window.mainloop()
