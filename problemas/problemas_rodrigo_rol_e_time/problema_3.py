from ler_fasta import ler_fasta
import os

def gerar_relatorio(resultados, arquivo_saida):
    with open(arquivo_saida, 'w') as f:
        for resultado in resultados:
            status_mutacao = "Presente" if resultado['mutacao_presente'] else "Não Presente"
            f.write(f"ID: {resultado['id']}, Mutação na posição 1000: {status_mutacao}\n")

def verificar_mutacao(sequencia, posicao, nucleotideo_original, nucleotideo_mutado):
    if len(sequencia) >= posicao:
        nucleotideo_na_posicao = sequencia[posicao - 1]  # Posições em Python são indexadas a partir de 0
        return nucleotideo_na_posicao == nucleotideo_mutado and nucleotideo_na_posicao != nucleotideo_original
    return False

def main():
    diretorio_arquivo = os.path.join("arquivos", "Flaviviridae-genomes.fasta")
    arquivo_relatorio = "relatorio_mutacao.txt"

    
    objetos_organismo = ler_fasta(diretorio_arquivo)
    
    resultados = []
    
    
    posicao_mutacao = 1000
    nucleotideo_original = 'A'
    nucleotideo_mutado = 'G'
    
    
    for organismo in objetos_organismo:
        print(f"Organismo: {organismo.id}")

       
        sequencia = organismo.sequencia
        nucleotideo_1000 = sequencia[999]  # Acesso direto ao nucleotídeo na posição 1000 (index 999)

        
        mutacao_presente = verificar_mutacao(sequencia, posicao_mutacao, nucleotideo_original, nucleotideo_mutado)

        if mutacao_presente:
            print("A mutação está presente na posição 1000.")
        else:
            print("A mutação não está presente na posição 1000.")
        
        
        resultados.append({
            'id': organismo.id,
            'mutacao_presente': mutacao_presente
        })
        print() 
    
    
    gerar_relatorio(resultados, arquivo_relatorio)
    print(f"Relatório gerado: {arquivo_relatorio}")

if __name__ == "__main__":
    main()
