---
name: Qnife
description: "Coutelier artisan à Haubourdin : un atelier sombre, des couteaux nommés, un ton espiègle sans bruit."
colors:
  ink: "oklch(0.14 0.004 260)"
  anthracite: "oklch(0.23 0.006 260)"
  graphite: "oklch(0.34 0.006 260)"
  mist: "oklch(0.74 0.005 260)"
  paper: "oklch(0.97 0.004 90)"
typography:
  display:
    fontFamily: "Mostra Nuova, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(3.4rem, 13vw, 8.5rem)"
    fontWeight: 700
    lineHeight: 0.92
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Mostra Nuova, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(2.4rem, 7vw, 4.5rem)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.03em"
  body:
    fontFamily: "Mostra Nuova, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 300
    lineHeight: 1.65
  label:
    fontFamily: "Mostra Nuova, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 700
  logo:
    fontFamily: "Petit Formal Script, Snell Roundhand, Georgia, serif"
    fontSize: "2.4rem"
    fontWeight: 400
rounded:
  card: "1.25rem"
  panel: "1.75rem"
  pill: "999px"
spacing:
  gutter: "clamp(1.25rem, 5vw, 4rem)"
  section: "clamp(4rem, 12vw, 8rem)"
components:
  button-primary:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0.9rem 1.7rem"
    height: "3.5rem"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "0.9rem 1.7rem"
  card-knife:
    backgroundColor: "{colors.anthracite}"
    rounded: "{rounded.card}"
  tile-price:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.card}"
    padding: "1.75rem"
  chip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "0.4rem 0.9rem"
---

# Design System: Qnife

## Overview

**Creative North Star: "Le tablier du coutelier"**

Un atelier de nuit, mais un atelier où l'on rit : fond encre, photographies chaudes de forge, et une interface qui joue au lieu de poser. Le noir, l'anthracite et le blanc cassé portent tout ; la couleur n'existe que dans les photos. L'espièglerie vient de la forme (pastille inclinée, cartes légèrement penchées, bandeau défilant, sceau qui tourne), jamais d'une teinte de plus.

Le ton est sobre et chaleureux dans les mots : pas d'exclamations, pas de jargon. Le jeu est dans le geste visuel, la voix reste posée.

**Key Characteristics:**
- Noir / anthracite / blanc cassé, aucune couleur d'accent : les photos font le reste.
- Arrondis généreux sur les surfaces (cartes 1.25rem, panneaux 1.75rem), boutons en pilule.
- Plat au repos : séparation par aplats et filets, pas d'ombre de profondeur.
- Un seul grand mouvement par écran (bandeau, sceau, survol des cartes).
- Typographie géométrique en gras serré pour les titres ; script réservé au Q du logo.

## Colors

Une palette de nuit à cinq valeurs, tintée froid (teinte 260), plus un blanc cassé chaud.

### Neutral
- **Encre d'atelier** (oklch(0.14 0.004 260)): fond de page et texte sur surface claire.
- **Anthracite de la forge** (oklch(0.23 0.006 260)): fonds de sections secondaires et de cartes avant chargement de la photo.
- **Graphite** (oklch(0.34 0.006 260)): filets et séparateurs.
- **Brume d'acier** (oklch(0.74 0.005 260)): texte secondaire, survol du bouton principal.
- **Papier craie** (oklch(0.97 0.004 90)): texte principal sur sombre, fond de la seule section claire (tarifs) et du bandeau.

### Named Rules
**The Photo-Only Colour Rule.** Aucune couleur n'est ajoutée à l'interface. Toute teinte vient d'une photographie.
**The One Light Section Rule.** Les surfaces claires (bandeau, tarifs) sont rares et franches : jamais de gris moyen entre l'encre et le papier craie.

## Typography

**Display Font:** Mostra Nuova Bold (repli Avenir Next, Segoe UI, system-ui)
**Body Font:** Mostra Nuova Light/Regular
**Logo:** Petit Formal Script, uniquement pour le « Q »

**Character:** Une géométrique chaleureuse en gras serré pour parler fort, en maigre aéré pour lire. Le script du Q est la signature de la main.

### Hierarchy
- **Display** (700, clamp(3.4rem, 13vw, 8.5rem), 0.92): titre d'accueil.
- **Headline** (700, clamp(2.4rem, 7vw, 4.5rem), 1): titres de section.
- **Body** (300, 1.0625rem, 1.65, 62ch max): textes courants.
- **Label** (700, 0.9–1.1rem): pastilles, noms de couteaux, boutons.

### Named Rules
**The Tight Bold Rule.** Les titres sont gras, interligne ≤ 1, crénage serré (≥ -0.04em). Le corps reste maigre.

## Layout

Conteneur de 78rem, gouttière fluide (1.25rem à 4rem), sections séparées par 4rem à 8rem. Mobile d'abord : une colonne, grilles de 2 puis 4 cartes dès 52rem. Le hero passe en deux colonnes (texte, photo) dès 52rem. Pas de défilement horizontal à aucune largeur.

## Elevation & Depth

Plat par défaut : la profondeur vient du contraste entre aplats (encre, anthracite, papier) et de la rotation légère des cartes, pas d'ombres. Aucune exception : la pastille d'accueil n'a pas d'ombre non plus.

### Named Rules
**The Flat-At-Rest Rule.** Aucune ombre sur une surface au repos ; le survol relève la carte (translation, rotation à 0), il ne l'ombre pas.

## Shapes

Arrondis généreux : cartes 1.25rem, panneaux 1.75rem, tous les boutons, chips et étiquettes en pilule. Cartes penchées de 1 à 1.5 degré en alternance. Le sceau est un disque.

## Components

### Buttons
- **Shape:** pilule (999px), hauteur 3.5rem.
- **Primary:** fond papier craie, texte encre ; sur fond clair, fond encre et texte papier. Survol : fond brume d'acier.
- **Ghost:** transparent, filet 1.5px papier ; au survol il se remplit.

### Cards / Containers
- **Corner Style:** 1.25rem. Photo plein cadre, étiquette en pilule blanche en bas à gauche.
- **Hover:** zoom 1.03 de la photo, la carte se redresse.

### Tiles (tarifs)
Quatre tuiles alternées encre et papier, prix en gras 2.4rem, mention « dès » en maigre.

### Navigation
Logo Q en script à gauche, quatre liens en ligne à droite, soulignement au survol et page courante. Pas de menu burger.

### Sceau
Disque papier craie avec le texte « COUTELIER DES HAUTS-DE-FRANCE » en cercle qui tourne (22 s), Q au centre. Immobile si l'utilisateur réduit les animations.

## Do's and Don'ts

### Do:
- **Do** garder l'interface en noir, anthracite et papier craie ; laisser les photos apporter la couleur.
- **Do** utiliser le gras serré pour les titres et le maigre pour le corps.
- **Do** limiter le mouvement à un geste fort par écran et couper l'animation si l'utilisateur la réduit.
- **Do** écrire d'une voix sobre et chaleureuse.

### Don't:
- **Don't** ajouter une couleur d'accent à l'interface.
- **Don't** mettre d'ombre de profondeur sur une surface au repos.
- **Don't** utiliser des glyphes Unicode ou emoji comme icônes ou séparateurs ; dessiner un symbole.
- **Don't** inventer prix, délais, avis ou chiffres que le coutelier n'a pas fournis.
