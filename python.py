

# bangcuuchuong = int(input("Bạn muốn hiện bảng cửu chương mấy?"))

# for x in range(1, 11):
#   print( bangcuuchuong, " x " , x , " = ",        bangcuuchuong * x)

chuoi = ""

for n in range(1, 11):
  for x in range(2, 10):
    chuoi += str(x) + " x " +  str(n) + " = " + str(n * x) + "\t"
  print(chuoi)
  chuoi = ""

