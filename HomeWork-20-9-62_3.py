#3.โปรแกรมรับข้อมูลชื่อ นามสกุล จากนั้นให้แยกชื่อและนามสกุลออกจากกัน และแสดงจำนวนอักขระของชื่อและนามสกุล
#input รับค่าชื่อและนามสกุลเข้ามาทางแป้นพิมพ์
#process ใช้คำสั่ง len เพื่อวัดความยาวของตัวอักษรว่ามีกี่ตัว
#Define of variable กำหนดให้ข้อมูลทั้งหมดที่รับเข้ามาเป็น str หรือตัวอักษร
name,surname =(str(e) for e in input("NAME AND SURNAME :").split())
#output เมื่อทำขั้นตอน process แล้วจะได้ output แล้วแสดงข้อมูลออกทางหน้าจอด้วยคำสั่ง print
print("NAME =", len(name),"SURNAME =", len(surname))







