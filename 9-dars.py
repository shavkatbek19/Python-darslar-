# mehmonlar = ['Ali', 'Vali', 'Soli', 'Anvar']

# print( 'Salom', mehmonlar[0])

# print('salom', mehmonlar[2])

# for mehmon in mehmonlar:
#     print('Salom', mehmon)
# mehmonlar.sort()

# for mehmon in mehmonlar:
#     print("Salom", mehmon)

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi")

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi\n")

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
# print("Hurmat bilan, Palonchiyevlar oilasi\n")

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
    
#     print(mehmonlar) # bu qator tsikl tashqarisida bo'lishi kerak edi

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
    
# print(mehmonlar)

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
# for son in sonlar:  # sonlar dagi har bir son uchun
#     sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = [] # bo'sh ro'yxat
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)
# kinolar = []
# print(input("5 ta kino nomi yozing"))

# for k in range(5):
#     kinolar.append(input(f"{k+1} - nomini yozing - "))
#     print(kinolar)

# sonlar = list(range(11,100,2))
# for son in sonlar:
#     print(son**3)

# ismlar = ['Ali', 'Soli', 'Vali',]

# for ism in ismlar:
#     print(f"Salom {ism} - bizning sahifamizga hush kelisan")
# print(f"Ismlar kodi {len(ism) } - marta takrorlandi ")

# # Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
# # va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# ismlar = ['Ali','Vali','Hasan','Husan','Olim']
# for ism in ismlar:
#     print(f"Assalom alaykum, {ism}. Sahifamizga xush kelibsiz!")

# # Yuoqirdagi tsikl tugaganidan so'ng, 
# # ekranga "Kod n marta takrorlandi" degan xabar chiqaring 
# # (n o'rniga kod necha marta takrorlanganini yozing)
# print(f"Kod {len(ismlar)} marta takrorlandi")

# # 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
# # Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# sonlar = list(range(11,100,2))
# for son in sonlar:
#     print(son**3)

# # Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
# # va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# kinolar = []
# print("5 ta sevimli kinoingiz qaysilar?")
# for k in range(5):
#     kinolar.append(input(f"{k+1}-kino:"))
# print(kinolar)    

# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
# ismlar = []
# for n in range(n_people):
#     ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
# print(ismlar)

sonlar = list(range(120,1200,2))
print(sonlar)
print(f"Saonlar uzunligi - {len(sonlar)}")
print(f" Sonlar yig'indisi {sum(sonlar)}")
print(f"En katta son {max(sonlar)}\n Eng kichik sonlar {min(sonlar)}")
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[530:540])