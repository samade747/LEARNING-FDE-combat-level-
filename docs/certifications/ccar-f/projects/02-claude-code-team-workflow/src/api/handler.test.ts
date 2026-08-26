// Sample file so .claude/rules/testing-conventions.md's glob (**/*.test.*) has something to match.
import { handleRefundRequest } from "./handler";

test("rejects non-object input", () => {
  expect(handleRefundRequest(null).errorCategory).toBe("validation");
});
