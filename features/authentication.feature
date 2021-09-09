Feature: Search question database

  Background: Preconditions
    Given I access database questions site

  @invalidSearch
  Scenario:Make a invalid search
    When I search a question "Science:"
    Then I must see a message error

  @validSearch
  Scenario: Make a valid search
    When I search a valid question "Is Tartu the capital of Estonia?"
    Then I see the "Is Tartu the capital of Estonia?" question

  @categorySearch
  Scenario: Make a search in category
    When I search in category for "Science: Computers"
    Then I see 25 result list

  @pageControl
  Scenario: Show page control in search page
    When I search in category for "Science: Computers"
    Then I see page control