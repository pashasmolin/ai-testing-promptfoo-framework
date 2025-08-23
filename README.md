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

 Install dependencies:
```bash
   pip install -r requirements.txt
```

### Set up .env with API keys
```bash
    OPENAI_API_KEY=...
    ANTHROPIC_API_KEY=...
    GOOGLE_API_KEY=...
```

### Run single config file with tests
```bash
    promptfoo eval -c configs/promptfoo.yaml
```


### Run selected files and generate combined table report with promptfoo cmd
```bash
    promptfoo eval -c prompts/T0_security.yaml \
                -c prompts/T1_hallucination.yaml \
                -c prompts/T2_bias.yaml \
                -o results/combined.json \
                -o results/combined.html \
                --no-cache
```

### Run selected files and generate combined table report with python for convinence 
```bash
    python run_all.py
```