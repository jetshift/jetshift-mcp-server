import requests
import json

from api import config


def jetshift_databases() -> str:
    """
    List all JetShift databases via the REST API.
    """
    try:
        resp = requests.get(f"{config.JETSHIFT_API_URL}/databases/")
        resp.raise_for_status()
        return resp.text.strip()
    except Exception as e:
        return f"Error fetching databases: {e}"


def create_database(dialect: str, title: str, host: str, port: int, username: str, password: str, database: str) -> str:
    """
    Create a new JetShift database connection.

    Args:
        dialect: Type of database (dialects., 'mysql', 'postgresql', 'clickhouse').
        title: A title for the database.
        host: Database host address.
        port: Database port number.
        username: Database username.
        password: Database password.
        database: Database name.

    Returns:
        Success message or error.
    """
    try:
        payload = {
            "dialect": dialect,
            "type": "target",
            "title": title,
            "host": host,
            "port": port,
            "username": username,
            "password": password,
            "database": database,
            "secure": False,
            "status": True,
        }
        resp = requests.post(f"{config.JETSHIFT_API_URL}/databases/", json=payload)
        resp.raise_for_status()
        data = resp.json()
        return f"Database '{title}' created successfully! ID: {data.get('id')}"
    except Exception as e:
        return f"Error creating database: {e}"


def get_database(database_id: int) -> str:
    """
    Retrieve a JetShift database connection by its ID.
    """
    try:
        url = f"{config.JETSHIFT_API_URL}/databases/{database_id}/"
        resp = requests.get(url)
        if resp.status_code == 200:
            return json.dumps(resp.json(), indent=2)
        elif resp.status_code == 404:
            return f"Database with ID {database_id} not found."
        else:
            return f"Error [{resp.status_code}]: {resp.text}"
    except Exception as e:
        return f"Error fetching database: {e}"


def update_database(database_id: int, data: dict) -> str:
    """
    Update a JetShift database by its ID.

    :param database_id: ID of the database to update
    :param data: Dictionary containing fields to update
    """
    try:
        url = f"{config.JETSHIFT_API_URL}/databases/{database_id}/"
        headers = {'Content-Type': 'application/json'}
        resp = requests.patch(url, headers=headers, data=json.dumps(data))

        if resp.status_code == 200:
            return f"Database with ID {database_id} updated successfully.\n{json.dumps(resp.json(), indent=2)}"
        elif resp.status_code == 404:
            return f"Database with ID {database_id} not found."
        else:
            return f"Error [{resp.status_code}]: {resp.text}"
    except Exception as e:
        return f"Error updating database: {e}"


def delete_database(database_id: int) -> str:
    """
    Delete a JetShift database by its ID.
    """
    try:
        url = f"{config.JETSHIFT_API_URL}/databases/{database_id}/"
        resp = requests.delete(url)
        if resp.status_code == 204:
            return f"Database with ID {database_id} deleted successfully."
        elif resp.status_code == 404:
            return f"Database with ID {database_id} not found."
        else:
            return f"Error [{resp.status_code}]: {resp.text}"
    except Exception as e:
        return f"Error deleting database: {e}"
