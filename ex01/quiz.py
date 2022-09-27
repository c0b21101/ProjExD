import random

def shutudai(mondai_lst):
    mondai = random.choice(mondai_lst)
    print("問題：" + mondai["q"])
    return mondai["a"]

def kaito(ans_lst):
    ans = input("答えるんだ：")
    if ans in ans_lst:
        print("正解！！！")
    else:
        print("出直してこい")

if __name__ == "__main__":
    mondai_lst = [
        {"q":"サザエの旦那の名前は？", "a":["マスオ","ますお"]},
        {"q":"カツオの妹の名前は？", "a":["ワカメ","わかめ"]},
        {"q":"タラオはカツオから見てどんな関係？", "a":["甥","おい","甥っ子","おいっこ"]},
    ]
    ans_lst = shutudai(mondai_lst)
    kaito(ans_lst)

