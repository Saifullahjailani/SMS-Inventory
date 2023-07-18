CREATE TABLE IF NOT EXISTS products(
    id TEXT PRIMARY KEY,
    name TEXT,
    price FLOAT8 CHECK (price >= 0)
);

CREATE TABLE IF NOT EXISTS customers(
    id BIGSERIAL PRIMARY KEY,
    name TEXT,
    address TEXT,
    ph_num TEXT
);

CREATE TABLE IF NOT EXISTS sales (
    id BIGSERIAL PRIMARY KEY,
    date_sold TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    receipt_id TEXT,
    quantity INTEGER NOT NULL CHECK(quantity >= 0),
    product_id TEXT REFERENCES products (id),
    customer_id BIGINT REFERENCES customers (id),
    discount FLOAT8,
    discounted_price FLOAT8 NOT NULL CHECK(quantity >= 0)
);
