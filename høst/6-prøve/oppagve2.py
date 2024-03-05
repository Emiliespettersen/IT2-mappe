def main():
    ISO = input("Hva din fødselsdato i ISO format? ")
    norsk = norsk_standar (ISO)
    print (norsk)

def norsk_standar (ISO):
    tall, tall, tall = ISO.split()
    return  tall [0:1] + tall [2:3] + tall [4:7] 

main()


#Her hadde jeg tenk å splitte opp tallene slik at jeg bare kunne gjøre om rekkefølgen.
