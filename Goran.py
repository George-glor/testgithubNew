def f_1(text, alternative1, alternative2, alternative3, alternative4, correct_answer):
    print(text)
    print(alternative1)
    print(alternative2)
    print(alternative3)
    print(alternative4)

    svar = int(input(">"))
    if(svar == correct_answer):
        print("Good job")   
    else:
        print("wrong answer:(")

f_1('varfår kallas språket så?', '1.Namnet kommer från en reptil', '2.Namnet på språket kommer från BBC komediserie "Monty Pythons Flying Circus"', '3.Efternamnet på skaparen är Python', '4.vet ej', 2)
f_1('Vad ar är Python i TIOBE 2021-ränkingen?', '1. Tredje plats', '2. Andra plats', '3. Första plats', '4. Fjärde plats', 3)
f_1("Python's kärnfilosofi sammanfattas i dokumentet The Zen of Python (PEP 20). Vilket av dessa påståenden gäller inte Python's filosofi?", "1.Läsbarheten räknas", "2.Vackert är bättre än fult", "3.Det bästa är fiende till det goda", "4. Enkelt är bättre än komplex", 3)
f_1("Vad betyder 'unpythonic' i Python community?", "1. Kod med många fel", "2. Kod som är svår att förstå eller läsa", "3. Kod som skriven på ett annat programmeringsspråk", "4.  ", 2)