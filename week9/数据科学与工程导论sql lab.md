# 数据科学与工程导论sql lab

3. 在新数据库中新建一张 user表,插入几条数据,属性包含:唯一标识(id),姓名(name),性别(sex),年龄( age),联系方式( phone)。

```sql
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    sex VARCHAR(10),
    age INT,
    phone VARCHAR(20)
);
```

4. 写出 SQI语句,查询user表中所有年龄在20—30范围内的用户。

```sql
SELECT * FROM user 
WHERE age >= 20 AND age <= 30;
```

5. 写出SQI语句,删除user表中名字包含“张”的用户。

```sql
DELETE FROM user
WHERE name LIKE '%张%';
```

注：`LIKE` 操作符用于匹配包含 "张" 的名字，`%` 是通配符，表示匹配任意字符。



6. 写出SQL语句,计算user表中所有用户的平均年龄。

```sql
SELECT AVG(age) AS average_age
FROM user;
```

注：这条 SQL 语句将计算 `user` 表中所有用户的年龄的平均值，并将结果命名为 "average_age"。



7. 写出SQI语句,查询user表中年龄在20—30范围内,名字包含“张”的用户,并按照年龄从大到小排序输出。

```sql
SELECT *
FROM user
WHERE age >= 20 AND age <= 30 AND name LIKE '%张%'
ORDER BY age DESC;
```

8. 新建两张表, team表(id, teamName) , score表(id, teamid,userid,score)。其中，score表中的teamid为指向team表id的外键, userid为指向user表id的外键。

```sql
-- 创建 team 表
CREATE TABLE team (
    id INT AUTO_INCREMENT PRIMARY KEY,
    teamName VARCHAR(50) NOT NULL
);

-- 创建 score 表
CREATE TABLE score (
    id INT AUTO_INCREMENT PRIMARY KEY,
    teamid INT,
    userid INT,
    score INT,
    FOREIGN KEY (teamid) REFERENCES team(id),
    FOREIGN KEY (userid) REFERENCES user(id)
);
```

注：`FOREIGN KEY (teamid) REFERENCES team(id)`：这部分代码指定了 `teamid` 列是 `score` 表中的一个外键，并且它引用了 `team` 表的 `id` 列作为参考。这意味着每次在 `score` 表中插入一行数据时，`teamid` 列的值必须存在于 `team` 表的 `id` 列中，否则将引发外键约束错误。这确保了 `score` 表中的 `teamid` 列只包含有效的团队标识。

9. 写出 SQI.语句,查询teamName为"ECNU”的队伍中,年龄小于20的用户们。

```sql
SELECT u.*
FROM user u
JOIN score s ON u.id = s.userid
JOIN team t ON s.teamid = t.id
WHERE t.teamName = 'ECNU' AND u.age < 20;
```

注：这个查询语句联结了三张表，首先将 `user` 表和 `score` 表联结，然后将 `score` 表和 `team` 表联结，最后根据筛选条件选择符合条件的记录，即 `teamName` 为 "ECNU" 的队伍中，年龄小于 20 岁的用户。

10. 写出SQL语句,计算teamName为“ECNU”的总分(假设score存在null 值, null值默认为0加入计算)。

```sql
SELECT t.teamName, COALESCE(SUM(s.score), 0) AS total_score
FROM team t
LEFT JOIN score s ON t.id = s.teamid
WHERE t.teamName = 'ECNU'
GROUP BY t.teamName;
```

注：

1. 联结了 `team` 表和 `score` 表，使用 `LEFT JOIN` 来包括所有的队伍，即使它们在 `score` 表中没有相关的得分记录。
2. 使用 `COALESCE` 函数将 `score` 列中的 `NULL` 值替换为 0，以确保将所有得分记录包括在计算中。
3. 使用 `SUM` 函数计算了每支队伍的总分，包括 `NULL` 值被替换为 0 后的得分。
4. 通过 `GROUP BY` 子句，它确保了结果按照队伍的名称进行分组，这里是 "ECNU"。