import psycopg2
from configparser import ConfigParser

config = ConfigParser()
config.read('pipeline.conf')

try:
    conn = psycopg2.connect(
        host=config.get('postgres_config', 'host'),
        port=config.get('postgres_config', 'port'),
        user=config.get('postgres_config', 'user'),
        password=config.get('postgres_config', 'password'),
        database=config.get('postgres_config', 'database')
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 1;")
    result = cursor.fetchone()
    print(f"✅ Connection successful! Query result: {result}")
    cursor.close()
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")