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
- Modification pages détails
- Ajout icône panier dans la barre de navigation
- Ajout de transitions lors du chargement des pages


---

### Aperçu de la page d'accueil actuelle (originale) :
![Capture d’écran du 2022-11-08 17-09-25](https://user-images.githubusercontent.com/103674276/200616353-5ebe01b0-3a21-4046-829b-69339a1dd89b.png)
---

### Aperçu de la page responsive menu pour les grands écrans (WIP) :
![Capture d’écran du 2022-11-16 18-54-37](https://user-images.githubusercontent.com/103674276/202256484-47efd269-7eb3-4f94-a118-9914087cd584.png)

---

### Aperçu de la page responsive menu pour moyens et petits écrans 1 (WIP) :
![Capture d’écran du 2022-11-12 21-19-02](https://user-images.githubusercontent.com/103674276/201492951-43d45e5c-37c0-4a4b-b7df-33d5e47d4859.png)

---

### Aperçu de la page responsive menu pour moyens et petits écrans après clic sur l'îcone "hamburger" (WIP) :
![Capture d’écran du 2022-11-16 18-56-25](https://user-images.githubusercontent.com/103674276/202256815-4811710b-2e30-4909-8bc6-f25794b53dce.png)



---

### Aperçu de la page "Pizzas traditionnelles"(filtre par catégorie) :
![Capture d’écran du 2022-11-16 18-57-45](https://user-images.githubusercontent.com/103674276/202257105-c5d1e658-6d73-489d-bfc8-26805139dd34.png)


---
### Aperçu de la page "Pizzas végétariennes" (filtre par propriété) :
![Capture d’écran du 2022-11-16 18-58-40](https://user-images.githubusercontent.com/103674276/202257306-89c5ff19-bb2c-4005-b469-c72349f97860.png)



---
### Aperçu d'une page détails de pizza (WIP):
![Capture d’écran du 2022-11-16 18-59-26](https://user-images.githubusercontent.com/103674276/202257428-d1a5c192-957b-4e07-9baa-093fcefe63ef.png)


---
### Aperçu d'une page détails de pizza en version moyens et petits écrans (WIP):
![Capture d’écran du 2022-11-16 19-00-23](https://user-images.githubusercontent.com/103674276/202257617-bf16dac4-78ff-40aa-b7dc-6aa3588c740b.png)









