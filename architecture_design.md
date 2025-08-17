# Architecture de l'Application Zitouna Tamkeen

## Vue d'ensemble

L'application Zitouna Tamkeen sera développée comme une application web progressive (PWA) utilisant React avec une expérience adaptative pour mobile et desktop. Cette approche permettra une maintenance plus simple qu'une application React Native native tout en offrant une expérience utilisateur optimale sur tous les appareils.

## Architecture Technique

### Frontend
- **Framework**: React 18 avec TypeScript
- **Styling**: Tailwind CSS + Shadcn/UI pour les composants
- **Animations**: Framer Motion pour les animations fluides
- **Responsive Design**: Approche mobile-first avec breakpoints adaptatifs
- **PWA**: Service Workers pour le fonctionnement hors ligne

### Backend
- **Framework**: Node.js avec Express ou Flask (Python)
- **Base de données**: MongoDB ou PostgreSQL
- **Authentification**: JWT avec rôles (utilisateur/admin)
- **API**: RESTful API avec documentation Swagger

### Déploiement
- **Frontend**: Vercel ou Netlify
- **Backend**: Railway ou Heroku
- **Base de données**: MongoDB Atlas ou Supabase

## Modèles de Données

### Utilisateur
```typescript
interface User {
  id: string;
  email: string;
  nom: string;
  prenom: string;
  telephone: string;
  role: 'user' | 'admin';
  dateCreation: Date;
  statut: 'actif' | 'inactif';
}
```

### Guide de Documents
```typescript
interface DocumentGuide {
  id: string;
  titre: string;
  description: string;
  etapes: Etape[];
  documentsRequis: DocumentRequis[];
  dateCreation: Date;
  dateModification: Date;
  statut: 'actif' | 'inactif';
}

interface Etape {
  id: string;
  numero: number;
  titre: string;
  description: string;
  instructions: string;
  documentsAssocies: string[];
}

interface DocumentRequis {
  id: string;
  nom: string;
  description: string;
  obligatoire: boolean;
  formatAccepte: string[];
  tailleMax: number;
}
```

### Soumission Utilisateur
```typescript
interface Soumission {
  id: string;
  utilisateurId: string;
  guideId: string;
  etapeActuelle: number;
  documentsUploades: DocumentUploade[];
  statut: 'en_cours' | 'complete' | 'en_attente_revision';
  dateCreation: Date;
  dateModification: Date;
}

interface DocumentUploade {
  id: string;
  documentRequisId: string;
  nomFichier: string;
  cheminFichier: string;
  dateUpload: Date;
  statut: 'en_attente' | 'valide' | 'rejete';
  commentaires?: string;
}
```

## Flux Utilisateur

### Utilisateur Mobile/Desktop
1. **Accueil**: Présentation de Zitouna Tamkeen avec animations
2. **Authentification**: Connexion/Inscription
3. **Tableau de bord**: Vue d'ensemble des demandes en cours
4. **Guides disponibles**: Liste des processus de demande
5. **Processus étape par étape**: Interface guidée pour soumettre les documents
6. **Suivi**: Statut des demandes et notifications

### Administrateur
1. **Tableau de bord admin**: Statistiques et vue d'ensemble
2. **Gestion des guides**: Création/modification des processus
3. **Gestion des utilisateurs**: Administration des comptes
4. **Révision des soumissions**: Validation des documents
5. **Rapports**: Analytics et métriques

## Expérience Responsive

### Mobile (< 768px)
- Navigation par onglets en bas
- Cartes empilées verticalement
- Formulaires optimisés pour le tactile
- Animations subtiles pour les transitions

### Desktop (≥ 768px)
- Sidebar de navigation
- Layout en grille pour les cartes
- Tooltips et hover effects
- Animations plus élaborées

## Thème Zitouna Tamkeen

### Palette de couleurs
- **Primaire**: Vert olive (#6B8E23) - inspiré du logo
- **Secondaire**: Vert foncé (#2F4F2F)
- **Accent**: Or (#DAA520)
- **Neutre**: Gris (#F5F5F5, #E5E5E5, #CCCCCC)

### Typographie
- **Titres**: Poppins (moderne et lisible)
- **Corps**: Inter (optimisé pour la lecture)
- **Arabe**: Noto Sans Arabic (support multilingue)

### Animations
- **Logo**: Animation de shading avec effet de profondeur
- **Transitions**: Smooth et naturelles (300ms ease-in-out)
- **Micro-interactions**: Feedback visuel sur les actions utilisateur

