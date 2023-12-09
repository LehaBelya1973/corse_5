import psycopg2

class DBManager():
    def get_companies_and_vacancies_count(self):
        pass

    def get_all_vacancies(self):
        pass

    def get_avg_salary(self):
        pass

    def get_vacancies_with_higher_salary(self):
        pass

    def get_vacancies_with_keyword(self, keyword, cur):
        cur.execute(f'''SELECT * FROM vacancies WHERE vacancy_name LIKE "%{keyword}%"''')
        result = cur.fetchall()
        return result
