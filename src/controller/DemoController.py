from controller.APIController import APIController
from service.APIService import APIService
from model.Demo import Demo

class DemoController(APIController):

    @classmethod
    def getList(that):
        demo = Demo()
        res, err = APIService.getList(demo)
        return that.respond(res, err)
    
    def getItem(that, id):
        demo = Demo()
        res, err = APIService.getItem(demo)
        return that.respond(res, err)

    @classmethod
    def create(that, values, required_values=[]):
        demo = Demo()
        res, err = APIService.post(demo, values, required_values)
        return that.respond(res, err)

    @classmethod
    def update(that, id, values):
        demo = Demo()
        res, err = APIService.put(demo, id, values)
        return that.respond(res, err)

    @classmethod
    def delete(that, id):
        demo = Demo()
        res, err = APIService.delete(demo, id)
        return that.respond(res, err)
        