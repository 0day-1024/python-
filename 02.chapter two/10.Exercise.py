'''
练习 2.11：添加注释 
选择你编写的两个程序，在每个程序中⾄少添加⼀条注释。
如果程序太简单，实在没有什么需要说明的，就在程序⽂件开头加上你的姓名和当前⽇期，再⽤⼀句话阐述程序的功能。
'''
full_name = "ada lovelace"

#* 使⽤ f 字符串可以完成很多任务，如利⽤与变量关联的信息来创建完整的消息
print(f"Hello, {full_name.title()}!")

#* 还可以使⽤ f 字符串来创建消息，再把整条消息赋给变量
message = f"Hello, {full_name.title()}!"
print(message)
