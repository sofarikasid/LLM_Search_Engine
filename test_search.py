import pytest
from unittest.mock import patch
from mylib.search import final_result


@pytest.mark.parametrize(
    "query, expected_response",
    [
        (
            "walmart",
            [
                "OFFER: Arber, at Walmart\ncombined: ARBER WALMART",
                "OFFER: Back to the Roots Seeds, at Walmart\ncombined: Packaged Meals & Sides BACK TO THE ROOTS WALMART",
                "OFFER: OxiClean™ Laundry Stain Removers, select varieties at Walmart\ncombined: WALMART OXICLEAN",
                "OFFER: Gorton's at select retailers\ncombined: Frozen Seafood Jerky & Dried Meat Frozen Meals WALMART GORTONS",
                "OFFER: Gorton's Air Fried Butterfly Shrimp, at Walmart\ncombined: Frozen Seafood Jerky & Dried Meat Frozen Meals WALMART GORTONS",
                "OFFER: L’Oréal Paris Men Expert hair color, spend $9 at Walmart\ncombined: Hair Care LOREAL PARIS HAIR COLOR WALMART",
                "OFFER: L'Oréal Paris Men Expert hair color, spend $19 at Walmart\ncombined: Hair Care LOREAL PARIS HAIR COLOR WALMART",
                "OFFER: Back to the Roots Grow Kits at Walmart or The Home Depot\ncombined: Packaged Meals & Sides BACK TO THE ROOTS WALMART",
                "OFFER: Cooked Perfect® Meatballs, at Walmart\ncombined: Frozen Chicken COOKED PERFECT WALMART",
                "OFFER: Purex® laundry detergent, select varieties, at Walmart\ncombined: PUREX Laundry Supplies WALMART",
            ],
        ),
    ],
)
@patch("builtins.input", side_effect=["query_1", "query_2"])
def test_final_result(mock_input, query, expected_response):
    response = final_result(query)
    assert type(response) == type(expected_response)


if __name__ == "__main__":
    pytest.main()
