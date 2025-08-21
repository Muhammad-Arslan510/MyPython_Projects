#------"Design and implement a Currency Converter application that allows the user to input an amount in Pakistani Rupees (PKR) and converts it into equivalent amounts in different international currencies-------------
print("From this list of countries, You can check the exchange rate of any currency")
countries={
    "1":"US Dollar(USD)",
    "2":"Euro(EUR)",
    "3":"British Pound (GBP)",
    "4":"Canadian Dollar (CAD)",
    "5":"Australian Dollar (AUD)",
    "6":"Saudi Riyal (SAR)",
    "7":"UAE Dirham (AED)",
    "8":"Turkish Lira (TRY)",
    "9":"Indian Rupee (INR)",
    "10":"Chinese Yuan (CNY)",
    "11":"Japanese Yen (JPY)",
    "12":"Swiss Franc (CHF)",
    "13":"Swedish Krona (SEK)",
    "14":"Norwegian Krone (NOK)",
    "15":"Danish Krone (DKK)"
}
print(countries)
print("Please Choose number from 1 to 15 ")
n=int(input("Enter Any Number From 1 to 15="))
if n==1:
    print("Pakistani Rupees to Us Dollars")
    def us_dollar(pkr):
        us_value=pkr/280
        print("Your Us Dollar is= ", us_value," USD")
    u=int(input("Enter Your Amount "))
    us_dollar(u)
    
elif n==2:
    print("Pakistani Rupees to  EURO")
    def euro(pkr):
        euro_value=pkr/300
        print("Yor Total Euro is= ",euro_value," EUR")
    e=int(input("Enter Any Amount= "))
    euro(e)

elif n==3:
    print("Pakistani Rupees to British Pound")
    def brit_pound(pkr):
        brit_value=pkr/350
        print("Your Total British Pound  Amount is= ",brit_value," GBP")
    b=int(input("Enter Any Amount= "))
    brit_pound(b)
elif n==4:
    print("Pakistani Rupees to Candian Dollar")
    def candian_dollar(pkr):
        candian_value=pkr/200
        print("Yout Total Candian dollar Amount  is= ",candian_value," CAD")
    c=int(input("Enter Any Amount= "))
    candian_dollar(c)
elif n==5:
    print("Pakistani Rupees to Australian Dollar")
    def australian_dollar(pkr):
        australian_value=pkr/185
        print("Your Total Australian Dollar Amount  is= ",australian_value," AUD")
    au=int(input("Enter Any Amount= "))
    australian_dollar(au)
elif n==6:
    print("Pakistani Rupees to Saudi Riyal")
    def Saudi_Riyal(pkr):
        Saudi_value=pkr/75
        print("Your Total Saudi Rayal Amount  is= ",Saudi_value," SAR")
    s=int(input("Enter Any Amount= "))
    Saudi_Riyal(s)
elif n==7:
    print("Pakistani Rupees to UAE Dirham")
    def UAE_Dirham(pkr):
        UAE_valu=pkr/76
        print("Your Total UAE Dirham Amount is= ",UAE_valu," AED")
    ua=int(input("Enter Any Amount= "))
    UAE_Dirham(ua)
elif n==8:
    print("Pakistani Rupees to Us Turkish Lira ")
    def Turkish_Lira(pkr):
        Turkish_value=pkr/10
        print("Your Total Turkish Lira Amount is= ",Turkish_value," TRY")
    t=int(input("Enter Any Amount= "))
    Turkish_Lira(t)
elif n==9:
    print("Pakistani Rupees to Indian Rupees")
    def Indian_Rupee(pkr):
        Indian_value=pkr/3.5
        print("Your Total Insdian Rupees Amount is= ",Indian_value," INR")
    I=int(input("Enter Any Amount= "))
    Indian_Rupee(I)
elif n==10:
    print("Pakistani Rupees to Chinese Yaun")
    def Chinese_Yuan(pkr):
        chinese_value=pkr/40
        print("Your Total Chinese Yaun Amount is= ",chinese_value," CNY")
    ch=int(input("Enter Any Amount= "))
    Chinese_Yuan(ch)
elif n==11:
    print("Pakistani Rupees to Japanese Yen")
    def Japanese_Yen(pkr):
        Japanese_Value=pkr/2
        print("Your Total Japanese Yen Amount is= ",Japanese_Value," JPY")
    J=int(input("Enter Any Amount= "))
    Japanese_Yen(J)
elif n==12:
    print("Pakistani Rupees to Swiss Franc ")
    def Swiss_Franc(pkr):
        Swiss_value=pkr/320
        print("Your Total Swiss Franc Amount  is= ",Swiss_value," CHF")
    s=int(input("Enter Any Amount= "))
    Swiss_Franc(s)
elif n==13:
    print("Pakistani Rupees to Swedish Krona")
    def Swedish_Krona(pkr):
        Swedish_value=pkr/26
        print("Your Total Swedish Korna Amount is= ",Swedish_value," SEK")
    S=int(input("Enter Any Amount= "))
    Swedish_Krona(S)
elif n==14:
    print("Pakistani Rupees to Norwegian Krone ")
    def Norwegian_Krone(pkr):
        Norwegian_value=pkr/27
        print("Your Total Norwegian Krone Amount  is= ",Norwegian_value," NOK")
    N=int(input("Enter Any Amount "))
    Norwegian_Krone(N)
elif n==15:
    print("Pakistani Rupees to Danish Krone ")
    def Danish_Krone(pkr):
        Danish_value=pkr/40
        print("Your Total Danish Krone  Amount is= ",Danish_value," DKK")
    d=int(input("Enter Any Amount= "))
    Danish_Krone(d)
else:
    print("Please Enter Only Menthoned Number")
