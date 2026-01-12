def get_user(user_id)  # 语法错误：缺冒号
    # 安全漏洞：SQL注入
    return db.query("SELECT * FROM users WHERE id = " + user_id)
