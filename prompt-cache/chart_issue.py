"""Issue evidence chart from real llm_usage.json files (no mock): fixed prefix vs conversation per call."""
from __future__ import annotations
import glob, json, os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

H2 = "/private/tmp/claude-501/-Users-averatec-CODING-github-daily/67dc4658-183c-4da2-b638-efcfd39c0fe0/scratchpad/vt-home"
homes = [os.path.expanduser("~/.vibe-trading"), H2, H2 + "-baseline"]
runs = []
for h in homes:
    for f in sorted(glob.glob(h + "/runs/*/llm_usage.json")):
        u = json.load(open(f))
        if u["per_iteration"]:
            runs.append((f.split("/")[-2], u))
all_in = [x["input_tokens"] for _, u in runs for x in u["per_iteration"]]
floor = min(all_in)
n_calls = len(all_in)
biggest = max(runs, key=lambda r: len(r[1]["per_iteration"]))
name, u = biggest
calls = list(range(1, len(u["per_iteration"]) + 1))
inputs = [x["input_tokens"] for x in u["per_iteration"]]
prefix = [min(v, floor) for v in inputs]
tail = [v - p for v, p in zip(inputs, prefix)]

fig, axes = plt.subplots(1, 2, figsize=(12, 4.2), gridspec_kw={"width_ratios": [3, 2]})
ax = axes[0]
ax.bar(calls, prefix, color="#c0392b", label=f"resent static prefix (floor {floor:,} tokens)")
ax.bar(calls, tail, bottom=prefix, color="#7f8c8d", label="conversation tail")
ax.set_title(f"One real run ({len(calls)} model calls, claude-sonnet-5): input tokens billed per call")
ax.set_xlabel("model call"); ax.set_ylabel("input tokens"); ax.legend(loc="lower right")
ax.set_ylim(0, max(inputs) * 1.08)
ax = axes[1]
ax.hist(all_in, bins=20, color="#c0392b")
ax.axvline(floor, color="black", linestyle="--")
ax.set_title(f"All {n_calls} calls across {len(runs)} runs: input tokens per call")
ax.set_xlabel("input tokens"); ax.set_ylabel("calls")
ax.annotate(f"floor {floor:,}\n(system prompt + 107 tool schemas)", xy=(floor, ax.get_ylim()[1] * 0.9), xytext=(floor + 2000, ax.get_ylim()[1] * 0.9), fontsize=8)
fig.suptitle("Vibe-Trading built-in agent, Anthropic provider, no cache_control sent: the static prefix is billed at full price on every call")
fig.tight_layout()
out = sys.argv[1]
fig.savefig(out, dpi=140)
print("wrote", out, "runs", len(runs), "calls", n_calls, "floor", floor, "sum_input", sum(all_in), "biggest_run", name)
