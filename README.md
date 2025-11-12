# Git
Use `git init --separate-git-dir <folder>` to create a git repository in different path.
```shell
git init --separate-git-dir E:\aiml-git-repo
```

# uv venv
Use `uv venv <folder>` to create a virtual environment in different path.
```shell
uv venv E:\aiml-venv
```
    (or)
```shell
export UV_PROJECT_ENVIRONMENT=E:\\aiml-venv
```
add above line in .env file and run following commands
```shell
source .env

uv venv

uv sync
```
