# qnife-site

Site vitrine de Qnife (qnife.fr). Astro, statique, déployé par GitHub Actions sur GitHub Pages.

```bash
npm install
npm run dev      # aperçu local http://localhost:4321
npm run build    # génère dist/
```

- Photos : `python scripts/build-images.py` (sélection → WebP 480/800/1200 + `src/data/photos.json`). Les sources (export Instagram, séance photo) restent hors dépôt.
- Image de partage : `python scripts/make-og.py`.
- Contenu éditable : `src/data/site.ts` (coordonnées, prix), pages dans `src/pages/`.
- Domaine : `public/CNAME` = qnife.fr. Le sous-domaine `tool.qnife.fr` reste libre pour KnifeForge.
- Aucun cookie, aucun traceur.

## Design figé

- Référence écrite : `DESIGN.md` (couleurs, typo, formes, interdits). Version validée : tag `v1.0-design`.
- Référence visuelle : `tests/visual/*.png` (7 pages x mobile et bureau).
- Avant toute publication : `npm run build && npm run visual` doit répondre « Design identique aux références ».
- Changement de design voulu : modifier, puis `npm run visual:update`, relire les captures, committer.
- Icônes : `python scripts/make-icons.py`.

## Modifier les textes

Les textes sont dans `src/content/pages/`, un fichier Markdown par page (`accueil.md`, `couteaux.md`, `atelier.md`, `sur-mesure.md`, `contact.md`, `mentions-legales.md`, `404.md`).

- Le bloc entre `---` en haut du fichier contient les textes courts : titres, intitulés, boutons, étapes, listes. Chaque ligne est `clé: valeur`. Mettre la valeur entre guillemets `"..."` si elle contient `:` ou commence par un caractère spécial.
- Pour un titre sur deux lignes, écrire `\n` dans la valeur, par exemple `"Votre histoire,\nvotre couteau."`.
- Les listes sont des tirets indentés sous la clé.
- Le corps du fichier (sous le second `---`) contient les longs paragraphes, avec `## Titre` pour une section. Pour un retour à la ligne sans nouveau paragraphe, finir la ligne par `\`.
- Les apostrophes restent droites (`'`) : le Markdown ne les transforme pas.
- Le titre et la description (balise `<title>`, moteurs de recherche) sont les deux premières lignes de chaque fichier.
- Les adresse, e-mail et prix viennent de `src/data/site.ts`, sauf dans les pages Mentions légales (écrits en dur dans le Markdown). Si l'un change, penser à mettre à jour les deux endroits.
- Vérifier avant de publier : `npm run build`, puis `npm run visual`.
