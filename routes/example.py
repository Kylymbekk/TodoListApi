from fastapi import APIRouter, Depends, Form, UploadFile
import datetime
import os
from sqlalchemy.orm import Session
from schema.example import ChangeExamplePostIn, ChangeIsDonePostIn
from utils.dependencies import get_db
from models.example import Example

router = APIRouter()


@router.get('/get')
def example(db: Session=Depends(get_db)):
    todos = db.query(Example).all()

    return {
        'data': todos,
        'status': 'success'
    }


@router.post('/post')
def add(files: UploadFile = Form(), title: str = Form(), text: str = Form(), date: str = Form(), dateEnd: str =Form(), db: Session=Depends(get_db)):
    if not os.path.exists(os.path.join(os.getcwd(), 'ass', str(datetime.datetime.now().year))):
        os.mkdir(os.path.join(os.getcwd(), 'ass', str(datetime.datetime.now().year)))
    if db.query(Example).filter(Example.title == title).first() is not None:
        raise ResponseException(text='busy', status=401)
    todo = Example(title=title, date=date, dateEnd=dateEnd, files=files.filename, text=text)
    db.add(todo)
    db.commit()
    db.refresh(todo)

    with open(os.path.join(os.getcwd(), 'ass', str(datetime.datetime.now().year), files.filename), 'wb+') as f:
        f.write(files.file.read())

    return {
        'item': todo,
        'status': 'success'
    }


@router.delete('/delete')
def delete(id: int, db: Session=Depends(get_db)):
    todos = db.query(Example).filter(Example.id == id).first()
    os.remove(os.path.join(os.getcwd(), 'ass', str(datetime.datetime.now().year), todos.files))

    db.delete(todos)
    db.commit()

    return {
        'status': 'success'
    }


@router.get('/edit')
def edit(id:int, db: Session=Depends(get_db)):
    todos = db.query(Example).filter(Example.id == id).first()

    return {
        'data': todos,
        'status': 'success'
    }


@router.post('/changeEdit')
def changeEdit(request: ChangeExamplePostIn, db: Session=Depends(get_db)):
    todos = db.query(Example).filter(Example.id == request.id).first()
    todos.title = request.title
    todos.dateEnd = request.dateEnd
    todos.text = request.text
    db.commit()
    db.refresh(todos)

    return {
        'item': todos,
        'status': 'success'
    }


@router.post('/done')
def isdone(request: ChangeIsDonePostIn, db: Session=Depends(get_db)):
    todos = db.query(Example).filter(Example.id == request.id).first()
    todos.isDone = request.done
    db.commit()

    return {
        'status': 'success'
    }