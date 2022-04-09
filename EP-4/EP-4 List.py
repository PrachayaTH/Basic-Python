Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
friend = []
friend.append('somsri')
print(friend)
['somsri']
friend.append('somsak')
print(friend)
['somsri', 'somsak']
friend.append('somchai')
print(friend)
['somsri', 'somsak', 'somchai']
print(friend[0])
somsri
friend.insert(0,'sompong')
print(friend)
['sompong', 'somsri', 'somsak', 'somchai']
friend.insert(2,'somkiat') #การเพิ่มชื่อระหว่างค่าต่าง ๆ
print(friend)
['sompong', 'somsri', 'somkiat', 'somsak', 'somchai']
#ย้าย somsak มาไว้หน้าสุด
friend.insert(0, friend.pop(3) ) #การย้ายชื่อ somsak
print(friend)
['somsak', 'sompong', 'somsri', 'somkiat', 'somchai']
#การลบ somchai ออกจากลิส
friend.remove('somchai')
print(friend)
['somsak', 'sompong', 'somsri', 'somkiat']
print(friend.remove('somkiat'))
None
print(friend)
['somsak', 'sompong', 'somsri']
print(friend.pop(2))
somsri
print(friend)
['somsak', 'sompong']
type(friend)
<class 'list'>
teacher = ('Korkai','Khorkai','korkwai')
type(teacher)
<class 'tuple'>
#tuple คือข้อมูลที่สมบูรณ์หรือไม่มีการแก้ไขแล้ว



vocab = {'cat':'แมว','dog':'หมา','pig':['หมู','สุกร']}
print(vocab['pig'])
['หมู', 'สุกร']
print(vocab['pig'][0])
หมู
print(vocab['pig'][1])
สุกร
