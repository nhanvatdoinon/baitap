#!/usr/bin/env python
# coding: utf-8

# In[3]:


import mysql.connector
conn = mysql.connector.connect(
      host ="localhost",
      user ="root",
      passwd ="kimtoan123",
      database = "qldiemthi",
      buffered=True
)
cursor = conn.cursor()
## tao bang sinh vien
sql_sinhvien = '''create table sinhvien(
    MaSV varchar(10) primary key,
    TenSV varchar(255) not null,
    GioiTinh varchar(10) null,
    DiaChi varchar(255) null,
    SoDienThoai varchar(30) null

);'''
sql_diemthi = """
    create table diemthi(
        MaSV varchar(10) not null,
        DiemToan float not null,
        DiemLy float not null,
        DiemHoa float not null,
        foreign key(MaSV) references sinhvien(MaSV)
    );"""
cursor.execute(sql_sinhvien)
cursor.execute(sql_diemthi)

# them data sinh vien
sql_insert  = "INSERT INTO sinhvien(MaSV,TenSv,GioiTinh,DiaChi,SoDienThoai) values (%s, %s, %s,%s,%s)"
data_sinhvien = [['01', 'Toàn', 'Nam','HN','31321321'],
 ['02', 'Duc', 'Nam', 'HCM', '+84789789789'],
 ['03', 'Như', "Nữ", 'HP', '+84828978666']]
cursor.executemany(sql_insert,data_sinhvien)
conn.commit()

# them data diem
sql_insert_diem = "INSERT INTO diemthi(MaSV,DiemToan,DiemLy,DiemHoa) values (%s, %s, %s, %s)"
data_diemthi = [['01', 7.8, 2.1, 7.4],
 ['02', 8.6, 7.7, 6.7],
 ['03', 4.4, 3.6, 6.7]]      
cursor.executemany(sql_insert_diem,data_diemthi)
conn.commit()

# truy van tong diem > x
tongdiem = int(input("Nhap tong diem"))
sql_tongdiem = """
    SELECT sv.MaSV,TenSV,GioiTinh,DiaChi,SoDienThoai,DiemToan,DiemLy,DiemHoa,(DiemToan + DiemLy + DiemHoa) as tongdiem
    FROM sinhvien as sv ,diemthi as dt
    WHERE sv.MaSV = dt.MaSV 
    GROUP BY sv.MaSV
    HAVING tongdiem > 'tongdiem'

""";
cursor.execute(sql_tongdiem)
## in ra thong tin
records = cursor.fetchall()
#conn.commit()
for row in records1:
        print("MaSV = ", row[0], )
        print("Tên = ", row[1])
        print("GioiTinh  = ", row[2])
        print("DiaChi  = ", row[3])
        print("SoDienThoai",row[4])
        print("DiemToan",row[5])
        print("DiemLy",row[6])
        print("DiemHoa",row[7],"\n")
        
        
# truy van diem toan > 2
x = float(input("Nhap diem toan"))
x
sql_diemtoan = """
    SELECT sv.MaSV,TenSV,GioiTinh,DiaChi,SoDienThoai,DiemToan,DiemLy,DiemHoa
    FROM sinhvien as sv ,diemthi as dt
    WHERE sv.MaSV = dt.MaSV and DiemToan > "x"
    ORDER BY sv.MASV,TenSV
""";
cursor.execute(sql_diemtoan)
records1 = cursor.fetchall()
print("Total number of rows in table: ", cursor.rowcount)
for row in records1:
        print("MaSV = ", row[0], )
        print("Tên = ", row[1])
        print("GioiTinh  = ", row[2])
        print("DiaChi  = ", row[3])
        print("SoDienThoai",row[4])
        print("DiemToan",row[5])
        print("DiemLy",row[6])
        print("DiemHoa",row[7],"\n")

# truy van thong tin theo ten
ten = str(input("Nhapten"))
ten
sql_thongtin = """
    SELECT sv.MaSV,TenSV,GioiTinh,DiaChi,SoDienThoai,DiemToan,DiemLy,DiemHoa
    FROM sinhvien as sv ,diemthi as dt
    WHERE sv.MaSV = dt.MaSV and TenSV = '{}'
    ORDER BY sv.MASV,TenSV
""";
#sql_thongtin.format(ten)
cursor.execute(sql_thongtin.format(ten))
records2 = cursor.fetchall()
records2
for row in records2:
        print("MaSV = ", row[0], )
        print("Tên = ", row[1])
        print("GioiTinh  = ", row[2])
        print("DiaChi  = ", row[3])
        print("SoDienThoai",row[4])
        print("DiemToan",row[5])
        print("DiemLy",row[6])
        print("DiemHoa",row[7],"\n")


# In[ ]:




