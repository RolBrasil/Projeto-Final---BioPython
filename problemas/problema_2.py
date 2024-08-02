from bio.sequencia import Sequencia
from bio.organismo_fasta import OrganismoFasta
from bio.ler_fasta import ler_fasta
import os

diretorio_arquivo = os.path.join("arquivos", "Flaviviridae-genomes.fasta")

objetos_organismo = ler_fasta(diretorio_arquivo)

for organismo in objetos_organismo:
    print(f"Organismo: {organismo.id}")

    sequencia_translate = organismo.sequencia.traduzir()
    print(f"Sequência de proteína: {sequencia_translate}")

    print()
