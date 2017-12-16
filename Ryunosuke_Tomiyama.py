fuga = {1 : "aaa", 2: "bbb", 3: "ccc", 4: "ddd"}

def hoge (fuga):
    
    text = "【今日やったこと】 \n"
    text += fuga[1] + "\n"
    text += "【今日学んだこと】 \n"
    text += fuga[2] + "\n"
    text += "【明日行うこと】 \n"
    text += fuga[3] + "\n"
    text += "【次回までの課題】 \n"
    text += fuga[4] + "\n"
    return text
print(hoge (fuga))
