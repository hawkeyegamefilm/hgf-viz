import pandas as pd

df = pd.read_csv('data/iowa_rb_buckets_sheet.csv')

html = df.to_html(classes=["table", "table-striped", "table-hover"], formatters={
    'Loss': "{:,.2%}".format,
    'No gain': "{:,.2%}".format,
    '1-4y': "{:,.2%}".format,
    '5-9y': "{:,.2%}".format,
    '10+': "{:,.2%}".format,
})

text_file = open("iowa_rb_buckets.html", "w")
text_file.write(
    """<!-- Latest compiled and minified Bootstrap CSS --> <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" />""")

text_file.write(html)
text_file.close()
