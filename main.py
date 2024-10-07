from tkinter import *

from modules import Database, GUI, Hashing, Cryptography, Regex, actions, UserNotFoundError

userData = []
exit_code = -1

loginGeo = GUI.login_geometry
regGeo = GUI.register_geometry
frmGeo = GUI.form_geometry


def lgnToReg(_) -> None:
    lgnRegWindow.geometry(f'{regGeo[0]}x{regGeo[1]}')
    main_frame.winfo_children()[0].destroy()
    GUI.register(main_frame, signUpFunction, regToLgn)


def regToLgn(_) -> None:
    lgnRegWindow.geometry(f'{loginGeo[0]}x{loginGeo[1]}')
    main_frame.winfo_children()[0].destroy()
    GUI.login(main_frame, signInFunction, lgnToReg)


def signUpFunction(first_name: str, master_user_name: str, master_password: str) -> None:

    if not first_name or not master_user_name or not master_password:
        if len(footer_frame.winfo_children()):
            footer_frame.winfo_children()[0].destroy()
        GUI.unsuccessfullMessage(footer_frame, actions['empty_fields_reg'])
        footer_frame.after(
            2000, lambda: footer_frame.winfo_children()[0].destroy())
        return

    if not Regex.verifyMasterUserName(master_user_name):
        if len(footer_frame.winfo_children()):
            footer_frame.winfo_children()[0].destroy()
        GUI.unsuccessfullMessage(footer_frame, actions['credentials']['username'])
        footer_frame.after(
                2000, lambda: footer_frame.winfo_children()[0].destroy())
        return
        
    if not Regex.verifyPassword(master_password):
        if len(footer_frame.winfo_children()):
            footer_frame.winfo_children()[0].destroy()
        GUI.unsuccessfullMessage(footer_frame, actions['credentials']['password'])
        footer_frame.after(
                2000, lambda: footer_frame.winfo_children()[0].destroy())
        return
        
    hashed_password = Hashing.creatingHash(master_password)
    Cryptography.generateKey()
    unique_key = Cryptography.getKey().decode()
    Cryptography.destroyKey()

    try:
        Database.userInsertion(
            first_name, master_user_name, hashed_password, unique_key)
        if len(footer_frame.winfo_children()):
            footer_frame.winfo_children()[0].destroy()
        GUI.successfullMessage(footer_frame, actions['register'])
        footer_frame.after(
            2000, lambda: footer_frame.winfo_children()[0].destroy())
        footer_frame.after(1000, lambda: regToLgn(None))

    except:
        if len(footer_frame.winfo_children()):
            footer_frame.winfo_children()[0].destroy()
        GUI.unsuccessfullMessage(footer_frame, actions['register'])
        footer_frame.after(
            2000, lambda: footer_frame.winfo_children()[0].destroy())


def signInFunction(master_user_name: str, master_password: str) -> None:

    if not master_user_name or not master_password:
        if len(footer_frame.winfo_children()):
            footer_frame.winfo_children()[0].destroy()
        GUI.unsuccessfullMessage(footer_frame, actions['empty_fields_login'])
        footer_frame.after(
            2000, lambda: footer_frame.winfo_children()[0].destroy())
        return

    try:
        stored_password_hash = Database.getUserHashedPassword(master_user_name)
        if Hashing.verifyingHash(master_password, stored_password_hash):
            if len(footer_frame.winfo_children()):
                footer_frame.winfo_children()[0].destroy()
            first_name = Database.getUserFirstName(master_user_name)
            userData.append(master_user_name)
            userData.append(first_name)
            GUI.successfullMessage(footer_frame, actions['login'])
            footer_frame.after(1000, lambda: GUI.clearImg())
            footer_frame.after(1000, lambda: lgnRegWindow.destroy())
            global exit_code
            exit_code = 1
        else:
            if len(footer_frame.winfo_children()):
                footer_frame.winfo_children()[0].destroy()
            GUI.unsuccessfullMessage(footer_frame, actions['credentials'])
            footer_frame.after(
                2000, lambda: footer_frame.winfo_children()[0].destroy())


    except UserNotFoundError:
        if len(footer_frame.winfo_children()):
            footer_frame.winfo_children()[0].destroy()
        GUI.unsuccessfullMessage(footer_frame, actions['not_found'])
        footer_frame.after(
                2000, lambda: footer_frame.winfo_children()[0].destroy())

    except:
        if len(footer_frame.winfo_children()):
            footer_frame.winfo_children()[0].destroy()
        GUI.unsuccessfullMessage(footer_frame, actions['login'])
        footer_frame.after(
                2000, lambda: footer_frame.winfo_children()[0].destroy())


