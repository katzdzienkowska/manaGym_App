from db.run_sql import run_sql

from models.member import Member

def save(member):
    sql = "INSERT INTO members (name, dob, membership, active) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.name, member.dob, member.membership, member.active]
    results = run_sql(sql, values)
    member.id = results[0]["id"]
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for result in results:
        member = Member(result["name"], result["dob"], result["membership"], result["active"], result["id"])
        members.append(member)
    return members

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

