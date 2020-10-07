from typing import List, Dict, Union, Callable

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    for sett in data:
        new_name = sett['name'].capitalize()
        sett['name'] = new_name
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value
    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for sett in data:
        del sett[redundant_keys]
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    all_items = []
    for sett in data:
        for i in sett.values():
            if i == value:
                all_items.append(sett)
    return all_items


def task_4_return_lambda_sum_2_ints(x, y):
    """
    Return lambda operator which take 2 integer params and returns their sum
    """
    return (lambda x, y: x + y)(x, y)


def task_5_append_str_to_list_and_return(input_data: List, elem: str):
    """
    Return list with the element appended to it.
    But the list itself should not be changed
    """
    new_list = [i for i in input_data]
    new_list.append(elem)
    return new_list


def task_6_insert_function_result_into_string(func: Callable):
    """
    Return string, consisting of data, returned by func, surrounded by "start" and "finish"
    Rule: + operation can not be used, solution should be one-liner
    :param func: callable taking no parameters, returning string
    Examples:
        func returns "run", resulting string should be - "start run finish"
    """
    return f'start {func()} finish'


def task_7_insert_2_vars_into_string(age: float, habit: str):
    """
    Template string: "I have <first placeholder> years and I love <second placeholder>"
    where first placeholder should have only one number in fractional part,
    and second should have field size of 10 even if is is longer - only 10 positions should be occupied.
    Examples:
        "I have 10.4 years and I love cars      "
    """
    age = int(age * 10) / 10
    if len(habit) == 10:
        txt = habit
    elif len(habit) > 10:
        txt = habit[:10]
    else:
        i = 10 - len(habit)
        txt = habit + i * ' '
    return f'I have {age} years and I love {txt}'
