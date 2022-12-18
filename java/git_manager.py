import requests
import re
import git

ERROR_READ_PROBLEM = "READ ERROR: 문제를 읽어오지 못하였습니다."
ERROR_GET_REPOSITORY = "REPOSITORY ERROR: 로컬 리포지토리를 읽어오지 못하였습니다."
ERROR_GIT_COMMIT = "COMMIT ERROR: 커밋을 수행하지 못하였습니다. 해당 파일이 있는지 확인해주세요."
ERROR_GIT_PUSH = "PUSH ERROR: 원격 리포지토리에 반영하지 못하였습니다."


def get_title(number):
    # read problem title
    try:
        url = f"https://www.acmicpc.net/problem/{number}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }
        html = requests.get(url, headers=headers).content.decode("utf8")
        title = re.search(r"<title>\d*번: (.*)</title>", html).group(1)
        return title
    except:
        print(ERROR_READ_PROBLEM)
        exit()


def get_commit_message(title, number):
    # create commit message
    header = f"Add solution of {number}"
    body = f"- [{number}. {title}] 문제 풀이"
    commit_message = header + "\n" + body
    return commit_message


def commit_and_push(number, commit_message):
    try:
        repository = git.Repo("../.git")
    except:
        print(ERROR_GET_REPOSITORY)
        exit()
    commit(repository, number, commit_message)
    push(repository)


def commit(repository, number, commit_message):
    try:
        repository.git.add(f"./java/Q{number}/Main.java")
        repository.git.commit(f"./java/Q{number}/Main.java", message=commit_message)
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
number = int(input("문제 번호 입력: "))

title = get_title(number)
print(f"문제정보: [{number}. {title}]")
is_commit_and_push = input("커밋하시겠습니까? [y/n]: ")
if is_commit_and_push == "y" or is_commit_and_push == "Y":
    commit_and_push(number, get_commit_message(title, number))
else:
    print("동작이 취소되었습니다.")
