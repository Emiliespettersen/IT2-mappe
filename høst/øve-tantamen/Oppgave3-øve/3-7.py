
#oppgave3.7

def samlet_vaksine(krav_hvert_land):
    vaksiner = []
    for krav in krav_hvert_land: 
        for vaksine in krav:
            if not vaksine in vaksiner: 
                vaksiner.append(vaksine)
    return vaksiner