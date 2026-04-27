from flask import Flask, render_template, request
import random

app = Flask(__name__)

# --- ТВОИ РЕПЛИКИ (НЕ МЕНЯЕМ) ---
greetings = [
    "Здравствуй, добрый (надеюсь) человек! Пришел за утешением? Присаживайся поудобней и поведай котику свои печальки. Мур- мур-мур."
]

comfort = [
    "Да у них сухой корм вместо мозгов!",
    "Это от зависти. У тебя консерва в миске, а у них мышь на вписке!",
    "Они не стоят содержимого твоего лотка, чел!",
    "Если мир повернулся к тебе хвостовой частью, дай ему пинка!",
    "Жизнь это картонная коробка с шуршащими пакетиками. Каждый день ты суешь в нее лапу, вытаскиваешь пакетик и шуршишь им радостно. Но иногда попадается гандон.",
    "Неприятности, как дерьмо мимо лотка. Случаются.",
    "Вот же мерзкие крысы! Хочешь я нагажу им в питьевой фонтанчик?"
]

endings = [
    "Я тебя утешил? Обними котика и ступай дальше по своим граблям.",
    "Настроение улучшилось? Покорми котика и иди занимать достойное место в пищевой цепи.",
    "Помогло? Почеши котика за ушком и катись клубочком по ухабам своей судьбы."
]

# --- служебное ---
def rand(arr):
    return random.choice(arr)

@app.route("/", methods=["GET", "POST"])
def home():
    greeting = rand(greetings)

    user_text = None
    cat_answer = None
    show_choices = False
    goodbye = False

    if request.method == "POST":
        action = request.form.get("action")

        if action == "complain":
            user_text = request.form.get("user_text", "").strip()

            if user_text:
                cat_answer = f"""{rand(comfort)}

{rand(endings)}"""
                show_choices = True

        elif action == "leave":
            goodbye = True

    return render_template(
        "index.html",
        greeting=greeting,
        user_text=user_text,
        cat_answer=cat_answer,
        show_choices=show_choices,
        goodbye=goodbye
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
