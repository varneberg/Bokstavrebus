
def read_file(file):
    new_list = []
    with open(file, "r") as f1:
        for line in f1:
            line = line.lower()
            new_list.append(line.split(None, 1)[0])
    return new_list


def write_list(from_file, to_file):
    words = read_file(from_file)
    f = open(to_file, 'a')
    for line in words:
        f.write("%s\n" % line)


def correct_list(from_file, to_file):
    unordered_list = read_file(from_file)
    f = open(to_file, "w")
    word_list = list(set(unordered_list))
    for i in word_list:
        f.write("%s\n" % i)


def regen_list():
    temp_file = "ordlister/temp_ordliste.txt"
    write_list("ordlister/ordliste_aspell_nn.txt", temp_file)
    write_list("ordlister/ordliste_banneord.txt", temp_file)
    write_list("ordlister/ordliste_folkeeventyr.txt",temp_file)
    write_list("ordlister/ordliste_gamle_norske_fornavn.txt", temp_file)
    write_list("ordlister/ordliste_snl_datoer.txt", temp_file)
    write_list("ordlister/ordliste_snl_egennavn.txt",temp_file)
    write_list("ordlister/ordliste_snl_fellesord.txt", temp_file)
    write_list("ordlister/ordliste_ssb_norske_etternavn.txt", temp_file)
    write_list("ordlister/ordliste_ssb_norske_fornavn.txt", temp_file)
    #write_list("ordlister/ordliste_aspell_en.txt", temp_file)
    write_list("ordlister/norske_scrabble_ord.txt", temp_file)
    write_list("ordlister/ordliste_aspell_no.txt", temp_file)



    correct_list(temp_file, "wordlist.txt")

def add_word(word):
    open("big_no_wordlist.txt")

if __name__ == '__main__':
    #a = input("Velg et alternativ: \n(1) Legg til nytt ord \n(2) Nullstill ordliste\n")

    #if a == 2:
    regen_list()
