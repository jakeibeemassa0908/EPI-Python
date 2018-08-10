"""Programming Challenge Description:
The goal of this challenge is to design a cash register program. You will be given two decimal numbers. The first is the purchase price (PP) of the item. The second is the cash (CH) given by the customer. Your register currently has the following bills/coins within it: 
'PENNY': .01,
'NICKEL': .05,
'DIME': .10,
'QUARTER': .25,
'HALF DOLLAR': .50,
'ONE': 1.00,
'TWO': 2.00,
'FIVE': 5.00,
'TEN': 10.00,
'TWENTY': 20.00,
'FIFTY': 50.00,
'ONE HUNDRED': 100.00
The aim of the program is to calculate the change that has to be returned to the customer.
Input:
Your program should read lines of text from standard input. Each line contains two numbers which are separated by a semicolon. The first is the Purchase price (PP) and the second is the cash(CH) given by the customer.
Output:
For each line of input print a single line to standard output which is the change to be returned to the customer. In case the CH < PP, print out ERROR. If CH == PP, print out ZERO. For all other cases print the amount that needs to be returned, in terms of the currency values provided. The output should be alphabetically sorted.
"""
import sys
def change(line):
    values = line.split(";")
    purchase_price = float(values[0])
    cash = float(values[1])
    change = [0.01,0.05,0.10,0.25,0.50,1.00,2.00,5.00,10.00,20.00,50.00,100.00]
    match = {0.01:"PENNY",0.05:"NICKEL",0.10:"DIME",0.25:"QUARTER",0.50:"HALF DOLLAR",1.00:"ONE",2.00:"TWO",5.00:"FIVE",10.00:"TEN",20.00:"TWENTY",50.00:"FIFTY",100.00:"ONE HUNDRED"}
    match_str=[]
    return_val = []
    change.reverse()
    
    if purchase_price == cash:
        return "ZERO"
    elif cash < purchase_price:
        return "ERROR"
    else:
        give_back = cash - purchase_price
        while give_back > 1.0 :
            for num in change:
                if num <= give_back:
                    return_val.append(num)
                    give_back -= num
                    break
        
        for num in return_val:
            match_str.append(match[num])
        
        return ",".join(match_str)
       
        
print change("15.94;16.00")

"""
Programming Challenge Description:
We say a portfolio matches the benchmark when the market value percentage of each asset in the portfolio matches the market value percentage of each asset in the benchmark. Your challenge is to write a program that determines the transactions necessary to make a portfolio match a benchmark, assuming the total market value of the portfolio stays the same.

Background

A portfolio is a collection of assets such as stocks and bonds. A portfolio could have 10 shares of Vodafone stock, 15 shares of Google stock and 15 shares of Microsoft bonds.

A benchmark is also just a collection of assets. A benchmark could have 15 shares of Vodafone stock, 10 shares of Google stock and 15 shares of Microsoft bonds.

The market value of a stock is 
shares * price
The market value of a bond is
shares * (price + accrued interest) * 0.01

A transaction is when you “buy” or “sell” a particular asset. For instance, you can decide to buy 5 shares of Vodafone stock which, given the portfolio described above, would result in you having 15 shares of Vodafone stock.

An asset’s market value percentage can be calculated by dividing the market value of the asset by the total market value of every asset in the portfolio or benchmark. For example, given the portfolio described above and assuming all assets have a price of 5 and accrued interest is 0.05, the market value percentage of Vodafone would be
(10 * 5) / ( (10 * 5) + (15 * 5) + (15 * (5 + 0.05) * 0.01) )

Inputs and Outputs

You will receive a string in the following format Portfolio:Benchmark where Portfolio & Benchmark each are in the same format.

Here is the format: Name,AssetType,Shares,Price,AccruedInterest where each asset within Portfolio or Benchmark is separated by '|' symbol.

The output for the transactions is TransactionType,Name,Shares

Assumptions

Shares & Price are positive decimals
There will always be at least 1 asset present in the Portfolio and Benchmark
A particular asset will only be a stock or a bond, but not both
The final trades should be rounded to the nearest decimals
The trades should be sorted in ascending order based on the names of the assets
Input:
Vodafone,STOCK,10,50,0|Google,STOCK,15,50,0|Microsoft,BOND,15,100,0.05:Vodafone,STOCK,15,50,0|Google,STOCK,10,50,0|Microsoft,BOND,15,100,0.05

Output:
BUY,Vodafone,5
SELL,Google,5"""

