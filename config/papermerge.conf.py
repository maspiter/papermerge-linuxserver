DBUSER = "root"
DBPASS = "root"
DBHOST = "mariadb"
DBNAME = "papermerge"
MEDIA_DIR = "/data/media"
STATIC_DIR = "/app/papermerge/static"
MEDIA_URL = "/media/"
STATIC_URL = "/static/"
# map this dir to the host in docker-compose.yml
IMPORTER_DIR = "/opt/import"

OCR_DEFAULT_LANGUAGE = "nld"

OCR_LANGUAGES = {
    "eng": "English",
    "nld": "Dutch",
}
