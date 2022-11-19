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
- Ajout champ image dans le modèle + affichage dynamique des photos de pizzas dans les pages "détails"
- Modification de la navigation : uniquement la version avec menu déroulant lors d'un clic sur l'icône "hamburger" a été conservée (en vue d'un projet d'essai d'ajout dynamique des catégories dans le menu)

---

### Aperçu de la page d'accueil actuelle (originale) :
![Capture d’écran du 2022-11-08 17-09-25](https://user-images.githubusercontent.com/103674276/200616353-5ebe01b0-3a21-4046-829b-69339a1dd89b.png)
---

### Aperçu de la page responsive menu pour les grands écrans (Version modifiée 1) :
![Capture d’écran du 2022-11-16 18-54-37](https://user-images.githubusercontent.com/103674276/202256484-47efd269-7eb3-4f94-a118-9914087cd584.png)

### Aperçu de la page responsive menu pour les grands écrans (Version modifiée 2 WIP):
![Capture d’écran du 2022-11-19 18-32-15](https://user-images.githubusercontent.com/103674276/202863963-d00a8ff2-52f8-4e3f-ae95-75537ea85829.png)


---
### Aperçu de la page responsive menu pour moyens et petits écrans 1 (WIP) :
![Capture d’écran du 2022-11-12 21-19-02](https://user-images.githubusercontent.com/103674276/201492951-43d45e5c-37c0-4a4b-b7df-33d5e47d4859.png)

---

### Aperçu de la page responsive menu après clic sur l'îcone "hamburger" (WIP) :
![Capture d’écran du 2022-11-16 18-56-25](https://user-images.githubusercontent.com/103674276/202256815-4811710b-2e30-4909-8bc6-f25794b53dce.png)


---

### Aperçu de la page "Pizzas traditionnelles"(filtre par catégorie version modifiée 1) :
![Capture d’écran du 2022-11-16 18-57-45](https://user-images.githubusercontent.com/103674276/202257105-c5d1e658-6d73-489d-bfc8-26805139dd34.png)

### Aperçu de la page "Pizzas traditionnelles"(filtre par catégorie version modifiée 2 WIP) :
![Capture d’écran du 2022-11-19 18-39-01](https://user-images.githubusercontent.com/103674276/202864142-4fdfa190-c815-4b10-a252-c30eaac33126.png)



---
### Aperçu de la page "Pizzas végétariennes" (filtre par propriété version modifiée 1) :
![Capture d’écran du 2022-11-16 18-58-40](https://user-images.githubusercontent.com/103674276/202257306-89c5ff19-bb2c-4005-b469-c72349f97860.png)

### Aperçu de la page "Pizzas végétariennes" (filtre par propriété version modifiée 2 WIP) :
![Capture d’écran du 2022-11-19 18-40-19](https://user-images.githubusercontent.com/103674276/202864175-f48f0a6a-3051-4a47-ba6d-c3975083164b.png)



---
### Aperçu d'une page détails de pizza (version modifiée 1):
![Capture d’écran du 2022-11-16 18-59-26](https://user-images.githubusercontent.com/103674276/202257428-d1a5c192-957b-4e07-9baa-093fcefe63ef.png)

### Aperçus d'une page détails de pizza avec affichage dynamique des images (version modifiée 2 WIP):
![Capture d’écran du 2022-11-19 18-41-22](https://user-images.githubusercontent.com/103674276/202864217-665d1608-a304-4e4b-886a-cb547d6c84ab.png)
![Capture d’écran du 2022-11-19 18-42-07](https://user-images.githubusercontent.com/103674276/202864255-c7ae00d2-ea54-4062-8183-b3f0920600ed.png)


---
### Aperçu d'une page détails de pizza en version moyens et petits écrans (version modifiée 1):
![Capture d’écran du 2022-11-16 19-00-23](https://user-images.githubusercontent.com/103674276/202257617-bf16dac4-78ff-40aa-b7dc-6aa3588c740b.png)

### Aperçu d'une page détails de pizza en version moyens et petits écrans (version modifiée 2 WIP):
![Capture d’écran du 2022-11-19 18-44-36](https://user-images.githubusercontent.com/103674276/202864321-b58a964e-bc35-4f18-b012-c5f59f49b561.png)




---
### Formulaire de saisie d'une pizza dans la console d'administration de Django (ajout du champ image) :
![Capture d’écran du 2022-11-19 18-27-28](https://user-images.githubusercontent.com/103674276/202863778-1ce2d2e2-4db3-487e-92fb-84d4c1ed8c90.png)


---




