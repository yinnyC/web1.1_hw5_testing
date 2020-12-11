import pytest

from .app import app

#######################
# Index Tests
# (there's only one here because there is only one possible scenario!)
#######################


def test_index():
    """Test that the index page shows "Hello, World!" """
    res = app.test_client().get("/")
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    expected_page_text = "Hello, World!"
    assert expected_page_text == result_page_text


#######################
# Color Tests
#######################


def test_color_results_blue():
    result = app.test_client().get("/color_results?color=blue")

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Wow, blue is my favorite color, too!"
    assert expected_page_text == result_page_text


def test_color_results_scenario1():
    result = app.test_client().get("/color_results?color=purple")

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Wow, purple is my favorite color, too!"
    assert expected_page_text == result_page_text


def test_color_results_edgecase1():
    result = app.test_client().get("/color_results?color=111")

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "Wow, 111 is my favorite color, too!"
    assert expected_page_text == result_page_text


#######################
# Froyo Tests
#######################


def test_froyo_results_scenario1():
    result = app.test_client().get("/froyo_results?flavor=vanilla&toppings=peanut")

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You ordered vanilla flavored Fro-Yo with toppings peanut!"
    assert expected_page_text == result_page_text


def test_froyo_results_scenario2():
    result = app.test_client().get("/froyo_results?flavor=123&toppings=321")

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You ordered 123 flavored Fro-Yo with toppings 321!"
    assert expected_page_text == result_page_text


def test_froyo_results_edgecase1():
    result = app.test_client().get("/froyo_results?flavor=chocolate&toppings=caramel")

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You ordered chocolate flavored Fro-Yo with toppings caramel!"
    assert expected_page_text == result_page_text


def test_froyo_results_edgecase2():
    result = app.test_client().get(
        "/froyo_results?flavor=strawberry&toppings=marshmallow"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = (
        "You ordered strawberry flavored Fro-Yo with toppings marshmallow!"
    )
    assert expected_page_text == result_page_text


#######################
# Reverse Message Tests
#######################


def test_message_results_helloworld():
    form_data = {"message": "Hello World"}
    res = app.test_client().post("/message_results", data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "dlroW olleH" in result_page_text


def test_message_results_scenario2():
    form_data = {"message": "Yin"}
    res = app.test_client().post("/message_results", data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "niY" in result_page_text


def test_message_results_edgecase1():
    form_data = {"message": "WEB1.1"}
    res = app.test_client().post("/message_results", data=form_data)
    assert res.status_code == 200

    result_page_text = res.get_data(as_text=True)
    assert "1.1BEW" in result_page_text


#######################
# Calculator Tests
#######################


def test_calculator_results_scenario1():
    result = app.test_client().get(
        "/calculator_results?operand1=2&operation=add&operand2=2"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You chose to add 2 and 2. Your result is: 4"
    assert expected_page_text == result_page_text


def test_calculator_results_scenario2():
    result = app.test_client().get(
        "/calculator_results?operand1=2&operation=subtract&operand2=2"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You chose to subtract 2 and 2. Your result is: 0"
    assert expected_page_text == result_page_text


def test_calculator_results_scenario3():
    result = app.test_client().get(
        "/calculator_results?operand1=2&operation=multiply&operand2=2"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You chose to multiply 2 and 2. Your result is: 4"
    assert expected_page_text == result_page_text


def test_calculator_results_scenario4():
    result = app.test_client().get(
        "/calculator_results?operand1=2&operation=divide&operand2=2"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You chose to divide 2 and 2. Your result is: 1.0"
    assert expected_page_text == result_page_text


def test_calculator_results_edgecase1():
    result = app.test_client().get(
        "/calculator_results?operand1=10&operation=divide&operand2=0"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You chose to divide 10 and 0. Your result is: Error"
    assert expected_page_text == result_page_text


def test_calculator_results_edgecase2():
    result = app.test_client().get(
        "/calculator_results?operand1=1&operation=multiply&operand2=0"
    )

    assert result.status_code == 200

    result_page_text = result.get_data(as_text=True)
    expected_page_text = "You chose to multiply 1 and 0. Your result is: 0"
    assert expected_page_text == result_page_text