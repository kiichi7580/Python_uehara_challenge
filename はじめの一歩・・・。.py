# 1）自分の名前を出力

print("中里起一")

# 2）自分の名前・カタカナ・年齢を段に分けて出力

print("中里起一\nナカザトキイチ\n19歳")

# 3）自分の名前・体重・身長を出力し、それらを使ってその下にBMI値を出力

taiju = 60
sintyou = 1.65

print("中里起一\n" + str(taiju) + "kg\n" + str(sintyou * 100) + "cm")

BMI = taiju / (sintyou ** 2)
print(BMI)

# 4）12＋15＝出力し、その結果を次の段に出力

num = 12 + 15
print("12 + 15=\n" + str(num))

# 5）体重と体重を入力する欄を作り、その結果を出力 

taiju1 = int(input("体重を入力してください"))
sintyou1 = int(input("身長を入力してください"))

print(str(taiju1) + "kg")
print(str(sintyou1) + "cm")