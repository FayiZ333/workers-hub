class EmpRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'employee'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to emp_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'emp_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to emp_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'emp_db'
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'emp_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'emp_db'
        return None



class Emp2Router:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'db3'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to emp2_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'emp2_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to emp2_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'emp2_db'
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'emp2_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'emp2_db'
        return None