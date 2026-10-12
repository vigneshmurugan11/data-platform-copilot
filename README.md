# data-platform-copilot

An AI copilot for data platforms, built with Python and the Anthropic Claude API. This is a learning project that I'm building step by step.

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync
cp .env.example .env
```

On Windows PowerShell, use `Copy-Item .env.example .env` instead of `cp`. Then open `.env` and set `ANTHROPIC_API_KEY` to your key. The `.env` file is ignored by git, so the key is never committed.

## Run the tests

```bash
uv run pytest
```

## Lint and format

```bash
uv run ruff check
uv run ruff format
```
