# Screenshots for the "attempt elapsed clock" bug report

Four annotated strips. Each one is assembled from Playwright viewport captures
(Chromium, 1200x675, dark theme) taken against two local instances built from the
same tree: "before" at `f4a6b6e1` (unfixed), "after" with the fix applied. Same
prompts, same clicks. `t` is the wall clock since the prompt was sent, measured in
the page with `Date.now()` about a second before each capture. The boxed number is
what the UI showed at that moment.

- `A-before-tab-switch.png` and `B-after-tab-switch.png`: about 45 s into a run,
  click Runtime, wait 6 s, click the session again, then wait another 25 s.
- `C-before-toolless-reload.png` and `D-after-toolless-reload.png`: a tool-less
  turn right after it finished, then the same turn after a page reload.
