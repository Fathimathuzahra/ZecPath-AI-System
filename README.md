# ZecPath AI

AI-powered hiring system designed to support the recruitment process using
resume screening, candidate evaluation, interviews, scoring, and reporting.

## Project Structure

```text
zecpath-ai/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── parsers/
│   └── resume_parser.py
│
├── ats_engine/
│   └── ats_scorer.py
│
├── screening_ai/
├── interview_ai/
│
├── scoring/
│   └── scoring_engine.py
│
├── utils/
│   └── logger.py
│
├── tests/
│   ├── test_parser.py
│   ├── test_ats.py
│   └── test_scoring.py
│
├── logs/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md