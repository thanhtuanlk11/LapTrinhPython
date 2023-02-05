import tkinter as tk
 
import tkinter as tk
  
root=tk.Tk()
 
# setting the windows size
root.geometry("200x200")
  

name_var=tk.StringVar()
passw_var=tk.StringVar()
 
  

def submit():
 
    name=name_var.get()
    password=passw_var.get()
     
    print("Tên của bạn là : " + name)
    print("Mật khẩu của bạn là : " + password)
     
    name_var.set("")
    passw_var.set("")
     
     
# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'tài khoản', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
  
# creating a label for password
passw_label = tk.Label(root, text = 'mật khẩu', font = ('calibre',10,'bold'))
  
# creating a entry for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

sub_btn=tk.Button(root,text = 'Đăng nhập', command = submit)
  

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()