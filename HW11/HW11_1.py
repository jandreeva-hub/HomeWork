import polars as pl



df = pl.read_csv('events.csv')
print(df.head())
print(df['category_code'].n_unique())

print(df.select(
    pl.col('category_code').n_unique().alias('unique'),
    pl.approx_n_unique('category_code').alias('unique_approx')
))

df = pl.read_csv('events.csv', null_values='NaN')
description = df.describe()
print(df.filter(pl.col('category_code').is_null()))

df = df.with_columns(pl.col('category_code').forward_fill())
description = df.describe()
print(df.filter(pl.col('category_code').is_null()))

df_with_max_price = df.with_columns([
    pl.col('price').max().over('category_code').alias('max_price_by_category_code')
])
print(df_with_max_price.head(20))

df_with_avg_price = df.with_columns([
    pl.col('price').mean().over('category_code').alias('avg_price_by_category_code')
])


df_with_flag = df_with_avg_price.with_columns([
    (pl.col('price') > pl.col('avg_price_by_category_code')).alias('is_price_above_average')
])


print(df_with_flag)