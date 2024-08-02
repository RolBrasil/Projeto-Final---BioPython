
from ler_fasta import ler_fasta
from constantes import DNA_PARA_AMINOACIDO 
from sequencia import Sequencia




def traduzir_sequencias_proteinas(arquivo):
    organismos = ler_fasta(arquivo)
  
    if organismos:
        for organismo in organismos:
            print("ID:", organismo.id)
            print("Nome:", organismo.nome)

            sequencia = Sequencia(organismo.sequencia)
            sequencia_proteina = sequencia.traduzir()

            print("Sequência de Proteína:", sequencia_proteina)

    else:
        print("Nenhum organismo encontrado no arquivo.")


arquivo = "Flaviviridae-genomes.fasta"
traduzir_sequencias_proteinas(arquivo)