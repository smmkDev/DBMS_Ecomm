from fastapi import APIRouter
from connection import cursor, conn, connector
from models import Feedback 

router = APIRouter()

@router.get('/feedbacks/')
def get_all_feedbacks():

    cursor.execute("SELECT * FROM Feedback;")
    rows = cursor.fetchall()
    return rows

@router.post('/feedbacks/')
def create_feedback(feedback:Feedback):

    try:
        cursor.execute(
            f"""INSERT INTO Feedback (feedback_id, product_id, user_id, description)
                 VALUES ({feedback.feedback_id}, {feedback.product_id}, {feedback.user_id}, '{feedback.description}');
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.get('/feedbacks/{feedback_id}')
def get_feedback(feedback_id:int):

    try:
        cursor.execute(
            f"SELECT * FROM Feedback WHERE feedback_id={feedback_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    return {"Result": cursor.fetchall()}

@router.put('/feedbacks/{feedback_id}')
def update_feedback(feedback_id:int, updated_feedback:Feedback):

    try:
        cursor.execute(
            f"""
                UPDATE Feedback
                SET product_id={updated_feedback.product_id},
                    user_id={updated_feedback.user_id},
                    description='{updated_feedback.description}'
                WHERE feedback_id={feedback_id};
            """
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}

@router.delete('/feedbacks/{feedback_id}')
def delete_feedback(feedback_id:int):
    
    try:
        cursor.execute(
            f"DELETE FROM Feedback WHERE feedback_id={feedback_id};"
        )
    except connector.Error as error:
        return {"Error": error}
    conn.commit()
    return {"Response": "Success"}
