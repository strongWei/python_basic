#!/bin/python
# 6-8 exercise
# @author strong
# @email 1025155365@qq.com

pet1 = {
    "type":"type1",
    "belong":"strong"
}
pet2 = {
    "type":"type2",
    "belong":"ken"
}
pet3 = {
    "type":"type3",
    "belong":"hello"
}

pets = {
    "pet1":pet1,
    "pet2":pet2,
    "pet3":pet3
}
print(pets)
for name,petInfo in pets.items():
    print(name + '\n')
    for key,value in petInfo.items():
        print('\t' + key + ':' + value + '\n')
