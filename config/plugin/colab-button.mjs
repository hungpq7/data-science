import path from 'node:path';
import { fileURLToPath } from 'node:url';

const OWNER = 'hungpq7';
const REPOSITORY = 'data-science';
const BRANCH = 'main';

/*
 * Repository layout assumed:
 *
 * repository/
 * ├── myst.yml
 * ├── plugins/
 * │   └── colab-link.mjs
 * └── notebooks/
 *     └── example.ipynb
 */
const PROJECT_ROOT = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  '..',
);

function encodePath(filePath) {
  return filePath
    .split('/')
    .map(encodeURIComponent)
    .join('/');
}

const colabTransform = {
  name: 'add-colab-link',
  stage: 'document',

  plugin: () => (tree, file) => {
    const sourceFile = file.path;

    // Add the link only to actual Jupyter notebooks.
    if (!sourceFile || path.extname(sourceFile) !== '.ipynb') {
      return tree;
    }

    const notebookPath = path
      .relative(PROJECT_ROOT, path.resolve(sourceFile))
      .split(path.sep)
      .join('/');

    // Avoid links for files outside the repository.
    if (notebookPath.startsWith('../')) {
      return tree;
    }

    const url =
      `https://colab.research.google.com/github/` +
      `${OWNER}/${REPOSITORY}/blob/${BRANCH}/` +
      encodePath(notebookPath);

    tree.children.unshift({
      type: 'paragraph',
      children: [
        {
          type: 'link',
          url,
          children: [
            {
              type: 'text',
              value: 'Open this notebook in Google Colab',
            },
          ],
        },
      ],
    });

    return tree;
  },
};

export default {
  name: 'Google Colab links',
  transforms: [colabTransform],
};