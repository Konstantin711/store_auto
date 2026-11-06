import pytest


@pytest.fixture
def db_get_nav_menu(get_data_from_db):
    def _get_nav_menu(sex_slug: str):
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
                ON n.sex_id = s.id
                AND n.category_id = c.id
            LEFT JOIN store_app_headernavigationitem AS section_nav
                ON section_nav.sex_id = s.id
                AND section_nav.category_id IS NULL
            WHERE s.slug = %s
              AND COALESCE(n.is_active, TRUE)
              AND COALESCE(section_nav.is_active, TRUE)
            ORDER BY title;
        """

        result = get_data_from_db(
            query,
            (sex_slug,),
            fetch="all",
        )

        return result["title"].tolist()

    return _get_nav_menu


@pytest.fixture
def db_get_nav_hrefs(get_data_from_db):
    query = """
            SELECT DISTINCT
                s.slug AS sex_slug,
                '/catalog/' || s.slug || '/' || c.slug AS href
            FROM store_app_item AS i
            JOIN store_app_itemsex AS s
                ON s.id = i.parent_type_id
            JOIN store_app_item_category AS ic
                ON ic.item_id = i.id
            JOIN store_app_itemmaincategory AS c
                ON c.id = ic.itemmaincategory_id
            LEFT JOIN store_app_headernavigationitem AS category_nav
                ON category_nav.sex_id = s.id
                AND category_nav.category_id = c.id
            LEFT JOIN store_app_headernavigationitem AS section_nav
                ON section_nav.sex_id = s.id
                AND section_nav.category_id IS NULL
            WHERE s.slug IN (%s, %s)
              AND COALESCE(category_nav.is_active, TRUE)
              AND COALESCE(section_nav.is_active, TRUE)
            ORDER BY s.slug, href;
        """

    result = get_data_from_db(
        query,
        ("men", "women"),
        fetch="all",
    )

    hrefs_by_sex = (
        result.groupby("sex_slug")["href"]
        .apply(list)
        .to_dict()
    )

    men_hrefs = hrefs_by_sex.get("men", [])
    woman_hrefs = hrefs_by_sex.get("women", [])
    return men_hrefs, woman_hrefs
