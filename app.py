from flask import Flask, render_template_string
from best_team_prognose import main
import io
from contextlib import redirect_stdout

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Bestes Kicker-Team</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 40px; }
    table { border-collapse: collapse; width: 100%%; margin-top: 20px; }
    th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
    th { background: #f0f0f0; }
    pre { background: #f8f8f8; padding: 10px; }
  </style>
</head>
<body>
  <h1>Beste 37-Mio-Kombi</h1>
  <p>Formation: 3-4-3</p>

  <h2>Ergebnis</h2>
  <pre>{{ result }}</pre>

  <h2>CSV-Datei</h2>
  <p>Die Datei <code>kicker_manager_best_team_prognose_wunsch.csv</code> wurde erzeugt
     und liegt im Projektordner.</p>
</body>
</html>
"""

@app.route("/")
def index():
    buf = io.StringIO()
    with redirect_stdout(buf):
        main("spieler_mit_position.xlsx")  # deine Excel-Datei aus Repo laden
    result_text = buf.getvalue()
    return render_template_string(HTML_PAGE, result=result_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
