# Direct Code Audit: Agentic Monte Carlo (AMC)

**Audit date:** 2026-10-27  
**Repository:** https://github.com/layer6ai-labs/Agentic-Monte-Carlo  
**Paper:** ICML 2026, https://proceedings.mlr.press/v306/hwang26i.html  
**Repository license:** Apache-2.0 at the root. This does not automatically settle licenses for every vendored environment or dataset.  
**Status:** A potential particle-independence defect was identified in the current public main snapshot. It must be reproduced or clarified before using this code as a baseline. This is not evidence that the published paper's reported results are invalid.

## 1. Files and behavior inspected

- smc/agents/agent.py, current blob SHA 5199e32fbdb5f16a246178cbbd308537034659e0
- smc/bootstrap_filter.py, current blob SHA 2611c6755811629844c340fe83ec1123152d4092
- smc/clients.py, current blob SHA 256ca60c76e372464163a98bb6faf85cf806e2b6
- smc/smc.py, current blob SHA a995144829f87aa3757a3c5d9e65db5653781bd5

## 2. Potential correctness issue: cloned particles can share one mutable environment client

In smc/bootstrap_filter.py, resampling samples parents with replacement using random.choices(...), then replaces the population with agent.clone() for each selected parent (source: https://github.com/layer6ai-labs/Agentic-Monte-Carlo/blob/main/smc/bootstrap_filter.py).

In smc/agents/agent.py, AgentGymAgent.clone() assigns new_client = self.client, resets that same client, replays the parent's action history through it, and passes the same client object into the new agent (source: https://github.com/layer6ai-labs/Agentic-Monte-Carlo/blob/main/smc/agents/agent.py).

In smc/clients.py, AgentGymClient.reset() sends a reset request for the existing env_id, and step() sends actions to that same env_id; reset does not create an independent client/environment (source: https://github.com/layer6ai-labs/Agentic-Monte-Carlo/blob/main/smc/clients.py).

Therefore, when resampling selects the same parent multiple times, its cloned children can share the same mutable client/environment ID. The next parallel step can then apply multiple agents' actions to one environment while each agent maintains a separate conversation and action history. This appears to violate the independent-particle assumption used by the filter.

### Scope of the finding

- This is a code-level defect hypothesis with a clear aliasing path, not yet a reproduced runtime failure.
- It does not establish that the authors' reported paper results are invalid; the public branch may differ from the exact experiment snapshot, and a controlled reproduction is required.
- Do not silently patch the baseline and then call it an exact reproduction. Preserve an upstream snapshot, make the minimal fix in a separate patch, and report both behavior and provenance if this baseline is later used.

## 3. Required verification before any benchmark comparison

1. Construct a minimal local deterministic test with two resampling children selected from one parent.
2. Assert that each child has a distinct client object and distinct environment ID; assert that stepping child A cannot change child B's environment state.
3. If the test fails, preserve the unmodified source snapshot and create a separate corrected fork/patch. Do not infer paper-result invalidity from the test alone.
4. Verify environment-specific licenses and the exact experiment commit before any full reproduction.

No API calls, formal benchmark run, or code modification was performed in this audit.
