import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(7./100)
slowprint("stel je voor...")
slowprint("het is 1989 en je bent 16 jaar oud.")
slowprint("de Sovjet-Unie is net uit jullie land vertrokken en er is al een tijd een burgeroorlog gaande.")
slowprint("je zit ziek thuis terwijl je moeder je broertje en zusje naar school brengt.")
slowprint("opeens komt je vader binnen en zegt dat je je spullen moet inpakken en dat jullie moeten vertrekken.")
slowprint("je luistert naar je vader en pakt je favoriete knuffel in samen met essentiële spullen.")
slowprint("hij loopt met je naar de deur terwijl jij schreewt dat jullie moeten wachten op de rest van de familie.")

antwoord1 = input ("je vader zegt dat er geen tijd is om te wachten en dat je moet meegaan. wat kies jij? ")

if antwoord1.lower()== "meegaan" or antwoord1.lower()=="1":
    slowprint("")
    slowprint("je loopt met je vader je dorp uit, weg van huis.")
    slowprint("je bent nog steeds in de war waarom jullie moesten vertrekken van jullie huis. ")
    slowprint("jullie komen aan bij een controlepost.")
    slowprint("er wordt jullie gevraagd aan wie onze leider is.")
    slowprint("je vader zegt dat Maulana Samiul Haq zijn vader is, terwijl je die naam helemaal niet kent.")
    

    antwoord2 = input("zal je de waarheid vertellen aan de vreemdelingen, of vertrouw je je vader en lieg je met hem mee? ")

    if antwoord2.lower()=="liegen" or antwoord2.lower()=="1":
        slowprint("")
        slowprint("je zegt de zelfde naam als dat je vader zei, en loopt door de controlepost naar de andere kant.")
        slowprint("je loopt naar een kraan en vult je fles met water uit de kraan.")
        slowprint("een zwangere vrouw komt naar je toe en vraagt of je hier alleen bent.")
        slowprint("je zegt dat je hier met je vader bent terwijl je vader op dat moment achter je komt staan.")
        slowprint("'wij gaan proberen naar Libanon te komen met paard en wagen, we hebben nog wat plek over als jullie mee willen gaan' zegt de vrouw.")
        slowprint("'dat hoeft niet, wij kunnen makkelijk zelf lopen' zegt je vader.")

        antwoord3 = input("ben je het daar mee eens? wil je helemaal door de woestijn lopen? of ga je liever met hun mee? ")
    
        if antwoord3.lower()=="meegaan" or antwoord3.lower()=="2":
         slowprint("")
         slowprint("je zegt dat je moe bent en dat je liever met de wagen wil.")
         slowprint("je vader klimt in de wagen en gaat naast je zitten.")
         slowprint("jullie gaan met een groep mensen door de woestijn op weg naar Libanon.")
         slowprint("")
         slowprint("tijdens jullie reis zegt de jongen naast jou iets tegen je.")
         naam = input ("hey, ik ben Ali hoe heet jij? ")
         slowprint("'leuk je te ontmoeten "+ naam + "' zegt Ali.")
         
         antwoord4 = input("wil je misschien wat brood? het ziet er naar uit dat we nog lang met elkaar zitten. ")

         if antwoord4.lower()=="ja" or antwoord4.lower()=="1":
          slowprint("ali geeft de helft van zijn brood terwijl hij vriendelijk lacht.")
          slowprint("'ik hoop dat er geen oorlog is waar we naartoe gaan, ik heb al dagen niet veilig kunnen slapen' zegt Ali.")
          slowprint("'ons dorp is net aangevallen, ik weet niet eens waar de rest van mijn familie is' zeg je.")
          slowprint("er volgt een ongemakkelijke stilte.")
          antwoord5 = input("'heb je het koud?' zegt je vader")

          if antwoord5.lower()=="ja":
           slowprint("")
           slowprint("")
           slowprint("")
           slowprint("")

          elif antwoord5.lower()=="nee":
            slowprint("")
            slowprint("")
            slowprint("")
            slowprint("")


          

         elif antwoord4.lower()=="nee" or antwoord4.lower()=="2":
          slowprint("'dat is oké, ik kan begrijpen als je me niet vertrouwt' zegt hij.")
          slowprint("")
          slowprint("")
          slowprint("")

        elif antwoord3.lower()=="lopen":
         slowprint("")
         slowprint("")
         slowprint("")
         slowprint("")

         antwoord = input("")

    elif antwoord2.lower()=="waarheid" or antwoord2.lower()=="2":
        slowprint("")
        slowprint("je zegt dat je die naam helemaal niet kent.")
        slowprint("je vader kijkt je aan met een geschrokken blik.")
        slowprint("'oke...jullie weten wat je moet doen' zegt een van de bewakers daar.")
        slowprint("jullie worden in een truck gestopt met andere mensen en twee gewapende mannen.")
        slowprint("je wordt uit de auto gesleurd en weg getrokken van je vader.")
        antwoord3 = input("je ziet je vader een zak over zijn hoofd krijgen, wat ga je doen?(kies schreeuwen of duwen) ")

        if antwoord3.lower()=="schreewen" or antwoord3.lower()=="1": #einde 3 van de 5
         slowprint("")
         slowprint("je schreewt je vader je vader zijn naam.")
         slowprint("je vader probeert zich los te worstelen van de gewapende mannen maar faalt.")
         slowprint("je begint te huilen en schreeuwen naar je vader terwijl hij in een lijn naast andere mannen wordt gezet.")
         slowprint("er staan wapens op hem en de andere mannen gericht.")
         slowprint("je kijkt naar het laatste beeld van je vader en doet je ogen dicht.")
         slowprint("schoten worden gelost en je laat een schreeuw van wanhoop horen.")
         slowprint("je draait je om de horrors te zien...")
         slowprint("je vader ligt op de grond naast andere mannen.")
         slowprint("je schreewt je longen uit over wat je ziet.")
         slowprint("je hoort meer schoten komen van over de berg.")
         slowprint("de gewapende mannen worden doodgeschoten en je hoort geroep achter de bergen.")
         slowprint("de mannen die jou en andere kinderen en vrouwen vasthielden worden naast je neergeschoten.")
         slowprint("je ziet soldaten op jullie af komen en enige gevaren te neutraliseren.")
         slowprint("je rent naar ze vader om te kijken of hij nog leeft.")
         slowprint("'papa...papa sta op...' zeg je droevig.")
         slowprint("een soldaat loopt naar je toe en voelt zijn pols.")
         slowprint("hij kijkt je bedroeft aan een neemt je in zijn armen.")
         slowprint("hij draagt je naar een truck en plaats je naast wat andere kinderen.")
         slowprint("de truck rijd weg, ergens naar een veilige plek.")

         antwoord4 = input("")

        elif antwoord3.lower()=="duwen" or antwoord3.lower()=="2": #einde 2 van de 5
          slowprint("")
          slowprint("je duwt de vreemdelingen die je vast hielden weg.")
          slowprint("je rent naar je vader toe en geeft hem een knuffel omdat je weet dat het misschien je laatste kans is.")
          slowprint("je wordt weer weg getrokken van hem terwijl hij wordt geslagen en geschopt.")
          slowprint("je begint te huilen en schreeuwen naar je vader terwijl hij in een lijn naast andere mannen wordt gezet.")
          slowprint("er staan wapens op hem en de andere mannen gericht.")
          slowprint("je kijkt naar het laatste beeld van je vader en doet je ogen dicht.")
          slowprint("schoten worden gelost en je laat een schreeuw van wanhoop horen.")
          slowprint("je draait je om de horrors te zien...")
          slowprint("maar je ziet je vader in verbazing kijken.")
          slowprint("de gewapende mannen zijn doodgeschoten en je hoort geroep achter de bergen.")
          slowprint("de mannen die jou en andere kinderen en vrouwen vasthielden worden naast je neergeschoten.")
          print("je ziet soldaten op jullie af komen en enige gevaren te neutraliseren.")
          print("ze nemen jullie mee naar een veilige plek, waar jullie verzorgd zullen worden.")

elif antwoord1.lower() == "wachten" or antwoord1.lower()=="2": #einde 1 van de 5
    slowprint("")
    slowprint("je zegt dat je gaat wachten op je familie...")
    slowprint("je vader kijkt je bedroefd aan en geeft je een kus op je voorhoofd.")
    slowprint("hij loopt de deur uit en sluit hem achter zich.")
    slowprint("een uur later hoor je geruis beneden en rent naar beneden.")
    slowprint("het blijkt niet je familie niet te zijn...maar de taliban die komt binnenstormen.")
    slowprint("ze nemen je ergens mee...waar je nooit meer gevonden zal worden...")