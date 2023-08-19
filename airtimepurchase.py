"""
PROJECT:
Write a code for telecommunication company whereby a user can perform the following operations
1) Purchade diffrent data plan 
2) Purchase data with extra value
3) Purchase data bundles
4) Purchase data on buisness plan 
"""

import time
nt=0
userinput = input("Enter MTN dialing code to proceed: ")
if userinput == "*312#":
    time.sleep(2)
    print("""
    1) Data Plans
    2) XtraValue(Data + Voice)
    3) Social Bundles
    4) Buisness plan
    """)
   
    usercode = input(">>> ")
    if usercode == "1":                                     
        time.sleep(2)
        print("""
        1) Daily
        2) Weekly
        3) Monthly
        """)
        userResponse = input(">>> ")
        time.sleep(2)
        if userResponse == "1":
             print("""
             1)N50 for 40MB
             2)N100 for 100MB
             3)N100 for IG YOUTUBE(daily)
                     """)
             code=input(">>>")
             if code=="1":
                 print("you have succesful purchased a N50 for 40MB daily data plan for 24hrs")
             elif code=="2": 
                print("you have succesful purchased a N100 for 100MB daily data plan for 24hrs") 
             elif code=="3":
                 print("you have succesful purchased a N100 for IG, YOUTUBE daily data plan for 24hrs") 
             else:
                 print("you have entered the wrong input")         
        elif userResponse=="2":
            time.sleep(1)
            print("""
            1) N300 for 350MB
            2) N500 for 750MB(2-week plan)
            3)N500 for 750MB +N500 Talktime(Val/14days)
            """)
            zip=input(">>> ")
            if zip=="1":
                time.sleep(1)
                print("you have succesful purchased N300 for 350MB weekly data plan for a period of 7days")
            elif zip=="2":
                print("you have succesful purchased N500 for 750MB 2 weeks data plan for a period of 14days")    
            elif zip=="3":
                print("you have succesful purchased N500 for 750MB weekly data plan for a period of 7days")  
            else:
                print("you have entered a wrong input") 
        elif userResponse=="3":
            time.sleep(1)
            print("""
            1) N1,000 For 1.5GB
            2) N1200 For 2GB
            3)1,500 For 3GB
            """)  
            zip_code=input(">>> ")
            if zip_code=="1":
                time.sleep(1)
                print("you have succesful purchased a  N1,000 For 1.5GB monthly data plan for a period of 30days")
            elif zip_code=="2":
                time.sleep(1)
                print("you have succesful purchased a  N1,200 For 2GB monthly data plan for a period of 30days")
            elif zip_code=="3":
                time.sleep(1)
                print("you have succesful purchased a  N1,500 For 3GB monthly data plan for a period of 30days")    
        else:
            print("you have selected a wrong input")          
    elif usercode=="2":
        time.sleep(1)
        print("""
        1) xtra talk
        2) xtradata
        3)eligible intl destination
        4)xtradata+
        """)
        xtra_value=input(">>> ")
        if xtra_value=="1":
           print("""
           1) Xtra Talk 200
           2) Xtra Talk 300
           3) Xtra Talk 500
           """)
           xtra_talk=input(">>> ")
           if xtra_talk=="1":
               time.sleep(1)
               print("you have succesful purchased a xtra talk 200 plan")  
           elif xtra_talk=="2":
               time.sleep(1)
               print("you have succesfully purchased a xtratalk 300 plan")
           elif xtra_talk=="3":
               time.sleep(1)
               print("you have succesfully purchased a xtra talk 500 plan")    
           else:
               print("you have selected a wrong input")  
        elif xtra_value=="2":   
             print("""
           1) XtraData 200
           2) XtraData 300
           3) XtraData 500
             """)  
             xtra_data=input(">>> ")
             if xtra_data=="1":
                 time.sleep(1)
                 print("you have succesful purchased a xtra data 200 plan")
             elif xtra_data=="2":
                 time.sleep(1) 
                 print("you have successfully purchased a xtra data 300 plan")  
             elif xtra_data=="3":
                 time.sleep(1)
                 print("you have succesfully purchased xtra data 500 plan")     
             else:
                 print("you have entered a wrong input")    
        else:
            print("you have entered a wrong input")         
    elif usercode=="3":
        time.sleep(1)
        print("""
        1) whatsapp
        2) facebook
        3) instagram
        4)tiktok
        """)
        social_bundle=input(">>> ")
        if social_bundle=="1":
            print("you have succesfully purchased a whatsapp data bundle")
        elif social_bundle=="2":
            print("you have succesfully purchased a facebook data bundle")  
        elif social_bundle=="3":
            print("you have succesfully purchased a instagram data bundle")  
        elif social_bundle=="4":
            print("you have succesfully purchased a tik tok data bundle")          
        else: 
            print("you have entered a wrong input")    
    elif usercode=="4":
        time.sleep(1)
        print("""
        1) Bizplus bundles &vas
        2) thrtvebundle&vas
        3) broadband bundles
        4) enterprise wifi bundles
        5) data coupon
        6) check balance
        """)
        buisness_plan=input(">>> ")
        if buisness_plan=="1":
            print("you have succesfully purchased a Bizplus bundles &vas data bundle")
        elif buisness_plan=="2":
            print("you have succesfully purchased a thrtvebundle&vas data bundle")  
        elif buisness_plan=="3":
            print("you have succesfully purchased a broadband bundles data bundle")  
        elif buisness_plan=="4":
            print("you have succesfully purchased a  enterprise wifi bundles data bundle") 
        elif buisness_plan=="5":
            print("you have succesfully purchased a  data coupon data bundle")     
        elif buisness_plan=="6":
            print("you have 350GB left ofyour data plan")          
        else:
            print("you have entered a wrong input") 
    else:
            print("you have entered a wrong input")           

else:
    print("Invalid Code") 
