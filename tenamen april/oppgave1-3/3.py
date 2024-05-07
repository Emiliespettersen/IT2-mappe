

"""
FUNCTION er_primtall (tall)
    FOR EACH i LESSER THAN tall
        IF tall % i EQUAL TO 0
            RETURN true
        ENDIF
    ENDFOR
    RETURN false
ENDFUNSKJON

"""

# def er_primtall (tall):
#     for i < tall: # noe galt her.
#         if tall % i == 0:
#             return True
#     return False

def er_primtall(tall):
    for i in range(2, tall):
        if tall % i == 0:
            return True
    return False






