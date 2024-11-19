# Suppose you have a dictionary of survey responses:
# •keys are student names
# •values are favourite ice cream flavours (one of
# "chocolate", "vanilla", "strawberry")
# Write a function that takes a dictionary of survey responses
# and returns a new dictionary where:
# •keys are ice cream flavours
# •values are number of students with that favourite flavour

survey = {"Hanna": "vanilla",
          "Eli": "strawberry",
          "Tristan": "vanilla",
          "Ian": "vanilla",
          "Chase": "chocolate",
          "Abdul": "vanilla",
          "Gang": "strawberry"}

def icecream_survey(survey):
    """
    Return a dictionary of number of votes for each flavor from the survey dictionary
    :param survey: dict, name: flavor
    :return: dict, flavor: number of votes
    """
    # initialize a dictionary  with a structure {flavor: number of votes}
    result = {}
    # add number of votes to each flavor
    # check people's choice
    for name in survey:  # survey {name: flavor}
        flavor = survey[name]
        # write down the flavor and counting votes
        if flavor not in result:
            # create the record for the first time for that flavor
            result[flavor] = 1
        else: # flavor is existing key
            result[flavor] += 1 # add 1 vote

    return result

print(icecream_survey(survey))

def icecream_survey_option2(survey):
    """
    Return a dictionary of number of votes for each flavor from the survey dictionary
    :param survey: dict, name: flavor
    :return: dict, flavor: number of votes
    """
    # initialize a dictionary  with a structure {flavor: number of votes}
    result = {}
    # add number of votes to each flavor
    # check people's choice
    for name in survey:  # survey {name: flavor}
        flavor = survey[name]
        # write down the flavor and counting votes
        if flavor not in result:
            # initalize the record for the first time for that flavor, 0, and then add one
            result[flavor] = 0
        result[flavor] += 1  # add 1 vote

    return result
