def gross(basic,allowance):
    return basic+allowance

def deduction(gross):
    return gross*0.1

def net(gross):
    return gross-deduction(gross)
