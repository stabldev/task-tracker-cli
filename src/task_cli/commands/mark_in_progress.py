from task_cli.utils.data_service import DataService


def handle_mark_in_progress_task(args):
    ds = DataService()
    try:
        ds.update_task(args.id, status="in-progress")
    except RuntimeError as err:
        print(err)
