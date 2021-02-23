from tkinter import *
from tkinter import ttk
import pymysql
import time


class product:
    def __init__(self):
        self.master03 = Tk()
        self.master03.focus_force()
        self.master03.grab_set()
        self.master03.title("Product Details")
        self.master03.geometry("1545x847+0+0")
        self.master03.resizable(False, False)
        self.master03.config(bg='grey40')

        # Products variables
        self.product_code_var = StringVar()
        self.product_name_var = StringVar()
        self.product_line_var = StringVar()
        self.product_scale_var = StringVar()
        self.product_vendor_var = StringVar()
        self.product_description_var = StringVar()
        self.quantity_in_stock_var = StringVar()
        self.buy_price_var = StringVar()
        self.msrp_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        # Products Frame
        product_details_lbl = Label(self.master03, text="Product Details", font=("time new roman", 18, "bold"), bd=2, bg='Light cyan3')
        product_details_lbl.place(x=0, y=0, height=70, width=1550)

        F7 = LabelFrame(self.master03, text="Orders", bd=2, bg='cyan3')
        F7.place(x=3, y=73, height=700, width=520)

        product_code_lbl = Label(F7, text="Product Code", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=0, column=0, padx=20, pady=5, sticky='w')
        product_code_txt = Entry(F7, width=15, textvariable=self.product_code_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        product_name_lbl = Label(F7, text="Product Name", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=1, column=0, padx=20, pady=5, sticky='w')
        product_name_txt = Entry(F7, width=15, textvariable=self.product_name_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=1, column=1, pady=5, padx=10)

        product_line_lbl = Label(F7, text="Product Line ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=2, column=0, padx=20, pady=5, sticky='w')
        product_line_txt = Entry(F7, width=15, textvariable=self.product_line_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=2, column=1, pady=5, padx=10)

        product_scale_lbl = Label(F7, text="Product Scale ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=3, column=0, padx=20, pady=5, sticky='w')
        product_scale_txt = Entry(F7, width=15, textvariable=self.product_scale_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=3, column=1, pady=5, padx=10)

        product_vendor_lbl = Label(F7, text="Product Vendor ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=4, column=0, padx=20, pady=5, sticky='w')
        product_vendor_txt = Entry(F7, width=15, textvariable=self.product_vendor_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=4, column=1, pady=5, padx=10)

        product_description_lbl = Label(F7, text="Product Description ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=5, column=0, padx=20, pady=5, sticky='w')
        product_description_txt = Entry(F7, width=15, textvariable=self.product_description_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=5, column=1, pady=5, padx=10)

        Quantity_in_stock_lbl = Label(F7, text="Quantity In Stock ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=6, column=0, padx=20, pady=5, sticky='w')
        Quantity_in_stock_txt = Entry(F7, width=15, textvariable=self.quantity_in_stock_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=6, column=1, pady=5, padx=10)

        Buy_price_lbl = Label(F7, text="Buy Price ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=7, column=0, padx=20, pady=5, sticky='w')
        Buy_price_txt = Entry(F7, width=15, textvariable=self.buy_price_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=7, column=1, pady=5, padx=10)

        msrp_lbl = Label(F7, text="MSRP ", fg="grey55", bg='cyan3', font=("time new roman", 13, "bold")).grid(row=8, column=0, padx=20, pady=5, sticky='w')
        msrp_txt = Entry(F7, width=15, textvariable=self.msrp_var, font="arial 15", bd=4, relief=SUNKEN).grid(row=8, column=1, pady=5, padx=10)

        # Product add,update,insert button
        btn_lbl = LabelFrame(F7, bd=5, bg='lavender').place(x=5, y=410, height=110, width=505)
        add_btn = Button(F7, relief=GROOVE, text='Add', bg='slate grey', command=self.add_product, font='times 15 bold', width=20, bd=5).place(x=8, y=413, height=30, width=122)
        update_btn = Button(F7, relief=GROOVE, text='Update', bg='slate grey', command=self.update_data, font='times 15 bold', width=20, bd=5).place(x=133, y=413, height=30, width=122)
        delete_btn = Button(F7, relief=GROOVE, text='Delete', bg='slate grey', command=self.delete_date, font='times 15 bold', width=20, bd=5).place(x=258, y=413, height=30, width=122)
        clear_btn = Button(F7, relief=GROOVE, text='Clear', bg='slate grey', command=self.clear, font='times 15 bold', width=20, bd=5).place(x=383, y=413, height=30, width=122)
        search_lbl = Label(F7, text="Search by", fg="black", bg='lavender', font=("time new roman", 15, "bold"), bd=5).place(x=8, y=445, height=30, width=122)
        combo_serach = ttk.Combobox(F7, font='times 12 bold', textvariable=self.search_by, state='readonly')
        combo_serach['values'] = (' productCode', 'productLine')
        combo_serach.place(x=133, y=445, height=30, width=121)
        search_btn_txt = Entry(F7, width=15, font="arial 12", bg='white', textvariable=self.search_txt, relief=SUNKEN, bd=5).place(x=258, y=445, height=30, width=122)
        search_btn = Button(F7, relief=GROOVE, text='Search', bg='slate grey', command=self.search_date,font='times 15 bold', width=20, bd=5).place(x=383, y=445, height=30, width=122)
        all_orders_btn = Button(F7, relief=GROOVE, bg='slate grey', command=self.fetch_data05, text='Show All', font='times 15 bold', width=20, bd=5).place(x=133, y=478, height=30, width=122)
        back_btn = Button(F7, relief=GROOVE, text='Back', bg='slate grey', command=self.back_btn, font='times 15 bold', width=20, bd=5).place(x=258, y=478, height=30, width=122)


        F8 = Frame(self.master03, relief=GROOVE, bd=0, bg="LightCyan2")
        F8.place(x=525, y=73, width=1000, height=30)  # x=1070y=180
        product_details = Label(F8, text="Products Details", font="arial 15 bold", bd=7, relief=GROOVE, bg="gainsboro").pack(fill=X)
        self.table05_frame = Frame(self.master03, relief=GROOVE, bd=2, bg="powder blue")
        self.table05_frame.place(x=525, y=105, width=1000, height=670)
        scroll_x = Scrollbar(self.table05_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.table05_frame, orient=VERTICAL)
        self.product_table = ttk.Treeview(self.table05_frame, columns=('prodcode', 'prodname', 'prodline', 'prodscale', 'prodven', 'proddesc', 'quaninstck', 'buyprice', 'msrp'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)
        self.product_table.heading("prodcode", text="Product Code")
        self.product_table.heading("prodname", text="Product Name")
        self.product_table.heading("prodline", text="Product Line")
        self.product_table.heading("prodscale", text="Product Scale")
        self.product_table.heading("prodven", text="Product Vendor")
        self.product_table.heading("proddesc", text="Product Description")
        self.product_table.heading("quaninstck", text="Quantity In Stock")
        self.product_table.heading("buyprice", text="Buy Price")
        self.product_table.heading("msrp", text="MSRP")
        self.product_table['show'] = 'headings'
        self.product_table.column("prodcode", width=110)
        self.product_table.column("prodname", width=125)
        self.product_table.column("prodline", width=125)
        self.product_table.column("prodscale", width=125)
        self.product_table.column("prodven", width=125)
        self.product_table.column("proddesc", width=125)
        self.product_table.column("quaninstck", width=125)
        self.product_table.column("buyprice", width=125)
        self.product_table.column("msrp", width=125)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_cursor02)
        self.fetch_data05()

    def add_product(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("insert into products values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.product_code_var.get(),
                                                                                self.product_name_var.get(),
                                                                                self.product_line_var.get(),
                                                                                self.product_scale_var.get(),
                                                                                self.product_vendor_var.get(),
                                                                                self.product_description_var.get(),
                                                                                self.quantity_in_stock_var.get(),
                                                                                self.buy_price_var.get(),
                                                                                self.msrp_var.get()
                                                                                ))
        con.commit()
        self.fetch_data05()
        self.clear()
        con.close()

    def fetch_data05(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from products")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)
                con.commit()
        con.close()

    def clear(self):
        self.product_code_var.set("")
        self.product_name_var.set("")
        self.product_line_var.set("")
        self.product_scale_var.set("")
        self.product_vendor_var.set("")
        self.product_description_var.set("")
        self.quantity_in_stock_var.set("")
        self.buy_price_var.set("")
        self.msrp_var.set("")

    def get_cursor02(self, ev):
        cursor_row = self.product_table.focus()
        contents = self.product_table.item(cursor_row)
        row = contents['values']
        self.product_code_var.set(row[0])
        self.product_name_var.set(row[1])
        self.product_line_var.set(row[2])
        self.product_scale_var.set(row[3])
        self.product_vendor_var.set(row[4])
        self.product_description_var.set(row[5])
        self.quantity_in_stock_var.set(row[6])
        self.buy_price_var.set(row[7])
        self.msrp_var.set(row[8])

    def update_data(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("update products set productName=%s,productLine=%s,productScale=%s,productVendor=%s,productDescription=%s,quantityInStock=%s,buyPrice=%s,MSRP=%s where productCode=%s", (
                                                                                                                                                            self.product_name_var.get(),
                                                                                                                                                            self.product_line_var.get(),
                                                                                                                                                            self.product_scale_var.get(),
                                                                                                                                                            self.product_vendor_var.get(),
                                                                                                                                                            self.product_description_var.get(),
                                                                                                                                                            self.quantity_in_stock_var.get(),
                                                                                                                                                            self.buy_price_var.get(),
                                                                                                                                                            self.msrp_var.get(),
                                                                                                                                                            self.product_code_var.get()
                                                                                                                                                            ))
        con.commit()
        self.fetch_data05()
        self.clear()
        con.close()

    def delete_date(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("delete from products where productCode=%s",self.product_code_var.get())
        con.commit()
        con.close()
        self.fetch_data05()
        self.clear()

    def search_date(self):
        con = pymysql.connect(host="", user="", password="", database="")
        cur = con.cursor()
        cur.execute("select * from products where " + str(self.search_by.get()) + " LIKE '%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)
                con.commit()
        con.close()

    def back_btn(self):
        self.master03.destroy()
        import admin
        admin.admin_panel()