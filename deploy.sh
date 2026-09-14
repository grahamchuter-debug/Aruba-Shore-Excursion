#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Building Aruba Shore Excursion…"
npm run build

echo "Deploying Aruba Shore Excursion to Cloudflare..."
npx wrangler deploy

echo "Done. Check https://arubashoreexcursion.com/ shortly."
