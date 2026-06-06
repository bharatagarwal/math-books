.PHONY: serve build deploy repl

repl:
	uv run --with sympy --with ipython isympy

serve:
	uv run reader/serve.py

build:
	rm -rf public
	mkdir -p public/reader public/markdown public/mixtapes
	cp reader/index.html reader/app.js reader/styles.css public/reader/
	cp mixtapes/index.html mixtapes/app.js public/mixtapes/
	rsync -a --exclude='*.manifest.json' --exclude='.DS_Store' markdown/ public/markdown/
	rsync -a --exclude='.DS_Store' --exclude='.hypothesis' --exclude='.pytest_cache' --exclude='__pycache__' --exclude='*.pyc' code/ public/code/
	@printf '<meta http-equiv="refresh" content="0;url=/reader/">\n' > public/index.html

deploy: build
	wrangler deploy
