# Schéma de Base de Données - Projet Alfajiri

Ce document présente le schéma complet de la base de données déduit à partir de l'analyse des modèles de données du frontend (répertoire `Frontend/lib/types.ts`). Le système couvre les domaines de la comptabilité, de la logistique (flotte de camions), de la facturation et du suivi d'audit.

## 1. Table `Succursale`
**Rôle :** Gérer les différentes succursales opérationnelles de l'entreprise (ex: Zambie, Lubumbashi, Mine de Sabri, Frontières).

| Colonne | Type | Description |
| :--- | :--- | :--- |
| `id` | VARCHAR (PK) | Identifiant unique de la succursale (ex: zambie, lubumbashi) |
| `label` | VARCHAR | Nom complet de la succursale |
| `short` | VARCHAR | Code court de la succursale (ex: ZMB, LUB) |
| `color` | VARCHAR | Code couleur pour l'interface utilisateur |

## 2. Table `Dossier`
**Rôle :** Enregistrer les informations juridiques et fiscales des entreprises (ou filiales) gérées dans le système.

| Colonne | Type | Description |
| :--- | :--- | :--- |
| `id` | VARCHAR (PK) | Identifiant unique |
| `raisonSociale` | VARCHAR | Raison sociale de l'entreprise |
| `sigle` | VARCHAR | Sigle de l'entreprise |
| `statutJuridique` | VARCHAR | Forme juridique (ex: SARL, SA) |
| `rccm` | VARCHAR | Numéro de Registre du Commerce et du Crédit Mobilier |
| `idNat` | VARCHAR | Identification Nationale |
| `nImpot` | VARCHAR | Numéro d'impôt |
| `adresse` | TEXT | Adresse physique |
| `ville` | VARCHAR | Ville du siège |
| `pays` | VARCHAR | Pays du siège |
| `telephone` | VARCHAR | Numéro de téléphone de contact |
| `email` | VARCHAR | Adresse email de contact |
| `logo` | VARCHAR | Lien/Chemin vers le logo de l'entreprise |
| `devise` | VARCHAR | Devise de fonctionnement (ex: USD) |
| `exerciceEnCours` | VARCHAR | Année de l'exercice en cours |
| `dateDebut` | DATE | Date de début de l'exercice |
| `dateFin` | DATE | Date de fin de l'exercice |

## 3. Table `Journal`
**Rôle :** Définir les journaux comptables utilisés pour classer les écritures (Achats, Ventes, Caisse, Banque, Opérations Diverses).

| Colonne | Type | Description |
| :--- | :--- | :--- |
| `code` | VARCHAR (PK) | Code du journal (ACH, VTE, CAI, BQ, OD, FISC) |
| `libelle` | VARCHAR | Nom du journal |
| `type` | ENUM | Type de journal (achats, ventes, caisse, banque, od) |
| `succursale_id` | VARCHAR (FK) | Référence à la succursale associée |
| `dernierNumero` | INT | Compteur pour la numérotation des écritures |

## 4. Table `CompteComptable`
**Rôle :** Stocker le plan comptable (comptes généraux et auxiliaires) ainsi que leurs soldes.

| Colonne | Type | Description |
| :--- | :--- | :--- |
| `numero` | VARCHAR (PK) | Numéro du compte |
| `libelle` | VARCHAR | Intitulé du compte |
| `classe` | VARCHAR | Classe comptable (1 à 8) |
| `type` | ENUM | Type (general, auxiliaire) |
| `parent_numero` | VARCHAR (FK)| Numéro du compte parent |
| `lettable` | BOOLEAN | Indique si le compte est lettrable |
| `tiers_code` | VARCHAR (FK) | Référence vers la table Tiers (si applicable) |
| `soldeDebit` | DECIMAL | Solde débiteur actuel |
| `soldeCredit` | DECIMAL | Solde créditeur actuel |

## 5. Table `Tiers`
**Rôle :** Gérer les partenaires de l'entreprise (clients, fournisseurs, personnel, état).

| Colonne | Type | Description |
| :--- | :--- | :--- |
| `code` | VARCHAR (PK) | Code unique du tiers |
| `nom` | VARCHAR | Nom complet ou raison sociale du tiers |
| `type` | ENUM | Catégorie (fournisseur, client, personnel, etat, associe) |
| `compte` | VARCHAR (FK) | Numéro de compte auxiliaire associé |
| `soldeDebit` | DECIMAL | Total des débits |
| `soldeCredit` | DECIMAL | Total des crédits |

