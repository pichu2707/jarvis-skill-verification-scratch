# jarvis-skill-verification-scratch

> **This is a test fixture, not a real project.** It exists to verify [jarvis-android](https://github.com/pichu2707/jarvis-android)'s `github-release-review` skill against a real GitHub repository with a real, deliberate breaking-change release (`v0.1.0` → `v0.2.0`). It is intentionally minimal and kept public so the skill has a stable, always-available real-world target to test against.

## CLI

`greet <name>` prints a greeting.

## Release history (test data)

- `v0.1.0` — initial `greet(name)`.
- `v0.2.0` — **breaking**: `greet` now takes `name` as a keyword-only argument (`feat!:` + `BREAKING CHANGE:` footer), exactly the signal the skill under test is meant to detect.
