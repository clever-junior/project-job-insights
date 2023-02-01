from typing import Dict, List, Union

from src.insights.jobs import read


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


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])

        if callable(salary) or None in job.values() or min_salary > max_salary:
            raise ValueError
        return int(salary) in range(min_salary, max_salary)
    except TypeError:
        raise ValueError
    except KeyError:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filteredJobs = []

    for job_dict in jobs:
        try:
            verify = matches_salary_range(job_dict, salary)
        except ValueError:
            verify = False
        if verify:
            filteredJobs.append(job_dict)

    return filteredJobs
