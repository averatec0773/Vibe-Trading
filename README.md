# Screenshots for the "attempt elapsed clock" bug report

Four annotated strips, each assembled from Playwright viewport captures (Chromium,
1200x675, dark theme) taken against two local instances built from the same tree:
"before" at `f4a6b6e1` (unfixed), "after" with the fix applied. Same prompts, same
click sequence. `t` is the wall-clock time since the prompt was sent, measured in
the page with `Date.now()` about a second before each capture; the boxed number is
what the UI showed at that moment.

- `A-before-tab-switch.png` / `B-after-tab-switch.png`: ~45 s into a run → click
  **Runtime**, wait 6 s, click the session again → ~25 s later.
- `C-before-toolless-reload.png` / `D-after-toolless-reload.png`: a tool-less turn
  right after it finished, then the same turn after a page reload.
