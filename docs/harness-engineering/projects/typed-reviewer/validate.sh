#!/usr/bin/env bash
# Usage: ./validate.sh verdict.json
# Exit 0 = valid typed verdict. Exit 1 = protocol break -> route to NEEDS_HUMAN.
set -euo pipefail

FILE="${1:?usage: validate.sh <verdict.json>}"

verdict=$(jq -r '.verdict // empty' "$FILE")
reasons_len=$(jq '.reasons // [] | length' "$FILE")
files_present=$(jq 'has("files_reviewed")' "$FILE")

if [[ "$verdict" != "PASS" && "$verdict" != "FAIL" && "$verdict" != "NEEDS_HUMAN" ]]; then
  echo "PROTOCOL BREAK: verdict field is '$verdict', not one of PASS/FAIL/NEEDS_HUMAN -> route to NEEDS_HUMAN"
  exit 1
fi

if [[ "$reasons_len" -lt 1 ]]; then
  echo "PROTOCOL BREAK: reasons array is empty -> route to NEEDS_HUMAN"
  exit 1
fi

if [[ "$files_present" != "true" ]]; then
  echo "PROTOCOL BREAK: files_reviewed field missing -> route to NEEDS_HUMAN"
  exit 1
fi

echo "VALID: verdict=$verdict, reasons=$reasons_len, files_reviewed present"
exit 0
