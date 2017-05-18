Projet servant de fil rouge au cours [Testez votre projet en Python](https://openclassrooms.com/courses/testez-un-projet-python), disponible sur OpenClassrooms. Il s'agit d'un fork de [ce projet](https://github.com/OpenClassrooms-Student-Center/la_poo_avec_python/tree/master) utilisé dans un cours sur [la Programmation Orientée Objet en Python](https://openclassrooms.com/courses/decouvrez-la-programmation-orientee-objet-avec-python).

Nous simulons ici un monde virtuel peuplé de 100 000 personnes. Nous cherchons à connaître :
- à partir de quelle densité de population les personnes sont moins agréables que la moyenne,
- à partir de quel âge les personnes gagnent plus d'argent que la moyenne.

Lorsque le programme se lance, une première fenêtre affiche un graphique concernant la densité de population puis une seconde concernant le revenu.

# Installation de dépendences

Pour tracer des graphes, vous allez avoir besoin d'installer `matplotlib` :

    pip install matplotlib

# Données

Nous vous fournissons 100 000 agents, gracieusement créés grâce à [PPLAPI](http://pplapi.com).
*Pensez à dézipper le document !*

    unzip program/agents-100k.zip

Si vous souhaitez en générer de nouveaux, entrez la commande suivante :

    python program/download_agents -d agents-100k.json -c 100000

# Lancer le programme

    python model.py agents-100k.json


# Tests

Lancer les tests :

    pytest test*.py

Lancer les tests et voir la couverture de tests :

    pytest --cov=program test*.py

Lancer les tests et voir la couverture de tests en format HTML :

    pytest --cov=program --cov-report html test_*.py


# Contributors

[Régis Behmo](https://github.com/regisb)
[Céline Martinet Sanchez](https://github.com/celine-m-s)
