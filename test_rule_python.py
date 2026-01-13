# 规则1：禁止SQL字符串拼接（Sourcery配置的规则）
def bad_sql(user_id):
    # 违反规则：用字符串拼接SQL
    sql = "SELECT * FROM users WHERE id = " + str(user_id)
    return sql

def good_sql(user_id):
    # 符合规则：参数化查询
    sql = "SELECT * FROM users WHERE id = ?"
    return (sql, (user_id,))


# 规则2：禁止使用print，必须用logging（Sourcery配置的规则）
def bad_print():
    # 违反规则：使用print
    print("This is a print statement")

def good_logging():
    # 符合规则：使用logging
    import logging
    logging.info("This is a logging statement")


# 规则3：订单金额必须非空且>0（CodeRabbit配置的规则）
def bad_order_amount(amount):
    # 违反规则：未校验金额
    return amount * 2

def good_order_amount(amount):
    # 符合规则：校验金额
    if amount is None or amount <= 0:
        raise ValueError("Order amount must be positive")
    return amount * 2
