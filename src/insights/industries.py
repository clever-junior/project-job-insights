from typing import Dict, List

from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)

    industries = []

    for dictJob in data:
        for key, item in dictJob.items():
            if key == "industry":
                if item not in industries and len(item) > 0:
                    industries.append(item)
    print(key)
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_jobs = []

    for job_dict in jobs:
        for key, item in job_dict.items():
            if item == industry:
                filtered_jobs.append(job_dict)

    return filtered_jobs