def loginAndRegister() -> None:

    global lgnRegWindow
    lgnRegWindow = Tk()
    GUI.lgnRegInit()
    lgnRegWindow.resizable(False, False)
    lgnRegWindow.title("Password Manager")
    lgnRegWindow.config(background='#333333')
    lgnRegWindow.geometry(f'{loginGeo[0]}x{loginGeo[1]}')

    global main_frame, footer_frame
    main_frame = Frame(lgnRegWindow, bg='#333333')
    footer_frame = Frame(lgnRegWindow, bg='#333333')

    GUI.login(main_frame, signInFunction, lgnToReg)

    main_frame.pack()
    footer_frame.pack()

    lgnRegWindow.mainloop()

    if exit_code == 1:
        formAndList()


def formAndList() -> None:

    global frmLstWindow
    frmLstWindow = Tk()
    GUI.frmLstInit()
    frmLstWindow.title("Password Manager")
    frmLstWindow.resizable(False, False)
    frmLstWindow.config(background='#333333')
    frmLstWindow.geometry(f'{frmGeo[0]}x{frmGeo[1]}')

    global header_frame
    header_frame = Frame(frmLstWindow, bg='#333333')
    global main_frame
    main_frame = Frame(frmLstWindow, bg='#333333')
    global footer_frame
    footer_frame = Frame(frmLstWindow, bg='#333333')

    GUI.welcomeMsg(header_frame, userData[1], getAccountTable, logout)
    GUI.accountForm(main_frame, addAccount, getGeneratedPassword)

    header_frame.pack()
    main_frame.pack()
    footer_frame.pack()

    frmLstWindow.mainloop()

    if exit_code == -1:
        loginAndRegister()


def addAccount(platform: str, url: str, email: str, user_name: str, password: str):

    if not platform or not password:
        if len(footer_frame.winfo_children()):
            footer_frame.winfo_children()[0].destroy()
        GUI.unsuccessfullMessage(footer_frame, actions['empty_fields_account'])
        footer_frame.after(
            2000, lambda: footer_frame.winfo_children()[0].destroy())
        return

    try:
        unique_key = Database.getUserUniqueKey(userData[0]).encode()
        encrypted_password = Cryptography.encrypt(
            password, unique_key).decode()
        del unique_key
        Database.accountInsertion(
            userData[0], platform, url, email, user_name, encrypted_password)
        if len(footer_frame.winfo_children()):
            footer_frame.winfo_children()[0].destroy()
        GUI.successfullMessage(footer_frame, actions['account'])
        footer_frame.after(
            2000, lambda: footer_frame.winfo_children()[0].destroy())
    except:
        if len(footer_frame.winfo_children()):
            footer_frame.winfo_children()[0].destroy()
        GUI.unsuccessfullMessage(footer_frame, actions['account'])
        footer_frame.after(
            2000, lambda: footer_frame.winfo_children()[0].destroy())


def getGeneratedPassword(n: int = 15) -> str:

    while True:
        p = Hashing.generatePassword(n)
        if Regex.verifyPassword(p):
            return p


def getAccountTable():

    data = Database.getAccountTable(userData[0])

    for record in data:

        encrypted_password = record.pop().encode()
        unique_key = Database.getUserUniqueKey(userData[0]).encode()
        password = Cryptography.decrypt(encrypted_password, unique_key)
        record.insert(len(record), password)

    return data

def logout():
    global exit_code
    global userData
    exit_code = -1
    userData = []
    frmLstWindow.destroy()

loginAndRegister()