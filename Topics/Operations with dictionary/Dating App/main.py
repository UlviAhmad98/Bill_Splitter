def select_dates(potential_dates):
    if potential_dates["age"] > 30 and potential_dates["hobbies"] == "art" and potential_dates["city"] == "Berlin":
        return ", ".join(list(potential_dates['name']))
