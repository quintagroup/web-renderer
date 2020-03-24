import os 
from app import app

TEMPLATE_UPLOAD_DIRECTORY_PATH = os.path.join(app.config['UPLOAD_FOLDER'])
TEMPLATES_FOLDER = os.path.join(app.config['TEMPLATES_FOLDER'])
TEMPLATE_PREFIX = "doc_template"
GENERATED_DOC_PREFIX = "generated"
TEMPLATE_FILE_EXTENSION = "docx"
GENERATED_DOC_EXTENSION = "pdf"
TEST_PREFIX = "test"