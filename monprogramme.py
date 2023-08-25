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
        git_commit()


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

# fonction qui fait au minimum 5 commits git
def git_commit(nb_commits = 5):
    if nb_commits < 5:
        nb_commits = 5

    # initialiser git
    os.system("git init")

    for i in range(nb_commits):
        # faire une modification alleatoire.
        f = open("README.md", "a")
        f.write("Modification {}".format(i))
        f.close()

        # faire un commit
        os.system("git add .")
        os.system("git commit -m 'commit {}'".format(i))

# call main
if __name__ == "__main__":
    main()