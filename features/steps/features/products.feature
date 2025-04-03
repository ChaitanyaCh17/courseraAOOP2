Feature: Product Management

  Scenario: Read a product
    Given the following products exist
      | name     | category  | price | available |
      | Laptop   | Electronics | 999.99 | true |
    When I send a GET request to "/products/1"
    Then the response status code should be 200

  Scenario: Update a product
    Given the following products exist
      | name     | category  | price | available |
      | Laptop   | Electronics | 999.99 | true |
    When I send a PUT request to "/products/1" with the following data
      | name  | Updated Laptop |
    Then the response status code should be 200

  Scenario: Delete a product
    Given the following products exist
      | name     | category  | price | available |
      | Laptop   | Electronics | 999.99 | true |
    When I send a DELETE request to "/products/1"
    Then the response status code should be 204

  Scenario: List all products
    Given the following products exist
      | name     | category  | price | available |
      | Laptop   | Electronics | 999.99 | true |
      | Phone    | Electronics | 499.99 | false |
    When I send a GET request to "/products"
    Then the response status code should be 200

  Scenario: Search by name
    Given the following products exist
      | name     | category  | price | available |
      | Laptop   | Electronics | 999.99 | true |
    When I send a GET request to "/products?name=Laptop"
    Then the response status code should be 200

  Scenario: Search by category
    Given the following products exist
      | name     | category  | price | available |
      | Laptop   | Electronics | 999.99 | true |
    When I send a GET request to "/products?category=Electronics"
    Then the response status code should be 200

  Scenario: Search by availability
    Given the following products exist
      | name     | category  | price | available |
      | Laptop   | Electronics | 999.99 | true |
    When I send a GET request to "/products?available=true"
    Then the response status code should be 200
