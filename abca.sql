CREATE DATABASE QLSINHVIEN1;
use QLSINHVIEN1;



create table Khoa(
	MaKhoa varchar(10) primary key,
    TenKhoa varchar(100)
)
;

create table Lop(
	MaLop varchar(10) primary key,
    TenLop varchar(100),
    MaKhoa varchar(10) not null,
    foreign key(MaKhoa) references Khoa(MaKhoa)
)
;
create table SinhVien(
	MaSV varchar(10) primary key,
    TenSV varchar(100) null,
    GioiTinh varchar(100) null,
    NgaySinh datetime null,
    MaLop varchar(10) not null,
    foreign key(MaLop) references Lop(MaLop)
)
;
create table MonHoc(
	MaMH varchar(10) primary key,
	TenMH nvarchar(100),
    SoTiet int
)
;
create table DiemThi(
	MaSV varchar(10) not null,
	MaMH varchar(10) not null,
    Diem_Thi float,
    primary key(MaSV, MaMH),
    foreign key(MaSV) references SinhVien(MaSV),
	foreign key(MaMH) references MonHoc(MaMH)
)
;
Insert into Khoa values('K01', 'CNTT');
Insert into Khoa values('K02', 'KTDT');
Insert into Khoa values('K03', 'ANTT');


Insert into Lop values('L01', 'Lop1','K01');
Insert into Lop values('L02', 'Lop2','K02');
Insert into Lop values('L03', 'Lop3','K03');
Insert into Lop values('L04', 'Lop4','K03');
Insert into Lop values('L05', 'Lop5','K01');


Insert into SinhVien values('001', N'Nguyễn Vĩnh An', N'Nam', '2021-2-7', 'L01');
Insert into SinhVien values('002', N'Nguyễn Kim Toàn', N'Nam', '2021-2-7', 'L02');
Insert into SinhVien values('003', N'Nguyễn Việt đức', N'Nữ', '2011-5-7', 'L02');
Insert into SinhVien values('004', N'Nguyễn thanh thảo', N'Nam', '2221-2-7', 'L03');
Insert into SinhVien values('005', N'Nguyễn abc', N'Nữ', '2022-7-2', 'L04');
Insert into SinhVien values('006', N'Nguyễn bc', N'Nam', '2021-5-7', 'L05');
Insert into SinhVien values('007', N'Nguyễn bcaa', N'Nam', '2021-5-9', 'L05');

Insert into MonHoc values('MH01', 'Toan','15');
Insert into MonHoc values('MH02', 'Ly','20');
Insert into MonHoc values('MH03', 'Hoa','30');

Insert into DiemThi values('001', 'MH01','6');
Insert into DiemThi values('002', 'MH02','6');
Insert into DiemThi values('003', 'MH03','3');
Insert into DiemThi values('004', 'MH01','2');

Select * from quanlisinhvien.diemthi;
Select * from quanlisinhvien.monhoc;

update DiemThi
set Diem_Thi = 9
where MaSV = '001';

update SinhVien
set MaLop = 'L01'
where MaSV = '007';

Select TenSV,GioiTinh from SinhVien , DiemThi
Where SinhVien.MaSV = DiemThi.MaSV and Diem_Thi = '3';



