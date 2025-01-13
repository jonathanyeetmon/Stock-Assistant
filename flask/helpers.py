def count_techs(techs):
    buy = 0
    sell = 0
    hold = 0
    for tech in techs:
        print(tech)
        tech = tech["third_element"]
        if tech[0] == 'B':
            buy += 1
        elif tech[0] == 'S':
            sell += 1
        elif tech[0] == 'N':
            hold += 1
    if buy > sell and buy > hold:
        return "buy"
    elif sell > buy and sell > hold:
        return "sell"
    return "hold"
