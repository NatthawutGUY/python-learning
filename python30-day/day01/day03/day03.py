print("Are slopes equal?", slope1 == slope2)

#. หา x ที่ทำให้ y = x² + 6x + 9 เป็น 0
for x in range(-10, 11):
    y = x**2 + 6*x + 9
    print(x, y)

# ตรวจสอบค่า x ที่ y = 0
x = -3
y = x**2 + 6*x + 9
print("When x =", x, ", y =", y)

# 5. ความยาวของ 'python' และ 'dragon' และ falsy comparison
print(len("python"))
print(len("dragon"))
print(len("python") < len("dragon"))

#ใช้ and ตรวจสอบ 'on'
print("on" in "python" and "on" in "dragon")

# 7. ตรวจสอบคำว่า jargon
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)

#8. ตรวจสอบว่าไม่มี 'on' ทั้งใน dragon และ python
print("on" not in "dragon" and "on" not in "python")

#9. แปลงความยาวของ python เป็น float และ string
length = len("python")

print(float(length))
print(str(length))

#10. ตรวจสอบเลขคู่
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    
#10. ตรวจสอบเลขคู่
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    
#12. เปรียบเทียบชนิดข้อมูล
print(type("10") == type(10))

#13. int('9.8') เท่ากับ 10 หรือไม่
# int('9.8') จะ Error

print(int(float('9.8')) == 10)

#14. คำนวณรายได้ต่อสัปดาห์
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

pay = hours * rate

print("Your weekly earning is", pay )

#15. คำนวณจำนวนวินาทีที่มีชีวิตอยู่
years = int(input("Enter number of years you have lived: "))

seconds = years * 365 * 24 * 60 * 60

print("You have lived for", seconds, "seconds.")

for i in range (1, 6):
    print( i, 1, i, i ** 2, i**3)
