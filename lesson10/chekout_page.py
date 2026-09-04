import pytest

from pages.checkout_page import CheckoutPage


@pytest.mark.parametrize(
    "first_name, last_name, postal_code, should_pass, case_id",
    [
       
        ("محمد🕌", "לוי\u200E", "12345", True, "unicode_rtl_emoji_mixed_script"),

        
        ("A", "", "1", False, "boundary_empty_required_last_name"),

       
        ("Jane", "Doe", "9" * 5000, True, "boundary_5000_char_postal_code"),

       
        ("   John   ", "  \t  ", "  94103  ", True, "whitespace_only_and_padded_values"),

        
        ("<script>alert(1)</script>", "'; DROP TABLE users;--", "1' OR '1'='1",
         True, "xss_and_sql_injection_payloads"),
    ],
)


def test_checkout_form_edge_cases(
    logged_in_page, first_name, last_name, postal_code, should_pass, case_id
):
    logged_in_page.locator("#add-to-cart-sauce-labs-backpack").click()

    checkout = CheckoutPage(logged_in_page)
    checkout.open_from_cart()
    checkout.fill_form(first_name, last_name, postal_code)

    if should_pass:
        assert checkout.is_on_overview_page(), (
            f"[{case_id}] expected checkout-step-two, got {logged_in_page.url} "
            f"| error: {checkout.get_error_text()}"
        )
    else:
        assert checkout.is_error_visible(), (
            f"[{case_id}] expected a validation error but the form was submitted"
        )
  