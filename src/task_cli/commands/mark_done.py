from task_cli.utils.data_service import DataService


def handle_mark_done_task(args):
    ds = DataService()
    try:
        ds.update_task(args.id, status="done")
    except RuntimeError as err:
        print(err)
