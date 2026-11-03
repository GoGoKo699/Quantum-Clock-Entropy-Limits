# Checking the hosted mathematics

[Verification overview](../README.md) · [Repository overview](../../README.md)

The hosted-rendering workflow reads a commit-pinned version of every tracked Markdown page and opens the corresponding public GitHub pages in a fresh, unsigned-in Chromium context. It compares source expressions with the actual rendered MathML at viewport widths of 1440 and 760 pixels. Source compilation is the reference for that comparison; it is not itself evidence of hosted rendering.

## Run the same check

Use Node.js 18 or later, Python 3.10 or later, Git, Playwright 1.56.1 and MathJax 3.2.1. Install the rendering dependencies outside the scientific checkout. From the repository root, with the dependency directory on `NODE_PATH`:

```bash
node verification/hosted/capture_hosted_math.cjs \
  --root "$PWD" \
  --repository GoGoKo699/Quantum-Clock-Entropy-Limits \
  --revision "$(git rev-parse HEAD)" \
  --output /absolute/new-empty-capture-directory \
  --contract verification/hosted/contract.json
```

The output directory must be new or empty. The collector reads Git objects, so uncommitted changes are not included. The [GitHub Actions workflow](../../.github/workflows/hosted-math.yml) installs isolated dependencies, checks the pull request's exact head revision, and retains its report, HTML and screenshots as a workflow artifact. The job has read-only repository permissions.

## What the evidence covers

The collector checks the source revision and hashes, page and expression counts, MathML structure, relation symbols, labels and bounded display geometry. The [headline contract](contract.json) adds explicit text requirements for the main quantitative claims. Both viewport sizes must cover the same complete expression inventory. A missing page, unsupported source expression, renderer error or network failure remains a failed check.

After a substantive equation edit, inspect the new source inventory and update any affected contract entry to the intended expression, index and hash. Review the expected text against the scientific statement. A contract change must not hide a missing operand or a changed inequality.

Screenshots require a separate visual review of equation bodies, tables, navigation and legibility. Passing the structural comparison does not establish scientific correctness, exhaustive pixel-level quality, behavior in every browser or future GitHub rendering. Numerical reproduction remains the separate procedure in the [verification overview](../README.md).
