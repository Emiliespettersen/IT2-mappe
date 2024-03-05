#oppgave 3.4

def vinnerlag (hjemmelag, bortelag, hjemmemaal, bortemaal):
    if hjemmemaal > bortemaal:
        return hjemmelag
    elif bortemaal >hjemmemaal:
        return bortelag
    else:
        return "uavgjort"