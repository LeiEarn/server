from server import create_app

# app = create_app()
#
# app.run(host='localhost', port=8080)

if __name__ == '__main__':
    import server.model.User as user
    import server.model.Task as task

    result = user.UserTable.user_count()
    print(result)

    result = task.TaskTable.task_count()
    print(result)
