from odoo.tests.common import TransactionCase

class TestTask(TransactionCase):

    def test_01_create_task(self):
        """Verify that a task can be created successfully."""
        task = self.env['test.task'].create({
            'name': 'CI Test Task',
        })
        self.assertTrue(task.id, "Task was not created")
        self.assertEqual(task.name, 'CI Test Task')