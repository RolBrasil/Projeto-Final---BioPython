class OrganismoFasta:
    def __init__(self, id_, nome, sequencia):
        self.id = id_
        self.nome = nome
        self.sequencia = Sequencia(sequencia)
