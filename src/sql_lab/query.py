import logging
import os
import mysql.connector

# Configure logging so status messages show up in the terminal
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Read database credentials from environment variables (same pattern as process.py)
DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

# Table uploaded by process.py
TABLE = "mock"

def get_connection():
    """Open and return a connection to the MySQL database using the env var credentials."""
    logger.info("Connecting to database %s on %s", DBNAME, DBHOST)
    return mysql.connector.connect(
        host=DBHOST,
        user=DBUSER,
        password=DBPASS,
        database=DBNAME,
        port=3306,
    )


def get_data_by_group(value):
    """Return all rows from the mock table where the `group` column equals value.
    Filter column: `group`
    value is passed as a query parameter, never formatted into the SQL string."""
    # %s is a placeholder; the connector handles quoting/escaping of value
    query = "SELECT * FROM mock WHERE `group` = %s"
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # Pass the parameter as a one-element tuple (note the trailing comma)
        cursor.execute(query, (value,))
        rows = cursor.fetchall()
        logger.info("Retrieved %d rows where group = %r", len(rows), value)
        cursor.close()
        conn.close()
        return rows
    except mysql.connector.Error as e:
        logger.error("Error querying rows by group: %s", e)
        return []


def get_columns():
    """Return the list of column names in the mock table."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SHOW COLUMNS FROM mock")
        # The first field of each SHOW COLUMNS row is the column name
        columns = [row[0] for row in cursor.fetchall()]
        logger.info("Found columns in %s: %s", TABLE, columns)
        cursor.close()
        conn.close()
        return columns
    except mysql.connector.Error as e:
        logger.error("Error reading columns: %s", e)
        return []


def plot_counts(groupby):
    """Count rows per distinct value of the column groupby and return them as (value, count) pairs.
    Column names cannot be passed as %s parameters, so groupby is checked against
    the table's real column names before it is placed in the SQL string.
    """
    # Whitelist check prevents SQL injection through the column name
    if groupby not in get_columns():
        logger.error("Invalid column name: %r", groupby)
        return []

    # Backticks let us group by reserved words such as `group`
    query = f"SELECT `{groupby}`, COUNT(*) AS n FROM mock GROUP BY `{groupby}` ORDER BY n DESC"
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        counts = cursor.fetchall()
        logger.info("Counted %d distinct values of %s", len(counts), groupby)
        cursor.close()
        conn.close()
        return counts
    except mysql.connector.Error as e:
        logger.error("Error counting rows by %s: %s", groupby, e)
        return []


def main():
    """Demonstrate the query functions on the mock table."""
    # Filter rows by a group value
    rows = get_data_by_group("Team A")
    print(f"Rows in group 'Team A': {len(rows)}")
    for row in rows[:5]:
        print(row)

    # Count rows per group, then per another column
    for column in ["group", "gender"]:
        print(f"\nCounts by {column}:")
        for value, n in plot_counts(column):
            print(f"  {value}: {n}")


if __name__ == "__main__":
    main()
