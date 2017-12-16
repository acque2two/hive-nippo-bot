import datetime
YOUR_NAME = "(LINE NAME)"

print("%s さんの%sの日報" % (YOUR_NAME, datetime.datetime.now().date()))


message1 =input("今日のひとこと\n ")
message2 =input("本日学んだこと\n ")
message3 =input("明日やること\n ")
message4 =input("次回までの課題\n ")

print(message1+str("\n")+message2+str("\n")+message3+message4)
