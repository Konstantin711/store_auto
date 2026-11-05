import pytest

@pytest.fixture
def db_get_men_nav_menu(get_data_from_db):
    query = """
                SELECT DISTINCT
                    COALESCE(NULLIF(n.title_override, ''), c.title) AS title
                FROM store_app_item AS i
                JOIN store_app_itemsex AS s
                    ON s.id = i.parent_type_id
                JOIN store_app_item_category AS ic
                    ON ic.item_id = i.id
                JOIN store_app_itemmaincategory AS c
                    ON c.id = ic.itemmaincategory_id
                LEFT JOIN store_app_headernavigationitem AS n
                    ON n.sex_id = s.id AND n.category_id = c.id
                LEFT JOIN store_app_headernavigationitem AS section_nav
                    ON section_nav.sex_id = s.id
                    AND section_nav.category_id IS NULL
                WHERE s.slug = 'men'
                  AND COALESCE(n.is_active, TRUE)
                  AND COALESCE(section_nav.is_active, TRUE)
                ORDER BY title;
            """
    result = get_data_from_db(query, (), fetch="all")
    titles = result["title"].tolist()

    return titles

@pytest.fixture
def db_get_woman_nav_menu(get_data_from_db):
    query = """
                SELECT DISTINCT
                    COALESCE(NULLIF(n.title_override, ''), c.title) AS title
                FROM store_app_item AS i
                JOIN store_app_itemsex AS s
                    ON s.id = i.parent_type_id
                JOIN store_app_item_category AS ic
                    ON ic.item_id = i.id
                JOIN store_app_itemmaincategory AS c
                    ON c.id = ic.itemmaincategory_id
                LEFT JOIN store_app_headernavigationitem AS n
                    ON n.sex_id = s.id AND n.category_id = c.id
                LEFT JOIN store_app_headernavigationitem AS section_nav
                    ON section_nav.sex_id = s.id
                    AND section_nav.category_id IS NULL
                WHERE s.slug = 'woman'
                  AND COALESCE(n.is_active, TRUE)
                  AND COALESCE(section_nav.is_active, TRUE)
                ORDER BY title;
            """
    result = get_data_from_db(query, (), fetch="all")
    titles = result["title"].tolist()

    return titles