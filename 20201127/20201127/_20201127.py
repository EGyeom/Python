
#20201127 Study
#String
food = "Python\'s favorite food is perl"
print(food)
food = "Python's favorite food is perl"
print(food)

#MultiLine
multiline = '''
Life is too short
you need python
'''

print(multiline)
print(food + multiline)
# length len(string)
print(len(food+ multiline))

# String Indexing & Slicing
# [start : end] include start to end -1 ( start <= String < end)
# [-1] Last word
print(food[0] + food[14] + food[16])
print(food[0:6] + food[:-1])

# example
a = "20201127Sunny"
date = a[:8]
weather = a[8:]
print("Date : " + date)
print("Weather : " + weather)

# example
a = "Pithon"
print("Wrong Word : " + a)
a = a[:1]+ "y" + a[2:]
print("Right Word : " + a )

#Formating
a = "I eat %d apples." %3
print(a)
a = "I eat %s apples." % "five"
print(a)

num = 3.1452
s = "five"
a = "I eat %s apples for %s days" % (num,s)
print(a)
# arrange %10s -> lenght 10
# -left {0:<10} , +right {0:>10}
# center {0:=^10} 가운데 정렬 후 나머지 '='로 채움
# %0.4f % 3.42134234 -> 3.4213

#using format()
a = "I eat {number:0.2f} apples for {days} days".format(number = num, days =s)
print(a)

#using f version 3.6 미만 사용 불가

name = "Gyeom"
age = 27

print(f'My name is {name}. My age is {age}.')
print(f'Next Year my age is {age+1}.')
#f'{"hi":<10} left , f'{"hi":>10} right , f'{"hi:^10} center
#using dictionary
d = {'name' : 'gyeom', 'age' : 27}
print(f'My name is {d["name"]}. My age is {d["age"]}.')

#fucntions

a = "Hello"
print(a.count('l'))
print(a.find('e')) # a.index 다른점은 index 함수는 오류 발생시킴
print(",".join(a))
#join using in tuple, list

print(",".join(['a','b','c','d']))
print(a.upper())
print(a.lower())

#공백 지우기 lstrip, rstrip, strip

#문자열 바꾸기
a = "Hello World"
a.replace("H", "h")
print(a)
b = a.split(" ")
print(b)
