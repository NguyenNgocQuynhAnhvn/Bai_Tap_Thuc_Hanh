import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


root = Tk()
root.title("He thong quan ly sinh vien")
root.geometry("600x800")


# Tao 1 ket noi den database
conn = sqlite3.connect("Sinh_Vien.db")

# Tao ra doi tuong con tro
c = conn.cursor()

# Tao bang trong sql
try:
    c.execute(
        """
        Create Table If Not Exists Sinh_Vien
        (
            masinhvien INTERGER Primary Key,
            ho TEXT,
            ten TEXT,
            malop TEXT,
            namnhaphoc INTERGER,
            diemtb REAL
        )
        """)
except Exception as e:
    print(e) 
conn.close()


def them():
    try:
        # Kết nối và lấy dữ liệu
        conn = sqlite3.connect('Sinh_Vien.db')
        c = conn.cursor()
        
        # Lấy dữ liệu đã nhập
        id_value = id.get() 
        l_name_value = l_name.get()
        f_name_value = f_name.get()
        class_id_value = class_id.get()
        year_enroll_value = year_enroll.get()
        average_value = float(average.get())
        if average_value <0 or average_value >10:
            messagebox.showerror("Thong Bao!","Diem ban vua nhap khong hop le")
        else:
            pass 
            
        # Thực hiện câu lệnh để thêm
        c.execute("""
            INSERT INTO 
            Sinh_Vien (masinhvien, ho, ten, malop, namnhaphoc, diemtb)
            VALUES 
            (:masinhvien, :ho, :ten, :malop, :namnhaphoc, :diemtb)
        """,{
            'masinhvien' : id_value,
            'ho' : l_name_value,
            'ten': f_name_value,
            'malop': class_id_value,
            'namnhaphoc': year_enroll_value,
            'diemtb': average_value,
        })

        conn.commit()
        conn.close()

        # Reset form
        id.delete(0, END)
        l_name.delete(0, END)
        f_name.delete(0, END)
        class_id.delete(0, END)
        year_enroll.delete(0, END)
        average.delete(0, END)

        # Hien thi lai du lieu
        truy_van() 
    except Exception as e:
        print(f"Loi {e}")

def xoa():
    try:
        # Ket nooi den database
        conn = sqlite3.connect("Sinh_Vien.db")
        # Tao doi tuong con tro
        c = conn.cursor()
        c.execute("""
            Select *
            From Sinh_Vien
            Where masinhvien = :id
            """, {
                'id':enter_box.get()
                })
        # Lay 1 dong du lieu ra 
        records = c.fetchone()
 
        if records is None:
            messagebox.showwarning("Thong bao", "Id khong ton tai")
            enter_box.delete(0, END)
        else:
        # Thuc thi cau lenh sql
            c.execute("""Delete From Sinh_Vien
                        Where masinhvien= :id
                    """,{
                        'id':enter_box.get()
                        })
            enter_box.delete(0, END)
            conn.commit()
            
            # Sau khi xoa thi phai hien thi
            messagebox.showinfo("Thong bao", "Da xoa!")

        truy_van()
        conn.close()
    except Exception as e:
            print(e)

def cap_nhat():
    # Ket noi den database
    conn = sqlite3.connect("Sinh_Vien.db")
    # Tao đối tượng con trỏ
    c = conn.cursor()
    record_id = f_id_editor.get()

    # Thuc hien cau truy van
    c.execute("""
        UPDATE Sinh_Vien
        SET masinhvien = :id,
            ho = :last,
            ten = :first,
            malop = :class_id,
            namnhaphoc = :year_enroll,
            diemtb = :average
        WHERE masinhvien = :id
    """, {
        'id': record_id,
        'last': l_name_editor.get(),
        'first': f_name_editor.get(),
        'class_id': class_id_editor.get(),
        'year_enroll': year_enroll_editor.get(),
        'average': average_editor.get()

        # 'zipcode': zipcode_editor.get(),
    })
    
    # Lưu thay đổi và ngắt kết nối
    conn.commit()
    
    conn.close()
    editor.destroy()
    
    # Hien thi lai danh sach sau khi cap nhat
    truy_van()

