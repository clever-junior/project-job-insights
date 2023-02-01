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
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]
        salary = int(salary)
        if min_salary > max_salary:
            raise ValueError
        return salary >= min_salary and salary <= max_salary
    except KeyError:
        raise ValueError
    except TypeError:
        raise ValueError

def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
