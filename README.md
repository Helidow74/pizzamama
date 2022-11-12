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
- Ajout vue / template de détails de chaque pizza
- Ajout des liens vers les pages de détails


---

### Aperçu de la page d'accueil actuelle (originale) :
![Capture d’écran du 2022-11-08 17-09-25](https://user-images.githubusercontent.com/103674276/200616353-5ebe01b0-3a21-4046-829b-69339a1dd89b.png)
---

### Aperçu de la page responsive menu pour les grands écrans (WIP) :
![Capture d’écran du 2022-11-12 21-15-36](https://user-images.githubusercontent.com/103674276/201492905-33ea88ef-de2e-4e2c-9000-882015ad2695.png)
---

### Aperçu de la page responsive menu pour moyens et petits écrans 1 (WIP) :
![Capture d’écran du 2022-11-12 21-19-02](https://user-images.githubusercontent.com/103674276/201492951-43d45e5c-37c0-4a4b-b7df-33d5e47d4859.png)

---

### Aperçu de la page responsive menu pour moyens et petits écrans après clic sur l'îcone "hamburger" (WIP) :
![Capture d’écran du 2022-11-12 21-19-43](https://user-images.githubusercontent.com/103674276/201492973-e78d550f-9cd0-4fd6-bb7f-775fe06f43bc.png)


---

### Aperçu de la page "Pizzas traditionnelles"(filtre par catégorie) :
![Capture d’écran du 2022-11-12 21-20-49](https://user-images.githubusercontent.com/103674276/201493025-f782ee23-593d-4a62-a80e-5044e7317fe4.png)


---
### Aperçu de la page "Pizzas végétariennes" (filtre par propriété) :
![Capture d’écran du 2022-11-12 21-21-30](https://user-images.githubusercontent.com/103674276/201493048-49151ebe-56a2-487a-ace0-1b537b78a258.png)


---
### Aperçu d'une page détails de pizza (WIP):
![Capture d’écran du 2022-11-12 21-22-47](https://user-images.githubusercontent.com/103674276/201493089-ee6aafc9-3ffe-4155-b379-ca9c8a076d57.png)

---
### Aperçu d'une page détails de pizza en version moyens et petits écrans (WIP):
![Capture d’écran du 2022-11-12 21-24-06](https://user-images.githubusercontent.com/103674276/201493134-c50b31ec-ab21-4fc2-9f8e-9dbe5064d2af.png)









