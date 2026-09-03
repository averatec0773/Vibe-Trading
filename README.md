# Screenshots for the "attempt elapsed clock" bug report

Captured with Playwright (real Chromium, 1200x675, light theme) against two local
instances built from the same tree: `before-*` at `f4a6b6e1` (unfixed),
`after-*` with the fix applied. Same prompts, same click sequence.

- `before-1` / `after-1`: ~30 s after sending a ~1 min prompt.
- `before-2` / `after-2`: after clicking **Runtime**, waiting 6 s, and clicking the
  session again.
- `before-3` / `after-3`: a tool-less turn right after it finished (live path).
- `before-4` / `after-4`: the same turn after a page reload (history hydration).
