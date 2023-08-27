import qwerty

def question(Q):
    try:
        return {"question": Q, "answer": qwerty.main(Q)}
    except:
        return {"question": Q, "answer": "-"}

