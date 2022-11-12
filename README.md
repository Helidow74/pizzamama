# pizzamama2 (WIP)

Amélioration de la base de site dynamique de pizzeria créée lors d'un exercice d'apprentissage de Django.
Tout est en cours d'amélioration et les copies d'écran présentées ci-dessous sont encore pleines de défauts à corriger.

- Django version 4.1.3
- Python 3.10
- Django-tailwind CSS 3.1.6

---
**Liste des améliorations faites par rapport au projet original :**

- Ajout d'une barre de navigation (réalisée en Tailwind CSS)
- Ajout d'une version alternative responsive pour petits et moyens écrans avec menu déroulant qui apparaît lors d'un clic
sur l'icône "hamburger".
- Ajout d'une table de catégories dans le modèle + jointure avec table Pizza existante
- Ajout de nouveaux champs dans la table Pizza : catégorie, description
- Création d'un template de base
- Création des différentes pages (avec extends du template de base)
- Ajout des urls pour accéder aux différentes pages via les liens du menu
- Création des différentes vues avec filtrage des données pour chaque page créée.


---

### Aperçu de la page d'accueil actuelle (originale) :
![Capture d’écran du 2022-11-08 17-09-25](https://user-images.githubusercontent.com/103674276/200616353-5ebe01b0-3a21-4046-829b-69339a1dd89b.png)
---

### Aperçu de la page responsive menu pour les grands écrans (WIP) :
![Capture d’écran du 2022-11-08 17-38-52](https://user-images.githubusercontent.com/103674276/200623393-539e6775-48ec-401d-9896-f672479b781b.png)
---

### Aperçu de la page responsive menu pour moyens et petits écrans 1 (WIP) :
![Capture d’écran du 2022-11-08 17-40-59](https://user-images.githubusercontent.com/103674276/200623870-a70ee621-2694-4619-84a3-9f6ff6bdc6ab.png)
---

### Aperçu de la page responsive menu pour moyens et petits écrans après clic sur l'îcone "hamburger" (WIP) :
![Capture d’écran du 2022-11-08 17-41-39](https://user-images.githubusercontent.com/103674276/200623985-903f3584-0b64-40af-bcef-a241b9d058ac.png)

---

### Aperçu de la page "Pizzas traditionnelles"(filtre par catégorie) :
![Capture d’écran du 2022-11-12 14-47-56](https://user-images.githubusercontent.com/103674276/201477127-4f9b3cbb-3f85-421a-b065-7ad0405a431a.png)

---
### Aperçu de la page "Pizzas végétariennes" (filtre par propriété) :
![Capture d’écran du 2022-11-12 14-52-10](https://user-images.githubusercontent.com/103674276/201477245-7b630af5-b0fb-4039-b740-a46f7aa9f1d1.png)
