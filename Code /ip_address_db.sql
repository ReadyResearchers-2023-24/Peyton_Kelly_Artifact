Drop Table if exists ip_address_db;

Create Table IF NOT EXISTS ip_address_db(
    "ip_address_id" INTEGER,
    "ip_address" INTEGER,
    "ip_address_status" TEXT,
    "ip_address_created_at" datetime NOT NULL,
    "ip_address_updated_at" datetime NOT NULL,
);

INSERT INTO ip_address_db VALUES (ip_address_id, ip_address, ip_address_status, ip_address_created_at, ip_address_updated_at)