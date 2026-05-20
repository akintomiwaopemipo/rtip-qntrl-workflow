from src.services.blueprint_service import blueprint_service
from src.workflows.submission import submission_workflow


def get_blueprint_service():
    return blueprint_service

def get_submission_workflow():
    return submission_workflow
