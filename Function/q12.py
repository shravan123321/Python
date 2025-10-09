'''
   you're creating a monthly report for a cafe's sales.
   instead of putting all logic in one place. break it down.
   taxk:
     - Write a function generate_report() that calls.
       -fetch_sales()
       -filter_valid_orders()
       -summarize_data()
'''

def fetch_sales() :
    print("fetch_sales")

def filter_valid_order() :
    print("filter the valid order ")

def summarize_data() :
    print("Summarize the data ")

def generate_report() :
    fetch_sales()
    filter_valid_order()
    summarize_data()
    print("report is ready ")

print("monthly report cafe sales ")

generate_report()