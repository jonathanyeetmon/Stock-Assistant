def pre_process(ticker):
    ticker = ticker.upper()
    #remove spaces
    ticker=filter(str.isalpha,ticker)
    ticker = "".join(ticker)
    return ticker

print(pre_process(" a apl "))