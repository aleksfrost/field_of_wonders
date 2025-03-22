
from database.db import request_from_db, request_into_db


class Prise:

    prise_id: str

    def __init__(
            self,
            prise_id,
            prise_description,
            price_in_scores,
            discount_value,
            categorie_id,
            to_show):

        self.prise_id = prise_id
        self.prise_description = prise_description
        self.price_in_scores = price_in_scores
        self.categorie_id = categorie_id
        self.discount_value = discount_value
        self.to_show = to_show


def get_prises():
    stmnt = """
            select * from prises;
            """
    prises = [Prise(*pr) for pr in request_from_db(stmnt)]
    return prises

def get_prise(prise):
    stmnt = f"""
            select * from prises
            where prise_description = '{prise}';
            """
    prise = Prise(*request_from_db(stmnt)[0])
    return prise

def add_prise(prise_description, price_in_scores, categorie, discount_value):
    stmnt = f"""
            select * from categories
            where categorie_name = {categorie}
            ;
            """
    cat_id = request_from_db(stmnt)[0][0]
    if cat_id:
        stmnt = f"""
                insert into prises (prise_description, price_in_scores, discount_value, categorie_id)
                values
                ({prise_description}, {price_in_scores}, {discount_value}, {cat_id})
                ;
                """
        request_into_db(stmnt)
    else:
        stmnt = f"""
                insert into categories (categorie_name)
                values ({categorie})
                """
        request_into_db
        add_prise(prise_description, price_in_scores, categorie, discount_value)
