.PHONY: serve build deploy

serve:
	uv run reader/serve.py

build:
	rm -rf public
	mkdir -p public/reader public/markdown
	cp reader/index.html reader/app.js reader/styles.css public/reader/
	rsync -a --exclude='*.manifest.json' --exclude='.DS_Store' markdown/ public/markdown/
	rsync -a --exclude='.DS_Store' code/ public/code/
	@printf '<meta http-equiv="refresh" content="0;url=/reader/">\n' > public/index.html

deploy: build
	wrangler deploy
