import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Hệ thống quản lý sinh viên")
root.geometry("800x600")

conn = sqlite3.connect("SinhVien.db")
c = conn.cursor()

 # Tao bang de luu tru
# c.execute('''
#     CREATE TABLE Sinh_Vien(
#          MSSV INTEGER PRIMARY KEY AUTOINCREMENT,
#          Ho text,
#          Ten text,
#          MaLop text,
#          Namnhaphoc interger,
#          DTB interger
#      )
#  ''')

conn.close()

def them():
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('SinhVien.db')
    c = conn.cursor()
    # Lấy dữ liệu đã nhập
    Id_value = ID.get()
    name_value =f_name.get()
    lastName_value = l_name.get()
    ClassID_value = Class_ID.get()
    year_ernoll_value = year_ernoll.get()
    average_point_value = average_point.get()
    
    # Thực hiện câu lệnh để thêm
    c.execute('''
        INSERT INTO 
        Sinh_Vien (MSSV,Ho, Ten,MaLop , Namnhaphoc, DTB)
        VALUES 
        (:ID, :name, :last_name, :ClassID,:Yearenroll, :Averangepoint)
    ''',{
        'ID' : Id_value,
        'name' : name_value,
        'last_name' : lastName_value,
        'ClassID': ClassID_value,
        'Yearenroll': year_ernoll_value,
        'Averangepoint': average_point_value,
        
      }
    )
    conn.commit()
    conn.close()

    # Reset form
    ID.delete(0,END)
    f_name.delete(0,END)
    l_name.delete(0,END)
    Class_ID.delete(0,END)
    year_ernoll.delete(0,END)
    average_point.delete(0,END)
    

    # Hien thi lai du lieu
    truy_van()

def xoa():
    conn = sqlite3.connect('SinhVien.db')
    c = conn.cursor()
    c.execute(''' DELETE FROM
                        Sinh_Vien
                        WHERE MSSV =:id''',
            {'id':delete_box.get()})
    delete_box.delete(0, END)
    conn.commit()
    conn.close()
    messagebox.showinfo("Thông báo", "Đã xóa!")
    truy_van()
def chinh_sua():
    global editor
    editor = Tk()
    editor.title('Cập nhật bản ghi')
    editor.geometry("400x300")

    conn = sqlite3.connect('SinhVien.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM Sinh_Vien WHERE MSSV=:id", {'id':record_id})
    records = c.fetchall()

    global f_id_editor, f_name_editor, l_name_editor, Class_ID_editor, year_ernoll_editor, average_point_editor

    f_id_editor = Entry(editor, width=30)
    f_id_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=1, column=1, padx=20)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=2, column=1)
    Class_ID_editor = Entry(editor, width=30)
    Class_ID_editor.grid(row=3, column=1)
    year_ernoll_editor = Entry(editor, width=30)
    year_ernoll_editor.grid(row=4, column=1)
    average_point_editor = Entry(editor, width=30)
    average_point_editor.grid(row=5, column=1)
    

    f_id_label = Label(editor, text="ID")
    f_id_label.grid(row=0, column=0, pady=(10, 0))
    f_name_label = Label(editor, text="Họ")
    f_name_label.grid(row=1, column=0)
    l_name_label = Label(editor, text="Tên")
    l_name_label.grid(row=2, column=0)
    Class_ID_label = Label(editor, text="Mã Lớp")
    Class_ID_label.grid(row=3, column=0)
    year_ernoll_label = Label(editor, text="Năm nhập học")
    year_ernoll_label.grid(row=4, column=0)
    average_point_label = Label(editor, text="Điểm trung bình")
    average_point_label.grid(row=5, column=0)
   

    for record in records:
        f_id_editor.insert(0, record[0])
        f_name_editor.insert(0, record[1])
        l_name_editor.insert(0, record[2])
        Class_ID_editor.insert(0, record[3])
        year_ernoll_editor.insert(0, record[4])
        average_point_editor.insert(0, record[5])
        

    edit_btn = Button(editor, text="Lưu bản ghi", command=cap_nhat)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

def cap_nhat():
    conn = sqlite3.connect('SinhVien.db')
    c = conn.cursor()
    record_id = f_id_editor.get()

    c.execute("""UPDATE Sinh_Vien SET
           first_name = :first,
           last_name = :last,
           address = :ClassID,
           city = :city,
           state = :state,
           WHERE MSSV = :id""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'ClassID': Class_ID_editor.get(),
                  'city': year_ernoll_editor.get(),
                  'state': average_point_editor.get(),
                  'id': record_id
              })

    conn.commit()
    conn.close()
    editor.destroy()

    # Cập nhật lại danh sách bản ghi sau khi chỉnh sửa
    truy_van()

def truy_van():
    # Xóa đi các dữ liệu trong TreeView
    for row in tree.get_children():
        tree.delete(row)

    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('SinhVien.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Sinh_Vien")
    records = c.fetchall()

    # Hien thi du lieu
    for r in records:
        tree.insert("", END, values=(r[0],  r[1], r[2]))


    # Ngat ket noi
    conn.close()


# Khung cho các ô nhập liệu
input_frame = Frame(root)
input_frame.pack(pady=10)

# Các ô nhập liệu cho cửa sổ chính
ID = Entry(input_frame, width=30)
ID.grid(row=0, column=1, padx=20, pady=(10, 0))
f_name = Entry(input_frame, width=30)
f_name.grid(row=1, column=1)
l_name = Entry(input_frame, width=30)
l_name.grid(row=2, column=1)
Class_ID = Entry(input_frame, width=30)
Class_ID.grid(row=3, column=1)
year_ernoll = Entry(input_frame, width=30)
year_ernoll.grid(row=4, column=1)
average_point = Entry(input_frame, width=30)
average_point.grid(row=5, column=1)

# Các nhãn
ID_label = Label(input_frame, text="MSSV")
ID_label.grid(row=0, column=0, pady=(10, 0))
f_name_label = Label(input_frame, text="Họ")
f_name_label.grid(row=1, column=0)
l_label = Label(input_frame, text="Tên")
l_label.grid(row=2, column=0)
Class_ID_label = Label(input_frame, text="Mã lớp")
Class_ID_label.grid(row=3, column=0)
year_ernoll_label = Label(input_frame, text="Năm nhập học")
year_ernoll_label.grid(row=4, column=0)
average_point_label = Label(input_frame, text="Điểm trung bình")
average_point_label.grid(row=5, column=0)

# Khung cho các nút chức năng
button_frame = Frame(root)
button_frame.pack(pady=10)

# Các nút chức năng
submit_btn = Button(button_frame, text="Thêm bản ghi", command=them)
submit_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_btn = Button(button_frame, text="Hiển thị bản ghi")
query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
delete_box_label = Label(button_frame, text="Chọn ID để ")
delete_box_label.grid(row=2, column=0, pady=5)
delete_box = Entry(button_frame, width=30)
delete_box.grid(row=2, column=1, pady=5)
delete_btn = Button(button_frame, text="Xóa bản ghi", command=xoa)
delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
edit_btn = Button(button_frame, text="Chỉnh sửa bản ghi", command=chinh_sua)
edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=125)



# Khung cho Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Treeview để hiển thị bản ghi
columns = ("ID", "Họ", "Tên")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
tree.pack()

# Định nghĩa tiêu đề cho các cột
for col in columns:
    tree.heading(col, text=col)

truy_van()
root.mainloop()














