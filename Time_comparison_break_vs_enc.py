# we will suppose that we have known plaintext-ciphertext pair from the other program. 

import sympy
import random
import math
import time

file1 = open("Results_time_comparison.txt", "w+") 

for a in range(3,6):
    file1.write('a is '+ str(a)+ '\n')
    for lk in range(10,21):
        file1.write('lk= '+str(lk)+ '\n \n')
        
        file1.write("size of prime number in bits is "+str(lk)+ '\n')
        #Generate the secret key. 
        k=sympy.randprime(pow(2,lk-1),pow(2,lk))
        file1.write('secret key is '+str(k)+ '\n')
        m='In this paper, we shall learn to break cryptosystems.'


        # file1.writeing original string 
        #file1.write("The original string is : " + str(m))

        # using join() + ord() + format()
        # Converting String to binary
        res = ''.join(format(ord(i), '08b') for i in m)

        # file1.writeing result 
        #file1.write("The string after binary conversion : " + str(res))

        res_arr=[]
        for i in range(len(res)):
            res_arr.append(int(res[i]))


        #res_arr=list(res)
        #res_arr=list(map(int, res.split()))
        file1.write('The length of data in bits is: '+str(len(res_arr))+ '\n')


        ######################################################################################
        #   Encryption Starts from here 
        start_time_encryption=time.time()
        p=[]
        for i in range(len(res_arr)):
            p.append(random.randint(1,10)*k+res_arr[i])
        #file1.write(p)
        
        file1.write("value of a is "+str(a)+ '\n')
        lr=a*lk
        r=[]
        for i in range(len(res_arr)):
            r.append(random.randint(pow(2,lr), pow(2,lr+1)))
        c=[]
        for i in range(len(res_arr)):
            c.append(p[i]+k*r[i])

        #file1.write(c)
        end_time_encryption=time.time()
        
        ######################################################################################333
        # The break starts here. 
        # We suppose that we don't have the secret key k (prime number) and try to recover that. 

        start_time_break=time.time()
        cdash=[]
        #file1.write(c)
        for i in range(len(c)):
            if res_arr[i]==1:
                cdash.append(c[i]-1)
            else:
                cdash.append(c[i])
        file1.write("cdash formed + \n")
        #file1.write(cdash)
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
            #file1.write("for i="+str(i))
            #file1.write('kdash is '+str(kdash))
            #file1.write('cdash is '+str(cdash[i]))

            kdash=math.gcd(kdash, cdash[i])
            #file1.write("kdash is ")
            #file1.write(kdash)
            cd=arr_mod_d(cdash,kdash)
            #file1.write(cd)
            if cd==zero_c:
                break

        if cd==zero_c:
            file1.write("Break Successful \n")
            file1.write("Secret key is "+str(kdash)+ '\n')
        else:
            file1.write("Insufficient Data to Break the encryption + \n")

        end_time_break=time.time()







        # we observe that secret key is same as calculated.

        ####Decryption
        start_time_decryption=time.time()
        d=[]
        for i in range(len(c)):
            d.append(c[i]%k)
        #file1.write(d)

        if d==res_arr:
            file1.write('Encryption and Decryption successful \n ')
        else:
            file1.write("Decryption Failure \n ")

        end_time_decryption=time.time()




        file1.write("\n \n \n ")
        file1.write(' For lk= '+str(lk)+ 'and a ='+ str(a)+ '\n')
        file1.write("Time taken in encryption of text is \n")
        file1.write(str((end_time_encryption-start_time_encryption)*1000000)+"\n")

        file1.write("Time taken to recover secret key is \n")
        file1.write(str((end_time_break-start_time_break)*1000000)+"\n")

        file1.write("Time taken in decryption \n")
        file1.write(str((end_time_decryption-start_time_decryption)*1000000)+ '\n')

        file1.write('\n \n \n ')


file1.close()
