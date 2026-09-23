class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero


class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def exibir_info(self):
        print(f"FILME: {self.titulo}  Gênero: {self.genero} Duração: {self.duracao} min")


class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas

    def exibir_info(self):
        print(f"SÉRIE: {self.titulo} Gênero: {self.genero} Temporadas: {self.temporadas}")


class Podcast(Conteudo):
    def __init__(self, titulo, genero, episodios):
        super().__init__(titulo, genero)
        self.episodios = episodios

    def exibir_info(self):
        print(f"PODCAST: {self.titulo} Gênero: {self.genero} Episódios: {self.episodios}")


class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema

    def exibir_info(self):
        print(f"DOCUMENTÁRIO: {self.titulo} Gênero: {self.genero} Tema: {self.tema}")


filme1 = Filme("Interestelar", "Ficcao", 169)
filme2 = Filme("Shrek", "Animacao", 90)

serie1 = Serie("Stranger Things", "Ficcao", 4)
serie2 = Serie("The Office", "Comedia", 9)

# Criando o catálogo utilizando as variáveis criadas e novas instâncias
catalogo = [
    filme1,
    filme2,
    serie1,
    serie2,
    Serie("Round 6", "Suspense", 2),
    Documentario("Nosso Planeta", "Natureza", "Vida selvagem"),
    Podcast("Mano a Mano", "Entrevistas", 50)
]


print("--- CATÁLOGO COMPLETO ---")
for item in catalogo:
    print(f"Título: {item.titulo} Gênero: {item.genero}")

filme3 = Filme("Matrix", "Ficcao", 136)
catalogo.append(filme3)

print("\n--- ITENS DE FICÇÃO ---")
for item in catalogo:
    if item.genero == "Ficcao":
        print(f"Título: {item.titulo}")
