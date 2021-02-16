@newsletter

Feature: Subscription to newsletter

    @runThis
    Scenario Outline: User has is able to subscribe to newsletter
        Given I am on newsletter page
        When I fill fields with email
        And I fill fields with name
        And I fill fields with surname
        And I choose <type> from dropdown menu
        And I enter today date to 'Starting date' field
        And I marked that I have read the agreement
        And I clicked 'Submit' button
        Then modal with confirmation that user has been added to the newsletter is visible
        Examples:
        | type     |
        | IT       |
        | Industry |
        | Medical  |

    Scenario: User is informed about missing data
        Given I am on newsletter page
        When I leave all fields empty
        And I clicked 'Submit' button
        Then information about missing all fields is displayed correctly

   Scenario: Time of subscription is too short
       Given I am on newsletter page
       When I fill all fields with correct data
       And I enter tomorrow date to 'Ending date' field
       And I clicked 'Submit' button
       Then information that subscription must be longer day is visible

   @skip
   #Wait for further development
   Scenario: User can read agreement
       Given I am on newsletter page
       When I click to read an agreement
       Then agreement contains all valid data

   @skip
   #Wait for further development
   Scenario: User using already existing email should be informed
       Given I am on newsletter page
       When I fill all fields with correct data
       And I clicked 'Submit' button
       And I click OK button on confirmation modal
       And I repeat filing fields with the same data
       Then information that email is already in use is visible

   @skip
   #Wait for further development
   Scenario Outline: User is informed about not filling email filed correctly
       Given I am on newsletter page
       When I fill email field with incorrect <data>
       Then warning about wrong email is visible

       Examples:
       | data       |
       | aaaaaaaaa  |
       | @gmail.com |
