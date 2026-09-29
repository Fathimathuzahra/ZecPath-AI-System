from parsers.resume_parser import parse_resume


def test_resume_parser():
    result = parse_resume("Sample resume")

    assert result["name"] == "Sample Candidate"
    assert "Python" in result["skills"]


if __name__ == "__main__":
    test_resume_parser()
    print("Resume parser test passed.")