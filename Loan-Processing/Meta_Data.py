# Meta data for loan processing system
def metadata():
    criteria = [{"cs_start": 0, "cs_end": 199, "loan": 10000, "duration": 36, "interest_rate": 5},
                 {"cs_start": 300, "cs_end": 399, "loan": 10000, "duration": 36, "interest_rate": 3},
                 {"cs_start": 0, "cs_end": 199, "loan": 20000, "duration": 36, "interest_rate": 5},
                 {"cs_start": 200, "cs_end": 299, "loan": 20000, "duration": 36, "interest_rate": 4},
                 {"cs_start": 300, "cs_end": 399, "loan": 20000, "duration": 36, "interest_rate": 3},
                 {"cs_start": 0, "cs_end": 199, "loan": 30000, "duration": 36, "interest_rate": 5},
                 {"cs_start": 200, "cs_end": 299, "loan": 30000, "duration": 36, "interest_rate": 4},
                 {"cs_start": 300, "cs_end": 399, "loan": 30000, "duration": 36, "interest_rate": 3},
                 {"cs_start": 200, "cs_end": 299, "loan": 10000, "duration": 36, "interest_rate": 4},
                 ]
    sorted_criteria = sorted(criteria, key=lambda i: (i["loan"], i["cs_start"]))
    return sorted_criteria
