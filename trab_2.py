# Define a classe Contato para representar um contato da agenda (item a)
class Contato:
    # Inicializa um objeto Contato com nome, telefone, endereço e relação (item a)
    def __init__(self, nome, telefone, endereco, relacao):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.relacao = relacao

    # Define a representação em string de um objeto Contato (item c)
    def __str__(self):
        return f'Nome: {self.nome}\nTelefone: {self.telefone}\nEndereço: {self.endereco}\nRelação: {self.relacao}\n'


# Define a classe Agenda para representar uma agenda telefônica (item a)
class Agenda:
    # Inicializa um objeto Agenda com uma lista vazia de contatos (item a)
    def __init__(self):
        self.contatos = []

    # Insere um contato na agenda ou altera um contato existente com o mesmo nome (item b)
    def inserir_contato(self, contato):
        for c in self.contatos:
            if c.nome == contato.nome:
                c.telefone = contato.telefone
                c.endereco = contato.endereco
                c.relacao = contato.relacao
                return
        self.contatos.append(contato)

    # Remove um contato da agenda pelo nome (item b)
    def remover_contato(self, nome):
        for i, c in enumerate(self.contatos):
            if c.nome == nome:
                del self.contatos[i]
                return

    # Busca um contato na agenda pelo nome ou parte do nome (item a)
    def buscar_contato(self, nome):
        for contato in self.contatos:
            if nome in contato.nome:
                return contato
        return None

    # Lista todos os contatos da agenda (item c)
    def listar_contatos(self):
        for contato in self.contatos:
            print(contato)

    # Salva os contatos da agenda em um arquivo (item d)
    def salvar_contatos(self, arquivo):
        with open(arquivo, 'w') as f:
            for contato in self.contatos:
                f.write(f'{contato.nome},{contato.telefone},{contato.endereco},{contato.relacao}\n')

    # Recupera os contatos da agenda de um arquivo (item d)
    def recuperar_contatos(self, arquivo):
        with open(arquivo, 'r') as f:
            for linha in f:
                dados = linha.strip().split(',')
                contato = Contato(dados[0], dados[1], dados[2], dados[3])
                self.inserir_contato(contato)


# Exemplo de uso das classes Agenda e Contato para criar uma agenda com alguns contatos,
# realizar algumas operações e salvar/recuperar os contatos de um arquivo (item e e f).
if __name__ == '__main__':
    agenda = Agenda()

    agenda.inserir_contato(Contato('Fulano', '99999999', 'Rua A', 'UFF'))
    agenda.inserir_contato(Contato('Ciclano', '88888888', 'Rua B', 'Cederj'))
    agenda.inserir_contato(Contato('Beltrano', '88889999', 'Rua C', 'Infância'))

    agenda.inserir_contato(Contato('Fulano', '77777777', 'Rua D', ''))
    agenda.remover_contato('Ciclano')

    agenda.listar_contatos()

    agenda.salvar_contatos('contatos.txt')
    agenda.recuperar_contatos('contatos.txt')

