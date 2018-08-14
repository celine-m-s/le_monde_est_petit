Projet servant de fil rouge au cours [Testez votre projet en Python](https://openclassrooms.com/courses/testez-un-projet-python), disponible sur OpenClassrooms. Il s'agit d'un fork de [ce projet](https://github.com/OpenClassrooms-Student-Center/la_poo_avec_python/tree/master) utilisé dans un cours sur [la Programmation Orientée Objet en Python](https://openclassrooms.com/courses/decouvrez-la-programmation-orientee-objet-avec-python).

Nous simulons ici un monde virtuel peuplé de 100 000 personnes. Nous cherchons à connaître :
- à partir de quelle densité de population les personnes sont moins agréables que la moyenne,
- à partir de quel âge les personnes gagnent plus d'argent que la moyenne.

Lorsque le programme se lance, une première fenêtre affiche un graphique concernant la densité de population puis une seconde concernant le revenu.

# Installation de dépendences

Créez un environnement virtuel et lancez l'installation des dépendences listées dans le fichier `requirements.txt`.

Attention : ce script nécessite Tkinter et il ne peut être installé en utilisant Pip. Si vous ne l'avez pas encore, vous pouvez l'installer sour Linux en tapant `sudo apt-get install python3.6-tk`.

# Données

Nous vous fournissons 100 000 agents, gracieusement créés grâce à [PPLAPI](http://pplapi.com).
*Pensez à dézipper le document !*

    unzip program/agents-100k.zip

Si vous souhaitez en générer de nouveaux, entrez la commande suivante :

    python program/download_agents.py -d program/agents-100k.json -c 100000

# Lancer le programme

    python program/world.py program/agents-100k.json


# Tests

Lancer les tests :

    pytest test*.py

Lancer les tests et voir la couverture de tests :

    pytest --cov=program test*.py

Lancer les tests et voir la couverture de tests en format HTML :

    pytest --cov=program --cov-report html test_*.py


# Version de Python
Ce code est fonctionnel avec Python 3. Dernière version testée : 3.6.5.

# Contributeurs

[Régis Behmo](https://github.com/regisb)
[Céline Martinet Sanchez](https://github.com/celine-m-s)
