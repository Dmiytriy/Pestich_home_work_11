from __future__ import annotations

import json



def load_candidates_from_json() -> list[dict]:
    """
    Читает JSON-файл и возвращает кандидатов.
    :rtype: object
    """

    with open('candidates.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def get_candidate(candidate_id: int) -> dict:
    """
    Загружает одного кандидата по id.
    """

    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    """
    Возвращает кандидата по имени
    """

    result = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name: str) -> list[dict]:
    """
    Возвращает кандидатов по навыку
    """

    result = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result

