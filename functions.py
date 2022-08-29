def movieLang(lang):
   if(lang == "en"):
    return("Language is English")
   elif(lang == "es"):
    return("Language is spanish")
   else:
    return("General Language")

input_data=input("Enter movie language symbol: ")
print(movieLang(input_data))

    
