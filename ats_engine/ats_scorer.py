def calculate_ats_score(candidate_skills, required_skills):
    matched = set(candidate_skills) & set(required_skills)

    if not required_skills:
        return 0

    return (len(matched) / len(required_skills)) * 100