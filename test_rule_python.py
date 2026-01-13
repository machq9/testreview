import sqlite3
import logging

# ====================== 规则1：SQL拼接校验（安全规范） ======================
# 违反规则：字符串拼接构造SQL（存在注入风险）
def bad_sql_query(order_id):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    # 违规点：字符串拼接SQL
    sql = "SELECT * FROM orders WHERE id = " + str(order_id)
    cursor.execute(sql)
    return cursor.fetchone()

# 符合规则：参数化查询
def good_sql_query(order_id):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    # 合规：参数化查询
    sql = "SELECT * FROM orders WHERE id = ?"
    cursor.execute(sql, (order_id,))
    result = cursor.fetchone()
    conn.close()
    return result

# ====================== 规则2：Print禁用校验（工程规范） ======================
# 违反规则：使用print输出业务日志
def bad_print_usage(order_id):
    # 违规点：使用print
    print(f"订单{order_id}支付失败：金额不足")
    return False

# 符合规则：使用logging输出
def good_logging_usage(order_id):
    # 合规：使用logging（指定级别）
    logging.basicConfig(level=logging.INFO)
    logging.error(f"订单{order_id}支付失败：金额不足")
    return False

# ====================== 规则3：订单金额校验（业务逻辑） ======================
# 违反规则：未校验订单金额（空值/负数）
def bad_order_amount(amount):
    # 违规点：未校验amount是否非空/正数
    total = amount * 1.08  # 加8%税费
    return total

# 符合规则：完整校验金额并抛异常
def good_order_amount(amount):
    # 合规：校验非空+正数，抛指定异常
    if amount is None:
        raise ValueError("订单金额必须为正数：金额不能为空")
    if amount <= 0:
        raise ValueError("订单金额必须为正数：金额不能小于等于0")
    total = amount * 1.08
    return total

# ====================== 混合场景测试（多规则违规） ======================
# 违反所有3条规则
def bad_mixed_scenario(order_id, amount):
    print(f"处理订单{order_id}，金额{amount}")  # 违规：print
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    sql = f"UPDATE orders SET amount = {amount} WHERE id = {order_id}"  # 违规：SQL拼接
    cursor.execute(sql)  # 无金额校验（违规）
    return True
