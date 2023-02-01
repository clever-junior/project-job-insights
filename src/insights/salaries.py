# import sys
from typing import Dict, List, Union

from src.insights.jobs import read

# sys.path.append(
#     "C:/Users/clever-junior/OneDrive/Documentos/Code/Trybe/Computer-Science/sd-021-a-project-job-insights"
# )


def get_max_salary(path: str) -> int:
    data = read(path)

    salariesList = []

    for dictJob in data:
        for key, item in dictJob.items():
            if key == "max_salary" and item != "" and item != "invalid":
                salariesList.append(int(item))

    return max(salariesList)


def get_min_salary(path: str) -> int:
    data = read(path)

    salaries_list = []

    for dict_job in data:
        for key, item in dict_job.items():
            if key == "min_salary" and item != "" and item != "invalid":
                salaries_list.append(int(item))

    return min(salaries_list)


invalid_job = {"max_salary": 0, "min_salary": 20}

job = {"max_salary": 10000, "min_salary": 200}

salary = 1000


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if callable(salary):
            raise ValueError
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        int_salary = int(salary)
        if min_salary > max_salary:
            raise ValueError
        return int_salary >= min_salary and int_salary <= max_salary
    except KeyError:
        raise ValueError
    except TypeError:
        raise ValueError


jobs = [
    {"max_salary": 0, "min_salary": 10},
    {"max_salary": 10, "min_salary": 100},
    {"max_salary": 10000, "min_salary": 200},
    {"max_salary": 15000, "min_salary": 0},
    {"max_salary": 1500, "min_salary": 0},
    {"max_salary": -1, "min_salary": 10},
]

salaries = [0, 1, 5, 1000, 2000, -1, -2, None, "", [], {}, lambda: 1]


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filteredJobs = []

    for job_dict in jobs:
        try:
            verify = matches_salary_range(job_dict, salary)
        except ValueError:
            verify = False
        except TypeError:
            verify = False
            print(verify)
        if verify:
            filteredJobs.append(job_dict)

    return filteredJobs
