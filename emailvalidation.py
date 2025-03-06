email = input("Enter the email :") # min character in email 6 g@g.com ya g@g.in
k,j,d=0,0,0
if len(email)>=6: #1
    if email[0].isalpha():#2
        if("@" in email) and (email.count("@")==1): #3
            v=email[-1] # v means verify .com and .in 
            if(email[-4:-1]+v==".com")^(email[-3:-1]+v==".in"): #4
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                          j=1
                    elif i.isdigit():
                        continue
                    elif i=="_"or i=="."or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("worng Email 5")
                else:
                    print("Right")
            else:
                print("worng email 4")
        else:
            print("worng email 3")
    else:
        print("worng email 2")
else:
    print("worng email 1")



# string code logic .com and .in ka check 
# v=email[-1]
# if(email[-4:-1]+v==".com")^(email[-3:-1]+v==".in"):
#     print("yes")
# else:
#     print("worng ")
