
class Sequencia:
    def __init__(self, sequencia):
        self.sequencia = sequencia

    def complementar(self):
        complemento = {"A": "T", "T": "A", "C": "G", "G": "C"}
        nova_sequencia = "".join(complemento[base] for base in self.sequencia)
        return Sequencia(nova_sequencia)

    def complementar_reversa(self):
        complemento_reverso = {"A": "T", "T": "A", "C": "G", "G": "C"}
        nova_sequencia = "".join(complemento_reverso[base] for base in self.sequencia[::-1])
        return Sequencia(nova_sequencia)

    def transcrever(self):
        transcricao = {"A": "U", "T": "A", "C": "G", "G": "C"}
        nova_sequencia = "".join(transcricao[base] for base in self.sequencia)
        return Sequencia(nova_sequencia)

    def traduzir(self, parar=False):
        codons = [self.sequencia[i:i + 3] for i in range(0, len(self.sequencia), 3)]
        traducao = ""
        for codon in codons:
            if codon in DNA_PARA_AMINOACIDO:
                if parar and DNA_PARA_AMINOACIDO[codon] == "*":
                    break
                traducao += DNA_PARA_AMINOACIDO[codon]
            else:
                traducao += "X"
        return traducao

    def calcular_percentual(self, bases):
        total_bases = len(self.sequencia)
        total_bases_especificas = sum(base in bases for base in self.sequencia)
        percentual = total_bases_especificas / total_bases
        return percentual
