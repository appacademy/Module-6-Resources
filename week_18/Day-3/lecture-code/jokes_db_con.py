import psycopg2

CONNECTION_PARAMETERS = {
    "dbname": "dadjokes",
    "user": "dadjokesuser",
    "password": "jokes"
}


with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as curs:
        # curs.execute(
        #     """
        #     CREATE TABLE jokes(
        #     id SERIAL PRIMARY KEY,
        #     joke_body VARCHAR(250),
        #     punchline VARCHAR(250),
        #     rating VARCHAR(15)
        #     );
        #     """
        # )
        def create_joke(joke_body, punchline, rating):
            curs.execute(
                """
                INSERT INTO jokes (joke_body, punchline, rating)
                VALUES(%(joke_body)s, %(punchline)s, %(rating)s)
                """,
                {
                    "joke_body": joke_body,
                    "punchline": punchline,
                    "rating": rating
                }
            )
            curs.execute(
                """
                INSERT INTO jokes (joke_body, punchline, rating)
                VALUES(%s, %s, %s)
                """,
                [
                    joke_body,
                    punchline,
                    rating
                ]
            )
            
        # create_joke("Why did the scarecrow get a promotion?",
        #     "He was outstanding in his field", "G")

        def get_all_jokes():
            curs.execute(
                """
                SELECT *
                FROM jokes;
                """
            )

            results = curs.fetchall()
            print(results)

        get_all_jokes()