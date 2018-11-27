from . import admin


@admin.route("/admin")
def index():
    return "这是admin中的首页"
