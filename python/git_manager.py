import urllib.request
import re
import git

ERROR_READ_PROBLEM = "ERROR: fail to read problem"
ERROR_GET_REPOSITORY = "ERROR: fail to get local repository"
ERROR_GIT_COMMIT = "ERROR: fail to commit"
ERROR_GIT_PUSH = "ERROR: fail to push"


def get_title(number):
    # read problem title
    try:
        html = urllib.request.urlopen(
            f"https://www.acmicpc.net/problem/{number}").read().decode("utf8")
        title = re.search(r"<title>\d*번: (.*)</title>", html).group(1)
        return title
    except:
        print(ERROR_READ_PROBLEM)
        exit()


def get_commit_message(title, number):
    # create commit message
    header = f"Add solution of {number}"
    body = f"- [{number}. {title}] 문제 풀이"
    commit_message = header + '\n' + body
    return commit_message


def commit_and_push(file_name, commit_message):
    try:
        repository = git.Repo('../.git')
    except:
        print(ERROR_GET_REPOSITORY)
        exit()
    commit(repository, file_name, commit_message)
    push(repository)


def commit(repository, file_name, commit_message):
    try:
        repository.git.add(f"*/{file_name}")
        repository.git.commit(f"*/{file_name}", message=commit_message)
    except:
        print(ERROR_GIT_COMMIT)
        exit()


def push(repository):
    try:
        repository.git.push("origin", "master")
    except:
        print(ERROR_GIT_PUSH)
        # reset commit
        exit()


# type problem number
number = int(input())

title = get_title(number)

commit_message = get_commit_message(title, number)

commit_and_push(f"{number}.py", commit_message)
