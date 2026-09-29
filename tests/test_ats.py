from ats_engine.ats_scorer import calculate_ats_score


def test_ats_score():
    score = calculate_ats_score(
        ["Python", "SQL", "Pandas"],
        ["Python", "SQL", "Pandas", "Machine Learning"]
    )

    assert score == 75.0


if __name__ == "__main__":
    test_ats_score()
    print("ATS test passed.")