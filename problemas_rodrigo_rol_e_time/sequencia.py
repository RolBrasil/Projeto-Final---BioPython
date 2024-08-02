from constantes import DNA_PARA_AMINOACIDO
class Sequencia:
    def __init__(self, sequencia):
        self.sequencia = sequencia

    def complementar(self):
        complemento = ""
        for base in self.sequencia:
            if base == 'A':
                complemento += 'T'
            elif base == 'T':
                complemento += 'A'
            elif base == 'C':
                complemento += 'G'
            elif base == 'G':
                complemento += 'C'
        return Sequencia(complemento)

    def complementar_reversa(self):
        complemento_reverso = ""
        for base in reversed(self.sequencia):
            if base == 'A':
                complemento_reverso += 'T'
            elif base == 'T':
                complemento_reverso += 'A'
            elif base == 'C':
                complemento_reverso += 'G'
            elif base == 'G':
                complemento_reverso += 'C'
        return Sequencia(complemento_reverso)

    def transcrever(self):
        transcricao = ""
        for base in self.sequencia:
            if base == 'T':
                transcricao += 'U'
            else:
                transcricao += base
        return Sequencia(transcricao)

    def traduzir(self, parar=False):
        traducao = ""
        for i in range(0, len(self.sequencia), 3):
            codon = self.sequencia[i:i+3]
            if codon in DNA_PARA_AMINOACIDO:
                if DNA_PARA_AMINOACIDO[codon] == "*":
                    if parar:
                        break
                    else:
                        traducao += "*"
                else:
                    traducao += DNA_PARA_AMINOACIDO[codon]
            else:
                traducao += "X"
        return traducao

    def calcular_percentual(self, bases):
        total_bases = len(self.sequencia)
        count = 0
        for base in self.sequencia:
            if base in bases:
                count += 1
        return count / total_bases