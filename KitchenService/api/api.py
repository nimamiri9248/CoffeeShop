from flask_smorest import Blueprint
from flask.views import MethodView
from api.schemas import (
    GetScheduleOrderSchema,
    GetScheduleOrdersSchema,
    ScheduleOrderSchema,
    ScheduleStatusSchema,
    GetKitchenScheduleParameters

)

blueprint = Blueprint('kitchen',__name__,description='Kitchen API')


@blueprint.route('/kitchen/schedules')
class KitchenSchedules(MethodView):
    @blueprint.arguments(GetKitchenScheduleParameters,location='query')
    @blueprint.response(schema=GetScheduleOrdersSchema,status_code=200)
    def get(self,parameters):
        return 'Kitchen Schedules'

    @blueprint.arguments(ScheduleOrderSchema)
    @blueprint.response(schema=GetScheduleOrderSchema,status_code=201)
    def post(self,payload):
        return payload
    
@blueprint.route('/kitchen/schedules/<order_id>')
class KitchenSchedule(MethodView):
    @blueprint.response(schema=GetScheduleOrderSchema,status_code=200)
    def get(self,schedule_id):
        return 'Kitchen Schedule'

    @blueprint.arguments(ScheduleOrderSchema)
    @blueprint.response(schema=GetScheduleOrderSchema,status_code=200)
    def put(self,schedule_id,payload):
        return payload

    @blueprint.response(status_code=204)
    def delete(self,schedule_id):
        return None

@blueprint.response(status_code=200,schema=GetScheduleOrderSchema)   
@blueprint.route('/kitchen/schedules/<schedule_id>/cance')
def cancel_schedule(schedule_id):
    return 'Cancel Kitchen Schedule'

@blueprint.response(status_code=200,schema=GetScheduleOrderSchema)
@blueprint.route('/kitchen/schedules/<schedule_id>/status')
def get_schedule_status(schedule_id):
    return 'Get Kitchen Schedule Status'


