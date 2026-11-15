import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Textes des pages, en Markdown : un fichier par page dans src/content/pages/.
// Le frontmatter (entre ---) porte le titre et la description ; le corps porte le texte.
const pages = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/pages' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
  }).passthrough(), // les autres champs (titres, boutons, listes) sont libres par page
});

export const collections = { pages };
