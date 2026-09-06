# Anthropic prompt caching, before and after

`prompt-cache-before-after.png`: the real AgentLoop with the real 107-tool registry run against a local stand-in for the Messages API (SSE streaming plus a prefix-hash cache simulation), three model calls per run, flag off then flag on. Bars split each call's input into cache read, cache write and uncached tokens as recorded in llm_usage.json. Token counts are length estimates from the stand-in, so the ratios are the evidence rather than the absolute numbers.

`mock-requests.jsonl`: one line per request the stand-in received (whether the top-level cache_control was present, whether the system prompt arrived as a marked block, tool count, message count, simulated usage).

`prefix-cost-per-call.png`: real usage data from 19 local runs (194 model calls, claude-sonnet-5) read from each run's llm_usage.json. Left: one 47-call run, each bar split at the observed floor of 70,389 input tokens (system prompt plus 107 tool schemas) versus the conversation tail. Right: histogram of input tokens per call across all 194 calls. Produced by `chart_issue.py`.