## 6. Table `Ecriture`
**Rôle :** Représenter l'en-tête d'une pièce comptable (transaction globale).

| Colonne | Type | Description |
| :--- | :--- | :--- |
| `id` | VARCHAR (PK) | Identifiant interne unique |
| `numero` | VARCHAR | Numéro de pièce comptable formaté |
| `journal_code` | VARCHAR (FK)| Journal d'appartenance |
| `date` | DATE | Date d'enregistrement |
| `libelle` | VARCHAR | Description globale de l'opération |
| `statut` | ENUM | État (brouillard, valide) |
| `saisiePar` | VARCHAR | Nom/ID de l'utilisateur ayant saisi l'écriture |
| `validePar` | VARCHAR | Nom/ID du validateur (optionnel) |
| `piece` | VARCHAR | Référence ou nom du fichier de la pièce justificative |

## 7. Table `LigneEcriture`
**Rôle :** Détailler la répartition des montants au crédit ou au débit pour une écriture donnée.

| Colonne | Type | Description |
| :--- | :--- | :--- |
| `id` | VARCHAR (PK) | Identifiant unique de la ligne |
| `ecriture_id` | VARCHAR (FK)| Référence vers l'écriture parente |
| `date` | DATE | Date de la ligne |
| `compte_numero` | VARCHAR (FK)| Compte imputé |
| `libelleCompte` | VARCHAR | Intitulé du compte (redondance souvent utilisée en vue métier) |
| `libelle` | VARCHAR | Description de la ligne |
| `debit` | DECIMAL | Montant débité |
| `credit` | DECIMAL | Montant crédité |
| `auxiliaire` | VARCHAR (FK) | Référence au compte auxiliaire si applicable |

## 8. Table `Camion`
**Rôle :** Suivre la flotte logistique, le statut des transits et les coûts associés (douanes, transport).

| Colonne | Type | Description |
| :--- | :--- | :--- |
| `id` | VARCHAR (PK) | Identifiant unique |
| `immat` | VARCHAR | Plaque d'immatriculation |
| `chauffeur` | VARCHAR | Nom du chauffeur |
| `transporteur` | VARCHAR | Entreprise de transport |
| `chargement` | DECIMAL | Poids du chargement (tonnes) |
| `statut` | ENUM | État du trajet (chargement, transit_zambie, douane, arrive_sabri, etc.) |
| `dateDepart` | DATETIME | Date et heure de départ |
| `dateArrivee` | DATETIME | Date et heure d'arrivée (si atteinte) |
| `position` | VARCHAR | Localisation actuelle |
| `progression`| INT | Pourcentage de complétion du trajet |
| `bl` | VARCHAR | Numéro de Bon de Livraison |
| `factureTransport`| DECIMAL | Coût facturé par le transporteur |
| `douaneMontant`| DECIMAL | Frais de douane payés |

## 9. Table `Facture`
**Rôle :** Gérer la facturation commerciale vis-à-vis des clients.

| Colonne | Type | Description |
| :--- | :--- | :--- |
| `id` | VARCHAR (PK) | Identifiant unique |
| `numero` | VARCHAR | Numéro officiel de la facture |
| `date` | DATE | Date de la facturation |
| `client_code` | VARCHAR (FK) | Référence vers le client (table Tiers) |
| `montantHT` | DECIMAL | Montant Hors Taxes |
| `tva` | DECIMAL | Montant de la TVA |
| `montantTTC` | DECIMAL | Montant Toutes Taxes Comprises |
| `statut` | ENUM | État de paiement (impayee, payee, partielle) |
| `echeance` | DATE | Date d'échéance de paiement |

## 10. Table `Immobilisation`
**Rôle :** Suivre le patrimoine matériel et immatériel de l'entreprise pour l'amortissement.

| Colonne | Type | Description |
| :--- | :--- | :--- |
| `id` | VARCHAR (PK) | Identifiant unique |
| `code` | VARCHAR | Code d'inventaire |
| `libelle` | VARCHAR | Nom de l'actif |
| `categorie` | VARCHAR | Catégorie (Véhicules, Bâtiments, Logiciels, etc.) |
| `dateAcquisition` | DATE | Date d'achat |
| `valeurAcquisition`| DECIMAL | Prix d'achat |
| `duree` | INT | Durée d'amortissement (années) |
| `methode` | ENUM | Méthode d'amortissement (lineaire, degressive) |
| `cumulAmortissement`| DECIMAL | Amortissements déjà enregistrés |
| `vnc` | DECIMAL | Valeur Nette Comptable |
| `dotationAnnuelle` | DECIMAL | Charge d'amortissement de l'année |
| `succursale_id` | VARCHAR (FK) | Succursale d'affectation |

