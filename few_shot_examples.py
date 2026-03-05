few_shots = [
    {
        'Question': "How many t-shirts do we have left for Nike in XS size and white color?",
        'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
        'SQLResult': "Result of the SQL query",
        'Answer': "91"
    },
    {
        'Question': "How much is the total price of the inventory for all S-size t-shirts?",
        'SQLQuery': "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
        'SQLResult': "Result of the SQL query",
        'Answer': "22292"
    },
    {
        'Question': "If we have to sell all the Levi's T-shirts today with discounts applied. How much revenue will our store generate?",
        'SQLQuery': "SELECT SUM(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) AS total_revenue FROM (SELECT SUM(price*stock_quantity) AS total_amount, t_shirt_id FROM t_shirts WHERE brand = 'Levi' GROUP BY t_shirt_id) a LEFT JOIN discounts ON a.t_shirt_id = discounts.t_shirt_id",
        'SQLResult': "Result of the SQL query",
        'Answer': "16725.4"
    },
    {
        'Question': "How many white color Levi's t-shirts do we have available?",
        'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
        'SQLResult': "Result of the SQL query",
        'Answer': "290"
    },
    {
        'Question': "How many total t-shirts do we have for Nike?",
        'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike'",
        'SQLResult': "Result of the SQL query",
        'Answer': "287"
    },
    {
        'Question': "What is the total revenue if we sell all small size Adidas t-shirts today after discounts?",
        'SQLQuery': "SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) AS total_revenue FROM (SELECT sum(price*stock_quantity) AS total_amount, t_shirt_id FROM t_shirts WHERE brand = 'Adidas' AND size = 'S' GROUP BY t_shirt_id) a LEFT JOIN discounts ON a.t_shirt_id = discounts.t_shirt_id",
        'SQLResult': "Result of the SQL query",
        'Answer': "6112.0"
    },
    {
        'Question': "How much revenue will the store make by selling all XL-size t-shirts with discounts?",
        'SQLQuery': "SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) AS total_revenue FROM (SELECT sum(price*stock_quantity) AS total_amount, t_shirt_id FROM t_shirts WHERE size = 'XL' GROUP BY t_shirt_id) a LEFT JOIN discounts ON a.t_shirt_id = discounts.t_shirt_id",
        'SQLResult': "Result of the SQL query",
        'Answer': "19618.0"
    }
]
