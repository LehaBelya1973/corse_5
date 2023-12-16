import psycopg2


class DBManager:

    def __init__(self, db_name, user, password, host, port):
        self.conn = psycopg2.connect(db_name=db_name,
                                     user=user,
                                     password=password,
                                     host=host,
                                     port=port)

    def get_companies_and_vacancies_count(self):
        cur = self.conn.cursor()
        cur.execute('''my sql request''')
        return cur.fetchall

    def get_all_vacancies(self):
        cur = self.conn.cursor()
        cur.execute('''my sql request''')
        return cur.fetchall

    def get_avg_salary(self):
        cur = self.conn.cursor()
        cur.execute('''my sql request''')
        return cur.fetchall

    def get_vacancies_with_higher_salary(self):
        cur = self.conn.cursor()
        cur.execute('''my sql request''')
        return cur.fetchall

    def get_vacancies_with_keyword(self, keyword, cur):
        cur.execute(f'''SELECT * FROM vacancies WHERE vacancy_name LIKE "%{keyword}%"''')
        result = cur.fetchall()
        return result
