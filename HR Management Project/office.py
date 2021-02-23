from tkinter import *
from tkinter import ttk
import pymysql
import time


class office:
    def __init__(self):
        self.master04 = Tk()
        self.master04.title("Customers Details")
        self.master04.geometry("1545x730+0+0") #y=847
        self.master04.resizable(False, False)
        self.master04.config(bg='grey40')
        self.master04.focus_force()
        self.master04.grab_set()

        # Offices variables
        self.office_code01_var = StringVar()
        self.city01_var = StringVar()
        self.phone01_var = StringVar()
        self.address_line01_var = StringVar()
        self.address_line02_var = StringVar()
        self.state01_var = StringVar()
        self.country01_var = StringVar()
        self.postal_code01_var = StringVar()
        self.territory01_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # ProductLine variable
        self.productLine_var = StringVar()
        self.text_desc_var = StringVar()
        self.html_desc_var = StringVar()
        self.image_var = StringVar()

        # Office Frame
        office_details_lbl = Label(self.master04, text="Office Details", font=("time new roman", 18, "bold"), bd=2, bg='Light cyan3')
        office_details_lbl.place(x=0, y=0, height=70, width=1550)

        F12 = LabelFrame(self.master04, text="Offices", bd=2, bg='cyan3')
        F12.place(x=3, y=73, height=650, width=520)

        office_code_lbl = Label(F12, text="Office Code", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=0, column=0, padx=20, pady=5, sticky='w')
        office_code_txt = Entry(F12, width=15, textvariable=self.office_code01_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        city01_lbl = Label(F12, text="City", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=1, column=0, padx=20, pady=5, sticky='w')
        city01_txt = Entry(F12, width=15, textvariable=self.city01_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=1, column=1, pady=5, padx=10)

        phone01_lbl = Label(F12, text="Phone ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=2, column=0, padx=20, pady=5, sticky='w')
        phone01_txt = Entry(F12, width=15, textvariable=self.phone01_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=2, column=1, pady=5, padx=10)

        address_line1_lbl = Label(F12, text="Address Line1 ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=3, column=0, padx=20, pady=5, sticky='w')
        address_line1_txt = Entry(F12, width=15, textvariable=self.address_line01_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=3, column=1, pady=5, padx=10)

        address_line2_lbl = Label(F12, text="Address Line2", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=4, column=0, padx=20, pady=5, sticky='w')
        address_line2_txt = Entry(F12, width=15, textvariable=self.address_line02_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=4, column=1, pady=5, padx=10)

        state01_lbl = Label(F12, text="State ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=5, column=0, padx=20, pady=5, sticky='w')
        state01_txt = Entry(F12, width=15, font="arial 15", textvariable=self.state01_var, bd=4, relief=SUNKEN).grid(row=5, column=1, pady=5, padx=10)

        country01_lbl = Label(F12, text="Country ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=6, column=0, padx=20, pady=5, sticky='w')
        country01_txt = Entry(F12, width=15, font="arial 15", textvariable=self.country01_var, bd=4, relief=SUNKEN).grid(row=6, column=1, pady=5, padx=10)

        postal_code_lbl = Label(F12, text="Postal Code ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=7, column=0, padx=20, pady=5, sticky='w')
        postal_code_txt = Entry(F12, width=15, font="arial 15", textvariable=self.postal_code01_var, bd=4, relief=SUNKEN).grid(row=7, column=1, pady=5, padx=10)

        territory_lbl = Label(F12, text="Territory ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=8, column=0, padx=20, pady=5, sticky='w')
        territory_txt = Entry(F12, width=15, font="arial 15", textvariable=self.territory01_var, bd=4, relief=SUNKEN).grid(row=8, column=1, pady=5, padx=10)

        # productline frame
        F14 = LabelFrame(self.master04, text="Productline", bd=2, bg='cyan3')
        F14.place(x=526, y=360, height=365, width=450)
        product_line_lbl = Label(F14, text="ProductLine", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=0, column=0, padx=20, pady=5, sticky='w')
        product_line_txt = Entry(F14, width=15, textvariable=self.productLine_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        text_desc_lbl = Label(F14, text="Text Desc", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=1, column=0, padx=20, pady=5, sticky='w')
        text_desc_txt = Entry(F14, width=15, textvariable=self.text_desc_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=1, column=1, pady=5, padx=10)

        html_desc_lbl = Label(F14, text="HTML Desc ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=2, column=0, padx=20, pady=5, sticky='w')
        html_desc_txt = Entry(F14, width=15, textvariable=self.html_desc_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=2, column=1, pady=5, padx=10)

        image_lbl = Label(F14, text="Image ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=3, column=0, padx=20, pady=5, sticky='w')
        image_txt = Entry(F14, width=15, textvariable=self.image_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=3, column=1, pady=5, padx=10)

        # Product add,update,insert button
        btn_lbl = LabelFrame(F12, bd=5, bg='lavender').place(x=2, y=507, height=110, width=513)
        add_btn = Button(F12, relief=GROOVE, text='Add', bg='slate grey', command=self.add_office, font='times 15 bold', width=20, bd=5).place(x=7, y=513, height=30, width=122)
        update_btn = Button(F12, relief=GROOVE, text='Update', bg='slate grey', command=self.update_data, font='times 15 bold', width=20, bd=5).place(x=133, y=513, height=30, width=122)
        delete_btn = Button(F12, relief=GROOVE, text='Delete', bg='slate grey', command=self.delete_date, font='times 15 bold', width=20, bd=5).place(x=258, y=513, height=30, width=122)
        clear_btn = Button(F12, relief=GROOVE, text='Clear', bg='slate grey',command=self.clear, font='times 15 bold', width=20, bd=5).place(x=383, y=513, height=30, width=122)
        search_lbl = Label(F12, text="Search by", fg="black", bg='lavender', font='times 15 bold').place(x=8, y=546, height=30, width=122)
        combo_search01 = ttk.Combobox(F12, font='times 13 bold', textvariable=self.search_by, state='readonly')
        combo_search01['values'] = (' officeCode', ' country')
        combo_search01.place(x=133, y=546, height=30, width=122)
        search_btn_txt = Entry(F12, textvariable=self.search_txt, bg='white',font="arial 12", bd=4, relief=SUNKEN, width=20).place(x=258, y=546, height=30, width=122)
        search_btn = Button(F12, relief=GROOVE, text='Search', bg='slate grey',command=self.search_date, font='times 15 bold', width=20, bd=5).place(x=383, y=546, height=30, width=122)
        all_orders_btn = Button(F12, relief=GROOVE, command=self.fetch_data06, bg='slate grey',text='Show All', font='times 15 bold', width=20, bd=5).place(x=133, y=579, height=30, width=122)
        back_lbl = Button(F12, relief=GROOVE, text="Back", command=self.back_btn, bg='slate grey',font='times 15 bold', bd=5, width=20).place(x=258, y=579, height=30, width=122)

        # productLine add, update, delete button
        btn_lbl01 = Frame(F14, bd=5, relief=GROOVE, bg='lavender').place(x=2, y=220, height=110, width=442)
        add_btn = Button(F14, relief=GROOVE, text='Add', bg='slate grey',font='times 15 bold', command=self.add_productLine, width=20, bd=5).place(x=8, y=243, height=30, width=142)
        update_btn = Button(F14, relief=GROOVE, text='Update', bg='slate grey', command=self.update_data01, font='times 15 bold', width=20, bd=5).place(x=152, y=243, height=30, width=142)
        delete_btn = Button(F14, relief=GROOVE, text='Delete', bg='slate grey', command=self.delete_date01, font='times 15 bold', width=20, bd=5).place(x=298, y=243, height=30, width=142)
        clear_btn = Button(F14, relief=GROOVE, text='Clear', bg='slate grey', command=self.clear_data, font='times 15 bold', width=20, bd=5).place(x=80, y=276, height=30, width=140)
        all_productline_btn = Button(F14, relief=GROOVE, text='Show All', bg='slate grey', command=self.fetch_data07, font='times 15 bold', width=20, bd=5).place(x=223, y=276, height=30, width=140)

        F13 = Frame(self.master04, relief=GROOVE, bd=0, bg="LightCyan2")
        F13.place(x=525, y=73, width=1000, height=30)  # x=1070y=180
        office_details = Label(F13, text="Office Details", font="arial 15 bold", bd=7, relief=GROOVE, bg="gainsboro").pack(fill=X)
        self.table06_frame = Frame(self.master04, relief=GROOVE, bd=2, bg="cyan")
        self.table06_frame.place(x=525, y=105, width=1000, height=250)
        scroll_x = Scrollbar(self.table06_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.table06_frame, orient=VERTICAL)
        self.offices_table = ttk.Treeview(self.table06_frame, columns=('ofccode', 'city', 'phone', 'addline1', 'addline2', 'state', 'country', 'postcode', 'territory'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.offices_table.xview)
        scroll_y.config(command=self.offices_table.yview)
        self.offices_table.heading("ofccode", text="Office Code")
        self.offices_table.heading("city", text="City")
        self.offices_table.heading("phone", text="Phone")
        self.offices_table.heading("addline1", text="Address Line1")
        self.offices_table.heading("addline2", text="Address Line2")
        self.offices_table.heading("state", text="State")
        self.offices_table.heading("country", text="Country")
        self.offices_table.heading("postcode", text="Postal Code")
        self.offices_table.heading("territory", text="Territory")
        self.offices_table['show'] = 'headings'
        self.offices_table.column("ofccode", width=110)
        self.offices_table.column("city", width=125)
        self.offices_table.column("phone", width=125)
        self.offices_table.column("addline1", width=125)
        self.offices_table.column("addline2", width=125)
        self.offices_table.column("state", width=125)
        self.offices_table.column("country", width=125)
        self.offices_table.column("postcode", width=125)
        self.offices_table.column("territory", width=125)
        self.offices_table.pack(fill=BOTH, expand=1)
        self.offices_table.bind("<ButtonRelease-1>", self.get_cursor02)
        self.fetch_data06()

        # productline frame
        F15 = Frame(self.master04, relief=GROOVE, bd=0, bg="powder blue")
        F15.place(x=979, y=358, width=550, height=365)
        product_line = Label(F15, text="Product Line", font="arial 15 bold", bd=7, relief=GROOVE, bg="gainsboro").pack(fill=X)
        self.table07_frame = Frame(self.master04, relief=GROOVE, bd=2, bg="powder blue")
        self.table07_frame.place(x=981, y=400, width=549, height=323)
        scroll_x = Scrollbar(self.table07_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.table07_frame, orient=VERTICAL)
        self.productLine_table = ttk.Treeview(self.table07_frame, columns=('prodline', 'textdesc', 'htmldesc', 'image'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.productLine_table.xview)
        scroll_y.config(command=self.productLine_table.yview)
        self.productLine_table.heading("prodline", text="ProductLine")
        self.productLine_table.heading("textdesc", text="Text Desc")
        self.productLine_table.heading("htmldesc", text="HTML Desc")
        self.productLine_table.heading("image", text="Image")
        self.productLine_table['show'] = 'headings'
        self.productLine_table.column("prodline", width=110)
        self.productLine_table.column("textdesc", width=125)
        self.productLine_table.column("htmldesc", width=125)
        self.productLine_table.column("image", width=125)
        self.productLine_table.pack(fill=BOTH, expand=1)
        self.productLine_table.bind("<ButtonRelease-1>", self.get_cursor03)
        self.fetch_data07()

    def add_office(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("insert into offices values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.office_code01_var.get(),
                                                                               self.city01_var.get(),
                                                                               self.phone01_var.get(),
                                                                               self.address_line01_var.get(),
                                                                               self.address_line02_var.get(),
                                                                               self.state01_var.get(),
                                                                               self.country01_var.get(),
                                                                               self.postal_code01_var.get(),
                                                                               self.territory01_var.get()
                                                                               ))
        con.commit()
        self.fetch_data06()
        self.clear()
        con.close()

    def fetch_data06(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from offices")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.offices_table.delete(*self.offices_table.get_children())
            for row in rows:
                self.offices_table.insert('', END, values=row)
                con.commit()
        con.close()

    def clear(self):
        self.office_code01_var.set("")
        self.city01_var.set("")
        self.phone01_var.set("")
        self.address_line01_var.set("")
        self.address_line02_var.set("")
        self.state01_var.set("")
        self.country01_var.set("")
        self.postal_code01_var.set("")
        self.territory01_var.set("")

    def get_cursor02(self, ev):
        cursor_row = self.offices_table.focus()
        contents = self.offices_table.item(cursor_row)
        row = contents['values']
        self.office_code01_var.set(row[0])
        self.city01_var.set(row[1])
        self.phone01_var.set(row[2])
        self.address_line01_var.set(row[3])
        self.address_line02_var.set(row[4])
        self.state01_var.set(row[5])
        self.country01_var.set(row[6])
        self.postal_code01_var.set(row[7])
        self.territory01_var.set(row[8])

    def update_data(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("update offices set city=%s,phone=%s,addressLine1=%s,addressLine2=%s,state=%s,country=%s,postalCode=%s,territory=%s where officeCode = %s", (
            self.city01_var.get(),
            self.phone01_var.get(),
            self.address_line01_var.get(),
            self.address_line02_var.get(),
            self.state01_var.get(),
            self.country01_var.get(),
            self.postal_code01_var.get(),
            self.territory01_var.get(),
            self.office_code01_var.get()
        ))
        con.commit()
        self.fetch_data06()
        self.clear()
        con.close()

    def delete_date(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("delete from offices where officeCode=%s", self.office_code01_var.get())
        con.commit()
        con.close()
        self.fetch_data06()
        self.clear()

    def search_date(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from offices where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.offices_table.delete(*self.offices_table.get_children())
            for row in rows:
                self.offices_table.insert('', END, values=row)
                con.commit()
        con.close()

    def back_btn(self):
        self.master04.destroy()
        import admin
        admin.admin_panel()

    def add_productLine(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("insert into productlines values(%s,%s,%s,%s)", (self.productLine_var.get(),
                                                                     self.text_desc_var.get(),
                                                                     self.html_desc_var.get(),
                                                                     self.image_var.get()
                                                                     ))
        con.commit()
        self.fetch_data07()
        self.clear_data()
        con.close()

    def fetch_data07(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from productlines")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.productLine_table.delete(*self.productLine_table.get_children())
            for row in rows:
                self.productLine_table.insert('', END, values=row)
                con.commit()
        con.close()

    def clear_data(self):
        self.productLine_var.set("")
        self.text_desc_var.set("")
        self.html_desc_var.set("")
        self.image_var.set("")

    def get_cursor03(self, ev):
        cursor_row = self.productLine_table.focus()
        contents = self.productLine_table.item(cursor_row)
        row = contents['values']
        self.productLine_var.set(row[0])
        self.text_desc_var.set(row[1])
        self.html_desc_var.set(row[2])
        self.image_var.set(row[3])

    def update_data01(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("update productlines set textDescription=%s,htmlDescription=%s,image=%s where productLine = %s", (self.text_desc_var.get(),
                                                                                                                      self.html_desc_var.get(),
                                                                                                                      self.image_var.get(),
                                                                                                                      self.productLine_var.get()
                                                                                                                      ))
        con.commit()
        self.fetch_data07()
        self.clear_data()
        con.close()

    def delete_date01(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("delete from productlines where productLine=%s", self.productLine_var.get())
        con.commit()
        con.close()
        self.fetch_data07()
        self.clear_data()