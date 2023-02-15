import pandas as pd
import os
from datetime import date
import json


def get_stat(file=os.listdir(f"data/vacancies")[-1]):
    vacancies = pd.read_excel(f"./data/vacancies/{file}/prepared_data/DataFrame.xlsx", engine="openpyxl")

    def num_prof_roles(row):
        all_prof_roles = {"company": row["index"]}
        for prof_role in vacancies["prof_role"].unique():
            all_prof_roles[prof_role] = (len(vacancies[(vacancies["company"] == row["index"]) &
                                                       (vacancies["prof_role"] == prof_role)]))
        return all_prof_roles

    def num_years(row):
        all_years = {"company": row["index"]}
        for years_exp in vacancies["experience"].unique():
            all_years[years_exp] = (len(vacancies[(vacancies["company"] == row["index"]) &
                                                  (vacancies["experience"] == years_exp)]))
        return all_years

    def all_analytics(row):
        all_prof_roles = {"company": row["index"]}
        for prof_role in vacancies["prof_role"].unique():
            for years_exp in vacancies["experience"].unique():
                all_prof_roles[prof_role + "" "" + years_exp] = (len(vacancies[
                                                                         (vacancies["company"] == row["index"]) &
                                                                         (vacancies["experience"] == years_exp) &
                                                                         (vacancies["prof_role"] == prof_role)]))
            all_prof_roles[prof_role + "all"] = len(vacancies[(vacancies["company"] == row["index"]) &
                                                              (vacancies["prof_role"] == prof_role)])

        return all_prof_roles

    def average_salary_prof_roles(row):
        average_salary_prof_roles = {"compamy": row["index"]}
        for prof_role in vacancies["prof_role"].unique():
            average_salary_prof_roles[prof_role] = round(vacancies[(vacancies["company"] == row["index"]) &
                                                                   (vacancies["prof_role"] == prof_role)])[
                "salary_from"].dropna(
                inplace=False).mean()
        return average_salary_prof_roles

    def average_salary_years_exp(row):
        average_salary_years_exp = {"company": row["index"]}
        for years_exp in vacancies["experience"].unique():
            average_salary_years_exp[years_exp] = round(vacancies[(vacancies["company"] == row["index"]) &
                                                                  (vacancies["experience"] == years_exp)])[
                "salary_from"].dropna(
                inplace=False).mean()
        return average_salary_years_exp

    def info_prof_roles(row):
        info_prof_roles_row = {"prof_role": row["index"]}
        for years_experience in vacancies["experience"].unique():
            info_prof_roles_row[years_experience] = round(vacancies[(vacancies["prof_role"] == row["index"]) &
                                                                    (vacancies["experience"] == years_experience)])[
                "salary_from"].dropna(inplace=False).mean()
        return info_prof_roles_row

    def fill_nan_salary(row):
        salary_from = row["salary_from"]
        salary_to = row["salary_to"]
        if pd.isna(salary_from) is True and pd.isna(salary_to) is False:
            salary_from = salary_to
        if pd.isna(salary_from) is False and pd.isna(salary_to) is True:
            salary_to = salary_from
        return salary_from, salary_to

    companies_stat = vacancies["company"].value_counts().reset_index()

    prof_roles = companies_stat.apply(num_prof_roles, axis="columns").to_list()

    years_experience = companies_stat.apply(num_years, axis="columns").to_list()

    average_salary_prof_role = companies_stat.apply(average_salary_prof_roles, axis="columns").to_list()

    average_salary_years_experience = companies_stat.apply(average_salary_years_exp, axis="columns").to_list()

    prof_roles_stat = vacancies["prof_role"].value_counts().reset_index()

    info_prof_roles_stat = prof_roles_stat.apply(info_prof_roles, axis="columns").to_list()

    return json.dumps({"name": "analytics", "description": "some_text", "prof_roles": prof_roles,
                       "years_experience": years_experience,
                       "average_salary_prof_role": average_salary_prof_role,
                       "average_salary_years_experience": average_salary_years_experience,
                       "info_prof_roles_stat": info_prof_roles_stat})



jsObj = json.loads(get_stat())
print(jsObj['prof_roles'])
