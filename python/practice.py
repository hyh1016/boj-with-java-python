# 여러 가지 도전해보는 페이지
li1 = [1, 2, 3]
li2 = li1
li3 = li1[:]
print(id(li1) == id(li2))
print(id(li1) == id(li3))