import unittest
import pandas as pd
from main import df, monthly_revenue, product_revenue, customer_revenue, top_customers

class TestOrdersAnalysis(unittest.TestCase):

    def test_monthly_revenue(self):
        # Define expected results
        expected_monthly_revenue = df.groupby('month').apply(lambda x: (x['product_price'] * x['quantity']).sum())
        # Check if the results match
        pd.testing.assert_series_equal(monthly_revenue, expected_monthly_revenue)

    def test_product_revenue(self):
        # Define expected results
        expected_product_revenue = df.groupby('product_name').apply(lambda x: (x['product_price'] * x['quantity']).sum())
        # Check if the results match
        pd.testing.assert_series_equal(product_revenue, expected_product_revenue)

    def test_customer_revenue(self):
        # Define expected results
        expected_customer_revenue = df.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum())
        # Check if the results match
        pd.testing.assert_series_equal(customer_revenue, expected_customer_revenue)

    def test_top_customers(self):
        # Define expected results
        expected_top_customers = customer_revenue.nlargest(10)
        # Check if the results match
        pd.testing.assert_series_equal(top_customers, expected_top_customers)

if __name__ == '__main__':
    unittest.main()
