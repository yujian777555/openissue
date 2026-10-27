# Exploratory Lane: Evolutionary Search over Black-Box Agent Trajectories

**Screen date:** 2026-10-27  
**Status:** Exploratory only. No method, thesis topic, or innovation point is approved.  
**User constraint:** Communication evolution is excluded from the thesis candidate pool.  
**Project boundary:** This research belongs only to yujian777555/openissue.

## 1. Research question

Can a structured evolutionary search improve a frozen black-box LLM agent's test-time action search by recombining partial trajectories only when their observable execution states are compatible, outperforming strong sequential Monte Carlo and standard search baselines?

The candidate is not “replace SMC with a genetic algorithm.” A plain algorithm swap is not a defensible innovation. The possible mechanism under examination is **state-validated trajectory recombination**:

- **Genotype:** an action/observation trajectory with an explicit task-instance identity and provenance for each action.
- **Mutation:** branch from a saved/replayed prefix and ask the unchanged base agent to generate an alternative continuation, then re-execute it in the environment.
- **Crossover:** identify two parent trajectories that reach an equivalent observable state under the same task instance; splice a suffix only at that compatibility point, then replay/validate the resulting plan. Never use hidden evaluator state to choose an action or splice point. If exact state equivalence is unavailable from allowed observations, use an explicit replay-based validity check or drop the operator.
- **Selection:** retain candidates by task success and a diversity criterion tied to behaviorally distinct, valid trajectories. Diversity is a search safeguard, not by itself the novelty claim.
- **Invariant:** every candidate must be re-executable from the task's initial state; invalid or semantically incompatible offspring are rejected, not silently counted as new individuals.

## 2. Closest work and what it blocks

| Work | Established mechanism | Consequence |
|---|---|---|
| **Agentic Monte Carlo (AMC), ICML 2026** — https://proceedings.mlr.press/v306/hwang26i.html | Treats optimal black-box agent behavior as a posterior over trajectories and uses a learned value function with sequential Monte Carlo (SMC) resampling, leaving the base model unchanged. Official code: https://github.com/layer6ai-labs/Agentic-Monte-Carlo | Strongest direct baseline for test-time search over black-box tool-agent trajectories. A GA-versus-SMC comparison alone is not enough. The current public code also has a potential clone/client aliasing issue; see research/AMC_CODE_AUDIT.md. |
| **Adaptive SMC (ASMC), ICML 2026** — https://proceedings.mlr.press/v306/wang26kb.html | Adapts particle population to task difficulty and adds cache-coherent resampling for LLM token trajectories. | Adaptive population and efficient resampling are already studied. Its task is token-generation inference rather than stateful tool-action trajectories. |
| **Keep the Lineages Alive (LP-SMC), 2026 preprint** — https://arxiv.org/abs/2610.25932 | Uses Chopthin resampling plus a weight floor to preserve low-weight lineages in diffusion-LLM decoding. | “Preserve diversity during resampling” or “avoid particle collapse” alone is not novel. The domain differs, but this is direct algorithmic adjacency. |
| **EVOTOOL, ACL 2026** — https://aclanthology.org/2026.acl-long.2016/ | Evolves a reusable modular tool-use policy via trajectory-grounded blame, targeted module mutation, and diversity-aware population selection. | Policy-level evolutionary search and trajectory-informed mutation are already established. A per-instance trajectory search method must be clearly distinguished from reusable policy evolution. |
| **DUPO, EMNLP 2026** — https://aclanthology.org/2026.emnlp-main.836/ | Separates PLAN and TOOL spans and uses chain-aware upstream advantages in policy optimization. | Typed plan/action separation is adjacent prior art, but DUPO is RL training rather than EC. |
| **T-MAP, EMNLP 2026** — https://aclanthology.org/2026.emnlp-main.68/ | Uses trajectory-aware evolutionary search to discover adversarial prompts that realize attacks through multi-step tool execution. | Trajectory-aware EA is not new by itself. Its adversarial objective differs from benign task-completion optimization. |
| Classical plan-space genetic algorithms, genetic programming, MCTS, beam search, and best-of-N | Search over plans or action sequences, with varying assumptions about state transitions and recombination. | These must be included before claiming a new operator. The classical planning/GP literature has not yet been exhaustively audited for this lane. |

## 3. Why this may or may not be a useful direction

Potentially meaningful gap: a tool-agent trajectory is not an ordinary text string. Actions change the environment, so arbitrary sequence crossover can splice a suffix whose preconditions no longer hold. A compatibility-aware crossover with replay validation may address a specific representational failure that standard string-level recombination ignores.

Reasons to be skeptical:
- State-compatible splice points may be rare, making crossover ineffective.
- Replaying a candidate can be expensive and can introduce stochastic variation.
- If the operator needs hidden state or privileged environment access, it is not a fair agent method.
- Existing plan-space genetic algorithms may already contain equivalent state-aware crossover.
- AMC's current public code may require a correctness fix before it can serve as a reliable baseline.
- A performance gain caused only by more model calls or environment interactions is not acceptable; compare at matched interaction/query counts as a control, not as the thesis's main contribution.

## 4. Falsifiable gate I0

Do not implement until all of the following are satisfied:

1. Audit plan-space GA/GP and evolutionary planning papers for state-compatible recombination and executable plan repair.
2. Resolve the AMC clone/client aliasing issue through a minimal local test and record the exact source commit used for any baseline.
3. Specify the observable-state equivalence relation and show it does not read hidden labels, gold solutions, or evaluator internals.
4. Define a small deterministic tool environment where state snapshots/replay are legal, plus held-out task compositions and verifiable success predicates.
5. Pre-register comparisons: AMC/SMC, best-of-N, beam/MCTS where feasible, mutation-only EA, naive sequence crossover, and state-validated crossover. Use identical model, action, and environment-interaction limits for primary comparisons.
6. Require improvements on held-out task compositions and valid execution rate, not merely training-task success.
7. **Stop** if state-aware crossover does not improve over mutation-only EA and the strongest feasible non-EA search, or if prior art already covers the operator.

## 5. Next action

Complete the prior-art audit for state-compatible plan crossover and inspect AMC's exact environment-cloning semantics. Only then decide whether this lane passes Gate I0. No API experiments, formal benchmark runs, or implementation are authorized by this screen.
