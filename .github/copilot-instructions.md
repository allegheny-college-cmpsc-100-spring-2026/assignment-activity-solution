# Copilot Workspace Instructions

## 1) Project Overview
- Python learning assignment focused on small function implementation and tests.
- This repository is an educational template. Keep code simple and clear.

## 2) Environment / Tooling
- Python 3.11+ assumed.
- Test command: `uv run pytest -s` from repository root.
- Run app: `uv run python src/main.py`.

## 3) Code patterns and conventions
- Minimal dependencies (standard library only).
- Keep functions small and testable.
- Include docstrings and comments for learners.
- In this teaching repo, some type hints may be intentionally wrong for static typing demonstration.

## 4) Behavior for Copilot assistance
- Require user to produce their own tests; provide guidance and examples rather than complete test suites (matches existing learner-centered agent in `.github/agents/coding-agent.agent.md`).
- Do not provide any code for tests; instead, guide users using higher-level concepts and examples.
- Provide the command "uv run pytest -s" to run tests, but do not provide the actual test code.
- For bug fixes or refactors, do not overwrite the existing educational prompts.
- Encourage users to understand and debug code rather than just providing correct code snippets. This is a learning exercise, so the focus should be on education rather than just providing correct answers.

## 5) Recommended workflow for contributors
1. Read `src/main.py`.
2. Implement/package one change at a time.
3. Run `uv run pytest -s` and validate output.
4. Prefer `black` style

## 6) Notes for agent developers
- This repo is tiny; no monorepo complexities.
- Keep edits confined to `src/` for features
- Leave `main()` as an entrypoint and avoid changing interactive I/O behavior unless requested.
