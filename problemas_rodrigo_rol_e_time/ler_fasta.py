class OrganismoFasta:
    def __init__(self, id, nome, sequencia):
        self.id = id
        self.nome = nome
        self.sequencia = sequencia

def ler_fasta(arquivo):
    organismos = []
    with open(arquivo) as file:
        id = ""
        nome = ""
        sequencia = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if id:
                    organismos.append(OrganismoFasta(id, nome, sequencia))
                    id = ""
                    nome = ""
                    sequencia = ""
                id, nome = line[1:].split(None, 1)
            else:
                sequencia += line
        if id:
            organismos.append(OrganismoFasta(id, nome, sequencia))
    return organismos