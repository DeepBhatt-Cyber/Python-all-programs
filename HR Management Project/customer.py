from tkinter import *
from tkinter import ttk
import pymysql
import time


class customers:
    def __init__(self):
        self.master02 = Tk()
        self.master02.focus_force()
        self.master02.grab_set()
        self.master02.title("Customers Details")
        self.master02.geometry("1545x847+0+0")
        self.master02.resizable(False, False)
        self.master02.config(bg='grey40')

        # Customers variables
        self.customer_number02_var = StringVar()
        self.customer_name_var = StringVar()
        self.contact_last_name_var = StringVar()
        self.contact_first_name_var = StringVar()
        self.phone_var = StringVar()
        self.address_line1_var = StringVar()
        self.address_line2_var = StringVar()
        self.city_var = StringVar()
        self.state_var = StringVar()
        self.postal_code_var = StringVar()
        self.country_var = StringVar()
        self.salesRep_EmpNo_var = StringVar()
        self.credit_limit_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # Employees Frame
        customers_details_lbl = Label(self.master02, text="Customers Details", font=("time new roman", 18, "bold"), bd=2, bg='Light cyan3')
        customers_details_lbl.place(x=0, y=0, height=70, width=1550)

        F11 = LabelFrame(self.master02, text="Customer", bd=2, bg='cyan3')
        F11.place(x=3, y=73, height=730, width=520)

        cust_num_lbl = Label(F11, text="Customer Number", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=0, column=0, padx=20, pady=5, sticky='w')
        cust_num_txt = Entry(F11, width=15, textvariable=self.customer_number02_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cust_name_lbl = Label(F11, text="Customer Name", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=1, column=0, padx=20, pady=5, sticky='w')
        cust_name_txt = Entry(F11, width=15, textvariable=self.customer_name_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=1, column=1, pady=5, padx=10)

        cont_last_name_lbl = Label(F11, text="Contact Last Name ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=2, column=0, padx=20, pady=5, sticky='w')
        cont_last_name_txt = Entry(F11, width=15, textvariable=self.contact_last_name_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=2, column=1, pady=5, padx=10)

        cont_first_name_lbl = Label(F11, text="Contact First Name ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=3, column=0, padx=20, pady=5, sticky='w')
        cont_first_name_txt = Entry(F11, width=15, textvariable=self.contact_first_name_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=3, column=1, pady=5, padx=10)

        phone_lbl = Label(F11, text="Phone ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=4, column=0, padx=20, pady=5, sticky='w')
        phone_txt = Entry(F11, width=15, textvariable=self.phone_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=4, column=1, pady=5, padx=10)

        address_line1_lbl = Label(F11, text="Address Line1 ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=5, column=0, padx=20, pady=5, sticky='w')
        address_line1_txt = Entry(F11, width=15, textvariable=self.address_line1_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=5, column=1, pady=5, padx=10)

        address_line2_lbl = Label(F11, text="Address Line2 ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=6, column=0, padx=20, pady=5, sticky='w')
        address_line2_txt = Entry(F11, width=15, textvariable=self.address_line2_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=6, column=1, pady=5, padx=10)

        city_lbl = Label(F11, text="City ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=7, column=0, padx=20, pady=5, sticky='w')
        city_txt = Entry(F11, width=15, textvariable=self.city_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=7, column=1, pady=5, padx=10)

        state_lbl = Label(F11, text="State ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=8, column=0, padx=20, pady=5, sticky='w')
        state_txt = Entry(F11, width=15, textvariable=self.state_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=8, column=1, pady=5, padx=10)

        postal_code_lbl = Label(F11, text="Postal Code ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=9, column=0, padx=20, pady=5, sticky='w')
        postal_code_txt = Entry(F11, width=15, textvariable=self.postal_code_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=9, column=1, pady=5, padx=10)

        country_lbl = Label(F11, text="Country ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=10, column=0, padx=20, pady=5, sticky='w')
        country_txt = Entry(F11, width=15, textvariable=self.country_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=10, column=1, pady=5, padx=10)

        salesrep_empno_lbl = Label(F11, text="SalesRep EmpNo. ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=11, column=0, padx=20, pady=5, sticky='w')
        salesrep_empno_txt = Entry(F11, width=15, textvariable=self.salesRep_EmpNo_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=11, column=1, pady=5, padx=10)

        credit_limit_lbl = Label(F11, text="Credit Limit ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=12, column=0, padx=20, pady=5, sticky='w')
        credit_limit_txt = Entry(F11, width=15, textvariable=self.credit_limit_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=12, column=1, pady=5, padx=10)

        # Customer add,update,insert button
        btn_lbl = LabelFrame(F11, bd=5, bg='lavender').place(x=3, y=580, height=110, width=510)
        add_btn = Button(F11, relief=GROOVE, text='Add', bg='slate grey', command=self.add_customer, font='times 15 bold', width=20, bd=5).place(x=8, y=583, height=30, width=123)
        update_btn = Button(F11, relief=GROOVE, text='Update', bg='slate grey', command=self.update_data, font='times 15 bold', width=20, bd=5).place(x=134, y=583, height=30, width=123)
        delete_btn = Button(F11, relief=GROOVE, text='Delete', bg='slate grey', command=self.delete_date, font='times 15 bold', width=20, bd=5).place(x=257, y=583, height=30, width=123)
        clear_btn = Button(F11, relief=GROOVE, text='Clear', bg='slate grey', command=self.clear, font='times 15 bold', width=20, bd=5).place(x=381, y=583, height=30, width=123)
        search_lbl = Label(F11, text="Search by", fg="black", bg='lavender', font='times 15 bold', bd=5).place(x=10, y=615, height=30, width=121)
        combo_serach = ttk.Combobox(F11, font='times 12 bold', textvariable=self.search_by, state='readonly')
        combo_serach['values'] = (' customerNumber', 'customerName')
        combo_serach.place(x=134, y=615, height=30, width=121)
        search_btn_txt = Entry(F11, width=15, font="arial 15", textvariable=self.search_txt, bd=4, relief=SUNKEN).place(x=257, y=615, height=30, width=121)
        search_btn = Button(F11, relief=GROOVE, text='Search', bg='slate grey', command=self.search_date, font='times 15 bold', width=20, bd=5).place(x=381, y=615, height=30, width=121)
        all_orders_btn = Button(F11, relief=GROOVE, text='Show All', bg='slate grey', command=self.fetch_data04, font='times 15 bold', width=20, bd=5).place(x=134, y=648, height=30, width=121)
        back_btn = Button(F11, relief=GROOVE, text='Back', bg='slate grey', command=self.back_btn, font='times 15 bold', width=20, bd=5).place(x=257, y=648, height=30, width=121)

        F12 = Frame(self.master02, relief=GROOVE, bd=0, bg="LightCyan2")
        F12.place(x=525, y=73, width=1000, height=30)  # x=1070y=180
        custs_detail = Label(F12, text="Customer Details", font="arial 15 bold", bd=7, relief=GROOVE, bg="gainsboro").pack(fill=X)
        self.table04_frame = Frame(self.master02, relief=GROOVE, bd=2, bg="powder blue")
        self.table04_frame.place(x=525, y=105, width=1000, height=700)
        scroll_x = Scrollbar(self.table04_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.table04_frame, orient=VERTICAL)
        self.customer_table = ttk.Treeview(self.table04_frame, columns=('custnum', 'custname', 'contlname', 'contfname', 'phone', 'addline1', 'addline2', 'city', 'state', 'postcode', 'country', 'salesrep', 'creditlimit'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.customer_table.xview)
        scroll_y.config(command=self.customer_table.yview)
        self.customer_table.heading("custnum", text="Customer No.")
        self.customer_table.heading("custname", text="Customer Name")
        self.customer_table.heading("contlname", text="Contact LName")
        self.customer_table.heading("contfname", text="Contact FName")
        self.customer_table.heading("phone", text="Phone")
        self.customer_table.heading("addline1", text="Address Line1")
        self.customer_table.heading("addline2", text="Address Line2")
        self.customer_table.heading("city", text="City")
        self.customer_table.heading("state", text="State")
        self.customer_table.heading("postcode", text="Postal Code")
        self.customer_table.heading("country", text="Country")
        self.customer_table.heading("salesrep", text="SalesRep EmpNo.")
        self.customer_table.heading("creditlimit", text="Credit Limit")
        self.customer_table['show'] = 'headings'
        self.customer_table.column("custnum", width=110)
        self.customer_table.column("custname", width=125)
        self.customer_table.column("contlname", width=125)
        self.customer_table.column("contfname", width=125)
        self.customer_table.column("phone", width=125)
        self.customer_table.column("addline1", width=125)
        self.customer_table.column("addline2", width=125)
        self.customer_table.column("city", width=125)
        self.customer_table.column("state", width=125)
        self.customer_table.column("postcode", width=125)
        self.customer_table.column("country", width=125)
        self.customer_table.column("salesrep", width=125)
        self.customer_table.column("creditlimit", width=125)
        self.customer_table.pack(fill=BOTH, expand=1)
        self.customer_table.bind("<ButtonRelease-1>", self.get_cursor02)
        self.fetch_data04()

    def add_customer(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.customer_number02_var.get(),
                                                                                             self.customer_name_var.get(),
                                                                                             self.contact_last_name_var.get(),
                                                                                             self.contact_first_name_var.get(),
                                                                                             self.phone_var.get(),
                                                                                             self.address_line1_var.get(),
                                                                                             self.address_line2_var.get(),
                                                                                             self.city_var.get(),
                                                                                             self.state_var.get(),
                                                                                             self.postal_code_var.get(),
                                                                                             self.country_var.get(),
                                                                                             self.salesRep_EmpNo_var.get(),
                                                                                             self.credit_limit_var.get()
                                                                                             ))
        con.commit()
        self.fetch_data04()
        self.clear()
        con.close()

    def fetch_data04(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from customers")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.customer_table.delete(*self.customer_table.get_children())
            for row in rows:
                self.customer_table.insert('', END, values=row)
                con.commit()
        con.close()

    def clear(self):
        self.customer_number02_var.set("")
        self.customer_name_var.set("")
        self.contact_last_name_var.set("")
        self.contact_first_name_var.set("")
        self.phone_var.set("")
        self.address_line1_var.set("")
        self.address_line2_var.set("")
        self.city_var.set("")
        self.state_var.set("")
        self.postal_code_var.set("")
        self.country_var.set("")
        self.salesRep_EmpNo_var.set("")
        self.credit_limit_var.set("")

    def get_cursor02(self, ev):
        cursor_row = self.customer_table.focus()
        contents = self.customer_table.item(cursor_row)
        row = contents['values']
        self.customer_number02_var.set(row[0])
        self.customer_name_var.set(row[1])
        self.contact_last_name_var.set(row[2])
        self.contact_first_name_var.set(row[3])
        self.phone_var.set(row[4])
        self.address_line1_var.set(row[5])
        self.address_line2_var.set(row[6])
        self.city_var.set(row[7])
        self.state_var.set(row[8])
        self.postal_code_var.set(row[9])
        self.country_var.set(row[10])
        self.salesRep_EmpNo_var.set(row[11])
        self.credit_limit_var.set(row[12])

    def update_data(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("update customers set customerName =%s ,contactLastName=%s,contactFirstName=%s,phone=%s,addressLine1=%s,addressLine2=%s,city=%s,state=%s,postalCode=%s,country=%s,salesRepEmployeeNumber=%s,creditLimit=%s where customerNumber=%s", (
                                                                                                                                                                                                       self.customer_name_var.get(),
                                                                                                                                                                                                       self.contact_last_name_var.get(),
                                                                                                                                                                                                       self.contact_first_name_var.get(),
                                                                                                                                                                                                       self.phone_var.get(),
                                                                                                                                                                                                       self.address_line1_var.get(),
                                                                                                                                                                                                       self.address_line2_var.get(),
                                                                                                                                                                                                       self.city_var.get(),
                                                                                                                                                                                                       self.state_var.get(),
                                                                                                                                                                                                       self.postal_code_var.get(),
                                                                                                                                                                                                       self.country_var.get(),
                                                                                                                                                                                                       self.salesRep_EmpNo_var.get(),
                                                                                                                                                                                                       self.credit_limit_var.get(),
                                                                                                                                                                                                       self.customer_number02_var.get()
                                                                                                                                                                                                       ))
        con.commit()
        self.fetch_data04()
        self.clear()
        con.close()

    def delete_date(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("delete from customers where customerNumber=%s",self.customer_number02_var.get())
        con.commit()
        con.close()
        self.fetch_data04()
        self.clear()

    def search_date(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from customers where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.customer_table.delete(*self.customer_table.get_children())
            for row in rows:
                self.customer_table.insert('', END, values=row)
                con.commit()
        con.close()

    def back_btn(self):
        self.master02.destroy()
        import admin
        admin.admin_panel()