print("stel je voor...")
print("het is 1989 en je bent 16 jaar oud.")
print("de Sovjet-Unie is net uit jullie land vertrokken en er is al een tijd een burgeroorlog gaande.")
print("je zit ziek thuis terwijl je moeder je broertje en zusje naar school brengt.")
print("opeens komt je vader binnen en zegt dat je je spullen moet inpakken en dat jullie moeten vertrekken.")
print("je luistert naar je vader en pakt je favoriete knuffel in samen met essentiële spullen.")
print("hij loopt met je naar de deur terwijl jij schreewt dat jullie moeten wachten op de rest van de familie.")

antwoord1 = input ("je vader zegt dat er geen tijd is om te wachten en dat je moet meegaan. wat kies jij? ")

if antwoord1.lower()== "meegaan":
    print("")
    print("je loopt met je vader je dorp uit, weg van huis.")
    print("je bent nog steeds in de war waarom jullie moesten vertrekken van jullie huis. ")
    print("jullie komen aan bij een controlepost.")
    print("er wordt jullie gevraagd aan wie onze leider is.")
    print("je vader zegt dat Maulana Samiul Haq zijn vader is, terwijl je die naam helemaal niet kent.")
    

    antwoord2 = input("zal je de waarheid vertellen aan de vreemdelingen, of vertrouw je je vader en lieg je met hem mee? ")

    if antwoord2.lower()=="liegen":
        print("")
        print("je zegt de zelfde naam als dat je vader zei, en loopt door de controlepost naar de andere kant.")
        print("je loopt naar een kraan en vult je fles met water uit de kraan.")
        print("een zwangere vrouw komt naar je toe en vraagt of je hier alleen bent.")
        print("je zegt dat je hier met je vader bent terwijl je vader op dat moment achter je komt staan.")
        print("'wij gaan proberen naar Libanon te komen met paard en wagen, we hebben nog wat plek over als jullie mee willen gaan' zegt de vrouw.")
        print("'dat hoeft niet, wij kunnen makkelijk zelf lopen' zegt je vader.")

        antwoord3 = input("ben je het daar mee eens? wil je helemaal door de woestijn lopen? of ga je liever met hun mee? ")
    
        if antwoord3.lower()=="meegaan":
         print("")
         print("je zegt dat je moe bent en dat je liever met de wagen wil.")
         print("je vader klimt in de wagen en gaat naast je zitten.")
         print("jullie gaan met een groep mensen door de woestijn op weg naar Libanon")
         print("")
         print("tijdens jullie reis zegt de jongen naast jou iets tegen je")
         naam = input ("hey, ik ben Ali hoe heet jij? ")
         print("leuk je te ontmoeten "+ naam)
         
         antwoord4 = input("wil je misschien wat brood? het ziet er naar uit dat we nog lang met elkaar zitten. ")

         if antwoord4.lower()=="ja":
          print("ali geeft de helft van zijn brood terwijl hij vriendelijk lacht.")
          print("")
          print("")
          print("")

         if antwoord4.lower()=="nee":
          print("")
          print("")
          print("")
          print("")

        elif antwoord3.lower()=="lopen":
         print("")
         print("")
         print("")
         print("")

         antwoord = input("")

    elif antwoord2.lower()=="waarheid":
        print("")
        print("je zegt dat je die naam helemaal niet kent.")
        print("je vader kijkt je aan met een geschrokken blik.")
        print("'oke...jullie weten wat je moet doen' zegt een van de bewakers daar.")
        print("jullie worden in een truck gestopt met andere mensen en twee gewapende mannen")

        antwoord3 = input("")

elif antwoord1.lower() == "wachten": #einde 1 van de 4
    print("")
    print("je zegt dat je gaat wachten op je familie...")
    print("je vader kijkt je bedroefd aan en geeft je een kus op je voorhoofd.")
    print("hij loopt de deur uit en sluit hem achter zich.")
    print("een uur later hoor je geruis beneden en rent naar beneden.")
    print("het blijkt niet je familie niet te zijn...maar de taliban die komt binnenstormen")
    print("ze nemen je ergens mee...waar je nooit meer gevonden zal worden...")