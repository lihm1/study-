
import easygui as eg
import sys
while 1:
    eg.msgbox("hi,欢迎大家进入第一个界面小游戏")
    msg="请问你希望学到什么呢？"
    title="小游戏互动"
    choices=["xuexi","hauhau","python","yinyue"]
    choice =eg.choicebox(msg,title,choices)
    eg.msgbox("你的选择是:"+str(choice),"结果")
    msg="你希望重新开始小游戏吗？"
    title="请选择"

    if eg.ccbox(msg,title):
        pass 
    else 
       sys.exit(0)