# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a mixed workspace exploring Anthropic SDK patterns. It contains three independent projects:

- **01_basic_agentic_loop/** — Agentic loop experimentation (learning)
- **02-test/** — Claude API client test utilities and chatbot experiments (active development)
- **03_website_generator/** — Website generation prototype (scaffolding phase)

Some projects are exploratory; others are ongoing work. Treat each as semi-independent.

## Environment Setup

- **Python 3.x** with venv
- **Requires:** `ANTHROPIC_API_KEY` in `.env` file at project root
- **SDK:** Anthropic Python SDK (`anthropic` package via pip)
- **Load dotenv:** All scripts load `.env` automatically with `load_dotenv()`

## Running Projects

Each project consists of raw Python scripts—no build step, no dependencies file yet. To run a script:

```bash
python 02-test/chat-bot.py
# or use the /test-script skill for convenience
```

## Anthropic SDK Patterns

When writing code that uses the Anthropic SDK:

1. **Client initialization:**
   ```python
   import anthropic
   client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY from environment
   ```

2. **API method:** Use `client.messages.create()`, not `client.chatbot.create()` or other variants.

3. **Model IDs:** Always use full version strings (e.g., `claude-haiku-4-5-20251001`, `claude-sonnet-4-6`) instead of short aliases.

4. **Message history:** Maintain a list of `{"role": "user"|"assistant", "content": "..."}` dicts for multi-turn conversations.

5. **Token limits:** Set `max_tokens` explicitly when calling the API (e.g., 500 for quick responses, 4000+ for detailed work).

## Common Gotchas

- **Undefined client variable:** Many scripts initialize Anthropic but forget `client = anthropic.Anthropic()`. Check that line is present.
- **Typos in variable names:** Watch for `contents` vs `content`, `message` vs `messages`, etc. These are silent failures until you hit the undefined variable.
- **Hardcoded model names:** Use environment variables or the constants already imported from `anthropic` instead of magic strings.
- **Missing error handling:** API calls can fail; wrap them in try/except and log meaningful errors (especially in ongoing projects).

## Code Style

- Use Python 3 style (f-strings, type hints where helpful)
- Format with `black` if available (see hooks below)
- No formal linter yet; keep scripts readable and avoid obvious issues

## Testing Individual Scripts

Use the `/test-script` skill to run a single Python script in `02-test/` with environment properly loaded.

