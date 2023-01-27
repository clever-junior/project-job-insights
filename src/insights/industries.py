import sys
from typing import Dict, List

from src.insights.jobs import read

sys.path.insert(
    0,
    "C:/Users/clever-junior/OneDrive/Documentos/Code/Trybe/Computer-Science/sd-021-a-project-job-insights/src/insights/jobs.py",
)


path = "C:/Users/clever-junior/OneDrive/Documentos/Code/Trybe/Computer-Science/sd-021-a-project-job-insights/data/jobs.csv"


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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
