from typing import Dict, List

# def get_unique_industries(path: str) -> List[str]:
# data = read(path)

# industries = []

# for dictJob in data:
#     for key, item in dictJob.items():
#         if item == "industry":
#             industries.append(item)
# return industries


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
