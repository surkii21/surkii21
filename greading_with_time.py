import time
print('Jai Shree Ram')
s=int(time.strftime('%H'))
if(s<=10):
    print('Good morning')
elif(s<=12):
    print("GOod noon")
elif(s<=15):
    print('Good afternoon')
elif(s<=18):
    print('Good evening')
else:
    print('Good night')
