from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None
while opcion != 4:from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None
while opcion != 4:
    print('Opciones del menu:')
    print("1. Agregar Peliculas")
    print("2. Listar Peliculas")
    print("3. Eliminar Catalogo de Peliculas")
    print("4. Salir")
    opcion = input("Escribre una opcion del menu (1-4): ")
    if opcion == "1":
        nombre_pelicula = input("Ingresa el nombre de la pelicula: ")
        pelicula = Pelicula(nombre_pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == "2":
        CatalogoPeliculas.listar_peliculas()
    elif opcion == "3":
        CatalogoPeliculas.eliminar()
else:
    print("Saliendo del programa...")
    
    print('Opciones del menu:')
    print("1. Agregar Peliculas")
    print("2. Listar Peliculas")
    print("3. Eliminar Catalogo de Peliculas")
    print("4. Salir")
    opcion = input("Escribre una opcion del menu (1-4): ")
    if opcion == "1":
        nombre_pelicula = input("Ingresa el nombre de la pelicula: ")
        pelicula = Pelicula(nombre_pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == "2":
        CatalogoPeliculas.listar_peliculas()
    elif opcion == "3":
        CatalogoPeliculas.eliminar()
else:
    print("Saliendo del programa...")
    