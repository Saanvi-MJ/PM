from tkinter import *
from PIL import Image, ImageTk
from enum import Enum
import os
import sys

class GUI:

    login_geometry = [500, 300]
    register_geometry = [500, 335]
    form_geometry = [650, 410]
    __images = []

    # * Function to get Images from AppData
    # * No Parameters
    # * Return: Base Path -> String
    @classmethod
    def imagePath(cls) -> str:

        try:
            base_path = os.path.join(sys._MEIPASS, 'images')
        except:
            base_path = r'.\images'

        return base_path

    # * Function to Clear Images
    # * No Parameters
    # * No Return Value

    @classmethod
    def clearImg(cls):
        cls.__images = {}

    # * Function to Fetch Images for Account Form and Account List
    # * No Parameters
    # * No Return Value
    @classmethod
    def frmLstInit(cls):
        import_tick_image = Image.open(GUI.imagePath()+r"\tick_image.png")
        import_cross_image = Image.open(GUI.imagePath()+r"\cross_image.png")
        import_logout_image = Image.open(GUI.imagePath()+r"\logout.png")
        import_eyes_closed_image = Image.open(GUI.imagePath()+r"\eyes-closed.png")
        import_eyes_open_image = Image.open(GUI.imagePath()+r"\eyes-open.png")


        resized_tick_image = import_tick_image.resize(
            (40, 40), Image.LANCZOS)
        resized_cross_image = import_cross_image.resize(
            (25, 25), Image.LANCZOS)
        resized_logout_image = import_logout_image.resize(
            (20, 20), Image.LANCZOS)
        resized_eyes_closed_image = import_eyes_closed_image.resize(
            (15, 15), Image.LANCZOS)
        resized_eyes_open_image = import_eyes_open_image.resize(
            (15, 15), Image.LANCZOS)
        
        cls.__images = {
            "tick": ImageTk.PhotoImage(resized_tick_image),
            "cross": ImageTk.PhotoImage(resized_cross_image),
            "logout": ImageTk.PhotoImage(resized_logout_image),
            "eyes-closed": ImageTk.PhotoImage(resized_eyes_closed_image),
            "eyes-open": ImageTk.PhotoImage(resized_eyes_open_image)
        }    

    # * Function to Fetch Images for Login and Register
    # * No Parameters
    # * No Return Value
    @classmethod
    def lgnRegInit(cls):
        import_tick_image = Image.open(GUI.imagePath()+r"\tick_image.png")
        import_cross_image = Image.open(GUI.imagePath()+r"\cross_image.png")
        import_eyes_closed_image = Image.open(GUI.imagePath()+r"\eyes-closed.png")
        import_eyes_open_image = Image.open(GUI.imagePath()+r"\eyes-open.png")
        
        resized_tick_image = import_tick_image.resize(
            (40, 40), Image.LANCZOS)
        resized_cross_image = import_cross_image.resize(
            (25, 25), Image.LANCZOS)
        resized_eyes_closed_image = import_eyes_closed_image.resize(
            (15, 15), Image.LANCZOS)
        resized_eyes_open_image = import_eyes_open_image.resize(
            (15, 15), Image.LANCZOS)

        cls.__images = {
            "tick": ImageTk.PhotoImage(resized_tick_image),
            "cross": ImageTk.PhotoImage(resized_cross_image),
            "eyes-closed": ImageTk.PhotoImage(resized_eyes_closed_image),
            "eyes-open": ImageTk.PhotoImage(resized_eyes_open_image)
        } 

    # * Login Page Screen
    # * Parameters: root, SignIn Function and Login to Register Function
    # * No Return Value
    @classmethod
    def login(cls, root: Frame, signInFunction, lgnToRegShifter) -> None:

        master_user_name = StringVar()
        master_password = StringVar()
        isPasswordVisibile = False
        f = Frame(root, width=500, height=195, bg='#333333')

        def togglePasswordVisibility():
            nonlocal isPasswordVisibile
            isPasswordVisibile = not isPasswordVisibile
            e_master_password.config(show="" if isPasswordVisibile else "*")
            visibilityToggler.config(image=cls.__images["eyes-open" if isPasswordVisibile else "eyes-closed"])

        Label(
            f,
            text="Sign In",
            font=('Kamerik 105 W00 Bold', 24),
            bg='#333333',
            fg='#75E6DA'
        ).grid(
            row=0,
            column=0,
            columnspan=3,
            pady=(15, 0)
        )
        Label(
            f,
            text="Username: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=1,
            column=0,
            pady=(25, 5),
            sticky=E
        )
        e_master_user_name = Entry(
            f,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
            textvariable=master_user_name
        )
        e_master_user_name.grid(
            row=1,
            column=1,
            pady=(25, 10),
            sticky=W
        )

        ToolTip(e_master_user_name, "Username can contain only Uppercase & Lowercase\nalphabets, Numbers, Period and Underscore", isError=True)

        Label(
            f,
            text="Password: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=2,
            column=0,
            sticky=E
        )
        e_master_password = Entry(
            f,
            textvariable=master_password,
            show="*",
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        )
        e_master_password.grid(
            row=2,
            column=1,
            sticky=W
        )

        ToolTip(e_master_password, "Password length must be between 8 & 35 and\n must contain Uppercase & Lowercase alphabets,\nnumbers and Special Characters", isError=True)

        visibilityToggler = Label(
            f,
            image=cls.__images["eyes-closed"],
            bg='#333333',
        )
        
        visibilityToggler.grid(
            row=2,
            column=2,
            pady=(2, 0),
            padx=(5, 0),
            sticky=W
        )

        visibilityToggler.bind("<Button-1>", lambda _: togglePasswordVisibility())

        Button(
            f,
            width=7,
            height=1,
            relief=SOLID,
            borderwidth=2,
            cursor='hand2',
            command=lambda: [
                signInFunction(master_user_name.get(), master_password.get(
                )), e_master_user_name.delete(0, END), e_master_password.delete(0, END)
            ],
            text="Sign In",
            font=('Kamerik 105 W00 Bold', 10),
            bg='#454545',
            highlightcolor="white",
            highlightbackground="white",
            highlightthickness=4,
            fg='#75E6DA'
        ).grid(
            row=4,
            column=0,
            columnspan=3,
            pady=(20, 0)
        )

        Label(
            f,
            text="Dont Have an Account?",
            font=('JetBrains Mono Medium', 9),
            bg='#333333',
            fg='white'
        ).grid(
            row=5,
            column=0,
            columnspan=3,
            pady=(12, 0)
        )

        l = Label(
            f,
            text="Register",
            font=('Kamerik 105 W00 Bold', 12),
            bg='#333333',
            fg='#75E6DA',
            cursor='hand2'
        )
        l.bind("<Button-1>", lgnToRegShifter)
        l.grid(row=6, column=0, columnspan=3)

        f.pack()

    # * Function to Display Login Successfull
    # * Parameters: root and Action Value -> Enum
    # * No Return Value
    @classmethod
    def successfullMessage(cls, root: Frame, actionValue) -> None:

        f = Frame(root, width=500, height=55, bg='#333333')

        Label(
            f,
            image=cls.__images["tick"],
            bg='#333333'
        ).grid(
            row=0,
            column=0,
            pady=(0, 5)
        )

        Label(
            f,
            text=actionValue['positive'],
            fg="#59d400",
            bg="#333333",
            font=('Kamerik 105 W00 Bold', 12),
        ).grid(
            row=0,
            column=1,
            pady=(0, 5)
        )

        f.pack(side='bottom', anchor='center', fill='both')

    # * Function to Display Login Unsuccessfull
    # * Parameters: root and Action Value -> Enum
    # * No Return Value
    @classmethod
    def unsuccessfullMessage(cls, root: Frame, actionValue) -> None:

        f = Frame(root, width=500, height=55, bg='#333333')

        Label(
            f,
            image=cls.__images["cross"],
            bg='#333333'
        ).grid(
            row=0,
            column=0,
            pady=(5, 0)
        )
        Label(
            f,
            text=actionValue['negative'],
            fg="#de151f",
            bg="#333333",
            font=('Kamerik 105 W00 Bold', 12),
        ).grid(
            row=0,
            column=1,
            pady=(5, 0)
        )

        f.pack(side='bottom', anchor='s', fill='both')

    # * Register Page Screen
    # * Parameters: root, SignUp Function and Register to Login Function
    # * No Return Value
    @classmethod
    def register(cls, root: Frame, signUpFunction, regToLgnShifter) -> None:
        first_name = StringVar()
        master_user_name = StringVar()
        master_password = StringVar()
        isPasswordVisibile = False

        f = Frame(root, width=500, height=305, bg='#333333')

        def togglePasswordVisibility():
            nonlocal isPasswordVisibile
            isPasswordVisibile = not isPasswordVisibile
            e_master_password.config(show="" if isPasswordVisibile else "*")
            visibilityToggler.config(image=cls.__images["eyes-open" if isPasswordVisibile else "eyes-open"])

        Label(
            f,
            text="Sign Up",
            font=('Kamerik 105 W00 Bold', 24),
            bg='#333333',
            fg='#75E6DA'
        ).grid(
            row=0,
            column=0,
            columnspan=3,
            pady=(15, 0)
        )

        Label(
            f,
            text="First Name: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=1,
            column=0,
            pady=(25, 5),
            sticky=E
        )

        e_first_name = Entry(
            f,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
            textvariable=first_name
        )
        e_first_name.grid(
            row=1,
            column=1,
            pady=(25, 10),
            sticky=W
        )

        Label(
            f,
            text="Username: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=2,
            column=0,
            pady=(0, 5),
            sticky=E
        )

        e_master_user_name = Entry(
            f,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
            textvariable=master_user_name
        )
        e_master_user_name.grid(
            row=2,
            column=1,
            pady=(0, 10),
            sticky=W
        )

        ToolTip(e_master_user_name, "Username can contain only Uppercase & Lowercase\nalphabets, Numbers, Period and Underscore", isError=True)

        Label(
            f,
            text="Password: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=3,
            column=0,
            sticky=E
        )

        e_master_password = Entry(
            f,
            textvariable=master_password,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        )
        e_master_password.grid(
            row=3,
            column=1,
            sticky=W
        )

        ToolTip(e_master_password, "Password length must be between 8 & 35 and\n must contain Uppercase & Lowercase alphabets,\nnumbers and Special Characters", isError=True)

        visibilityToggler = Label(
            f,
            image=cls.__images["eyes-closed"],
            bg='#333333',
        )
        
        visibilityToggler.grid(
            row=3,
            column=2,
            pady=(2, 0),
            padx=(5, 0),
            sticky=W
        )

        visibilityToggler.bind("<Button-1>", lambda _: togglePasswordVisibility())

        Button(
            f,
            width=7,
            height=1,
            relief=SOLID,
            borderwidth=2,
            cursor='hand2',
            command=lambda: [
                signUpFunction(first_name.get(),
                               master_user_name.get(), master_password.get()),
                e_first_name.delete(0, END), e_master_user_name.delete(
                    0, END), e_master_password.delete(0, END)
            ],
            text="Sign Up",
            font=('Kamerik 105 W00 Bold', 10),
            bg='#454545',
            highlightcolor="white",
            highlightbackground="white",
            highlightthickness=4,
            fg='#75E6DA'
        ).grid(
            row=4,
            column=0,
            columnspan=3,
            pady=(20, 0)
        )

        Label(
            f,
            text="Already Have an Account?",
            font=('JetBrains Mono Medium', 9),
            bg='#333333',
            fg='white'
        ).grid(
            row=5,
            column=0,
            columnspan=3,
            pady=(12, 0)
        )

        l = Label(
            f,
            text="Login",
            font=('Kamerik 105 W00 Bold', 12),
            bg='#333333',
            fg='#75E6DA',
            cursor='hand2'
        )
        l.bind("<Button-1>", regToLgnShifter)
        l.grid(row=6, column=0, columnspan=3)

        f.pack()

    # * Welcome Message
    # * Parameters: root, First Name -> String
    # * No Return Value
    @classmethod
    def welcomeMsg(cls, root: Frame, firstName: str, getAccountTable, logout) -> None:

        f = Frame(root, width=650, height=55, bg='#333333')

        Label(
            f,
            text="Hello,",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white',
        ).grid(
            row=0,
            column=0,
            pady=(2, 0),
            padx=(2, 0),
            sticky=E
        )

        Label(
            f,
            text=firstName,
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='#75E6DA',
        ).grid(
            row=0,
            column=1,
            pady=(2, 0),
            sticky=W
        )

        l = Label(
            f,
            image=cls.__images["logout"],
            bg='#333333',
            cursor='hand2'
        )
        
        l.grid(
            row=0,
            column=2,
            pady=(2, 0),
            padx=(2, 0),
            sticky=W
        )

        l.bind("<Button-1>", lambda _: logout())
        
        

        l = Label(
            f,
            text='View Account List',
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white',
            cursor='hand2'
        )
        l.grid(row=0, column=2, pady=(2, 0), padx=(325, 0), sticky=E)
        l.bind("<Button-1>", lambda _: GUI.subWindow(f, getAccountTable()))

        f.pack(anchor='w', fill='x')

    # * Account Form Screen
    # * Parameters: root
    # * No Return Value

    @classmethod
    def accountForm(cls, root: Frame, addAccount, getGeneratedPassword):

        platform = StringVar()
        url = StringVar()
        email = StringVar()
        user_name = StringVar()
        password = StringVar()
        password_length = StringVar()
        password_length.set('Password Length')
        isPasswordVisibile = False

        def togglePasswordVisibility():
            nonlocal isPasswordVisibile
            isPasswordVisibile = not isPasswordVisibile
            e_password.config(show="" if isPasswordVisibile else "*")
            visibilityToggler.config(image=cls.__images["eyes-open" if isPasswordVisibile else "eyes-closed"])

        f = Frame(root, width=650, height=305, bg='#333333')

        Label(
            f,
            text='Account Form',
            font=('Kamerik 105 W00 Bold', 24),
            bg='#333333',
            fg='#75E6DA',
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(15, 0)
        )

        Label(
            f,
            text="Platform Name: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=1,
            column=0,
            pady=(25, 5),
            sticky=E
        )

        e_platform = Entry(
            f,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
            textvariable=platform,
        )
        e_platform.grid(row=1, column=1, pady=(25, 10), sticky=W)

        Label(
            f,
            text="Platform URL: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=2,
            column=0,
            pady=(0, 5),
            sticky=E
        )

        e_url = Entry(
            f,
            textvariable=url,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        )
        e_url.grid(row=2, column=1, pady=(0, 10), sticky=W)

        Label(
            f,
            text="Account Email: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=3,
            column=0,
            pady=(0, 5),
            sticky=E
        )

        e_email = Entry(
            f,
            textvariable=email,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        )
        e_email.grid(row=3, column=1, pady=(0, 10), sticky=W)

        Label(
            f,
            text="Account Username: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=4,
            column=0,
            pady=(0, 5),
            sticky=E
        )

        e_user_name = Entry(
            f,
            textvariable=user_name,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            relief=SOLID,
        )
        e_user_name.grid(row=4, column=1, pady=(0, 10), sticky=W)

        Label(
            f,
            text="Account Password: ",
            font=('JetBrains Mono Medium', 12),
            bg='#333333',
            fg='white'
        ).grid(
            row=5,
            column=0,
            sticky=E
        )

        e_password = Entry(
            f,
            textvariable=password,
            font=('JetBrains Mono Medium', 12),
            bg='#595959',
            fg='white',
            show="*",
            relief=SOLID,
        )
        e_password.grid(row=5, column=1, sticky=W)

        visibilityToggler = Label(
            f,
            image=cls.__images["eyes-closed"],
            bg='#333333',
        )
        
        visibilityToggler.grid(
            row=5,
            column=2,
            pady=(2, 0),
            padx=(5, 0),
            sticky=W
        )

        visibilityToggler.bind("<Button-1>", lambda _: togglePasswordVisibility())

        drop_down = OptionMenu(
            f,
            password_length,
            *range(10, 21),

        )

        drop_down.config(
            bg='#333333',
            fg='white',
            relief=FLAT,
            font=('JetBrains Mono Medium', 10),
            direction='below'
        )

        drop_down['menu'].config(
            bg='#333333',
            fg='white',
            relief=FLAT,
            borderwidth=1,
            font=('JetBrains Mono Medium', 10),
        )

        drop_down["highlightthickness"] = 0
        drop_down.grid(
            row=6,
            column=0,
            sticky=E,
            padx=(0, 20)
        )

        l = Label(
            f,
            text=' Click to Generate',
            compound=LEFT,
            font=('JetBrains Mono Medium', 10),
            bg='#333333',
            fg='white',
            cursor='hand2'
        )
        l.bind("<Button-1>",
               lambda _: [
                   e_password.delete(0, END), e_password.insert(
                       0, getGeneratedPassword(
                           int(password_length.get()) if password_length.get() != 'Password Length' else 15))
               ]
               )
        l.grid(row=6, column=1, sticky=W)

        Button(
            f,
            width=12,
            height=1,
            relief=SOLID,
            borderwidth=2,
            cursor='hand2',
            command=lambda: [
                addAccount(platform.get(), url.get(), email.get(),
                           user_name.get(), password.get()),
                e_platform.delete(0, END), e_url.delete(
                    0, END), e_email.delete(0, END),
                e_user_name.delete(0, END), e_password.delete(0, END)
            ],
            text="Add Account",
            font=('Kamerik 105 W00 Bold', 10),
            bg='#454545',
            highlightcolor="white",
            highlightbackground="white",
            highlightthickness=4,
            fg='#75E6DA'
        ).grid(
            row=7,
            column=0,
            columnspan=2,
            pady=(5, 0)
        )

        f.pack()

    # * All Accounts List Sub Screen
    @classmethod
    def subWindow(cls, root: Frame, account_list: list[list[str]]) -> None:

        heading_list = ['Platform', 'URL', 'Email', 'Username', 'Password']

        sub_window = Toplevel(
            root,
            bg='#333333',
            height=400,
            width=1300
        )

        sub_window.resizable(0, 1)
        sub_window.minsize(1300, 200)
        sub_window.maxsize(1300, 793)

        upper_frame = Frame(sub_window, width=1300, bg='#333333')
        middle_frame = Frame(sub_window, width=1300, bg='#333333')

        Label(
            upper_frame,
            text="Saved Accounts",
            font=('Kamerik 105 W00 Bold', 24),
            bg='#333333',
            fg='#75E6DA'
        ).grid(
            row=0,
            column=0,
            pady=(15, 30)
        )

        upper_frame.pack()

        for heading in heading_list:

            Label(
                middle_frame,
                text=heading,
                font=('JetBrains Mono Medium', 12),
                bg='#333333',
                fg='#75E6DA',
                borderwidth=1,
                relief=SOLID,
                width=25
            ).grid(
                row=0,
                column=heading_list.index(heading),
                ipady=7
            )


        for i, record in enumerate(account_list):

            if i == len(account_list)-1:
                padding_bottom = 20
            else:
                padding_bottom = 0

            for j, cell_data in enumerate(record):

                l = Label(
                    middle_frame,
                    text=cell_data,
                    font=('JetBrains Mono Medium', 12),
                    bg='#333333',
                    fg='white',
                    borderwidth=1,
                    relief=SOLID,
                    width=25
                )
                    
                l.grid(
                    row=i+1,
                    column=j,
                    ipady=7,
                    pady=(0, padding_bottom)
                )

                if j in {3, 4}:
                    l.config(cursor='hand2')
                    ToolTip(l, "Click to Copy to Clipboard", x=150, y=25)
                    l.bind("<Button-1>", lambda e: [e.widget.clipboard_clear(), e.widget.clipboard_append(e.widget.cget("text"))])

        middle_frame.pack()


class ToolTip:
    def __init__(self, widget, text, isError = False, x=0, y=0):
        self.widget = widget
        self.text = text
        self.isError = isError
        self.x = x or 10
        self.y = y or 27
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, _):
        if self.tooltip_window is not None:
            return
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + self.x
        y += self.widget.winfo_rooty() + self.y
        self.tooltip_window = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = Label(tw, text=self.text, background="#454545", fg="gold" if self.isError else "#75E6DA", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, _):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None
