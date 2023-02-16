from project import api
from flask import request
from flask_restx import reqparse, marshal


from project.controllers.api.base_resource import BaseResource
from project.models.relationship_type import (
    db,
    RelationshipType,
    relationship_type_model,
)


@api.route("/api/relationship_type")
class RelationshipTypeResource(BaseResource):
    @api.param(
        "id",
        "If set, get only 1 relationship type. If not set, get many relationship types.",
    )
    @api.param("limit", "max number of relationship_types.")
    @api.param("offset", "offset to get relationship_types.")
    @api.response(200, "Succeed")
    @api.response(404, "Not found")
    def get(self):
        if "id" in request.args:
            parser = reqparse.RequestParser()
            parser.add_argument("id", type=int)
            args = parser.parse_args()

            id = args["id"]
            api.logger.info(f"get_relationship_type id={id}")
            relationship_type = RelationshipType.query.get(id)
            if not relationship_type:
                return self.format_response(None, 404, "Not found")

            return self.format_response(
                marshal(relationship_type, relationship_type_model), 200, "Succeed"
            )

        parser = reqparse.RequestParser()
        parser.add_argument("limit", type=int, default=10)
        parser.add_argument("offset", type=int, default=0)
        args = parser.parse_args()

        limit = args["limit"]
        offset = args["offset"]
        api.logger.info(f"get_families offset={offset} limit={limit}")
        relationship_types = (
            RelationshipType.query.order_by(RelationshipType.id)
            .limit(limit)
            .offset(offset)
            .all()
        )
        total = RelationshipType.query.count()
        return self.format_response(
            {
                "data": marshal(relationship_types, relationship_type_model),
                "total": total,
            },
            200,
            "Succeed",
        )

    @api.expect(relationship_type_model)
    @api.response(200, "Succeed")
    def post(self):
        if not api.payload or "name" not in api.payload:
            return self.format_response(None, 400, "Bad Request")

        name = api.payload.get("name")
        api.logger.info(f"create_relationship_type")
        relationship_type = RelationshipType(name=name)
        db.session.add(relationship_type)
        db.session.commit()
        return self.format_response(
            marshal(relationship_type, relationship_type_model), 200, "Succeed"
        )

    @api.expect(relationship_type_model)
    @api.response(200, "Succeed")
    @api.response(404, "Not found")
    def put(self):
        if not api.payload or "id" not in api.payload:
            return self.format_response(None, 400, "Bad Request")

        id = api.payload.get("id")
        api.logger.info(f"edit_relationship_type id={id}")
        relationship_type = RelationshipType.query.get(id)
        if not relationship_type:
            return self.format_response(None, 404, "Not found")

        if "name" in api.payload:
            relationship_type.name = api.payload.get("name")
        db.session.commit()
        return self.format_response(
            marshal(relationship_type, relationship_type_model), 200, "Succeed"
        )

    @api.param("id", "id of relationship_type to delete.")
    @api.response(200, "Succeed")
    @api.response(404, "Not found")
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        args = parser.parse_args()

        id = args["id"]
        if not id:
            return self.format_response(None, 400, "Bad Request")

        api.logger.info(f"delete_relationship_type id={id}")
        relationship_type = RelationshipType.query.get(id)
        if not relationship_type:
            return self.format_response(None, 404, "Not found")

        db.session.delete(relationship_type)
        db.session.commit()
        return self.format_response(
            marshal(relationship_type, relationship_type_model), 200, "Succeed"
        )