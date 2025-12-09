def create_codon_dict(file_path):
   
    file = open(file_path, "r")
    rows = file.readlines()
    file.close()

    codon_dict = {}

    for row in rows:
        row = row.strip()
        if row == "":
            continue

        cells = row.split('\t')
        codon = cells[0]
        amino_acid = cells[2]

        codon_dict[codon] = amino_acid

    return codon_dict



