from src.domain.submission import create_broker_submission


class SubmissionWorkflow:

    def __init__(self):
        pass

    async def create_broker_submission(self):
        return await create_broker_submission()


submission_workflow = SubmissionWorkflow()