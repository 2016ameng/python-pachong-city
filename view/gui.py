from tkinter import *

#import city.model.mafeng.threadmfw as down
#import city.model.mafeng.processmfw as down
import city.model.mafeng.mfw as mafw
import city.model.tuniu.tuniu as tun
root = Tk() # 初始化Tk()
root.title("游记")    # 设置窗口标题
root.geometry('400x400+400+300')    # 设置窗口大小 注意：是x 不是*


def download():
    fa2.place(x=0, y=50) #触发事件时 显示frame place位置

def help():
    fa1.place(x=0, y=0)
def mfw():
    mafw.download1()  # 蚂蜂窝爬取文件对象
def tn():
    tun.download1()

menubar = Menu(root) #菜单栏

menubar1=Menu(menubar) #菜单
menubar2=Menu(menubar)
menubar3=Menu(menubar)

menubar1.add_command(label='文件爬取',command=download) #添加的是下拉菜单的菜单项 触发事件
menubar2.add_command(label='文件分析')
menubar3.add_command(label='帮助',command=help)

menubar.add_cascade(label='文件爬取',menu=menubar1) #menu 指明了要把那个菜单级联到该菜单栏上
menubar.add_cascade(label='文件分析',menu=menubar2)
menubar.add_cascade(label='帮助',menu=menubar3)

fa1 = Frame(root,height=50,width=400) #Frame就是屏幕上的一块矩形区域，多是用来作为容器
Label(fa1, text='点击文件爬取，选择途牛或者蚂蜂窝网站，开始爬取').pack()

v = IntVar() #创建一个Radiobutton组，并绑定到整型变量v
v.set(1)
fa2 = Frame(root,height=50,width=400)
Radiobutton(fa2,text='途牛',variable=v,value=1,command=tn).pack()
Radiobutton(fa2,text='蚂蜂窝', variable=v, value=2,command=mfw).pack()  #pack方法会让控件显示，并根据文本内容自动调节大小 command触发事件

fa3 = Frame(height=300,width=400,bg = 'black')
fa3.place(x=0,y=100)

root['menu'] = menubar # 最后可以用窗口的 menu 属性指定它的顶层菜单
root.mainloop() #让根窗口进入事件循环