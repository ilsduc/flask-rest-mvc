class APIService:

    # Be carefull here APIService is base on BaseModel class
    @classmethod
    def getList(that, instance):
        instances = instance.find()
        return instances, None

    @classmethod
    def getItem(that, instance, id):
        instance.findById(id)
        return instance, None
        
    @classmethod
    def post(that, instance, values, required_values):
        is_ok = all (k in values for k in required_values)
        if not is_ok:
            return None, 'Missing fields.'
        instance.hydrate(values)
        instance.save()
        return instance, None
        

    @classmethod
    def put(that, instance, id, values):
        instance.findById(id)
        # 
        if not instance.is_valid():
            return None, 'Bad request'

        instance.hydrate(values)
        instance.save()
        return instance, None
        

    @classmethod
    def delete(that, instance, id):
        instance.findById(id)
        # 
        if not instance.is_valid():
            return None, 'Bad request'

        instance.remove()
        return instance, None
        