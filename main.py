from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs


def main():
    db_session.global_init("db/blogs.db")
    dbs = db_session.create_session()
    for item in [["Scott", "Ridley", 21, "captain", "research engineer", "module_1",
                  "scott_chief@mars.org"],
                 ["Marshall", "Robert", 23, "engineer", "engineer", "module_34",
                  "marshall_engi@mars.org"],
                 ["Barker", "Frank", 26, "researcher", "researcher", "module_2",
                  "bark@mars.org"],
                 ["Smith", "Sharon", 22, "researcher", "explorer", "module_5", "sharon@mars.org"]]:
        user = User()
        user.surname = item[0]
        user.name = item[1]
        user.age = item[2]
        user.position = item[3]
        user.speciality = item[4]
        user.address = item[5]
        user.email = item[6]
        dbs.add(user)
    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = "2, 3"
    job.is_finished = False
    dbs.add(job)
    dbs.commit()


if __name__ == '__main__':
    main()