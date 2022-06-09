#https://realpython.com/preview/any-python/

def schedule_interview(applicant):
    print(f"Scheduled interview with {applicant['name']}")

applicants = [
    {
        "name": "Devon Smith",
        "programming_languages": ["c++", "ada"],
        "years_of_experience": 1,
        "has_degree": False,
        "email_address": "devon@email.com",
    },
    {
        "name": "Susan Jones",
        "programming_languages": ["python", "javascript"],
        "years_of_experience": 2,
        "has_degree": False,
        "email_address": "susan@email.com",
    },
    {
        "name": "Sam Hughes",
        "programming_languages": ["java"],
        "years_of_experience": 4,
        "has_degree": True,
        "email_address": "sam@email.com",
    },
]
for applicant in applicants:
    knows_python = "python" in applicant["programming_languages"]
    experienced_dev = applicant["years_of_experience"] >= 5

    meets_criteria = (
        knows_python
        or experienced_dev
        or applicant["has_degree"]
    )
    if meets_criteria:
        schedule_interview(applicant)