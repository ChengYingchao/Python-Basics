age = input('please input your age:')
age = int(age)
if age <= 18:
    print('your age is ',age)
    print('teenager')
elif age >=50:
    print('your age is',age)
    print('old people')
else:
    print('your age is',age)
    print('adult')
if 86:
    print('ture')

#练习一：
height = 1.75
weight =80.5
bmi = weight/height**2
print("练习一：BMI指标是",bmi)
if bmi < 18.5:
    print("哈哈 你好瘦啊，该多吃多运动！")
elif 18.5<=bmi<25:
    print("太好了，你的身材好匀称，继续保持！")
elif 25<= bmi <28:
    print("过重，你还是要稍微控制一下饮食")
elif 28 <= bmi < 31:
    print("不行啊，太胖了，管住嘴，迈开腿，去吧")
else:
    print("哎呀，你这是病，得治疗，肥胖症，需要寻求医生的专业建议。")
