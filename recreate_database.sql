-- Create transactions table
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    phone TEXT,
    amount REAL,
    type TEXT,
    status TEXT DEFAULT 'SUCCESS'
);

-- Create marketplace table
CREATE TABLE IF NOT EXISTS marketplace (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    barcode TEXT,
    village TEXT
);

-- Create system_settings table
CREATE TABLE IF NOT EXISTS system_settings (
    key TEXT PRIMARY KEY,
    value TEXT
);

-- Insert your actual transaction
INSERT INTO transactions (timestamp, phone, amount, type, status) 
VALUES ('2025-12-29 09:35:05', '27831234567', 450.0, 'PURCHASE_GOAT', 'SUCCESS');

-- Insert sample marketplace items (we'll add more)
INSERT INTO marketplace (name, price, village) VALUES
('Carrots', 15.50, 'Gundo'),
('Chickens', 120.00, 'Sibasa'),
('Maize', 8.75, 'Mukhomi'),
('Tomatoes', 12.30, 'Manini');

-- Insert system settings
INSERT INTO system_settings (key, value) VALUES
('total_users', '708'),
('last_tx_id', '1'),
('platform_version', '4.1');
