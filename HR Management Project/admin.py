from tkinter import *
from tkinter import ttk
import pymysql
import time


class admin_panel:
    def __init__(self):
        self.master = Tk()
        self.master.title("Admin Panel")
        self.master.geometry("1530x847+0+0")
        self.master.resizable(False, False)
        self.master.config(bg='grey40')

        adminpanel = Label(self.master, relief=GROOVE, text='Admin Panel', font='times 24 bold', fg='brown4', bg='Light cyan3', bd=6)
        adminpanel.place(x=0, y=5, height=40, width=1530)

        # =========================================Variables IN MasterFrame==================================
        self.order_number_var = StringVar()
        self.product_code_var = StringVar()
        self.quantinty_ordered_var = StringVar()
        self.price_each_var = StringVar()
        self.order_line_number_var = StringVar()
        self.order_number01_var = StringVar()
        self.order_date_var = StringVar()
        self.required_date_var = StringVar()
        self.shipping_date_var = StringVar()
        self.status_var = StringVar()
        self.comment_var = StringVar()
        self.customer_number_var = StringVar()
        self.customer_number01_var = StringVar()
        self.cheque_no_var = StringVar()
        self.payment_date_var = StringVar()
        self.amount_var = StringVar()
        self.search_by = StringVar()
        self.search_by01 = StringVar()
        self.search_by02 = StringVar()
        self.search_txt = StringVar()
        self.search_txt01 = StringVar()
        self.search_txt02 = StringVar()

        # Clickable list
        F0 = LabelFrame(self.master, bd=2, bg='white')
        F0.place(x=0, y=50, height=55, width=1530)

        emp_btn = Button(F0, relief=GROOVE, text='Employees', font=("time new roman", 17, "bold"), width=26, command=self.employees, bg='LightYellow3', bd=5).grid(row=0, column=0)
        cust_btn = Button(F0, relief=GROOVE, text='Customers', font=("time new roman", 17, "bold"), width=26, command=self.customers, bg='LightYellow3', bd=5).grid(row=0, column=1)
        prod_btn = Button(F0, relief=GROOVE, text='Products', font=("time new roman", 17, "bold"), width=26, command=self.products, bg='LightYellow3', bd=5).grid(row=0, column=2)
        ofc_btn = Button(F0, relief=GROOVE, text='Offices', font=("time new roman", 17, "bold"), width=26, command=self.offices, bg='LightYellow3', bd=5).grid(row=0, column=3)

        # Order Details Frame
        F1 = LabelFrame(self.master, text="Order Details", bd=2,  bg='cyan3')
        F1.place(x=0, y=110, height=455, width=505)

        order_number_lbl = Label(F1, text="Order Number", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=0, column=0, padx=20, pady=5, sticky='w')
        order_number_txt = Entry(F1, width=15, textvariable=self.order_number_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        product_code_lbl = Label(F1, text="Product Code", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=1, column=0, padx=20, pady=5, sticky='w')
        product_code_txt = Entry(F1, width=15, textvariable=self.product_code_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=1, column=1, pady=5, padx=10)

        qnty_ordered_lbl = Label(F1, text="Quantinty Ordered ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=2, column=0, padx=20, pady=5, sticky='w')
        qnty_ordered_txt = Entry(F1, width=15, textvariable=self.quantinty_ordered_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=2, column=1, pady=5, padx=10)

        price_lbl = Label(F1, text="Price Each ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=3, column=0, padx=20, pady=5, sticky='w')
        price_txt = Entry(F1, width=15, font="arial 15", textvariable=self.price_each_var, bd=4, relief=SUNKEN).grid(row=3, column=1, pady=5, padx=10)

        order_line_num_lbl = Label(F1, text="Order LineNumber ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=4, column=0, padx=20, pady=5, sticky='w')
        order_line_num_txt = Entry(F1, width=15, textvariable=self.order_line_number_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=4, column=1, pady=5, padx=10)

        # Add,Update and delete buttons in Order Deatils
        btn_lbl = LabelFrame(F1, bd=2, bg='lavender').place(x=0, y=325, height=110, width=500)
        add_btn = Button(F1, relief=GROOVE, text='Add', bg='slate grey', command=self.add_order_details, font='times 15 bold', width=20, bd=5).place(x=2, y=333, height=30, width=121)
        update_btn = Button(F1, relief=GROOVE, text='Update', bg='slate grey', command=self.update_data, font='times 15 bold', width=20, bd=5).place(x=126, y=333, height=30, width=121)
        delete_btn = Button(F1, relief=GROOVE, text='Delete', bg='slate grey', command=self.delete_date, font='times 15 bold', width=20, bd=5).place(x=250, y=333, height=30, width=121)
        clear_btn = Button(F1, relief=GROOVE, text='Clear', bg='slate grey', command=self.clear01, font='times 15 bold', width=20, bd=5).place(x=375, y=333, height=30, width=121)
        # btn_lbl01 = LabelFrame(F1, bd=2, bg='grey').place(x=0, y=377, height=55, width=500)
        search_lbl = Label(F1, text="Search by", fg="black", bg='lavender', bd=10, font='times 15 bold', width=20).place(x=2, y=368, height=30, width=121)
        combo_serach = ttk.Combobox(F1, font='times 12 bold', textvariable=self.search_by, state='readonly')
        combo_serach['values'] = (' orderNumber', ' productCode')
        combo_serach.place(x=126, y=368, height=30, width=121)
        search_btn_txt = Entry(F1, width=15, font="arial 12", textvariable=self.search_txt, bd=5, relief=SUNKEN).place(x=250, y=368, height=30, width=121)
        search_btn = Button(F1, relief=GROOVE, text='Search', bg='slate grey', bd=5, font='times 15 bold', command=self.search_data, width=15).place(x=375, y=368, height=30, width=121)
        all_orders_btn = Button(F1, relief=GROOVE, command=self.fetch_data, bd=5, text='Show All', bg='slate grey', font='times 15 bold', width=20).place(x=185, y=401, height=30, width=121)

        # Orders Layouts
        F4 = Frame(self.master, bd=0, bg="powder blue")
        F4.place(x=2, y=568, width=500, height=30)  # x=1070y=180
        orders_show = Label(F4, text="Order Details", font="arial 15 bold", bd=7, relief=GROOVE, bg="gainsboro").pack(fill=X)
        table_frame = Frame(self.master, relief=GROOVE, bd=2, bg="powder blue")
        table_frame.place(x=4, y=600, width=500, height=220)
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.order_table = ttk.Treeview(table_frame, columns=('ordnum', 'prodcode', 'qtyord', 'price', 'ordlinenum'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.order_table.xview)
        scroll_y.config(command=self.order_table.yview)
        self.order_table.heading("ordnum", text="Order Number")
        self.order_table.heading("prodcode", text="Product Code")
        self.order_table.heading("qtyord", text="Quantinty Ordered")
        self.order_table.heading("price", text="Price Each")
        self.order_table.heading("ordlinenum", text="Order LineNumber")
        self.order_table['show'] = 'headings'
        self.order_table.column("ordnum", width=90)
        self.order_table.column("prodcode", width=85)
        self.order_table.column("qtyord", width=110)
        self.order_table.column("price", width=75)
        self.order_table.column("ordlinenum", width=115)
        self.order_table.pack()
        self.order_table.bind("<ButtonRelease-1>", self.get_cursor)

        # Order Frame
        F2 = LabelFrame(self.master, text="Orders", bd=2, bg='cyan3')
        F2.place(x=512, y=110, height=455, width=505)

        order_num01_lbl = Label(F2, text="Order Number ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=0, column=0, padx=20, pady=5, sticky='w')
        order_num01_txt = Entry(F2, width=15, textvariable=self.order_number01_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        order_date_lbl = Label(F2, text="Order Date ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=1, column=0, padx=20, pady=5, sticky='w')
        order_date_txt = Entry(F2, width=15, textvariable=self.order_date_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=1, column=1, pady=5, padx=10)

        required_date_lbl = Label(F2, text="Required Date ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=2, column=0, padx=20, pady=5, sticky='w')
        required_date_txt = Entry(F2, width=15, textvariable=self.required_date_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=2, column=1, pady=5, padx=10)

        shipping_date_lbl = Label(F2, text="Shipping Date ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=3, column=0, padx=20, pady=5, sticky='w')
        shipping_date_txt = Entry(F2, width=15, textvariable=self.shipping_date_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=3, column=1, pady=5, padx=10)

        status_lbl = Label(F2, text="Status ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=4, column=0, padx=20, pady=5, sticky='w')
        status_txt = Entry(F2, width=15, textvariable=self.status_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=4, column=1, pady=5, padx=10)

        comment_lbl = Label(F2, text="Comment ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=5, column=0, padx=20, pady=5, sticky='w')
        comment_txt = Entry(F2, width=15, textvariable=self.comment_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=5, column=1, pady=5, padx=10)

        customer_number_lbl = Label(F2, text="Customer Number ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=6, column=0, padx=20, pady=5, sticky='w')
        customer_number_txt = Entry(F2, width=15, textvariable=self.customer_number_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=6, column=1, pady=5, padx=10)

        # Add, Update, Delete in Orders
        btn_lbl = LabelFrame(F2, bd=2, bg='lavender').place(x=0, y=325, height=110, width=500)
        add_btn = Button(F2, relief=GROOVE, command=self.add_order, text='Add', bg='slate grey', font='times 15 bold', width=20, bd=5).place(x=2, y=333, height=30, width=121)
        update_btn = Button(F2, relief=GROOVE, text='Update', bg='slate grey', command=self.update_data01, font='times 15 bold', width=20, bd=5).place(x=126, y=333, height=30, width=121)
        delete_btn = Button(F2, relief=GROOVE, text='Delete', bg='slate grey', command=self.delete_date01, font='times 15 bold', width=20, bd=5).place(x=250, y=333, height=30, width=121)
        clear_btn = Button(F2, relief=GROOVE, text='Clear', bg='slate grey', command=self.clear02, font='times 15 bold', width=20, bd=5).place(x=375, y=333, height=30, width=121)
        search_lbl = Label(F2, text="Search by", fg="black", bg='lavender', font='times 15 bold', width=20).place(x=2, y=368, height=30, width=121)
        combo_serach01 = ttk.Combobox(F2, font='times 12 bold', textvariable=self.search_by01, state='readonly')
        combo_serach01['values'] = (' orderNumber', ' customerNumber')
        combo_serach01.place(x=126, y=368, height=30, width=121)
        search_btn_txt = Entry(F2, width=15, font="arial 12", textvariable=self.search_txt01, bd=5, relief=SUNKEN).place(x=250, y=367, height=30, width=121)
        search_btn = Button(F2, relief=GROOVE, text='Search', bg='slate grey', font='times 15 bold', command=self.search_data01, width=15).place(x=375, y=368, height=30, width=121)
        all_orders_btn = Button(F2, relief=GROOVE, command=self.fetch_data01, text='Show All', bg='slate grey', font='times 15 bold', width=20, bd=5).place(x=185, y=401, height=30, width=121)

        # Order Show Layouts
        F5 = Frame(self.master, relief=GROOVE, bd=0, bg="powder blue")
        F5.place(x=510, y=570, width=505, height=30)  # x=1070y=180
        orders_details = Label(F5, text="Orders Show", font="arial 15 bold", bd=7, relief=GROOVE, bg="gainsboro").pack(fill=X)
        table01_frame = Frame(self.master, relief=GROOVE, bd=2, bg="powder blue")
        table01_frame.place(x=510, y=600, width=505, height=220)
        scroll_x = Scrollbar(table01_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table01_frame, orient=VERTICAL)
        self.order01_table = ttk.Treeview(table01_frame, columns=('ordnum01', 'orddate', 'reqdate', 'shipdate', 'status', 'comment', 'custnum'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.order01_table.xview)
        scroll_y.config(command=self.order01_table.yview)
        self.order01_table.heading("ordnum01", text="Order No.")
        self.order01_table.heading("orddate", text="Ord Date")
        self.order01_table.heading("reqdate", text="Req Date")
        self.order01_table.heading("shipdate", text="Shipping Date")
        self.order01_table.heading("status", text="Status")
        self.order01_table.heading("comment", text="Comment")
        self.order01_table.heading("custnum", text="Customer No")
        self.order01_table['show'] = 'headings'
        self.order01_table.column("ordnum01", width=75)
        self.order01_table.column("orddate", width=80)
        self.order01_table.column("reqdate", width=80)
        self.order01_table.column("shipdate", width=110)
        self.order01_table.column("status", width=75)
        self.order01_table.column("comment", width=90)
        self.order01_table.column("custnum", width=90)
        self.order01_table.pack()
        self.order01_table.bind("<ButtonRelease-1>", self.get_cursor01)

        # Payments Frame
        F3 = LabelFrame(self.master, text="Payments", bd=2, bg='cyan3')
        F3.place(x=1025, y=110, height=455, width=505)

        customer_number02_lbl = Label(F3, text="Customer Number ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=0, column=0, padx=20, pady=5, sticky='w')
        customer_number02_txt = Entry(F3, width=15, textvariable=self.customer_number01_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        cheque_number_lbl = Label(F3, text="Cheque No. ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=1, column=0, padx=20, pady=5, sticky='w')
        cheque_number_txt = Entry(F3, width=15, textvariable=self.cheque_no_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=1, column=1, pady=5, padx=10)

        payment_date_lbl = Label(F3, text="Payment Date ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=2, column=0, padx=20, pady=5, sticky='w')
        payment_date_txt = Entry(F3, width=15, textvariable=self.payment_date_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=2, column=1, pady=5, padx=10)

        amount_lbl = Label(F3, text="Amount ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=3, column=0, padx=20, pady=5, sticky='w')
        amount_txt = Entry(F3, width=15, textvariable=self.amount_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=3, column=1, pady=5, padx=10)

        # Add, update and delete in payments
        btn_lbl = LabelFrame(F3, bd=2, bg='lavender').place(x=0, y=325, height=110, width=500)
        add_btn = Button(F3, relief=GROOVE, command=self.add_payment, text='Add', bg='slate grey', font='times 15 bold', width=20, bd=5).place(x=2, y=333, height=30, width=121)
        update_btn = Button(F3, relief=GROOVE, text='Update', bg='slate grey', command=self.update_data02, font='times 15 bold', width=20, bd=5).place(x=126, y=333, height=30, width=121)
        delete_btn = Button(F3, relief=GROOVE, text='Delete', bg='slate grey', command=self.delete_date02, font='times 15 bold', width=20, bd=5).place(x=250, y=333, height=30, width=121)
        clear_btn = Button(F3, relief=GROOVE, text='Clear', bg='slate grey', command=self.clear03, font='times 15 bold', width=20, bd=5).place(x=375, y=333, height=30, width=121)
        search_lbl = Label(F3, text="Search by", fg="black", bg='lavender', font='times 15 bold', bd=5).place(x=2, y=368, height=30, width=121)
        combo_serach02 = ttk.Combobox(F3, font='times 12 bold', textvariable=self.search_by02, state='readonly')
        combo_serach02['values'] = (' customerNumber', ' paymentDate')
        combo_serach02.place(x=126, y=368, height=30, width=121)
        search_btn_txt = Entry(F3, width=15, font="arial 12", textvariable=self.search_txt02, bd=5, relief=SUNKEN).place(x=250, y=368, height=30, width=121)
        search_btn = Button(F3, relief=GROOVE, text='Search', bg='slate grey', font='times 15 bold', command=self.search_data02, width=20, bd=5).place(x=375, y=368, height=30, width=121)
        all_orders_btn = Button(F3, relief=GROOVE, command=self.fetch_data02, text='Show All', bg='slate grey', font='times 15 bold', width=20, bd=5).place(x=185, y=401, height=30, width=121)

        # payment layout
        F6 = Frame(self.master, relief=GROOVE, bd=0, bg="powder blue")
        F6.place(x=1020, y=570, width=505, height=30)  # x=1070y=180
        payment_details = Label(F6, text="Payments Details", font="arial 15 bold", bd=7, relief=GROOVE, bg="gainsboro").pack(fill=X)
        table02_frame = Frame(self.master, relief=GROOVE, bd=2, bg="powder blue")
        table02_frame.place(x=1020, y=602, width=505, height=220)
        scroll_x = Scrollbar(table02_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table02_frame, orient=VERTICAL)
        self.payment_table = ttk.Treeview(table02_frame, columns=('ordnum02', 'chequenum', 'paydate', 'amount'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.payment_table.xview)
        scroll_y.config(command=self.payment_table.yview)
        self.payment_table.heading("ordnum02", text="Order No.")
        self.payment_table.heading("chequenum", text="Cheque No")
        self.payment_table.heading("paydate", text="Payment Date")
        self.payment_table.heading("amount", text="Amount")
        self.payment_table['show'] = 'headings'
        self.payment_table.column("ordnum02", width=110)
        self.payment_table.column("chequenum", width=125)
        self.payment_table.column("paydate", width=125)
        self.payment_table.column("amount", width=125)
        self.payment_table.pack()
        self.payment_table.bind("<ButtonRelease-1>", self.get_cursor02)
        self.fetch_data()
        self.fetch_data01()
        self.fetch_data02()

        self.root.mainloop()

    def add_order_details(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("insert into orderdetails values(%s,%s,%s,%s,%s)", (self.order_number_var.get(),
                                                                        self.product_code_var.get(),
                                                                        self.quantinty_ordered_var.get(),
                                                                        self.price_each_var.get(),
                                                                        self.order_line_number_var.get()
                                                                        ))
        con.commit()
        self.fetch_data()
        self.clear01()
        con.close()

    def fetch_data(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from orderdetails")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.order_table.delete(*self.order_table.get_children())
            for row in rows:
                self.order_table.insert('', END, values=row)
                con.commit()
        con.close()

    def clear01(self):
        self.order_number_var.set("")
        self.product_code_var.set("")
        self.quantinty_ordered_var.set("")
        self.price_each_var.set("")
        self.order_line_number_var.set("")

    def get_cursor(self, ev):
        cursor_row = self.order_table.focus()
        contents = self.order_table.item(cursor_row)
        row = contents['values']
        self.order_number_var.set(row[0])
        self.product_code_var.set(row[1])
        self.quantinty_ordered_var.set(row[2])
        self.price_each_var.set(row[3])
        self.order_line_number_var.set(row[4])

    def update_data(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("update orderdetails set productCode=%s,quantityOrdered=%s,priceEach=%s,orderLineNumber=%s where orderNumber=%s", (
            self.product_code_var.get(),
            self.quantinty_ordered_var.get(),
            self.price_each_var.get(),
            self.order_line_number_var.get(),
            self.order_number_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear01()
        con.close()

    def delete_date(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("delete from orderdetails where orderNumber=%s", self.order_number_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear01()

    def search_data(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from orderdetails where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.order_table.delete(*self.order_table.get_children())
            for row in rows:
                self.order_table.insert('', END, values=row)
                con.commit()
        con.close()

    def add_order(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("insert into orders values(%s,%s,%s,%s,%s,%s,%s)", (self.order_number01_var.get(),
                                                                        self.order_date_var.get(),
                                                                        self.required_date_var.get(),
                                                                        self.shipping_date_var.get(),
                                                                        self.status_var.get(),
                                                                        self.comment_var.get(),
                                                                        self.customer_number_var.get()
                                                                        ))
        con.commit()
        self.fetch_data01()
        self.clear02()
        con.close()

    def fetch_data01(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from orders")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.order01_table.delete(*self.order01_table.get_children())
            for row in rows:
                self.order01_table.insert('', END, values=row)
                con.commit()
        con.close()

    def clear02(self):
        self.order_number01_var.set("")
        self.order_date_var.set("")
        self.required_date_var.set("")
        self.shipping_date_var.set("")
        self.status_var.set("")
        self.comment_var.set("")
        self.customer_number_var.set("")

    def get_cursor01(self, ev):
        cursor_row = self.order01_table.focus()
        contents = self.order01_table.item(cursor_row)
        row = contents['values']
        self.order_number01_var.set(row[0])
        self.order_date_var.set(row[1])
        self.required_date_var.set(row[2])
        self.shipping_date_var.set(row[3])
        self.status_var.set(row[4])
        self.comment_var.set(row[5])
        self.customer_number_var.set(row[6])

    def update_data01(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("update orders set orderDate=%s,requiredDate=%s,shippedDate=%s,status=%s,comments=%s,customerNumber=%s where orderNumber=%s", (
            self.order_date_var.get(),
            self.required_date_var.get(),
            self.shipping_date_var.get(),
            self.status_var.get(),
            self.comment_var.get(),
            self.customer_number_var.get(),
            self.order_number01_var.get()
        ))
        con.commit()
        self.fetch_data01()
        self.clear02()
        con.close()

    def delete_date01(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("delete from offices where orderNumber=%s", self.order_number_var.get())
        con.commit()
        con.close()
        self.fetch_data01()
        self.clear02()

    def search_data01(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from orders where"+str(self.search_by01.get()) + " LIKE '%" + str(self.search_txt01.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.order01_table.delete(*self.order01_table.get_children())
            for row in rows:
                self.order01_table.insert('', END, values=row)
                con.commit()
        con.close()

    def add_payment(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("insert into payments values(%s,%s,%s,%s)", (self.customer_number01_var.get(),
                                                                 self.cheque_no_var.get(),
                                                                 self.payment_date_var.get(),
                                                                 self.amount_var.get()
                                                                 ))
        con.commit()
        self.fetch_data02()
        self.clear03()
        con.close()

    def fetch_data02(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from payments")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.payment_table.delete(*self.payment_table.get_children())
            for row in rows:
                self.payment_table.insert('', END, values=row)
                con.commit()
        con.close()

    def clear03(self):
        self.customer_number01_var.set("")
        self.cheque_no_var.set("")
        self.payment_date_var.set("")
        self.amount_var.set("")

    def get_cursor02(self, ev):
        cursor_row = self.payment_table.focus()
        contents = self.payment_table.item(cursor_row)
        row = contents['values']
        self.customer_number01_var.set(row[0])
        self.cheque_no_var.set(row[1])
        self.payment_date_var.set(row[2])
        self.amount_var.set(row[3])

    def update_data02(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("update payments set checkNumber=%s,paymentDate=%s,amount=%s where customerNumber=%s", (
            self.cheque_no_var.get(),
            self.payment_date_var.get(),
            self.amount_var.get(),
            self.customer_number01_var.get()
        ))
        con.commit()
        self.fetch_data02()
        self.clear03()
        con.close()

    def delete_date02(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("delete from payments where customerNumber=%s", self.customer_number01_var.get())
        con.commit()
        con.close()
        self.fetch_data02()
        self.clear03()

    def search_data02(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from payments where"+str(self.search_by02.get())+" LIKE '%"+str(self.search_txt02.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.payment_table.delete(*self.payment_table.get_children())
            for row in rows:
                self.payment_table.insert('', END, values=row)
                con.commit()
        con.close()

    def employees(self):
        self.master.destroy()
        import employee
        employee.employee()

    def customers(self):
        self.master.destroy()
        import customer
        customer.customers()

    def products(self):
        self.master.destroy()
        import product
        product.product()

    def offices(self):
        self.master.destroy()
        import office
        office.office()
