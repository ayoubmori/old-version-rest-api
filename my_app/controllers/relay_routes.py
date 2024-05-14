from my_app.models.relay import relays
from flask_restx import Resource, Namespace, fields

# from my_app.services.GPIO_control import *

# views_app = Blueprint("views", __name__)

# Define namespaces
relay_ns = Namespace("relay", description="Relay operations", path="/api")


@relay_ns.route("/relay/<string:relay_id>")
class Relay(Resource):
    @relay_ns.response(200, "Success")
    @relay_ns.response(400, "Invalid input")
    def get(self, relay_id):
        """Get the status of a relay"""
        if relay_id in relays:
            relay = relays[relay_id]
            return relay.as_dict(), 200
        else:
            return {"error": f"Relay with id {id} does not exist"}, 404


@relay_ns.route("/relay/<string:relay_id>/on")
class RelayOn(Resource):
    @relay_ns.expect(
        relay_ns.model(
            "Relay On Input",
            {
                "relay_id": fields.String(
                    description="ID of the relay to be turned on",
                    required=True,
                    example="relay1",
                )
            },
            description="JSON object containing the ID of the relay to be turned on",
        )
    )
    @relay_ns.response(200, "Success")
    @relay_ns.response(400, "Invalid input")
    @relay_ns.response(404, "Relay not found")
    def post(self, relay_id):
        """Turn a relay ON."""
        """
        Get a specific course
        ---
        parameters:
          - in: path
            name: course_id
            type: integer
            required: true
        responses:
          200:
            description: Details of the requested course
          404:
            description: Course not found
        """
        if relay_id in relays:
            relay = relays[relay_id]
            relay.turn_on()
            return relays[relay_id].as_dict(), 200
        else:
            return {"error": f"Relay with id '{relay_id}' does not exist"}, 404


@relay_ns.route("/relay/<string:relay_id>/off")
class RelayOff(Resource):
    @relay_ns.expect(
        relay_ns.model(
            "Relay Off Input",
            {
                "relay_id": fields.String(
                    description="ID of the relay to be turned off",
                    required=True,
                    example="relay1",
                )
            },
            description="JSON object containing the ID of the relay to be turned off",
        )
    )
    @relay_ns.response(200, "Success")
    @relay_ns.response(400, "Invalid input")
    @relay_ns.response(404, "Relay not found")
    def post(self, relay_id):
        """Turn a relay OFF."""
        if relay_id in relays:
            relay = relays[relay_id]
            relay.turn_off()
            return relays[relay_id].as_dict(), 200
        else:
            return {"error": f"Relay with id '{relay_id}' does not exist"}, 404


@relay_ns.route("/relay")
class RelayList(Resource):
    @relay_ns.response(200, "Success")
    @relay_ns.response(400, "couldn" "t get the relays")
    def get(self):
        """Get all relays status"""
        all_relays_status = {}
        for id, relay in relays.items():
            all_relays_status[f"relay_{id}"] = relay.as_dict()
        return all_relays_status
