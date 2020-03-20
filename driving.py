country = input("請問您是哪國人： ")
age = int(input("請問您的年齡是？： "))

if country == "台灣":
    if age >= 18:
        print("恭喜您，可以考駕照了！")
    else:
        print("您還不能考駕照。")

elif country == "美國":
    if age >= 16:        
        print("恭喜您，可以考駕照了！")
    else:
        print("您還不能考駕照。")

else:
    print("沒有", country,"的考駕照資料。")