# JetBrainsOSSProjectCheck

JetBrainsOSSProjectCheck 是一个用于简单检查 JetBrains 开源许可证项目是否符合要求的工具。如果项目不符合要求，它会输出不符合的原因。

## 功能

- 检查指定 GitHub 用户的所有非归档仓库的提交活动。
- 输出符合活动要求和不符合活动要求的仓库列表及其原因。
- 生成 Markdown 格式的结果报告 (`result.md`)。
- 支持多线程和进度条显示检查进度。

## 安装

1. 克隆仓库：
    ```bash
    git clone https://github.com/你的用户名/JetBrainsOSSProjectCheck.git
    cd JetBrainsOSSProjectCheck
    ```

2. 安装依赖项：
    ```bash
    pip install -r requirements.txt
    ```

## 使用

1. 运行脚本：
    ```bash
    python check_user_repos.py
    ```

2. 输入 GitHub 用户地址和个人访问令牌（如果 `access_token.txt` 文件不存在）：
    ```plaintext
    请输入GitHub用户地址:
    https://github.com/用户名?tab=repositories
    ```

3. 脚本将检查该用户的所有非归档仓库，并在控制台显示进度条。完成后，将生成 `result.md` 文件，包含每个仓库的检查结果。

## 示例

运行示例：
```bash
python check_user_repos.py
请输入GitHub用户地址:
https://github.com/用户名?tab=repositories
```

生成的 `result.md` 文件示例：

# 仓库活动检查结果 (2023-06-01 12:00:00)

## https://github.com/用户名/仓库名
符合活动要求。

## https://github.com/用户名/另一个仓库名
不符合活动要求，原因如下：
- 1个月前没有代码提交。
- 3个月前没有代码提交。

## 注意事项

- 请确保 `access_token.txt` 文件存放在项目根目录，并且在 `.gitignore` 文件中忽略该文件，以防止泄露个人访问令牌。
- 如果没有 `access_token.txt` 文件，脚本会提示你输入 GitHub 个人访问令牌，并将其保存到 `access_token.txt` 文件中。

## .gitignore

确保 `.gitignore` 文件中包含以下内容：

```
access_token.txt
```


好的，以下是完善后的 `README.md` 文件内容：

```
markdownCopy code# JetBrainsOSSProjectCheck

JetBrainsOSSProjectCheck 是一个用于简单检查 JetBrains 开源许可证项目是否符合要求的工具。如果项目不符合要求，它会输出不符合的原因。

## 功能

- 检查指定 GitHub 用户的所有非归档仓库的提交活动。
- 输出符合活动要求和不符合活动要求的仓库列表及其原因。
- 生成 Markdown 格式的结果报告 (`result.md`)。
- 支持多线程和进度条显示检查进度。

## 安装

1. 克隆仓库：
    ```bash
    git clone https://github.com/你的用户名/JetBrainsOSSProjectCheck.git
    cd JetBrainsOSSProjectCheck
    ```

2. 安装依赖项：
    ```bash
    pip install -r requirements.txt
    ```

## 使用

1. 运行脚本：
    ```bash
    python check_user_repos.py
    ```

2. 输入 GitHub 用户地址和个人访问令牌（如果 `access_token.txt` 文件不存在）：
    ```plaintext
    请输入GitHub用户地址:
    https://github.com/用户名?tab=repositories
    ```

3. 脚本将检查该用户的所有非归档仓库，并在控制台显示进度条。完成后，将生成 `result.md` 文件，包含每个仓库的检查结果。

## 示例

运行示例：
```bash
python check_user_repos.py
```

输入 GitHub 用户地址：

```
plaintextCopy code请输入GitHub用户地址:
https://github.com/用户名?tab=repositories
```

生成的 `result.md` 文件示例：

```
markdownCopy code# 仓库活动检查结果 (2023-06-01 12:00:00)

## https://github.com/用户名/仓库名
符合活动要求。

## https://github.com/用户名/另一个仓库名
不符合活动要求，原因如下：
- 1个月前没有代码提交。
- 3个月前没有代码提交。
```

## 注意事项

- 请确保 `access_token.txt` 文件存放在项目根目录，并且在 `.gitignore` 文件中忽略该文件，以防止泄露个人访问令牌。
- 如果没有 `access_token.txt` 文件，脚本会提示你输入 GitHub 个人访问令牌，并将其保存到 `access_token.txt` 文件中。

## .gitignore

确保 `.gitignore` 文件中包含以下内容：

```
plaintext
Copy code
access_token.txt
```

## 许可证

本项目基于 MIT 许可证开源。详细信息请参见 LICENSE 文件。
