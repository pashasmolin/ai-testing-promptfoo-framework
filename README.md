# AI Testing Framework (Promptfoo-based)

This repo is a scalable testing harness for evaluating LLMs using [Promptfoo](https://www.promptfoo.dev/docs).

### Features
- Organized per test group YAML prompt sets
- Centralized model/provider configs
- Supports multiple models (OpenAI, Anthropic, Gemini, Mistral, Ollama, etc.)
- Custom evaluators for refusal, stability, bias
- JSON/CSV/HTML result exports for analysis
- CI/CD ready (e.g. nightly test runs)

### Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt


### Set up .env with API keys

OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
GOOGLE_API_KEY=...

### Run tests

promptfoo eval -c configs/promptfoo.yaml
