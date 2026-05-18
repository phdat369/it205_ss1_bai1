# Phân tích
# Hiện tại lỗi đang sai là do sau khi lưu vào biến và in ra phiếu thì đặt sai biến không đúng với vị trí của nó nên từ đó gây ra thông tin sai lệch

# Sửa code 

print(' -- HỆ THỐNG TIEP NHẬN BỆNH NHÂN --- ');
name_patient = input ( 'Nhập tên bệnh nhân: ');
age = int(input ('Mời bạn nhập tuổi: '));
symptom = input ('Mời bạn nhập triệu chứng bênh: ');

print(' - PHIẾU KHÁM BỆNH --- ');
print ('Tên bệnh nhân:', name_patient);
print('Tuổi:', age);
print ('Triệu chứng:', symptom);