from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)

    job_types = []

    for job in jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):

    list_jobs = []

    for job in jobs:
        if job["job_type"] == job_type and job["job_type"] not in list_jobs:
            list_jobs.append(job)

    return list_jobs


def get_unique_industries(path):

    jobs = read(path)

    industries = []

    for job in jobs:
        if job["industry"] not in industries and job["industry"]:
            industries.append(job["industry"])

    return industries


def filter_by_industry(jobs, industry):
    industries = []

    for job in jobs:
        if job["industry"] == industry:
            industries.append(job)

    return industries


def get_max_salary(path):
    jobs = read(path)

    max_salaries = []

    for job in jobs:
        if job["max_salary"] != "" and job["max_salary"].isdigit():
            salary = int(job["max_salary"])
            max_salaries.append(salary)

    return max(max_salaries)


def get_min_salary(path):

    jobs = read(path)

    min_salaries = []

    for job in jobs:
        if job["min_salary"] != "" and job["min_salary"].isdigit():
            min_salaries.append(int(job["min_salary"]))

    return min(min_salaries)


def matches_salary_range(job, salary):

    min_salary = job.get('min_salary')
    max_salary = job.get('max_salary')

    if not isinstance(salary, int):
        raise ValueError('Salary must be a positive number.')

    if not isinstance(min_salary, int):
        raise ValueError('Job min salary must be a number.')

    if not isinstance(max_salary, int):
        raise ValueError('Job min salary must be a number.')

    if (max_salary < min_salary):
        raise ValueError('Job min salary must be lower than max.')

    return min_salary <= salary <= max_salary


def filter_by_salary_range(jobs, salary):
    valid_jobs = []

    for job in jobs:
        try:
            result = matches_salary_range(job, salary)
        except ValueError:
            None
        else:
            if result:
                valid_jobs.append(job)

    return valid_jobs
