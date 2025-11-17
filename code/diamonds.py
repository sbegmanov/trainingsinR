import polars

df = polars.read_csv("data/diamonds.csv", schema_overrides={"viaf":polars.Utf8})
df.schema

