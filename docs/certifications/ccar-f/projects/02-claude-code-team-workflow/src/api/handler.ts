// Sample file so .claude/rules/api-conventions.md's glob (src/api/**/*) has something to match.
export function handleRefundRequest(input: unknown): { errorCategory?: string; ok: boolean } {
  if (typeof input !== "object" || input === null) {
    return { errorCategory: "validation", ok: false };
  }
  return { ok: true };
}
