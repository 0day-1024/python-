'''
管理列表
在你创建的列表中，元素的排列顺序常常是⽆法预测的，因为你并⾮总能控制⽤户提供数据的顺序。
但你经常需要以特定的顺序呈现信息，Python 提供了很多管理列表的⽅式，可根据具体情况选⽤。
'''

#* 使⽤ sort() ⽅法对列表进⾏永久排序
#* Python ⽅法 sort() 让你能够较为轻松地对列表进⾏排序。
#* 假设你有⼀个汽⻋列表，并要让其中的汽⻋按字⺟顺序排列。
#* 为了简化这项任务，假设该列表中的所有值都是全⼩写的。
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars) #* sort() ⽅法能永久地修改列表元素的排列顺序。

print("\n")

#* 还可以按与字⺟顺序相反的顺序排列列表元素，只需向 sort() ⽅法传递参数 reverse=True 即可。
#* 先排序，再反转
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort(reverse=True)
print(cars) #* 同样，对列表元素排列顺序的修改也是永久的

print("\n")

#* 使⽤ sorted() 函数对列表进⾏临时排序
#* 要保留列表元素原来的排列顺序，并以特定的顺序呈现它们，可使⽤sorted() 函数。
#* sorted() 函数让你能够按特定顺序显⽰列表元素，同时不影响它们在列表中的排列顺序。
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

print("\n")

#* 注意，在调⽤ sorted() 函数后，列表元素的排列顺序并没有变。
#* 如果要按与字⺟顺序相反的顺序显⽰列表，也可向 sorted() 函数传递参数 reverse=True。
#* 先排序，再反转
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars, reverse=True))
print(cars)

#* 在并⾮所有的值都是全⼩写的时，按字⺟顺序排列列表要复杂⼀些。
#* 在确定排列顺序时，有多种解读⼤写字⺟的⽅式，此时要指定准确的排列顺序，可能会⽐这⾥所做的更加复杂。
print("\n")

#* 反向打印列表
#* 要反转列表元素的排列顺序，可使⽤ reverse() ⽅法。
#* 假设汽⻋列表是按购买时间排列的，可轻松地按相反的顺序排列其中的汽⻋
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() #* reverse() 不是按与字⺟顺序相反的顺序排列列表元素，只是反转列表元素的排列顺序
print(cars)

#* reverse() ⽅法会永久地修改列表元素的排列顺序，
#* 但可随时恢复到原来的排列顺序，只需对列表再次调⽤ reverse() 即可。
print("\n")

#* 确定列表的⻓度
#* 使⽤ len() 函数可快速获悉列表的⻓度。
#* Python 在计算列表元素数时从 1 开始，因此你在确定列表⻓度时应该不会遇到差⼀错误。
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))