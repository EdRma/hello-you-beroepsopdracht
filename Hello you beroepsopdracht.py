print("stel je voor...")
print("je bent thuis omdat je ziek was terwijl je moder je broertje en zusje naar school brengt.")
print("je zit op de vloer te spelen met je speelgoed...")
print("opeens komt je vader binnen en zegt dat je je spullen moet inpakken en dat jullie moeten vertrekken.")
print("je luistert naar je vader en pakt je favoriete knuffel in samen met essentiële spullen.")
print("hij loopt met je naar de deur terwijl jij schreewt dat ze moeten wachten op de rest van de familie.")

antwoord1 = input ("je vader zegt dat er geen tijd is om te wachten en dat je moet meegaan. wat kies jij?  ")

if antwoord1.lower()== "meegaan":
    print("je gaat naar beneden om een broodje te maken en op je ipad te kijken of er nog iets is gebeurd")
    antwoord2 = input("ga je nu douchen of je spullen inpakken? typ D of S: ")

    if antwoord2.lower()=="D":
        print("je stapt onder de douche en kleed je daarna aan")
        print("je loopt naar het station maar bent erachter gekomen dat je hem hebt gemist hierdoor zal je telaat komen en is nu het spel voorbij")

    elif antwoord2.lower()=="S":
        print("je pakt je spullen in en kleed je aan omdat het al bijna 8 uur is")
        print("je loopt naar de trein en stapt in onderweg naar amsterdam sloterdijk")
        print("je komt aan op amsterdam slooterdijk en loopt naar het mediacollege")
        print("je hebt het optijd gehaald en dus het spel gewonnen")



elif antwoord1.lower() == "wachten":
    print("je zegt dat je gaat wachten op je familie...")
    print("je vader kijkt je bedroefd aan en geeft je een kus op je voorhoofd.")
    print("hij loopt de deur uit en sluit hem achter zich.")
    print("een uur later hoor je geruis beneden en rent naar beneden.")
    print("het blijkt niet je familie niet te zijn...maar de taliban die komt binnenstormen")
    print("ze nemen je ergens mee...waar je nooit meer gevonden zal worden...")