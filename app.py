from flask import Flask, render_template_string
from best_team_prognose import main

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
  </style>
</head>
<body>
  <h1>Beste 37-Mio-Kombi (3-4-3)</h1>
  <h2>Gesamtpunkte: {{ total_points }} | Gesamtkosten: {{ total_cost }}</h2>
  <table>
    <tr>
      <th>Position</th>
      <th>Spieler</th>
      <th>Verein</th>
      <th>Punkte</th>
      <th>Preis</th>
    </tr>
    {% for p in team %}
    <tr>
      <td>{{ p["Position"] }}</td>
      <td>{{ p["Angezeigter Name"] }}</td>
      <td>{{ p["Verein"] }}</td>
      <td>{{ p["Punkte"]|int }}</td>
      <td>{{ "{:,}".format(int(p["Marktwert"])).replace(",", ".") }}</td>
    </tr>
    {% endfor %}
  </table>
</body>
</html>
"""

@app.route("/")
def index():
    team, total_points, total_cost = main("spieler_mit_position.xlsx", return_team=True)
    return render_template_string(HTML_PAGE, team=team, total_points=int(total_points), total_cost=int(total_cost))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
