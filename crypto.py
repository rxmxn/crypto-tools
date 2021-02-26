import click

@click.group()
def crypto():
    """Run some calculations"""
    click.echo("Let me help you running some calculations")

@crypto.command()
@click.option('--money_spent', default=None, help='Amount of money that you have spent already in a coin')
@click.option('--current_coins_amount', default=None, help='Amount of coins of a certain cryptocurrency that you are holding')
@click.option('--want', default=None, help='Cost that you want to reach and get earnings when the value of the coin gets higher than that')
@click.option('--current_price', default=None, help='Current price of the currency you want to trade')
def amount_needed(want, current_price, money_spent, current_coins_amount):
    calculate(float(want), float(current_price), float(money_spent), float(current_coins_amount))

@crypto.command()
@click.option('--money_spent', default=None, help='Amount of money that you have spent already in a coin')
@click.option('--current_coins_amount', default=None, help='Amount of coins of a certain cryptocurrency that you are holding')
@click.option('--current_price', default=None, help='Current price of the currency you want to trade')
@click.option('--initial_price', default=None, help='Initial price of the currency you want to trade, i.e. if currency\'s value is > this price, you start making earnings')
def amount_range(initial_price, current_price, money_spent, current_coins_amount):
    for i in range(int(float(current_price))+1,int(float(initial_price)), 1):
        calculate(float(i), float(current_price), float(money_spent), float(current_coins_amount))

def calculate(want, current_price, money_spent, current_coins_amount):
    money_to_buy = (money_spent - want * current_coins_amount)/(want/current_price - 1)
    click.echo("For " + str(want) + " -> $" + str(money_to_buy))

if __name__ == '__main__':
    crypto()
