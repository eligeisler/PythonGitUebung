import unittest
# Importiere die App UND die globalen Variablen zum Zurücksetzen
from flask_todo import app, tasks


class TestTodoApi(unittest.TestCase):
    def setUp(self):
        """Wird vor jedem Test ausgeführt, um Isolation sicherzustellen."""
        self.client = app.test_client()  # [cite: 58, 74]

        # WICHTIG: Die Fake-Datenbank in flask_todo.py leeren
        tasks.clear()

        # Falls du den ID-Counter in flask_todo.py auch zurücksetzen willst,
        # müsste man ihn dort importierbar machen. Für diese Tests reicht
        # das Leeren der Liste meist aus.

    def test_add_task(self):
        """Testet das Erstellen einer Aufgabe."""
        response = self.client.post('/tasks', json={"title": "Einkaufen"})
        # Prüfe den Statuscode 201 (Created)
        self.assertEqual(response.status_code, 201)  # [cite: 62, 81]
        self.assertEqual(response.json["title"], "Einkaufen")

    def test_get_tasks(self):
        """Testet das Abrufen der Liste."""
        self.client.post('/tasks', json={"title": "Test-Task"})
        response = self.client.get('/tasks')  # [cite: 61, 80]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_delete_task(self):
        """Testet das Löschen einer existierenden Aufgabe."""
        # 1. Aufgabe erstellen
        post_res = self.client.post('/tasks', json={"title": "Löschen"})
        task_id = post_res.json["id"]  # Dynamisch die ID holen

        # 2. Diese ID löschen
        response = self.client.delete(f'/tasks/{task_id}')
        # Erwartet 204 (No Content) bei Erfolg
        self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()  # [cite: 16, 68]