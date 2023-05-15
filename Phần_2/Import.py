import pandas as pd

#import file danh mục loaihinh vào table loaihinh
dmlh = pd.read_excel(r'D:\HK2\CSDL\Đồ Án 1\DATA\danhmuc\DanhMucLoaiHinh.xlsx')
with open(r'D:\HK2\CSDL\Đồ Án 1\Phần_2\DanhMucLoaiHinh.sql', 'w', encoding='utf-8') as file:
    for index, row in dmlh.iterrows():
        sql = f"INSERT INTO `loaihinh` (malh, loaihinh) VALUES ({row['malh']}, N'{row['loaihinh']}')"
        file.write(sql + ";" +'\n')

#tạo file import danh mục loaitruong vào table loaitruong
dmlt = pd.read_excel(r'D:\HK2\CSDL\Đồ Án 1\DATA\danhmuc\DanhMucLoaiTruong.xlsx')
with open(r'D:\HK2\CSDL\Đồ Án 1\Phần_2\DanhMucLoaiTruong.sql', 'w', encoding='utf-8') as file:
    for index, row in dmlt.iterrows():
        sql = f"INSERT INTO `loaitruong` (malt, loaitruong) VALUES ({row['malt']}, N'{row['loaitruong']}')"
        file.write(sql + ';' + '\n')

# #tạo file import danh mục phongdt vào table phongdt 
dmp = pd.read_excel(r'D:\HK2\CSDL\Đồ Án 1\DATA\danhmuc\DanhMucPhong.xlsx')
with open(r'D:\HK2\CSDL\Đồ Án 1\Phần_2\DanhMucPhong.sql', 'w', encoding='utf-8') as file:
    for index, row in dmp.iterrows():
        sql = f"INSERT INTO `phongdt` (maphong, phongdt) VALUES ({row['maphong']}, N'{row['phongdt']}')"
        file.write(sql + ';' + '\n')
#tạo file import các file trường vào table school 
gdtx = pd.read_excel(r'D:\HK2\CSDL\Đồ Án 1\DATA\edited_data\gdtx.xlsx')
with open(r'D:\HK2\CSDL\Đồ Án 1\Phần_2\gdtx.sql', 'w', encoding='utf-8') as file:
    for index, row in gdtx.iterrows():
        sql = f"INSERT INTO `school` (matrg, ten, dchi, malh, malt, maphong, tenso) VALUES (N'{row['matruong']}', N'{row['ten']}', N'{row['dchi']}', {row['malh']}, {row['malt']}, {row['maphong']}, N'{row['tenso']}')"
        file.write(sql + ';' + '\n')
mn = pd.read_excel(r'D:\HK2\CSDL\Đồ Án 1\DATA\edited_data\mn.xlsx')
with open(r'D:\HK2\CSDL\Đồ Án 1\Phần_2\mn.sql', 'w', encoding='utf-8') as file:
    for index, row in mn.iterrows():
        sql = f"INSERT INTO `school` (matrg, ten, dchi, malh, malt, maphong, tenso) VALUES (N'{row['matruong']}', N'{row['ten']}', N'{row['dchi']}', {row['malh']}, {row['malt']}, {row['maphong']}, N'{row['tenso']}')"
        file.write(sql + ';' + '\n')
th = pd.read_excel(r'D:\HK2\CSDL\Đồ Án 1\DATA\edited_data\th.xlsx')
with open(r'D:\HK2\CSDL\Đồ Án 1\Phần_2\th.sql', 'w', encoding='utf-8') as file:
    for index, row in th.iterrows():
        sql = f"INSERT INTO `school` (matrg, ten, dchi, malh, malt, maphong, tenso) VALUES (N'{row['matruong']}', N'{row['ten']}', N'{row['dchi']}', {row['malh']}, {row['malt']}, {row['maphong']}, N'{row['tenso']}')"
        file.write(sql + ';' + '\n')
thcs = pd.read_excel(r'D:\HK2\CSDL\Đồ Án 1\DATA\edited_data\thcs.xlsx')
with open(r'D:\HK2\CSDL\Đồ Án 1\Phần_2\thcs.sql', 'w', encoding='utf-8') as file:
    for index, row in thcs.iterrows():
        sql = f"INSERT INTO `school` (matrg, ten, dchi, malh, malt,  maphong, tenso) VALUES (N'{row['matruong']}', N'{row['ten']}', N'{row['dchi']}', {row['malh']},{row['malt']}, {row['maphong']}, N'{row['tenso']}')"
        file.write(sql + ';' + '\n')
thpt = pd.read_excel(r'D:\HK2\CSDL\Đồ Án 1\DATA\edited_data\thpt.xlsx')
with open(r'D:\HK2\CSDL\Đồ Án 1\Phần_2\thpt.sql', 'w', encoding='utf-8') as file:
    for index, row in thpt.iterrows():
        sql = f"INSERT INTO `school` (matrg, ten, dchi, malh, malt,  maphong, tenso) VALUES (N'{row['matruong']}', N'{row['ten']}', N'{row['dchi']}', {row['malh']},{row['malt']}, {row['maphong']}, N'{row['tenso']}')"
        file.write(sql + ';' + '\n')