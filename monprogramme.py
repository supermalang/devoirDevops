# This is the main program file.
import os


# main function
def main():
    chemin = input("Donnez un chemin pour creer l'arborescence: ")

    # Verifier si le chemin existe
    if os.path.exists(chemin):
        print("Le chemin est un fichier ou repertoire qui existe deja.")
    # Si le chemin n'existe pas
    else:
        # on execute creer_arborescence
        creer_arborescence(chemin)


# Creation de l'arborescence
def creer_arborescence(chemin):
    os.mkdir(chemin)
    
    os.mkdir(chemin + "/data")
    os.mkdir(chemin + "/data/cleaned")
    os.mkdir(chemin + "/data/raw")

    os.mkdir(chemin + "/docs")
    f = open(chemin + "/LICENSE", "w")
    f.close()

    f = open(chemin + "/Makefile", "w")
    f.close()

    os.mkdir(chemin + "/models")

    os.mkdir(chemin + "/ notebooks")
    f = open(chemin + "/ notebooks/main.ipynb", "w")
    f.close()

    f = open(chemin + "/README.md", "w")
    f.close()

    os.mkdir(chemin + "/ reports")
    f = open(chemin + "/requirements.txt", "w")
    f.close()

    os.mkdir(chemin + "/ src")
    os.mkdir(chemin + "/ src/utils.py")

# call main
if __name__ == "__main__":
    main()