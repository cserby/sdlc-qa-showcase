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

inside `.vscode/settings.json`.

## Pre-commit check

Useful to run `black --check .` before pushing to CI, as jobs will fail on incorrect formatting there.

# Type checking

Use `mypy` for type checking.

## VSCode configuration

Put

```
{
    "python.linting.mypyEnabled": true
}
```

inside `.vscode/settings.json`.
