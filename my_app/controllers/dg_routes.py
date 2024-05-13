from my_app.models.degital_input import DegitalInputs
from flask_restx import Resource, Namespace, fields

# Define namespaces
dgip_ns = Namespace(
    "digital-input", description="digital-inputs operations", path="/api"
)


@dgip_ns.route("/digital-input/<string:dgip_id>")
class DegitalInput(Resource):
    def get(self, dgip_id):
        """Get the status of a digital-input"""
        if dgip_id in DegitalInputs:
            degital_input = DegitalInputs[dgip_id]
            return degital_input.as_dict(), 200
        else:
            return {"error": f"digital-input with id '{dgip_id}' does not exist"}, 404


@dgip_ns.route("/digital-input/<string:dgip_id>/on")
class DIGINOn(Resource):
    @dgip_ns.expect(
        dgip_ns.model(
            "digital-input On Input",
            {
                "dgip_id": fields.String(
                    description="ID of the digital-input to be turned on",
                    required=True,
                    example="DIGIN-1",
                )
            },
            description="JSON object containing the ID of the digital-input to be turned on",
        )
    )
    @dgip_ns.response(200, "Success")
    @dgip_ns.response(400, "Invalid input")
    @dgip_ns.response(404, "Relay not found")
    def post(self, dgip_id):
        """Turn a digital-input ON."""
        if dgip_id in DegitalInputs:
            relay = DegitalInputs[dgip_id]
            relay.turn_on()
            return DegitalInputs[dgip_id].as_dict(), 200
        else:
            return {"error": f"digital-input with id '{dgip_id}' does not exist"}, 404


@dgip_ns.route("/digital-input/<string:dgip_id>/off")
class DIGINOff(Resource):
    @dgip_ns.expect(
        dgip_ns.model(
            "digital-input Off Input",
            {
                "dgip_id": fields.String(
                    description="ID of the digital-input to be turned off",
                    required=True,
                    example="DIGIN-1",
                )
            },
            description="JSON object containing the ID of the digital-input to be turned off",
        )
    )
    @dgip_ns.response(200, "Success")
    @dgip_ns.response(400, "Invalid input")
    @dgip_ns.response(404, "Relay not found")
    def post(self, dgip_id):
        """Turn a relay ON."""
        if dgip_id in DegitalInputs:
            relay = DegitalInputs[dgip_id]
            relay.turn_off()
            return DegitalInputs[dgip_id].as_dict(), 200
        else:
            return {"error": f"digital-input with id '{dgip_id}' does not exist"}, 404


@dgip_ns.route("/digital-input")
class DegitalInputsList(Resource):
    def get(self):
        """Get all relays status"""
        all_relays_status = {}
        for dgip_id, relay in DegitalInputs.items():
            all_relays_status[f"relay_{dgip_id}"] = relay.as_dict()
        return all_relays_status
