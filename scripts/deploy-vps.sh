#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOST="${SSH_HOST:-187.127.71.3}"
USER="${SSH_USER:-root}"
PORT="${SSH_PORT:-22}"
TARGET="${SSH_TARGET:-/var/www/html/}"

echo "Deploying ${ROOT} -> ${USER}@${HOST}:${TARGET}"

rsync -avz --delete \
  --exclude '.git/' \
  --exclude '.github/' \
  --exclude 'content/' \
  --exclude 'scripts/' \
  --exclude 'README.md' \
  --exclude '.cursor/' \
  -e "ssh -p ${PORT} -o StrictHostKeyChecking=accept-new" \
  "${ROOT}/" "${USER}@${HOST}:${TARGET}"

echo "Done. Check: https://powercurvemedia.com/"
