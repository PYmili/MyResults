import bcrypt

class PasswordUtil:
    @staticmethod
    def password_hash(pwd: str) -> str:
        """
        对密码哈希处理
        :param pwd: 未哈希的密码
        :return: 哈希后的密码
        """
        # 将密码转换为字节类型
        password_bytes = pwd.encode('utf-8')
        # 生成哈希密码
        hashed_pwd = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        # 返回哈希后的密码
        return hashed_pwd.decode('utf-8')  # 将字节类型转换为字符串

    @staticmethod
    def check_password(stored_password: str, user_password: str) -> bool:
        """
        对未hash的密码验证
        :param stored_password: 存储的哈希密码
        :param user_password: 用户输入的未哈希的密码
        :return: 验证结果
        """
        # 将存储的哈希密码转换为字节类型
        stored_password_bytes = stored_password.encode('utf-8')
        # 将用户输入的密码转换为字节类型
        user_password_bytes = user_password.encode('utf-8')
        # 验证密码
        return bcrypt.checkpw(user_password_bytes, stored_password_bytes)


if __name__ == "__main__":
    # 哈希密码
    hashed_password = PasswordUtil.password_hash("admin")
    print(f"哈希后的密码: {hashed_password}")
    print(PasswordUtil.check_password(
        hashed_password,
        "admin"
    ))
