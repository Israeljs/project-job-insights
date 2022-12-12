import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        jobs_read = csv.DictReader(file, delimiter=",", quotechar='"')
        new_jobs = list(jobs_read)

    return new_jobs
