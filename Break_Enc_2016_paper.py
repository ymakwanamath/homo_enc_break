# we will suppose that we have known plaintext-ciphertext pair from the other program. 

import sympy
import random
import math
import time

lk=10
print("size of prime number in bits is "+str(lk))
#Generate the secret key. 
k=sympy.randprime(pow(2,lk),pow(2,lk+1))
print('secret key is '+str(k))
m='In this paper, we shall learn to break cryptosystems.'


# printing original string 
#print("The original string is : " + str(m))

# using join() + ord() + format()
# Converting String to binary
res = ''.join(format(ord(i), '08b') for i in m)

# printing result 
#print("The string after binary conversion : " + str(res))

res_arr=[]
for i in range(len(res)):
    res_arr.append(int(res[i]))


#res_arr=list(res)
#res_arr=list(map(int, res.split()))
print('The length of data in bits is: '+str(len(res_arr)))


######################################################################################
#   Encryption Starts from here 
start_time_encryption=time.time()
p=[]
for i in range(len(res_arr)):
    p.append(random.randint(1,10)*k+res_arr[i])
#print(p)
a=3
print("value of a is "+str(a))
lr=a*lk
r=[]
for i in range(len(res_arr)):
    r.append(random.randint(pow(2,lr), pow(2,lr+1)))
c=[]
for i in range(len(res_arr)):
    c.append(p[i]+k*r[i])

#print(c)
end_time_encryption=time.time()
####Decryption
start_time_decryption=time.time()
d=[]
for i in range(len(c)):
    d.append(c[i]%k)
#print(d)

if d==res_arr:
    print('Encryption and Decryption successful')
else:
    print("Decryption Failure")

end_time_decryption=time.time()
######################################################################################333
# The break starts here. 
# We suppose that we don't have the secret key k (prime number) and try to recover that. 

start_time_break=time.time()
cdash=[]
#print(c)
for i in range(len(c)):
    if res_arr[i]==1:
        cdash.append(c[i]-1)
    else:
        cdash.append(c[i])
print("cdash formed")
#print(cdash)
def arr_mod_d(arr,kd):
    new_arr=[]
    for i in range(len(arr)):
        new_arr.append(arr[i]%kd)
    return(new_arr)

zero_c=[]
for i in range(len(c)):
    zero_c.append(0)
kdash=cdash[0]
for i in range(1,len(c)):
    #print("for i="+str(i))
    #print('kdash is '+str(kdash))
    #print('cdash is '+str(cdash[i]))

    kdash=math.gcd(kdash, cdash[i])
    #print("kdash is ")
    #print(kdash)
    cd=arr_mod_d(cdash,kdash)
    #print(cd)
    if cd==zero_c:
        break

if cd==zero_c:
    print("Break Successful")
    print("Secret key is "+str(kdash))
else:
    print("Insufficient Data to Break the encryption")

end_time_break=time.time()
# we observe that secret key is same as calculated.

print("Time taken in encryption of text is ")
print(end_time_encryption-start_time_encryption)

print("Time taken to recover secret key is ")
print(end_time_break-start_time_break)

print("Time taken in decryption")
print(end_time_decryption-start_time_decryption)