# （1）自分の名前を出力してください。

print("中里起一")

# （2）入力された名前から「こんにちは。◯◯さん」という文字列を出力してください。

name = input()
print("こんにちは。" + name + "さん")

# （3）ランダムに取り出した2つの数を掛け算してその答えを出力してください。
import random
a = random.randrange(10)
b = random.randrange(10)

print(a * b)

# （4）入力された2つの数値を足してその答えを出力してください。

x = int(input())
y = int(input())

print(x + y)