def truy_van():
    # Xóa đi các dữ liệu trong TreeView
    for row in tree.get_children():
        tree.delete(row)

    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('Sinh_Vien.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Sinh_Vien")
    result = c.fetchall()
    print(result)
    # Hien thi du lieu
    for r in result:
        tree.insert("", END, values=(r[0], r[1], r[2], r[3], r[4], r[5]))

    # Ngat ket noi
    conn.close()

def chinh_sua():
    # Ket nooi den database
    conn = sqlite3.connect("Sinh_Vien.db")
    # Tao doi tuong con tro
    c = conn.cursor()

    c.execute("""
        Select masinhvien
        From Sinh_Vien
        Where masinhvien = :id
""",{
    'id':enter_box.get()
    })
    record = c.fetchone()


    if record is None:
        messagebox.showwarning("Thông báo", "ID không hợp lệ!")
    else:
        global editor
        editor = Tk()
        editor.title('Cập nhật bản ghi')
        editor.geometry("400x300")

        conn = sqlite3.connect('Sinh_Vien.db')
        c = conn.cursor()
        record_id = enter_box.get()
        c.execute("SELECT * FROM Sinh_Vien WHERE masinhvien = :id", {
            'id':record_id
            })
        records = c.fetchall()
        
            
        global f_id_editor, l_name_editor, f_name_editor, class_id_editor, year_enroll_editor, average_editor

        f_id_editor = Entry(editor, width=30)
        f_id_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        l_name_editor = Entry(editor, width=30)
        l_name_editor.grid(row=1, column=1, padx=20)
        f_name_editor = Entry(editor, width=30)
        f_name_editor.grid(row=2, column=1)
        class_id_editor = Entry(editor, width=30)
        class_id_editor.grid(row=3, column=1)
        year_enroll_editor = Entry(editor, width=30)
        year_enroll_editor.grid(row=4, column=1)
        average_editor = Entry(editor, width=30)
        average_editor.grid(row=5, column=1)


        # zipcode_editor = Entry(editor, width=30)
        # zipcode_editor.grid(row=6, column=1)

        f_id_label = Label(editor, text="ID")
        f_id_label.grid(row=0, column=0, pady=(10, 0))
        l_name_label = Label(editor, text="Họ")
        l_name_label.grid(row=1, column=0)
        f_name_label = Label(editor, text="Tên")
        f_name_label.grid(row=2, column=0)
        class_id_label = Label(editor, text="Mã lớp")
        class_id_label.grid(row=3, column=0)
        year_enroll_label = Label(editor, text="Năm nhập học")
        year_enroll_label.grid(row=4, column=0)
        average_label = Label(editor, text="Điểm trung bình")
        average_label.grid(row=5, column=0)
        
        # zipcode_label = Label(editor, text="Mã bưu chính")
        # zipcode_label.grid(row=6, column=0)

        for record in records:
            f_id_editor.insert(0, record[0])
            f_name_editor.insert(0, record[1])
            l_name_editor.insert(0, record[2])
            class_id_editor.insert(0, record[3])
            year_enroll_editor.insert(0, record[4])
            average_editor.insert(0, record[5])

            # zipcode_editor.insert(0, record[6])

        edit_btn = Button(editor, text="Cập nhật", command=cap_nhat)
        edit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

# Khung cho các ô nhập liệu
input_frame = Frame(root)
input_frame.pack(pady=10)

# Các ô nhập liệu cho cửa sổ chính
id = Entry(input_frame, width=30)
id.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(input_frame, width=30)
l_name.grid(row=1, column=1)

f_name = Entry(input_frame, width=30)
f_name.grid(row=2, column=1)

class_id = Entry(input_frame, width=30)
class_id.grid(row=3, column=1)

year_enroll = Entry(input_frame, width=30)
year_enroll.grid(row=4, column=1)

average = Entry(input_frame, width=30)
average.grid(row=5, column=1)

# Các nhãn
id_label = Label(input_frame, text="Mã sinh viên")
id_label.grid(row=0, column=0, pady=(10, 0))

lastname_label = Label(input_frame, text="Họ")
lastname_label.grid(row=1, column=0)

firstname_label = Label(input_frame, text="Tên")
firstname_label.grid(row=2, column=0)

class_id_label = Label(input_frame, text="Mã lớp")
class_id_label.grid(row=3, column=0)

year_enroll_label = Label(input_frame, text="Năm nhập học")
year_enroll_label.grid(row=4, column=0)

average_point_label = Label(input_frame, text="Điểm trung bình")
average_point_label.grid(row=5, column=0)

# Khung cho các nút chức năng
button_frame = Frame(root)
button_frame.pack(pady=10)

# Các nút chức năng
submit_btn = Button(button_frame, text="Thêm bản ghi", command=them)
submit_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(button_frame, text="Hiển thị bản ghi", command=truy_van)
query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

enter_box_label = Label(button_frame, text="Chọn ID")
enter_box_label.grid(row=2, column=0, pady=5)
enter_box = Entry(button_frame, width=30)
enter_box.grid(row=2, column=1, pady=5)

delete_btn = Button(button_frame, text="Xóa bản ghi", command=xoa)
delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

edit_btn = Button(button_frame, text="Chỉnh sửa bản ghi", command=chinh_sua)
edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Khung cho Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Treeview để hiển thị bản ghi
columns = ("MSSV", "Họ", "Tên", "Mã lớp", "Năm nhập học", "Điểm")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
tree.pack()

# Định nghĩa tiêu đề cho các cột
for col in columns:
    tree.heading(col, text=col)

# Gọi hàm truy vấn để hiển thị bản ghi khi khởi động
truy_van()

root.mainloop()