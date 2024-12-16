import sympy
import random

lk=15
#Generate the secret key. 
k=sympy.randprime(pow(2,lk),pow(2,lk+1))

m='Hello world, this is a new program.'


# initializing string 
test_str = "GeeksforGeeks"

# printing original string 
print("The original string is : " + str(m))

# using join() + ord() + format()
# Converting String to binary
res = ''.join(format(ord(i), '08b') for i in m)

# printing result 
print("The string after binary conversion : " + str(res))

res_arr=[]
for i in range(len(res)):
    res_arr.append(int(res[i]))


#res_arr=list(res)
#res_arr=list(map(int, res.split()))
print(len(res_arr))
p=[]
for i in range(len(res_arr)):
    p.append(random.randint(1,10)*k+res_arr[i])

a=3
lr=a*lk
r=[]
for i in range(len(res_arr)):
    r.append(random.randint(pow(2,lr), pow(2,lr+1)))
c=[]
for i in range(len(res_arr)):
    c.append(p[i]+k*r[i])

####Decryption

d=[]
for i in range(len(c)):
    d.append(c[i]%k)
print(d)

if d==res_arr:
    print('Encryption and Decryption successful')
else:
    print("Decryption Failure")