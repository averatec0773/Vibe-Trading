# Anthropic prompt caching, before and after

`prompt-cache-before-after.png`: the real AgentLoop with the real 107-tool registry run against a local stand-in for the Messages API (SSE streaming plus a prefix-hash cache simulation), three model calls per run, flag off then flag on. Bars split each call's input into cache read, cache write and uncached tokens as recorded in llm_usage.json. Token counts are length estimates from the stand-in, so the ratios are the evidence rather than the absolute numbers.

`mock-requests.jsonl`: one line per request the stand-in received (whether the top-level cache_control was present, whether the system prompt arrived as a marked block, tool count, message count, simulated usage).
