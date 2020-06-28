import os

class CatalogoPeliculas:
    
    path_file = "laboratorio_pelicula/files/peliculas.txt"
    
    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            file = open(CatalogoPeliculas.path_file, "a")
            file.write(pelicula.__str__() + "\n")
        except Exception as e:
            print("Ocurrio un error al agregar la pelicula ", e)
        finally:
            file.close()
            
    @staticmethod
    def listar_peliculas():
        try:
            file = open(CatalogoPeliculas.path_file,"r")
            print("Catalogo de Peliculas")
            print(file.read())
        except Exception as e:
            print("Ocurrio un error al leer las peliculas ", e)
        finally:
            file.close()

    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.path_file)
            print("Se borro el achivo con la siguiente ruta: " + CatalogoPeliculas.path_file)
        except Exception as e:
            print("Ocurrio un error al borrar el archivo", e)