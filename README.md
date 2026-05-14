# cicd-predictor-demo

Demo project for the CI/CD Failure Predictor diploma defense. Three
pre-staged commits trigger three different predictor decisions:

| Commit                | Diff                                | Expected decision |
|-----------------------|-------------------------------------|-------------------|
| `01-readme-typo`      | one-character README typo           | `AUTO_APPROVE`    |
| `02-add-dependency`   | bump deps, regenerate lockfile      | `WARN`            |
| `03-dockerfile-rewrite` | rewrite Dockerfile + restructure | `BLOCK`           |

These are reproducible demo scenarios — not real bugs.
