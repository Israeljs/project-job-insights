import pytest
from src.sorting import sort_by

mocked_reports = [
    {
        "job_title": "Marketing",
        "company": "Relief",
        "state": "NY",
        "city": "New York",
        "min_salary": "44587",
        "max_salary": "82162",
        "job_desc": "Marketing operations of the company.",
        "industry": "Finance",
        "rating": "4.0",
        "date_posted": "2020-05-08",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "0",
    },
    {
        "job_title": "Registered Nurse",
        "company": "Queens Boulevard Endoscopy Center",
        "state": "NY",
        "city": "Rego Park",
        "min_salary": "39876",
        "max_salary": "95748",
        "job_desc": "Full-Time Registered Nurse!",
        "industry": "",
        "rating": "3.0",
        "date_posted": "2020-04-25",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "1",
    },
    {
        "job_title": "Dental Hygienist",
        "company": "Batista Dental",
        "state": "NJ",
        "city": "West New York",
        "min_salary": "23467",
        "max_salary": "76585",
        "job_desc": """Part-time or Full-timedental hygienist position
        available in West New York, NJfor Mondays, Tuesdays, Wednesdays, and
        Saturday.Applicants may apply for any or all days. Beautiful upscale
        office with friendly staff.""",
        "industry": "",
        "rating": "",
        "date_posted": "2020-05-02",
        "valid_until": "2020-06-07",
        "job_type": "PART_TIME",
        "id": "2",
    },
]

mocked_reports_ordered_by_minimum_salary = [
    {
        "job_title": "Dental Hygienist",
        "company": "Batista Dental",
        "state": "NJ",
        "city": "West New York",
        "min_salary": "23467",
        "max_salary": "76585",
        "job_desc": """Part-time or Full-timedental hygienist position
        available in West New York, NJfor Mondays, Tuesdays, Wednesdays, and
        Saturday.Applicants may apply for any or all days. Beautiful upscale
        office with friendly staff.""",
        "industry": "",
        "rating": "",
        "date_posted": "2020-05-02",
        "valid_until": "2020-06-07",
        "job_type": "PART_TIME",
        "id": "2",
    },
    {
        "job_title": "Registered Nurse",
        "company": "Queens Boulevard Endoscopy Center",
        "state": "NY",
        "city": "Rego Park",
        "min_salary": "39876",
        "max_salary": "95748",
        "job_desc": "Full-Time Registered Nurse!",
        "industry": "",
        "rating": "3.0",
        "date_posted": "2020-04-25",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "1",
    },
    {
        "job_title": "Marketing",
        "company": "Relief",
        "state": "NY",
        "city": "New York",
        "min_salary": "44587",
        "max_salary": "82162",
        "job_desc": "Marketing operations of the company.",
        "industry": "Finance",
        "rating": "4.0",
        "date_posted": "2020-05-08",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "0",
    },
]

mocked_reports_ordered_by_maximum_salary = [
    {
        "job_title": "Registered Nurse",
        "company": "Queens Boulevard Endoscopy Center",
        "state": "NY",
        "city": "Rego Park",
        "min_salary": "39876",
        "max_salary": "95748",
        "job_desc": "Full-Time Registered Nurse!",
        "industry": "",
        "rating": "3.0",
        "date_posted": "2020-04-25",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "1",
    },
    {
        "job_title": "Marketing",
        "company": "Relief",
        "state": "NY",
        "city": "New York",
        "min_salary": "44587",
        "max_salary": "82162",
        "job_desc": "Marketing operations of the company.",
        "industry": "Finance",
        "rating": "4.0",
        "date_posted": "2020-05-08",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "0",
    },
    {
        "job_title": "Dental Hygienist",
        "company": "Batista Dental",
        "state": "NJ",
        "city": "West New York",
        "min_salary": "23467",
        "max_salary": "76585",
        "job_desc": """Part-time or Full-timedental hygienist position
        available in West New York, NJfor Mondays, Tuesdays, Wednesdays, and
        Saturday.Applicants may apply for any or all days. Beautiful upscale
        office with friendly staff.""",
        "industry": "",
        "rating": "",
        "date_posted": "2020-05-02",
        "valid_until": "2020-06-07",
        "job_type": "PART_TIME",
        "id": "2",
    },
]

mocked_reports_sorted_by_post_date = [
    {
        "job_title": "Marketing",
        "company": "Relief",
        "state": "NY",
        "city": "New York",
        "min_salary": "44587",
        "max_salary": "82162",
        "job_desc": "Marketing operations of the company.",
        "industry": "Finance",
        "rating": "4.0",
        "date_posted": "2020-05-08",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "0",
    },
    {
        "job_title": "Dental Hygienist",
        "company": "Batista Dental",
        "state": "NJ",
        "city": "West New York",
        "min_salary": "23467",
        "max_salary": "76585",
        "job_desc": """Part-time or Full-timedental hygienist position
        available in West New York, NJfor Mondays, Tuesdays, Wednesdays, and
        Saturday.Applicants may apply for any or all days. Beautiful upscale
        office with friendly staff.""",
        "industry": "",
        "rating": "",
        "date_posted": "2020-05-02",
        "valid_until": "2020-06-07",
        "job_type": "PART_TIME",
        "id": "2",
    },
    {
        "job_title": "Registered Nurse",
        "company": "Queens Boulevard Endoscopy Center",
        "state": "NY",
        "city": "Rego Park",
        "min_salary": "39876",
        "max_salary": "95748",
        "job_desc": "Full-Time Registered Nurse!",
        "industry": "",
        "rating": "3.0",
        "date_posted": "2020-04-25",
        "valid_until": "2020-06-07",
        "job_type": "FULL_TIME",
        "id": "1",
    },
]


def test_sort_by_criteria():
    sort_by(mocked_reports, "min_salary")
    assert mocked_reports == mocked_reports_ordered_by_minimum_salary

    sort_by(mocked_reports, "max_salary")
    assert mocked_reports == mocked_reports_ordered_by_maximum_salary

    sort_by(mocked_reports, "date_posted")
    assert mocked_reports == mocked_reports_sorted_by_post_date

    with pytest.raises(ValueError, match="invalid sorting criteria: any"):
        sort_by(mocked_reports, "any")

    with pytest.raises(ValueError, match="invalid sorting criteria:"):
        sort_by(mocked_reports, "")

    with pytest.raises(
        TypeError,
        match="sort_by\\(\\) missing 1 required "
        "positional argument: \\'criteria\\'",
    ):
        sort_by(mocked_reports)