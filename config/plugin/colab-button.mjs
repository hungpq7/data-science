import path from 'node:path';
import { fileURLToPath } from 'node:url';

const OWNER = 'hungpq7';
const REPOSITORY = 'data-science';
const BRANCH = 'main';

/*
 * Assumes:
 *
 * repository/
 * ├── myst.yml
 * ├── plugins/
 * │   └── colab-link.mjs
 * └── notebooks/
 *     └── example.ipynb
 */
const REPOSITORY_ROOT = fileURLToPath(
  new URL('../', import.meta.url),
);

function encodePath(value) {
  return value
    .split('/')
    .map(encodeURIComponent)
    .join('/');
}

const plugin = {
  name: 'Colab page links',

  transforms: [
    {
      name: 'add-colab-link',
      stage: 'document',

      plugin: () => (tree, file) => {
        const sourceFile = file.path
          ? path.resolve(String(file.path))
          : '';

        // This should appear in the terminal during the build.
        console.log(
          `[colab-link] processing: ${sourceFile || '<no file path>'}`,
        );

        // Only notebook pages receive the link.
        if (!sourceFile.toLowerCase().endsWith('.ipynb')) {
          return;
        }

        const notebookPath = path
          .relative(REPOSITORY_ROOT, sourceFile)
          .split(path.sep)
          .join('/');

        if (
          !notebookPath ||
          notebookPath.startsWith('../') ||
          path.isAbsolute(notebookPath)
        ) {
          console.warn(
            `[colab-link] file is outside repository root: ${sourceFile}`,
          );
          return;
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
                  value: 'Open in Google Colab',
                },
              ],
            },
          ],
        });

        console.log(`[colab-link] added: ${url}`);
      },
    },
  ],
};

export default plugin;