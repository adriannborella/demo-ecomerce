class RouterSql(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'data':
            return 'data'
        
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if(db == 'default'):
            return True
        return False