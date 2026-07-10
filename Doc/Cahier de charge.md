# Cahier des Charges & Plan MVP : Logiciels Comptabilité OHADA & Audit ISA

## Contexte et Objectifs
Le cabinet souhaite remplacer ses processus actuels, basés sur des saisies manuelles dans des fichiers Excel contenant des macros instables, par des solutions logicielles sur-mesure. 

L'objectif principal de cette première phase est de définir un **Minimum Viable Product (MVP)** pour les deux outils. Un MVP est la version la plus épurée possible du logiciel qui possède suffisamment de fonctionnalités pour être déployée et utilisée en production par vos équipes, apportant ainsi une valeur immédiate (stabilité, centralisation, sécurité) avant d'ajouter les modules plus complexes.

## User Review Required
> [!IMPORTANT]
> Veuillez lire attentivement les sections "Périmètre du MVP" ci-dessous. Le succès d'un MVP réside dans le fait de ne développer **que l'essentiel** pour le premier lancement. Si vous pensez qu'une fonctionnalité listée dans les "Modules Futurs" est absolument bloquante pour utiliser l'outil dès le premier jour, il faudra la déplacer dans le MVP.

## Open Questions
> [!WARNING]
> 1. **Récupération des données :** Actuellement, comment vos collaborateurs récupèrent-ils les données pour faire la saisie comptable ? (Factures papier, import de fichiers bancaires, import d'autres logiciels clients ?)
> 2. **Trame d'audit :** Avez-vous déjà une trame standard de dossier d'audit (liste des sections de contrôle) au format Word ou Excel que nous pourrions utiliser comme modèle de base ?

---

## 1. Logiciel de Comptabilité (Norme OHADA)

### Périmètre du MVP (Pour remplacer la saisie Excel)
Le MVP doit assurer les fondations de la tenue comptable, de manière plus robuste et rapide qu'Excel.

*   **Administration des Dossiers :** Création des entreprises clientes, gestion des exercices comptables (dates de début et de fin).
*   **Plan Comptable OHADA :** Base de données pré-remplie avec le plan comptable général SYSCOHADA révisé, avec possibilité d'ajouter des comptes auxiliaires pour chaque client.
*   **Saisie des Écritures (Les Journaux) :**
    *   Création des journaux standards (Achats, Ventes, Trésorerie, Opérations Diverses).
    *   Interface de saisie optimisée pour la rapidité au clavier (type "grille").
    *   **Contrôle strict :** Interdiction stricte de valider une écriture si elle n'est pas équilibrée (Débit = Crédit).
*   **Restitutions de base (Consultation & Export) :**
    *   Grand Livre des comptes (avec historique des mouvements).
    *   Balance Générale (à 6 colonnes : Solde d'ouverture, Mouvements, Soldes de clôture).
    *   Brouillard et impression des journaux.
    *   **Export des données :** Capacité d'exporter facilement ces états en format PDF et Excel pour les transmettre aux clients ou pour archivage.
*   **Sécurité de base :** Système de "Brouillard" (écritures modifiables) et validation (écritures figées/verrouillées, modifiables uniquement par contre-passation).

### Modules Futurs (Post-MVP, par itérations)
*   Module d'importation de fichiers (relevés bancaires CSV/OFX) pour le rapprochement bancaire automatique.
*   Module des Immobilisations (calcul automatique des tableaux d'amortissement).
*   Génération automatique des états financiers OHADA complets (Bilan, Compte de résultat, TAFIRE).
*   Gestion de la facturation interne et intégration analytique.

---

## 2. Logiciel d'Audit Financier (Norme ISA)

### Périmètre du MVP (Pour centraliser le dossier de travail)
L'objectif premier est de ne plus avoir des dizaines de fichiers Excel éparpillés par mission et d'automatiser les revues analytiques de base.

*   **Gestion des Missions :** Création d'une mission, affectation des collaborateurs (chef de mission, assistants), définition de la période auditée.
*   **Importation de la Balance :** Module permettant d'importer la balance générale du client (format Excel/CSV) ou de se connecter directement à la base du MVP Comptabilité.
*   **Structuration Automatique du Dossier (Les Cycles) :** À partir de la balance importée, le logiciel génère automatiquement les dossiers par cycle (Cycle A : Capitaux Propres, Cycle B : Immos, Cycle C : Stocks, etc.) selon le paramétrage du cabinet.
*   **Feuilles Maîtresses (Lead Schedules) :** Calcul et affichage automatique des feuilles maîtresses par cycle, comparant l'année N et l'année N-1 (variation en valeur et en pourcentage) directement basées sur la balance.
*   **Documentation du dossier :** Pour chaque compte ou cycle, possibilité de télécharger et lier des preuves d'audit (PDF, Excel, images) et un champ texte pour les conclusions du collaborateur.
*   **Archivage de base :** Possibilité de figer une mission terminée en "lecture seule" (Archive) pour éviter toute modification ultérieure.

### Modules Futurs (Post-MVP, par itérations)
*   Module complet ISA 315 : Identification et évaluation des risques, fixation de la matérialité (seuil de signification et erreur tolérable).
*   Outils d'échantillonnage statistique pour les tests de détails.
*   Gestion des feuilles d'ajustements et de reclassements (Audit Adjustments) avec impact en temps réel sur la balance provisoire post-audit.
*   Checklists obligatoires normées (indépendance, acceptation de la mission, etc.).
*   Génération automatique des rapports (Opinion d'audit).

---

## Exigences Techniques Transversales (Dès le MVP)

*   **Application Multi-plateformes (Web & Desktop) :** Les applications seront accessibles depuis un navigateur web classique, mais seront également disponibles sous forme de véritables logiciels de bureau installables (Desktop Windows/Mac), offrant une interface dédiée, indépendante et ultra-rapide.
*   **Accessibilité Mobile (Android) :** Le système sera accompagné d'une application mobile Android. Dans le cadre du MVP, celle-ci servira principalement de compagnon : consultation rapide des tableaux de bord, suivi d'avancement, et surtout **l'acquisition de preuves** (ex: prendre en photo une facture avec son téléphone pour qu'elle s'attache directement à une écriture comptable, ou prendre des photos lors d'un inventaire physique pour l'audit).
*   **Base de données centralisée et relationnelle :** Utilisation d'une base de données robuste (ex: PostgreSQL) pour garantir l'intégrité absolue des données financières.
*   **Piste d'Audit et Traçabilité (Logs) :** *C'est le point vital oublié du premier jet.* Tout logiciel financier sérieux doit tracer en arrière-plan chaque action (Ex: "L'utilisateur X a modifié cette écriture le 12/04 à 14h00").
*   **Sauvegardes Automatisées (Backups) :** Mise en place d'une stratégie de sauvegarde en 5 points vitaux :
    1.  **Extraction quotidienne ("Dump")** automatique des bases de données de comptabilité et d'audit.
    2.  **Planification (Cron)** de ces extractions en pleine nuit (ex: 02h00) pour ne pas perturber le travail.
    3.  **Externalisation stricte :** Les fichiers de sauvegarde sont immédiatement copiés vers un serveur distant ou un cloud sécurisé (Amazon S3, etc.) différent du serveur principal.
    4.  **Politique de rétention :** Conservation intelligente pour économiser l'espace (ex: 7 derniers jours, 4 dernières semaines, 12 derniers mois).
    5.  **Tests de restauration :** Procédures prévues pour tester régulièrement que les sauvegardes peuvent bien être réinstallées en cas de crise.
*   **Authentification et Rôles :** Connexion sécurisée avec des rôles distincts pour restreindre les accès (Ex: Un "Saisisseur" ne peut pas supprimer un dossier, seul un "Manager" peut clôturer un exercice).
