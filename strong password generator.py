
import string
import random
# set all the character in list 
s1=list(string.ascii_lowercase) #30%
s2=list(string.ascii_uppercase)#30%
s3=list(string.digits) # 20%
s4=list(string.punctuation) #20%

number_ch=input("Enter the number of the password :")

while True:
    try:
        number_ch=int(number_ch)
        if number_ch <6:
            print("Enter 6 character")
            number_ch=input("Enter the number of the password again :")
        else:
            break    
    except:
         number_ch=input("Enter the number of the password again the corect one  :")
   
# random character 
random.shuffle(s1) 
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


part1=round(number_ch*(30/100)) 
part2=round(number_ch*(20/100))
Password=[]
for i in range(part1):
    Password.append(s1[i])
    Password.append(s2[i])

for i in range(part2):
    Password.append(s3[i])
    Password.append(s4[i])

random.shuffle(Password)

Password="".join(Password[0:])
print(Password)