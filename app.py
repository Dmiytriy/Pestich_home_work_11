from flask import Flask, render_template

from utils import *

app = Flask(__name__)


@app.route("/")
def page_index():
    """Главная страница."""

    candidates: list[dict] = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:ind>")
def page_candidate(ind):
    """Страница кандидата"""

    candidate: dict = get_candidate(ind)
    return render_template('single.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def page_search_candidate(candidate_name):
    """Страница кандидатов по имени"""

    candidates: list[dict] = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route("/skill/<candidate_skill>")
def page_search_candidate_skill(candidate_skill):
    """Страница кандидатов по навыкам"""

    candidates: list[dict] = get_candidates_by_skill(candidate_skill)
    return render_template('skill.html', skill=candidate_skill, candidates=candidates)

if __name__ == "__main__":
    app.run()
