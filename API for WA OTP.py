import json
import random as r
# function for otp generation
def otpgen():
    otp=""
    for i in range(5):
        otp+=str(r.randint(1,9))
    # print ("Your One Time Password is ")
    # print (otp)
    return otp
# print(otpgen())
data = otpgen()
# data = json.dumps(data)
data = {"OTP" : data}

print(json.dumps(data))