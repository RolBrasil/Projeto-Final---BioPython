
from ler_fasta import ler_fasta
from constantes import DNA_PARA_AMINOACIDO 
from sequencia import Sequencia


def analisar_composicao_nucleotideos(arquivo):
    organismos = ler_fasta(arquivo)
  
    if organismos:
        for organismo in organismos:
            print("ID:", organismo.id)
            print("Nome:", organismo.nome)

            sequencia = Sequencia(organismo.sequencia)
            percentual_A = sequencia.calcular_percentual(["A"])
            percentual_T = sequencia.calcular_percentual(["T"])
            percentual_G = sequencia.calcular_percentual(["G"])
            percentual_C = sequencia.calcular_percentual(["C"])

            print("Percentual A:", percentual_A)
            print("Percentual T:", percentual_T)
            print("Percentual G:", percentual_G)
            print("Percentual C:", percentual_C)

    else:
        print("Nenhum organismo encontrado no arquivo.")


arquivo = "Flaviviridae-genomes.fasta"
analisar_composicao_nucleotideos(arquivo)