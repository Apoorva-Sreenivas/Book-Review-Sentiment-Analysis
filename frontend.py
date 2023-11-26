import tkinter as tk
import control

class Review_Main():
    
    def send_and_set_data(self):
        ctrl = control.Control()
        book_name = self.name_entry.get()
        overall_rating,book_name_1,book_name_2,author_name = ctrl.call(book_name)
        self.book_name1_var.set(book_name_1)
        self.overall_rating_var.set(overall_rating)
        self.book_name2_var.set(book_name_2)
        self.author_name_var.set(author_name)


    def show_window(self):
        w = tk.Tk()
        w.option_add("*Font", "aerial 10 bold")
        self.book_name1_var = tk.StringVar(w)
        self.book_name2_var = tk.StringVar(w)
        self.author_name_var = tk.StringVar(w)
        self.overall_rating_var = tk.StringVar(w)
        w.title("Book Review Analysis")
        bg = tk.PhotoImage(file="library1.png")
        label1 = tk.Label( w, image = bg) 
        label1.place(x = 0, y = 0) 
        f1 = tk.Frame(w,bg="brown4")
        book = tk.Label(f1,text="Enter Book Name")
        book.grid(row=0,column=0,padx=10,pady=10)
        self.name_entry = tk.Entry(f1)
        self.name_entry.grid(row=0,column=1,padx=10)
        enter = tk.Button(f1,text="Find",command=self.send_and_set_data)
        enter.grid(row=1,column=0,padx=10,pady=10,columnspan=2)
        book_name_1 = tk.Label(f1,text="Book Name")
        book_name_1.grid(row=2,column=0,padx=10,pady=10)
        book_name_11 = tk.Label(f1,textvariable=self.book_name1_var)
        book_name_11.grid(row=2,column=1,padx=10)
        book_name_12 = tk.Label(f1,textvariable=self.book_name2_var)
        book_name_12.grid(row=3,column=1,padx=10)
        author_name_1 = tk.Label(f1,text="Author Name")
        author_name_1.grid(row=4,column=0,padx=10,pady=10)
        author_name_11 = tk.Label(f1,textvariable=self.author_name_var)
        author_name_11.grid(row=4,column=1,padx=10)
        overall_rating_1 = tk.Label(f1,text="Overall Rating")
        overall_rating_1.grid(row=5,column=0,padx=10,pady=10)
        overall_rating_11 = tk.Label(f1,textvariable=self.overall_rating_var)
        overall_rating_11.grid(row=5,column=1)
        f1.place(relx=0.5,rely=0.5,anchor="center")
        w.geometry("626x358")
        w.mainloop()

rm = Review_Main()
rm.show_window()