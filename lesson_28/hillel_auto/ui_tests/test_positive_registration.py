def test_positive_registration(driver, main_page):
    main_page.register().account_dropdown_present()
