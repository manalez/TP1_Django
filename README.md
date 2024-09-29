# 💻 TP M1 DWM - Développement d'une Application d'Authentification avec Django

![Django](https://img.shields.io/badge/Django-3.2-green.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Status](https://img.shields.io/badge/Status-En%20cours-yellow.svg)

## 📑 Description du Projet
Ce projet consiste à développer une **application web** avec **Django**, permettant aux utilisateurs de s'inscrire et de se connecter via un système d'authentification. Il s'agit d'un exercice pratique du module de développement web pour le **Master 1 Développement Web et Mobile (DWM)**.

### 🎯 Objectifs :
- Implémenter un système de gestion d'utilisateurs avec inscription et connexion.
- Créer une page d'accueil pour rediriger les utilisateurs vers les pages d'inscription et de connexion.
- Utiliser **Bootstrap** pour styliser les formulaires et rendre l'interface utilisateur agréable et responsive.

## 🚀 Fonctionnalités
- 🌐 **Page d'accueil** : Présente des liens vers les pages d'inscription et de connexion.
- 🔑 **Inscription** : Un formulaire permettant à de nouveaux utilisateurs de créer un compte.
- 🔐 **Connexion** : Un formulaire pour se connecter avec un compte existant.
- 👨‍💼 **Gestion des utilisateurs** : Création, authentification et gestion de session des utilisateurs.

## 📁 Arborescence du projet
```bash
myauthproject/
│
├── accounts/                  # Application d'authentification
│   ├── migrations/            # Migrations de la base de données
│   ├── templates/             # Modèles HTML
│   │   ├── registration/
│   │   │   ├── login.html     # Modèle de connexion
│   │   │   └── register.html   # Modèle d'inscription
│   │   └── welcome.html       # Modèle de bienvenue
│   ├── __init__.py            # Fichier d'initialisation
│   ├── admin.py               # Configuration de l'admin
│   ├── apps.py                # Configuration de l'application
│   ├── forms.py               # Formulaires personnalisés
│   ├── models.py              # Modèles de base de données
│   ├── tests.py               # Tests
│   └── views.py               # Vues
│
├── myauthproject/             # Configuration du projet Django
│   ├── __init__.py
│   ├── settings.py            # Paramètres de l'application
│   ├── urls.py                # Configuration des URL
│   └── wsgi.py                # Interface WSGI pour déployer l'application
│
├── db.sqlite3                 # Base de données
├── manage.py                  # Fichier de gestion
└── requirements.txt           # Dépendances du projet




