# Fast-Api-Demo

Fast Api demo folder for MLOPS 2022 Data Scientist Trainees and DS Aspirants.

New environment

```bash
    conda create -n fast-api-demo python=3.9 -y
```

Activate the environment

```bash
    conda activate fast-api-demo
```

Requirements File

```bash
    touch requirements.txt
```

Connect to Github

```bash
git init
```

```bash
git add .
```

```bash
git commit -m "first commit"
```

oneliner updates for readme

```bash
git add . && git commit -m "update Readme.md"
```

pushing changes to new repo

```bash
git remote add origin git@github.com:kb1907/Fast-Api-Demo.git
git branch -M main
git push -u origin main
```
Changes automaticaly reflect in the web page
```bash
uvicorn app:app --reload
```
Add test file