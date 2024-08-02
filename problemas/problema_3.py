from bio.sequencia import Sequencia
from bio.organismo_fasta import OrganismoFasta
from bio.ler_fasta import ler_fasta
import os

diretorio_arquivo = os.path.join("arquivos", "Flaviviridae-genomes.fasta")

objetos_organismo = ler_fasta(diretorio_arquivo)

for organismo in objetos_organismo:
    print(f"Organismo: {organismo.id}")

    sequencia = organismo.sequencia
    nucleotideo_1000 = sequencia.nucleotideos[999]
    mutacao_presente = False
    
    if nucleotideo_1000 == "G":
        mutacao_presente = True

    if mutacao_presente:
        print("A mutação está presente na posição 1000.")
    else:
        print("A mutação não está presente na posição 1000.")
    
    print()
