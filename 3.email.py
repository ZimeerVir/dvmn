import smtplib
from dotenv import load_dotenv

from Yandex_pass import login, pass_

"""
       ХУЙНЯ ОТПРАВЛЯТ СООБЩЕНИЯ
"""

text = """
Привет,  %friend_name%!  %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""

website_for_text = "https://vk.com/zimeervir"
friend_name = "Чурка"
my_name = "Александр"

text = text.replace('%website%', website_for_text)
text = text.replace('%friend_name%', friend_name)
text = text.replace('%my_name%', my_name)

my_mail = 'ZimeerVir@yandex.ru'
to_mail = 'alexandrurentsev@yandex.ru'
heading_mail = "залупа!"

title_letter = f"""From: {my_mail}
To: {to_mail}
Subject: {heading_mail}
Content-Type: text/plain; charset="UTF-8";
"""
output_text = (title_letter + text).encode("UTF-8")

login_mail = login
pass_mail = pass_

print(output_text)

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login_mail, pass_mail)
server.sendmail(my_mail, to_mail, output_text)
server.quit()
