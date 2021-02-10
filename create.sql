CREATE TABLE products (
  title TEXT NOT NULL,
  asin VARCHAR(100) PRIMARY KEY
);

CREATE TABLE reviews (
    id SERIAl,
    asin VARCHAR(100) NOT NULL,
    title TEXT NOT NULL,
    review TEXT NOT NULL,
	CONSTRAINT fk_asin FOREIGN KEY(asin) REFERENCES products(asin)
);


