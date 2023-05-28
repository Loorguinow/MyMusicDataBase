def remove_element(dico, element):
    new_dico = {}
    for el in dico:
        if el != element:
            new_dico[el] = dico[el]
    dico = new_dico

def print_dico(dico):

    print("="*20)
    lendico = len(dico)
    cpt = 0
    for el in dico:
        cpt += 1
        if el != "":
            print(f"{el} - {dico[el]}")
            if cpt < lendico:
                print("-"*20)

    print("="*20)
