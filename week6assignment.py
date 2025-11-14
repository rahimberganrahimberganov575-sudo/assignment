def calculate_holding_profit(stock_tuple):
    ticker, sector, p_price, c_price, shares = stock_tuple
    profit = ((c_price - p_price) * shares)
    return profit 


def find_top_performer(portfolio):
    top_ticker = portfolio [0][0] 
    top_profit = calculate_holding_profit (portfolio[0])
    for stock in portfolio :
        ticker = stock[0]
        profit = calculate_holding_profit (stock)
        if profit > top_profit or (profit == top_profit and ticker < top_ticker):
           top_profit = profit
           top_ticker = ticker
    return top_ticker

def get_tickers_in_sector(portfolio, sector_name):
    tickers = []
    sector = []
    for stock in portfolio:
        if stock [1] == sector_name :
           tickers.append(stock[0])
    tickers.sort()
    return tickers

def get_sector_value_summary(portfolio):
    sector_values = []
    total = []
    for stock in portfolio :
        sector = stock[1]
        value = stock[3] * stock[4]
        if sector not in sector_values:
           sector_values.append(sector)
           total.append(value)
        else :
           index = sector_values.index(sector)
           total[index] += value
    final=[]
    for val in range(len(sector_values)):
        final.append((sector_values[val], total[val]))
    final.sort()
    return final
def analyze_portfolio(portfolio):
    top_ticker = find_top_performer(portfolio)
    tech_ticker = get_tickers_in_sector(portfolio ,"Technology")
    sec_summmary = get_sector_value_summary(portfolio)
    return ( top_ticker , tech_ticker , sec_summmary)
portfolio = [
    ('AAPL', 'Technology', 150.00, 175.00, 100),  # Profit: 2500
    ('JPM', 'Finance', 160.00, 165.00, 200),     # Profit: 1000
    ('GOOG', 'Technology', 2800.00, 2750.00, 10), # Profit: -500
    ('PFE', 'Healthcare', 40.00, 55.00, 500)     # Profit: 7500
]
print(analyze_portfolio(portfolio))