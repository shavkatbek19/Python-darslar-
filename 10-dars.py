# son = float(input("Juft son kiriting: "))
# if son%2:
#     print('Bu son juft emas.')
# else:
#     print("Rahmat!")

#2-Topshiriq
# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0;
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")

# #3-topshiriq

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# #4-topshiriq

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []

# for n in range(5):
#     savat.append(input(f"savatga {n+1} maxsulotni qo'shing >>> "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f" Do'konimizda {mahsulot} mahsulot bor")
#     else:
#         print(f"Do'konimizda {mahsulot} mahsulot yo'q")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# users = ['alisher','aziza','yasina','umar']

# login = input("Yangi login tanlang: ")

# if login in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")

# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")

print(3*'7')
print('abc' > 'bcd')