## 11. Table `AuditEntry`
**Rôle :** Assurer la traçabilité de sécurité et le suivi de l'activité des utilisateurs sur l'application.

| Colonne | Type | Description |
| :--- | :--- | :--- |
| `id` | VARCHAR (PK) | Identifiant unique du log |
| `timestamp` | DATETIME | Date et heure précise de l'action |
| `utilisateur` | VARCHAR | Utilisateur concerné |
| `role` | VARCHAR | Rôle de l'utilisateur lors de l'action |
| `ip` | VARCHAR | Adresse IP de connexion |
| `terminal` | VARCHAR | Dispositif utilisé (Desktop, Mobile...) |
| `action` | VARCHAR | Type d'action (CREATION, VALIDATION, SUPPRESSION, CONNEXION...) |
| `module` | VARCHAR | Module applicatif concerné |
| `objet` | VARCHAR | Description de la donnée touchée |
| `avant` | TEXT | Valeur avant modification (optionnel) |
| `apres` | TEXT | Valeur après modification (optionnel) |

## 12. Table `Parametre`
**Rôle :** Stocker les configurations globales du système et les préférences personnalisées des utilisateurs (Thème, Devise par défaut, Format de date, etc.).

| Colonne | Type | Description |
| :--- | :--- | :--- |
| `id` | VARCHAR (PK) | Identifiant unique de la configuration |
| `cle` | VARCHAR | Clé du paramètre (ex: `theme_apparence`, `devise_systeme`) |
| `valeur` | VARCHAR | Valeur du paramètre (ex: `dark`, `USD`, `fr-FR`) |
| `categorie` | VARCHAR | Catégorie (ex: `apparence`, `finance`, `localisation`, `notifications`, `ia`, `securite`) |
| `typeValeur` | ENUM | Type de donnée pour le parsing (string, boolean, number, json) |
| `utilisateur_id`| VARCHAR (FK) | Référence à l'utilisateur (NULL si paramètre global) |
| `description` | TEXT | Description expliquant à quoi sert ce paramètre |

## 13. Authentification et Sécurité (Table `Utilisateur`, `Role`, `Session`)
**Rôle :** Gérer les accès, l'authentification et les permissions des utilisateurs au sein de l'application.

### Table `Utilisateur`
| Colonne | Type | Description |
| :--- | :--- | :--- |
| `id` | VARCHAR (PK) | Identifiant unique de l'utilisateur |
| `email` | VARCHAR | Adresse email (sert souvent d'identifiant de connexion) |
| `motDePasse` | VARCHAR | Hash du mot de passe |
| `nom` | VARCHAR | Nom complet de l'utilisateur |
| `role_id` | VARCHAR (FK) | Référence au rôle principal de l'utilisateur |
| `succursale_id` | VARCHAR (FK) | Succursale d'affectation par défaut |
| `actif` | BOOLEAN | Indique si le compte est actif ou bloqué |
| `derniereConnexion`| DATETIME | Date et heure de la dernière connexion |

### Table `Role`
| Colonne | Type | Description |
| :--- | :--- | :--- |
| `id` | VARCHAR (PK) | Identifiant unique du rôle (ex: admin, comptable, auditeur) |
| `libelle` | VARCHAR | Nom d'affichage du rôle |
| `permissions` | JSON | Liste des permissions ou droits d'accès accordés |

### Table `Session`
| Colonne | Type | Description |
| :--- | :--- | :--- |
| `id` | VARCHAR (PK) | Identifiant de la session / Token |
| `utilisateur_id`| VARCHAR (FK) | Utilisateur connecté |
| `ip` | VARCHAR | Adresse IP de la session |
| `dateCreation` | DATETIME | Heure de début de la session |
| `dateExpiration`| DATETIME | Heure d'expiration de la session |

## 14. Autres Tables (Rapprochement et Tableau de Bord)
*Ces structures servent au rapprochement bancaire et au dashboard analytique.*

* **LigneReleve** : Historique des mouvements importés de la banque (`id`, `date`, `libelle`, `montant`, `sens`, `pointe`).
* **LigneCompta** : Flux comptables pour le lettrage bancaire (`id`, `date`, `libelle`, `compte`, `montant`, `sens`, `pointe`).
* **KPI** : Indicateurs clés paramétrables (`label`, `value`, `format`, `evolution`, `icon`, `color`).
