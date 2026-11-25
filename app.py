from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
	return """
	<!doctype html>
	<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Bardhi's DevOps Playground</title>
		<style>
			* { box-sizing: border-box; }
			body {
				margin: 0; min-height: 100vh; display: grid; place-items: center;
				font: 16px/1.6 system-ui, sans-serif; color: #e2e8f0;
				background: radial-gradient(circle at top, #164e63, #0f172a 60%);
			}
			main {
				width: min(680px, calc(100% - 32px)); padding: 48px;
				border: 1px solid #334155; border-radius: 24px;
				background: #0f172acc; box-shadow: 0 24px 80px #02061799;
			}
			.badge { color: #67e8f9; letter-spacing: .12em; text-transform: uppercase; }
			h1 { margin: 12px 0; font-size: clamp(2.2rem, 7vw, 4rem); line-height: 1.1; }
			p { color: #cbd5e1; }
			a { color: #67e8f9; }
			button {
				margin-top: 16px; padding: 12px 18px; border: 0; border-radius: 10px;
				color: #082f49; background: #67e8f9; font: inherit; font-weight: 700;
				cursor: pointer;
			}
			#message { min-height: 1.6em; color: #a7f3d0; }
		</style>
	</head>
	<body>
		<main>
			<div class="badge">☁ Bardhi's DevOps Playground 12345</div>
			<h1>Ship something<br>awesome.</h1>
			<p>A tiny Flask app, ready for its next deployment. Explore the <a href="/about">about page</a> or check the <a href="/health">health endpoint</a>.</p>
			<button onclick="document.getElementById('message').textContent = 'Nice. Now let’s build and deploy it!'">Get a little motivation</button>
			<p id="message" aria-live="polite"></p>
		</main>
	</body>
	</html>
	"""


@app.get("/about")
def about():
	return "This is a small Flask app with room to grow."


@app.get("/health")
def health():
	return jsonify(status="ok")


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=6000)
