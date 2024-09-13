
#* 检查是否不等
#* 要判断两个值是否不等，可使⽤不等运算符（!=）。
#* 下⾯使⽤⼀条 if 语句来演⽰如何使⽤不等运算符。
#* 我们将把顾客点的⽐萨配料（topping）存储在⼀个变量中，
#* 再打印⼀条消息，指出这名顾客点的配料是否是意式⼩银⻥（anchovies）
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

print("\n")

#* 数值⽐较
#* 检查数值⾮常简单。例如，下⾯的代码检查⼀个⼈是否是 18 岁：
age = 18
print(age == 18)

#* 还可以检查两个数是否不等。例如，下⾯的代码在提供的答案不正确时打印⼀条消息：
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

#* 条件语句可包含各种数学⽐较，如⼩于、⼩于等于、⼤于、⼤于等于：
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)