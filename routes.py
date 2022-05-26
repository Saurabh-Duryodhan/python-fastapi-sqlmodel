from fastapi.routing import APIRouter
from sqlmodel import Session, select
from database import engine
from typing import List, Dict
from models import *
import json
router = APIRouter()

session = Session(engine)


@router.get('/')
def index():
    return {'message': 'Hello World'}


@router.post('/results', response_model=List[Hero])
def get_users(reqBody: Hero, reqTeam: Team):
    team_a = Team(name=reqTeam.name, headquarter=reqTeam.headquarter)

    session.add(team_a)
    session.commit()

    spider_man = Hero(name=reqBody.name, secret_name=reqBody.secret_name,
                      age=reqBody.age, team_id=team_a.id)
    hero_res = session.add(spider_man)
    print(hero_res)
    session.commit()
    return hero_res


@router.get('get_heads/', response_model=List[Hero])
def get_all_heroes():
    statement = select(Hero)
    res = session.exec(statement).all()
    return res


@router.get('/get_hero/{id}', response_model=Hero, status_code=302)
def get_single_hero(id: int):
    statement = select(Hero).where(Hero.id == id)
    res = session.exec(statement).one()
    print(res)
    return res


@router.put('/update_hero/{id}', response_model=Hero, status_code=302)
def update_hero(id: int, reqBody: Hero):
    statement = select(Hero).where(Hero.id == id)
    res = session.exec(statement).one()
    print(res)
    res.name = reqBody.name
    res.secret_name = reqBody.secret_name
    res.age = reqBody.age
    session.commit()
    return res


@router.patch('/update_hero/{id}', response_model=Hero, status_code=302)
def update_hero(id: int, reqBody: Hero):
    statement = select(Hero).where(Hero.id == id)
    res = session.exec(statement).one()
    print(res)
    res.name = reqBody.name
    res.secret_name = reqBody.secret_name
    res.age = reqBody.age
    session.add(res)
    session.commit()
    return res


@router.delete('/delete_hero/{id}', response_model=Hero, status_code=200)
def delete_hero(id: int):
    statement = select(Hero).where(Hero.id == id)
    res = session.exec(statement).one()
    print(res)
    session.delete(res)
    session.commit()
    return res


@router.get('/get_team_rel/{id}',  status_code=302)
def find_Rel(id: int):
    statement = select(Hero, Team).where(
        Hero.team_id == Team.id, Hero.id == id)
    print(statement)
    results = session.exec(statement)
    for hero, team in results:
        mydict = dict(team=team, hero=hero)
        print(mydict)
    return mydict
