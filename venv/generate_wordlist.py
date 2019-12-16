
def read_file(file):
    new_list = []
    with open(file, "r") as f1:
        for line in f1:
            line = line.lower()
            new_list.append(line.split(None, 1)[0])
    return new_list


def write_list_to_file(from_file, to_file):
    write_list = read_file(from_file)
    f = open(to_file, 'a')
    for line in write_list:
        f.write("%s\n" % line)


def correct_list(from_file, to_file):
    unordered_list = read_file(from_file)
    f = open(to_file, "w")
    word_list = list(set(unordered_list))
    for i in word_list:
        f.write("%s\n" % i)


def regen_list():
    l1 = "ordlister/ordliste_aspell_nn.txt"
    l2 = "ordlister/ordliste_banneord.txt"
    l3 = "ordlister/ordliste_folkeeventyr.txt"
    l4 = "ordlister/ordliste_gamle_norske_fornavn.txt"
    l5 = "ordlister/ordliste_passord_topp_125.txt"
    l6 = "ordlister/ordliste_snl_datoer.txt"
    l7 = "ordlister/ordliste_snl_egennavn.txt"
    l8 = "ordlister/ordliste_snl_fellesord.txt"
    l9 = "ordlister/ordliste_ssb_norske_etternavn.txt"
    l10 = "ordlister/ordliste_ssb_norske_fornavn.txt"
    l11 = "ordlister/ordliste_aspell_en.txt"
    l12 = "ordlister/norske_scrabble_ord.txt"
    l13 = "ordlister/ordliste_aspell_no.txt"
    temp_file = "ordlister/temp_ordliste.txt"
    all_lists = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13]

    for i in all_lists:
        write_list_to_file(i, temp_file)

    correct_list(temp_file, "big_ordliste.txt")


if __name__ == '__main__':
    regen_list()