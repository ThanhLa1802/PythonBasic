from sql_connection import get_sql_connection

query = "SELECT * FROM grocery_store.products"
query2 = "SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM products \
INNER JOIN uom ON products.uom_id = uom.uom_id"

def get_all_products(connection):
    cursor = connection.cursor()
    cursor.execute(query2)

    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()

if __name__ == "__main__":
    connection = get_sql_connection()
    get_all_products(connection)