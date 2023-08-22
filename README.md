<h1 align="center">OpenClassrooms Project N°9</h1>
<h2 align="center">P9_DEVELOPPEZ-UNE-APPLICATION-WEB-EN-UTILISANT-DJANGO</h1>

![Logo LITReview](https://raw.githubusercontent.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django/main/documentation/litreview_logo.png)

Développez une application Web en utilisant Django

La société LITReview, spécialisée dans les technologies innovantes, envisage de concevoir et de mettre sur le marché une application web dédiée à une plateforme collaborative où les membres peuvent consulter ou demander des critiques de livres selon leurs besoins.

Les fonctionnalités prévues pour l'application comprennent :

1. Un système d'authentification robuste : les utilisateurs doivent pouvoir s'inscrire et se connecter, garantissant que seuls les membres authentifiés aient accès à la plateforme.

2. Un flux dynamique : les utilisateurs auront la possibilité de visualiser un flux d'activités comprenant les dernières publications et commentaires des personnes qu'ils suivent, présentés dans un ordre chronologique décroissant.

3. La possibilité de sollicitation : les utilisateurs pourront initier de nouveaux tickets pour demander des avis sur des ouvrages ou articles spécifiques.

4. Une interface de réponse : les membres pourront rédiger des critiques en réaction à des tickets existants ou initier des critiques indépendantes, en suivant un processus où ils génèrent d'abord un ticket suivi d'un commentaire en guise de réponse.

5. Gestion de contenu : les utilisateurs auront les droits de visualiser, éditer, ou supprimer leurs propres tickets et retours.

6. Interaction sociale : la plateforme permettra aux utilisateurs de suivre d'autres membres en utilisant leur identifiant, de visualiser la liste des personnes qu'ils suivent et d'ajuster leur réseau en choisissant de ne plus suivre certains utilisateurs si souhaité.

7. Cet ensemble de fonctionnalités a été conçu pour répondre aux besoins précis de la communauté et garantir une expérience utilisateur optimale.


## Liste des documents fournis avec la mission :

1. [La mission de ce projet](https://github.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django/blob/main/documentation/1-Mission-Projet_Litreview/1-Mission.pdf)
2. [Cahier des charges de ce projet](https://github.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django/blob/main/documentation/1-Mission-Projet_Litreview/2-Cahier_des_charges.pdf)
3. [Guide des étapes clés à suivre pour ce projet](https://github.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django/blob/main/documentation/1-Mission-Projet_Litreview/3-Guide_des_etapes_cles.pdf)
4. [Schéma de la base de données à suivre pour ce projet](https://github.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django/blob/main/documentation/1-Mission-Projet_Litreview/4-Schema_de_la_base_de_donnees.pdf)
5. [Les WireFrames à suivre pour ce projet](https://github.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django/blob/main/documentation/1-Mission-Projet_Litreview/5-Wireframes-FR.pdf)
6. [Exemple du fichier models.py pour s'inspirer](https://github.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django/blob/main/documentation/1-Mission-Projet_Litreview/6-models.py.pdf)

## Installation et exécution de l'application 

Vous devriez avoir une copie intégrale de ce code :

1. Clonez ou téléchargez ce dépôt de code à l'aide des commandes suivantes:
```
git clone https://github.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django
```
<br> Ou bien <br>
```
https://github.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django/archive/refs/heads/main.zip
```


2. Rendez-vous depuis un terminal à la racine de votre nouveau répertoire 

3. Créer un environnement virtuel pour le projet avec la commande :
```
python -m venv env 
```

4. Activez l'environnement virtuel avec la commande :
- sous windows.
```
env\Scripts\activate
``` 
- sous macos ou linux.
```
source env/bin/activate
```

5. Installez les dépendances du projet avec la commande : 
```
pip install -r requirements.txt
```

6. Utilisez le super-utilisateur déja créé (voir les identifiants plus bas), ou bien en Créer un avec la commande 
```
python manage.py createsuperuser
```
Et renseigez le nom d'utilisateur, une adresse e-mail et le mot de passe.

7. Mettez vous dans le dossier (litreview) avec la commande suivante :
```
cd litreview
```

8. Démarrer le serveur avec la commande :
```
python manage.py runserver
```

Les étapes 1 à 8 ne sont requises que pour l'installation initiale. Pour les lancements ultérieurs du serveur de l'application, il suffit d'exécuter les étapes 4 et 8 à partir du répertoire racine du projet.


## Connexion à l'application

Lorsque le serveur fonctionne, après l'étape 8 de la procédure, l’application peut être accessible via les urls : 

- http://localhost:8000/. 

ou bien

- http://127.0.0.1:8000/

Ce dernier ouvrira un navigateur qui vous présentera la page d’accueil de l’application permettant la connexion de l’utilisateur et un lien vers l’interface de création de compte.
Vous trouverez dans le tableau ‘Comptes utilisateurs’ ci-dessous les identifiants des utilisateurs déjà enregistrés.


 ## Comptes utilisateurs : 
 
| Nom d’utilisateur | Mot de passe     | Rôle             |
|-------------------|------------------|------------------|
| admin             | EL-walid_1234@+  | Super-Utilisateur|
| Si-Mo             | Courtoi26        | Utilisateur      |
| Souzane62         | Bitros95+        | Utilisateur      |
| Nadej39           | Kilom95+7        | Utilisateur      |
| Florent26         | Kabis95200+      | Utilisateur      |
| François40        | Limoge92008      | Utilisateur      |
| EL-Walid13        | Base1304@+       | Utilisateur      |


## Interface d’administration

L’interface d’administration de l’application est accessible via l’url suivante :
```
http://localhost:8000/admin. 
```
Vous serez dirigé vers la page de connexion de l’administrateur. Vous pouvez ainsi avoir accès à l’interface d’administration après la saisie des identifiants du Super-Utilisateur.

### Structure des dossiers et fichiers du projet :
Afin de voir la structure complete du projet, vous pouvez voir le fichier /documentations/structure_ce_projet.txt, oubien vous pouvez meme
générer de nouveau ce fichier de la façon suivante ;
Executez la commande suivante quand vous etes à la racine du projet : 
```
tree -I 'env|__pycache__|flake-report|__init__.py|migrations' >> structure_ce_projet.txt
```
[Click pour voir la structure actuelle:](https://github.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django/blob/main/documentation/structure_ce_projet.txt)

### Pep8

Le paquet flake8-html est présent dans l'environnemnt virtuel, vous pouvez générer un nouveau rapport avec la commande 
suivante :
```
flake8 --format=html --htmldir=flake-report
```
Puis, démarrez le fichier index.html existant dans le dossier /flake-report de la racine du projet


## Guide complet pour reconstruire ce projet depuis le debut

[Guide complet pour reconstruire ce projet](https://github.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django/blob/main/documentation/2-Conclusions/1-Guide_complet_pour_reconstruire_ce_projet_depuis_le_debut.pdf)


## Diagram des tables & relations de ma base de données

[Voir le diagram des tables de ma bese de donnée actuelle:](https://github.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django/blob/main/documentation/my_project_diagram.png)


## Questions / Réponses & Conclusions :

[Voir mon rapport des Questions/Reponses:](https://github.com/waleedos/2023_P9_LITRevu_Developpez_application_Web_avec_Django/blob/main/documentation/2-Conclusions/2-Questions-Reponses.pdf) 


### Powered by EL-WALID EL-KHABOU

E-mail : ewek.dev@gmail.com


