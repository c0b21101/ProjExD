import random
from site import abs_paths
import time
from re import A
from tracemalloc import start
from turtle import end_fill

all_alphabet = 26
target_chars = 10
defect_chars = 2
try_chars = 2

def shutudai(alphabet):
    #全アルファベットから、対象文字をランダムに10文字選ぶ
    all_chars = random.sample(alphabet, target_chars)
    print('対象文字', end="")
    for a in sorted(all_chars):
        print(a, end=" ")
    print()

    # 対象10文字から、欠損文字をランダムに2文字選ぶ
    abs_chars = random.sample(all_chars, defect_chars)
    print("表示文字：", end="")
    for a in all_chars: 
        if a not in abs_chars: # 欠損文字でなかったら表示
            print(a, end=" ")
    print()
    print("デバッグ用欠損文字：", abs_chars)
    return abs_chars

def kaito(seikai):
    ans = int(input("欠損文字はいくつあるでしょうか？："))
    if ans != defect_chars:
        print("不正解です")
    else:
        print("正解です. それでは、具体的に欠損文字を1つずつ入力してください")
        for i in range(ans):
            a = input(f"{i+1}文字目を入力してください：")
            if a not in seikai:
                print("不正解です.　またチャレンジしてください：")
                return False
            else:
                seikai.remove(a)
        else:
            print("欠損文字も含めて完全正解です！！")
            return True
    return False

if __name__ == "__main__":
    start = time.time()
    alphabet = [chr(i + 65) for i in range(all_alphabet)]
    print(alphabet)

    for i in range(try_chars):
        abs_chars = shutudai(alphabet)
        ans = kaito(abs_chars)
        if ans:
            break
        else:
            print("::"*20)
    end = time.time()
    print(f"経過時間：{(end-start):.2f}秒")