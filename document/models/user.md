# User Module - 用户模型

| 字段名         | 数据类型           | 说明                        |
| ----------- | -------------- |---------------------------|
| `username`  | `CharField`    | 用户名，最大长度为100字符            |
| `password`  | `CharField`    | 密码，存储为哈希值，最大长度为255字符      |
| `avatar`    | `ImageField`   | 用户头像，上传到`media\avatars`目录 |
| `is_public` | `BooleanField` | 是否为公开用户，默认为`False`        |
| `is_admin`  | `BooleanField` | 是否是管理员，默认为`False`         |
