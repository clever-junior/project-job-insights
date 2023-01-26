import csv
from functools import lru_cache
from typing import Dict, List


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf8") as file:
        return list(csv.DictReader(file))


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)

    jobs = []

    for dictJob in data:
        for key, item in dictJob.items():
            if item == "job_type":
                jobs.append(item)
    return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filteredJobs = []

    for jobDict in jobs:
        for key, item in jobDict.items():
            if item == job_type:
                filteredJobs.append(jobDict)

    return filteredJobs
