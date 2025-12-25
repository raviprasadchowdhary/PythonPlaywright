Feature: E2E Test Cases for Order Transaction
    As a user, I want to perform the End-to-End test cases for order transactions to ensure taht the functionality works as expected.

    Scenario: Verify order success message on order details page after placing an order
        Given User has valiid <username> & <password>
        And User is on the login page
        
        When User enters valid username and password & logins
        And user places order for a product
        
        Then User should see the order success message on the order details page

        Examples:
            | username                          | password          |
            | RahulChowdhary@gmail.com          | Rahul@123         |