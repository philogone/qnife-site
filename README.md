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
