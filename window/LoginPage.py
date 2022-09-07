import tkinter as tk
import tkinter.messagebox


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d+%d+%d' % (300, 180, 600, 200))
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.page = tk.Frame(self.root)
        self.page.pack()
        self.create_page()

    def create_page(self):
        tk.Label(self.page).grid(row=0, stick=tk.W)
        tk.Label(self.page, text='账户: ').grid(row=1, stick=tk.W, pady=10)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=tk.E)
        tk.Label(self.page, text='密码: ').grid(row=2, stick=tk.W, pady=10)
        tk.Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=tk.E)
        tk.Button(self.page, text='登陆', command=self.login_check).grid(row=3, stick=tk.W, pady=10)
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=tk.E)

    def login_check(self):
        name = self.username.get()
        pwd = self.password.get()
        if name == 'admin' and pwd == '123456':
            self.page.destroy()
            tkinter.messagebox.showinfo(title='Welcome', message='欢迎登陆')
        else:
            tkinter.messagebox.showerror(message='账号或密码错误')


if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()
