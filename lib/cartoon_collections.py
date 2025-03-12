def roll_call_dwarves(names):
    num=1
    for name in names:
        print(f"{num}. {name}")
        num=num+1

def summon_captain_planet(calls):
    calls= [f"{call.title()}!" for call in calls]
    return calls
        

def long_planeteer_calls(calls):
    for call in calls:
        if len(call)>4:
            return True
    return False

def find_the_cheese(foods):
    cheese=["cheddar","gouda","camembert"]
    for food in foods:
        if food in cheese:
            return food
    return None
