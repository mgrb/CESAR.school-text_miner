# CoockBook de Web Scraping
CESAR School - Mineração de Texto na Web

## Montando o ambiente
1. Instalar o uv 
1.1 No Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

1.2 No Windows:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Baixar este repositorio
```bash
git clone
```

3. acessar a pasta do repositorio
```bash
cd web-scraping
```

4. Para rodar o script
```bash
uv run src/web_scraping.py
``` 

5. Para abrir o ambiente no VSCode
```bash
uv sync
code .
```
