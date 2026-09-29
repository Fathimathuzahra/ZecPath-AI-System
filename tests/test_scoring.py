from scoring.scoring_engine import calculate_overall_score


def test_overall_score():
    score = calculate_overall_score([80, 90, 70])

    assert score == 80


if __name__ == "__main__":
    test_overall_score()
    print("Scoring test passed.")