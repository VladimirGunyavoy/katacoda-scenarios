def check_single_fullname(full_name):
    ...


def filter_by_last_name(full_names):
    matching_names = []

    for name in full_names:
        last_name = name.split()[-1].lower()
        if "р" not in last_name:
            matching_names.append(name)

    return matching_names
