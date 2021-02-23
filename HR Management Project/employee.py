from tkinter import *
from tkinter import ttk
import pymysql
import time


class employee:
    def __init__(self):
        self.master01 = Tk()
        self.master01.focus_force()
        self.master01.grab_set()
        self.master01.title("Employees Details")
        self.master01.geometry("1545x847+0+0")
        self.master01.resizable(False, False)
        self.master01.config(bg='grey40')

        # Employees variables
        self.employee_number_var = StringVar()
        self.last_name_var = StringVar()
        self.first_name_var = StringVar()
        self.extension_var = StringVar()
        self.email_var = StringVar()
        self.office_code_var = StringVar()
        self.report_to_var = StringVar()
        self.job_title_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()


        # Employees Frame
        employees_details_lbl = Label(self.master01, text="Employees Details", font=("time new roman", 18, "bold"), bd=2, bg='Light cyan3')
        employees_details_lbl.place(x=0, y=0, height=70, width=1550)

        F9 = LabelFrame(self.master01, text="Orders", bd=2, bg='cyan3')
        F9.place(x=3, y=73, height=700, width=520)

        employee_num_lbl = Label(F9, text="Employee Number", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=0, column=0, padx=20, pady=5, sticky='w')
        employee_num_txt = Entry(F9, width=15, textvariable=self.employee_number_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        last_name_lbl = Label(F9, text="Last Name", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=1, column=0, padx=20, pady=5, sticky='w')
        last_name_txt = Entry(F9, width=15, textvariable=self.last_name_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=1, column=1, pady=5, padx=10)

        first_name_lbl = Label(F9, text="First Name ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=2, column=0, padx=20, pady=5, sticky='w')
        first_name_txt = Entry(F9, width=15, textvariable=self.first_name_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=2, column=1, pady=5, padx=10)

        extension_lbl = Label(F9, text="Extension ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=3, column=0, padx=20, pady=5, sticky='w')
        extension_txt = Entry(F9, width=15, textvariable=self.extension_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=3, column=1, pady=5, padx=10)

        email_lbl = Label(F9, text="Email ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=4, column=0, padx=20, pady=5, sticky='w')
        email_txt = Entry(F9, width=15, textvariable=self.email_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=4, column=1, pady=5, padx=10)

        office_code_lbl = Label(F9, text="Office Code ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=5, column=0, padx=20, pady=5, sticky='w')
        office_code_txt = Entry(F9, width=15, textvariable=self.office_code_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=5, column=1, pady=5, padx=10)

        reports_to_lbl = Label(F9, text="Reports To ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=6, column=0, padx=20, pady=5, sticky='w')
        reports_to_txt = Entry(F9, width=15, textvariable=self.report_to_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=6, column=1, pady=5, padx=10)

        job_title_lbl = Label(F9, text="Job Title ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=7, column=0, padx=20, pady=5, sticky='w')
        job_title_txt = Entry(F9, width=15, textvariable=self.job_title_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=7, column=1, pady=5, padx=10)

        # Product add,update,insert button
        btn_lbl = LabelFrame(F9, bd=5, bg='lavender').place(x=3, y=400, height=110, width=510)
        add_btn = Button(F9, relief=GROOVE, command=self.add_employee, text='Add', bg='slate grey', font='times 15 bold', width=20, bd=5).place(x=7, y=403, height=30, width=122)
        update_btn = Button(F9, relief=GROOVE, text='Update', bg='slate grey', command=self.update_data, font='times 15 bold', width=20, bd=5).place(x=131, y=403, height=30, width=122)
        delete_btn = Button(F9, relief=GROOVE, text='Delete', bg='slate grey', font='times 15 bold', command=self.delete_data, width=20, bd=5).place(x=257, y=403, height=30, width=122)
        clear_btn = Button(F9, relief=GROOVE, text='Clear', bg='slate grey', font='times 15 bold', command=self.clear, width=20, bd=5).place(x=383, y=403, height=30, width=122)
        search_lbl = Label(F9, text="Search by", fg="black", bg='lavender', font=("time new roman", 15, "bold")).place(x=7, y=435, height=30, width=122)
        combo_serach = ttk.Combobox(F9, font='times 12 bold', textvariable=self.search_by, state='readonly')
        combo_serach['values'] = (' employeeNumber', ' lastName', ' jobTitle')
        combo_serach.place(x=131, y=435, height=30, width=121)
        search_btn_txt = Entry(F9, width=15, font="arial 12", textvariable=self.search_txt, bd=4, relief=SUNKEN).place(x=257, y=435, height=30, width=122)
        search_btn = Button(F9, relief=GROOVE, text='Search', bg='slate grey', font='times 15 bold', command=self.search_data, width=20, bd=5).place(x=383, y=435, height=30, width=122)
        all_orders_btn = Button(F9, relief=GROOVE, command=self.fetch_data03, text='Show All', bg='slate grey', font='times 15 bold', width=20, bd=5).place(x=131, y=468, height=30, width=122)
        back_btn = Button(F9, relief=GROOVE, text='Back', bg='slate grey', command=self.back_btn, font='times 15 bold', width=20, bd=5).place(x=257, y=468, height=30, width=122)

        # Employee layout
        F10 = Frame(self.master01, relief=GROOVE, bd=0, bg="LightCyan2")
        F10.place(x=525, y=73, width=1000, height=30)  # x=1070y=180
        orders_details = Label(F10, text="Employee Details", font="arial 15 bold", bd=7, relief=GROOVE, bg="gainsboro").pack(fill=X)
        self.table03_frame = Frame(self.master01, relief=GROOVE, bd=2, bg="powder blue")
        self.table03_frame.place(x=525, y=105, width=1000, height=670)
        scroll_x = Scrollbar(self.table03_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.table03_frame, orient=VERTICAL)
        self.employee_table = ttk.Treeview(self.table03_frame, columns=('empnum', 'lname', 'fname', 'extension', 'email', 'ofccode', 'repto', 'jobtitle'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        self.employee_table.heading("empnum", text="Employee No.")
        self.employee_table.heading("lname", text="Last Name")
        self.employee_table.heading("fname", text="First Name")
        self.employee_table.heading("extension", text="Extension")
        self.employee_table.heading("email", text="Email")
        self.employee_table.heading("ofccode", text="Office Code")
        self.employee_table.heading("repto", text="Report To")
        self.employee_table.heading("jobtitle", text="Job Title")
        self.employee_table['show'] = 'headings'
        self.employee_table.column("empnum", width=110)
        self.employee_table.column("lname", width=125)
        self.employee_table.column("fname", width=125)
        self.employee_table.column("extension", width=125)
        self.employee_table.column("email", width=125)
        self.employee_table.column("ofccode", width=125)
        self.employee_table.column("repto", width=125)
        self.employee_table.column("jobtitle", width=125)
        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease-1>", self.get_cursor02)
        self.fetch_data03()

    def add_employee(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("insert into employees values(%s,%s,%s,%s,%s,%s,%s,%s)", (self.employee_number_var.get(),
                                                                              self.last_name_var.get(),
                                                                              self.first_name_var.get(),
                                                                              self.extension_var.get(),
                                                                              self.email_var.get(),
                                                                              self.office_code_var.get(),
                                                                              self.report_to_var.get(),
                                                                              self.job_title_var.get()
                                                                              ))
        con.commit()
        self.fetch_data03()
        self.clear()
        con.close()

    def fetch_data03(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from employees")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, values=row)
                con.commit()
        con.close()

    def clear(self):
        self.employee_number_var.set("")
        self.last_name_var.set("")
        self.first_name_var.set("")
        self.extension_var.set("")
        self.email_var.set("")
        self.office_code_var.set("")
        self.report_to_var.set("")
        self.job_title_var.set("")

    def get_cursor02(self, ev):
        cursor_row = self.employee_table.focus()
        contents = self.employee_table.item(cursor_row)
        row = contents['values']
        self.employee_number_var.set(row[0])
        self.last_name_var.set(row[1])
        self.first_name_var.set(row[2])
        self.extension_var.set(row[3])
        self.email_var.set(row[4])
        self.office_code_var.set(row[5])
        self.report_to_var.set(row[6])
        self.job_title_var.set(row[7])

    def update_data(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("update employees set lastName=%s,firstName=%s,extension=%s,email=%s,officeCode=%s,reportsTo=%s,jobTitle=%s where employeeNumber=%s", (
                                                                                                                                     self.last_name_var.get(),
                                                                                                                                     self.first_name_var.get(),
                                                                                                                                     self.extension_var.get(),
                                                                                                                                     self.email_var.get(),
                                                                                                                                     self.office_code_var.get(),
                                                                                                                                     self.report_to_var.get(),
                                                                                                                                     self.job_title_var.get(),
                                                                                                                                     self.employee_number_var.get()
                                                                                                                                     ))
        con.commit()
        self.fetch_data03()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("delete from offices where employeeNumber=%s",self.employee_number_var.get())
        con.commit()
        con.close()
        self.fetch_data03()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from employees where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', END, values=row)
                con.commit()
        con.close()

    def back_btn(self):
        self.master01.destroy()
        import admin
        admin.admin_panel()
