Feature: Aquabot Logo

  Scenario Outline: Logo presence on Martin Fowler homepage
    Given launch chrome browser
    When open martinfowler homepage
    Then verify logo is displayed on homepage
    And close chrome browser

