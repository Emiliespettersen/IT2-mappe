#intro tester

logget_inn=False

if logget_inn:
    print("velkommen")
else:
    print("logg inn!!!")

#tester
##sammenligningsoperatorer
3>2  #større>mindre    større enn  "3>2  TRUE   5>6 FALSE"
3 >= 3 #større enn eller lik    "3>=3 TRUE"
2<3  #Mikndre enn   "2<3 TRUE"
4<=4 # mindre enn eller lik ""
1==1 #LIK "3=3 TRUE"
5!=2 #Ikke lik "2!=3"


print( 3!=2)#printer true i terminalen
resultatet_av_test = 42 == 12
print(resultatet_av_test)

#logisk operatorer
alder=71
yrke= "lærer"

alder> 70 and yrke =="lærer" # --> TRUE
alder< 70 or yrke =="lærer" # --> TRUE
  #FALSE         #TRUE
        #pga "or" så blir det TRUE
not alder> 70 #--> TRUE