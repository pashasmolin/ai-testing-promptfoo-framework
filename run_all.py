import subprocess
import pathlib

def run_promptfoo(selected):
    results_dir = pathlib.Path("results")
    results_dir.mkdir(parents=True, exist_ok=True)

    # Build command: promptfoo eval -c file1 -c file2 ...
    cmd = [
        "promptfoo", "eval",
    ]

    for ch in selected:
        cmd.extend(["-c", ch])

    cmd.extend([
        "-o", str(results_dir / "combined.json"),
        "-o", str(results_dir / "combined.html"),
        "--no-cache"
    ])

    print("\n=== Running combined Promptfoo eval ===")
    print(" ".join(cmd))
    subprocess.run(cmd, check=False)

if __name__ == "__main__":
    # Comment/uncomment challenges here
    selected = [
        "prompts/T0_security.yaml",
        "prompts/T1_hallucination.yaml",
        # "prompts/T2_bias.yaml",
        # "prompts/T3_consistency.yaml",
        # "prompts/T4_context.yaml",
        # "prompts/T5_alignment.yaml",
        # "prompts/T6_regulatory.yaml",
    ]

    if not selected:
        print("No challenge files selected!")
    else:
        run_promptfoo(selected)
