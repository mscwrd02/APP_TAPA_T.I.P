from flask import Blueprint
import pyrebase

from mySecrets import config

firebase = pyrebase.initialize_app(config)
database = firebase.database()

blueprint = Blueprint("counselors", __name__, url_prefix="/counselors")


@blueprint.route("/all", methods=["GET"])
def get_all_counselors():
    res = database.child("counselors").shallow().get().val()

    if not res:
        return {"status": "no counselors are available"}, 403

    counselor_list = []

    for uid in res:
        counselor_list.append(database.child("users").child(uid).get().val())

    return counselor_list, 200
