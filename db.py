def get_image_url(connection, image_param):
    cursor = connection.cursor()
    query = f"SELECT URL FROM PhoUrl WHERE useID = '{image_param}'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()

    return results[0][0]


def get_image_url_nat(connection, image_param):
    cursor = connection.cursor()
    query = f"SELECT URL FROM MangaUrl WHERE useID = '{image_param}'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()

    return results[0][0]