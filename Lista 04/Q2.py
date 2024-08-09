from datetime import datetime, timedelta

class Musica:
    def __init__(self, titulo, artista, album, dataInclusao, duracao):
        if titulo != "": self.__titulo == titulo
        else: raise ValueError()
        if artista != "": self.__artista == artista
        else: raise ValueError()
        if album != "": self.__album == album
        else: raise ValueError()
        if artista != "": self.__artista == artista
        else: raise ValueError()
        if dataInclusao == datetime.now(): self.__dataInclusao == dataInclusao
        else: raise ValueError()
        if duracao != timedelta(minutes = 0, seconds = 0): self.__duracao == duracao 
        else: raise ValueError() 

    def __str__(self):
        return f"Titulo: {self.__titulo}\nArtista: {self.__artista}\nAlbum: {self.__album}\n Data de Inclusão: {self.__titulo}"
        
class Playlist:
    def __init__(self, nome, descricao, musicas):
        if nome != "": self.__nome == nome
        else: raise ValueError()
        if descricao != "": self.__descricao == descricao
        else: raise ValueError()
        if musicas == []: self.__musicas == musicas
        else: raise ValueError()
        
    def PlayList(self):
        self.__nome = input("Nome da playlist: ")
        self.__descricao = input("Descrição: ")
    
    def Inserir(self, musica):
        self.__musicas.append(musica)
        

    def Listar(self):
        return self.__musicas
    
    def TempoTotal:
        
    
    def __str__(self):
        return f"Nome da playlist: {self.__nome}\nDescrição: {self.__descricao}\nMúsicas: {self.__musicas}"

musica = Musica("blood farm, nois, itsusone,  , 00:00)
