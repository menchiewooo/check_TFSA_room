import check_TFSA_util


def check_room():
    """

    :return: a float that is the current available TFSA contribution room
    """
    con_limit = check_TFSA_util.get_limit()
    # get balance from Wealth Simple
    print("##### Getting balance for Wealth Simple ##### ")
    balance_ws = check_TFSA_util.get_balance('ws')
    print(f"##### Balance of Wealth Simple: {balance_ws} #####")
    # get balance from Sunlife
    print("##### Getting balance for Sunlife ##### ")
    balance_sl = check_TFSA_util.get_balance('sl')
    print(f"##### Balance of Sunlife: {balance_sl} #####")
    # get balance from Questrade
    print("##### Getting balance for Questrade ##### ")
    balance_qst = check_TFSA_util.get_balance('qst')
    print(f"##### Balance of Questrade: {balance_sl} #####")

    # Subtract those balances from your contribution limit
    return float(con_limit) - balance_ws - balance_sl - balance_qst


if __name__ == '__main__':
    print(f"Your available TFSA room is {check_room()}")
