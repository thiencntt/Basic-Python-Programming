""" Tính tiền đi du lịch Phan Xi Păng
Để lên đỉnh Phan Xi Păng cần mua vé cáp treo a nghìn đồng/1 người lớn
                                          và b nghìn đồng/ 1 trẻ em
                              , vé xe lửa là u nghìn đồng/1 người lớn
                                          và v nghìn đồng/ 1 trẻ em.
Đoàn du lịch có x người, trong đó có y trẻ em.
Hãy xác định số tiền cần chuẩn bị để mua vé cho cả đoàn và đưa ra kết quả ra màn hình

Các dữ liệu a, b, u, v, x, y là các số nguyên không âm (y<=x)
Số tiền = a * (x-y) + u * (x-y) + b * y + v * y
        = (a + u) * (x - y) + (b + v) * y
"""
a = int(input("Hãy nhập giá vé cáp treo (người lớn):"))
b = int(input("Hãy nhập giá vé cáp treo (trẻ em):"))
u = int(input("Hãy nhập giá vé xe lửa (người lớn):"))
v = int(input("Hãy nhập giá vé xe lửa (trẻ em):"))
x = int(input("Hãy nhập số lượng người của đoàn du lịch:"))
y = int(input("Hãy nhập số lượng trẻ em trong đoàn du lịch:"))

tongtien = (a + u) * (x - y) + (b + v) * y
print("Tổng số tiền mà đoàn du lịch phải trả là: ", tongtien, " nghìn đồng")