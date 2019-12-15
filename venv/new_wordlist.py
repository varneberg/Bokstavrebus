
def read():
    new_list = []
    liste1 = "ordliste/norske_scrabble_ord.txt"
    liste2= "ordliste/aspell.txt"
    liste4="ordliste/ordliste_banneord.txt/"
    liste5="venv/ordlister/ordliste_folkeeventyr.txt"
    liste6="venv/ordlister/ordliste_gamle_norske_fornavn.txt"
    liste7="venv/ordlister/ordliste_passord_topp_125.txt"
    liste8="venv/ordlister/ordliste_snl_datoer.txt"
    liste9="ordliste/"
    liste10="ordliste/"
    liste11="ordliste/"


    with open("wordlist.txt", "r") as f1:
        for line in f1:
            line = line.lower()
            new_list.append(line.split(None, 1)[0])
    return new_list

def write():
    list = read()

    with open('ordliste.txt', 'w') as f:
        for i in list:
            f.write("%s\n" % i)

print(write())