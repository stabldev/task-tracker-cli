from task_cli.utils.data_service import DataService


def handle_list_tasks(args):
    ds = DataService()
    print(ds.read_tasks())
