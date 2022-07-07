from tkinter import*
import random
import os
from tkinter import messagebox


#===============main=====================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing System")
        bg_color = "#badc57"
        title = Label(self.root, text="Billing System", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#badc57", fg="Black", relief=GROOVE)
        title.pack(fill=X)
   
    # ============payment==============================
        self.water=IntVar()
        self.meter=IntVar()
        self.sanitary=IntVar()
        self.Dues=IntVar()
        self.other=IntVar()
    
    # ==============Total price================
      
        self.total_bill = StringVar()
        
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ===============Tax================================
        self.total=StringVar()

        self.tax=StringVar()
    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#badc57", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="#badc57", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)


    # ==========Payment=========================
        F3 = LabelFrame(self.root, text="Payment", font=('times new roman', 15, 'bold'), bd=10, fg="Black", bg="#badc57")
        F3.place(x=340, y=180, width=325, height=380)

        p1_lbl = Label(F3, text="Water Charge", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        p1_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        p1_txt = Entry(F3, width=10, textvariable=self.water, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        p1_txt.grid(row=0, column=1, padx=10, pady=10)

        p2_lbl = Label(F3, text="Meter Charge", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        p2_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        p2_txt = Entry(F3, width=10, textvariable=self.meter, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        p2_txt.grid(row=1, column=1, padx=10, pady=10)

        p3_lbl = Label(F3, text="Sanitary Charge", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        p3_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        p3_txt = Entry(F3, width=10, textvariable=self.sanitary, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        p3_txt.grid(row=2, column=1, padx=10, pady=10)

        p4_lbl = Label(F3, text="Dues", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        p4_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        p4_txt = Entry(F3, width=10, textvariable=self.Dues, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        p4_txt.grid(row=3, column=1, padx=10, pady=10)

        p5_lbl = Label(F3, text="Other Charge", font=('times new roman', 16, 'bold'), bg="#badc57", fg="black")
        p5_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        p5_txt = Entry(F3, width=10, textvariable=self.other, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        p5_txt.grid(row=4, column=1, padx=10, pady=10)



    # =================BillArea======================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=800, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="Black", bg="#badc57")
        F6.place(x=0, y=560, relwidth=1, height=140)

       

        m2_lbl = Label(F6, text="Total Price", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.total, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

     

     

        m5_lbl = Label(F6, text="Tax", font=('times new roman', 14, 'bold'), bg="#badc57", fg="black")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        

    # =======Buttons-======================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        t_btn = Button(btn_f, command=self.same, text="Total", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        t_btn.grid(row=0, column=0, padx=5, pady=5)

        t_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="white", pady=12, width=12, font='arial 13 bold')
        t_btn.grid(row=0, column=1, padx=5, pady=5)

        t_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="white", pady=15, width=12, font='arial 13 bold')
        t_btn.grid(row=0, column=2, padx=5, pady=5)

        t_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="white", pady=15, width=12, font='arial 13 bold')
        t_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()


    def same(self):

        self.w_p=self.water.get()*100
        self.m_p=self.meter.get()*75
        self.s_p=self.sanitary.get()*150
        self.d_p=self.Dues.get()*5
        self.o_p=self.other.get()*250
        
        self.price_total=float(
                            self.w_p+
                            self.m_p+
                            self.s_p+
                            self.d_p+
                            self.o_p 
                            )
        

        self.total.set("Rs." +str(self.price_total))
        self.t_tax=round((self.price_total*0.05),2)
        
        self.tax.set("Rs."+str(self.t_tax))

        self.total_bill = float(self.price_total+self.tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to WBS")
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n======================================")
        self.txtarea.insert(END,f"\n Particular \t\tUnit \t\tPrice")

    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.total_bill.get() == "Rs. 0.0" :
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
   
        if self.water.get():
            self.txtarea.insert(END, f"\n Water\t\t{self.water.get()}\t\t{self.w_p}")
        if self.meter.get() != 0:
            self.txtarea.insert(END, f"\n Meter\t\t{self.meter.get()}\t\t{self.m_p}")
        if self.sanitary.get() != 0:
            self.txtarea.insert(END, f"\n Sanitary\t\t{self.sanitary.get()}\t\t{self.s_p}")
        if self.Dues.get() != 0:
            self.txtarea.insert(END, f"\n Dues\t\t{self.Dues.get()}\t\t{self.d_p}")
        if self.other.get() != 0:
            self.txtarea.insert(END, f"\n Other\t\t{self.other.get()}\t\t{self.o_p}")
     
       
    # ===============taxes==============================
       
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Tax\t\t\t{self.grocery_tax.get()}")
        

        self.txtarea.insert(END, f"\n Total Bill:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
           
    # ============payment==============================
            self.water.set(0)
            self.meter.set(0)
            self.sanitary.set(0)
            self.Dues.set(0)
            self.other.set(0)
          
   
    # ====================taxes================================
            
            self.total_bill.set("")
          
            self.t_tax.set("")
        
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()