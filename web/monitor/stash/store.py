import base64
import hashlib
import json
import re
import sqlite3
from contextlib import closing
from pathlib import Path

from cryptography.fernet import Fernet


class StashStore:
    def __init__(self, database, secret_key, bucket=""):
        self.database = Path(database)
        self.bucket = bucket
        key = hashlib.sha256(b"poe-stash-store-v1:" + str(secret_key).encode("utf-8")).digest()
        self.cipher = Fernet(base64.urlsafe_b64encode(key))

    def _owner(self, owner):
        if not isinstance(owner, str) or not re.fullmatch(r"[A-Za-z0-9_-]{20,80}", owner):
            raise ValueError("Invalid stash connection identifier")
        return owner

    def _connection(self):
        self.database.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(self.database)
        connection.execute("CREATE TABLE IF NOT EXISTS stash_user_data (owner TEXT PRIMARY KEY, payload BLOB NOT NULL)")
        connection.commit()
        return connection

    def load(self, owner):
        owner = self._owner(owner)
        if self.bucket:
            from google.cloud import storage

            blob = storage.Client().bucket(self.bucket).get_blob(f"stash/users/{owner}.enc")
            if blob is None:
                return {}
            payload = blob.download_as_bytes()
        else:
            with closing(self._connection()) as connection:
                row = connection.execute("SELECT payload FROM stash_user_data WHERE owner = ?", (owner,)).fetchone()
            if row is None:
                return {}
            payload = row[0]
        return json.loads(self.cipher.decrypt(payload).decode("utf-8"))

    def save(self, owner, data):
        owner = self._owner(owner)
        payload = self.cipher.encrypt(json.dumps(data, ensure_ascii=False).encode("utf-8"))
        if self.bucket:
            from google.cloud import storage

            storage.Client().bucket(self.bucket).blob(f"stash/users/{owner}.enc").upload_from_string(payload, content_type="application/octet-stream")
        else:
            with closing(self._connection()) as connection, connection:
                connection.execute("INSERT INTO stash_user_data (owner, payload) VALUES (?, ?) ON CONFLICT(owner) DO UPDATE SET payload=excluded.payload", (owner, payload))

    def delete(self, owner):
        owner = self._owner(owner)
        if self.bucket:
            from google.cloud import storage

            blob = storage.Client().bucket(self.bucket).get_blob(f"stash/users/{owner}.enc")
            if blob:
                blob.delete()
        else:
            with closing(self._connection()) as connection, connection:
                connection.execute("DELETE FROM stash_user_data WHERE owner = ?", (owner,))