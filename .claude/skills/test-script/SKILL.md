---
name: test-script
description: Run a Python script from 02-test/ with environment variables loaded
---

## Purpose

Quickly execute and test individual Python scripts in the `02-test/` directory with the `.env` file loaded automatically. Useful for validating chatbot responses, API calls, or new experiments.

## Usage

```
/test-script <script-name.py>
```

Example:
```
/test-script chat-bot.py
```

## What it does

1. Verifies the script exists in `02-test/`
2. Checks that `.env` is present at the project root (with `ANTHROPIC_API_KEY`)
3. Runs the script with the environment variable set
4. Captures and displays output

## Example workflow

You've just edited `chat-bot.py` to fix a bug. Run:

```
/test-script chat-bot.py
```

The script will start, and you can interact with it or see errors in real time.

