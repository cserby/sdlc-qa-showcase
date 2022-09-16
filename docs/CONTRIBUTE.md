# Code formatting

Use `black` for code formatting.

## VSCode configuration

Put

```
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

inside `.vscode/config.json`.

## Pre-commit check

Useful to run `black --check .` before pushing to CI, as jobs will fail on incorrect formatting there.
