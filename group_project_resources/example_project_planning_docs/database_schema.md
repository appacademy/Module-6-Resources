# **Database Schema**

## `users`

| column name | data type | details                   |
|-------------|-----------|---------------------------|
| id          | integer   | not null, primary key     |
| username    | string    | not null,                 |
| email       | string    | not null, indexed, unique |
| created_at  | datetime  | not null                  |
| updated-at  | datetime  | not null                  |

## `fauxtweets`

| column name | data type | details               |
|-------------|-----------|-----------------------|
| id          | integer   | not null, primary key |
| content     | string    | not null              |
| userId      | integer   | not null, foreign key |
| created_at  | datetime  | not null              |
| updated-at  | datetime  | not null              |

* `userId` references `users` table

## `fauxcomments`

| column name   | data type | details               |
|---------------|-----------|-----------------------|
| id            | integer   | not null, primary key |
| content       | string    | not null              |
| userId        | integer   | not null, foreign key |
| fauxCommentId | integer   | not null, foreign key |
| created_at    | datetime  | not null              |
| updated-at    | datetime  | not null              |

* `userId` references `users` table
* `fauxCommentId` references `fauxcomments` table

## `fauxlikes`

| column name   | data type | details                        |
|---------------|-----------|--------------------------------|
| id            | integer   | not null, primary key          |
| userId        | integer   | not null, indexed, foreign key |
| fauxTweetId   | integer   | indexed, foreign key           |
| fauxCommentId | integer   | indexed, foreign key           |

* `userId` references `users` table
* `fauxTweetId` references `fauxtweets` table
* `fauxCommentId` references `fauxcomments` table
