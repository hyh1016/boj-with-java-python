import urllib.request
import re
import git

ERROR_READ_PROBLEM = "READ ERROR: 문제를 읽어오지 못하였습니다."
ERROR_GET_REPOSITORY = "REPOSITORY ERROR: 로컬 리포지토리를 읽어오지 못하였습니다."
ERROR_GIT_COMMIT = "COMMIT ERROR: 커밋을 수행하지 못하였습니다. 해당 파일이 있는지 확인해주세요."
ERROR_GIT_PUSH = "PUSH ERROR: 원격 리포지토리에 반영하지 못하였습니다."


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
        print(f"커밋이 완료되었습니다.")
    except:
        print(ERROR_GIT_COMMIT)
        exit()


def push(repository):
    try:
        repository.git.push("origin", "master")
        print("원격 레포지토리에 반영되었습니다.")
    except:
        print(ERROR_GIT_PUSH)
        # reset commit
        exit()


# type problem number
number = int(input())

title = get_title(number)

commit_message = get_commit_message(title, number)
print(f"문제정보: [{number}. {title}]")
is_commit_and_push = input("커밋하시겠습니까? [y/n]: ")
if is_commit_and_push == 'y' or is_commit_and_push == 'Y':
    commit_and_push(f"{number}.py", commit_message)
else:
    print("동작이 취소되었습니다.")
