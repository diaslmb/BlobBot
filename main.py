from telebot import types
import telebot
import time

bot = telebot.TeleBot("944482305:AAHrV0Jl-812v2WC9Psgpj3-x-3-lXWrMhc")

language_type = types.ReplyKeyboardMarkup()
language_type.row('Қазақша')
language_type.row('Русский')
language_type.row('English')


englnum_type = types.ReplyKeyboardMarkup()
englnum_type.row("About  us")
englnum_type.row("Our  goal")
englnum_type.row("Current  projects")
englnum_type.row("Team  members")
englnum_type.row("Our  instagram  site")
englnum_type.row("Order  a  projects")
englnum_type.row("Back")

rusnum_type = types.ReplyKeyboardMarkup()
rusnum_type.row("О  нас")
rusnum_type.row("Наша  цель")
rusnum_type.row("Нынешние  проекты")
rusnum_type.row("Состав")
rusnum_type.row("Наш  Instagram  сайт")
rusnum_type.row("Заказать  проекты")
rusnum_type.row("Назад")

kaznum_type = types.ReplyKeyboardMarkup()
kaznum_type.row("Біз  туралы")
kaznum_type.row("Біздің  мақсатымыз")
kaznum_type.row("Ағымдағы  жобалар")
kaznum_type.row("Команда  мүшелері")
kaznum_type.row("Біздің  инстаграм  парақшамыз")
kaznum_type.row("Жобаға  тапсырыс  беру")
kaznum_type.row("Артқа")

englname_type = types.ReplyKeyboardMarkup()
englname_type.row("Maksat  Irisbekov")
englname_type.row("Dias  Ilyas")
englname_type.row("Maksat  Kantai")
englname_type.row("Aigerim  Turegeldyeva")
englname_type.row("Miras  Burkhan")
englname_type.row("back")

rusname_type = types.ReplyKeyboardMarkup()
rusname_type.row("Максат  Ирисбеков")
rusname_type.row("Диас  Ильяс")
rusname_type.row("Максат  Кантай")
rusname_type.row("Айгерим  Турегельдыева")
rusname_type.row("Мирас  Бурхан")
rusname_type.row("назад")

kazname_type = types.ReplyKeyboardMarkup()
kazname_type.row("Мақсат  Ирисбеков")
kazname_type.row("Диас   Ильяс")
kazname_type.row("Мақсат  Кантай")
kazname_type.row("Әйгерім  Төрегелдиева")
kazname_type.row("Мирас   Бурхан")
kazname_type.row("артқа")

insta_rus = types.InlineKeyboardMarkup()
enter_insta_rus = types.InlineKeyboardButton(text="Перейти блоб страницу в интаграмме", url="https://www.instagram.com/blobindustries/?hl=ru")
insta_rus.add(enter_insta_rus)

insta_engl = types.InlineKeyboardMarkup()
enter_insta_engl = types.InlineKeyboardButton(text="Go blob page in intagram", url="https://www.instagram.com/blobindustries/?hl=ru")
insta_engl.add(enter_insta_engl)

insta_kaz = types.InlineKeyboardMarkup()
enter_insta_kaz = types.InlineKeyboardButton(text="Инстаграмдағы блог парағына өтіңіз", url="https://www.instagram.com/blobindustries/?hl=ru")
insta_kaz.add(enter_insta_kaz)

engl_project = types.ReplyKeyboardMarkup()
engl_project.row("Yes")
engl_project.row("No")

rus_project = types.ReplyKeyboardMarkup()
rus_project.row("Да")
rus_project.row("Нет")

kaz_project = types.ReplyKeyboardMarkup()
kaz_project.row("Иә")
kaz_project.row("Жоқ")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Тіл  тандаңыз\n\nВыберите  язык\n\nChoose  language", reply_markup=language_type)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
	if message.text == 'English':
		bot.send_message(message.chat.id, "Hello! I am BlobBala!\n1 - About  us\n2 - Our  goal\n3 - Current  projects\n4 - Team  members\n5 - Our  instagram  site\n6 - Order  a  projects\n7 - Back", reply_markup=englnum_type)		
	elif message.text == "About  us":
		#chat_id = "732957488"
		bot.send_message(message.chat.id, "Blob Industries is a team\nof like-minded robotics professionals.\nThe team has existed since July 2019.")
	elif message.text == "Our  goal":
		bot.send_message(message.chat.id, "The goal is to contribute to the development\nof our modern society not only in Kazakhstan,\nbut also in the world.\nIntroduce innovative technologies into the standard\nof society and ensure the perfect operation of systems")
	elif message.text == "Current  projects": 
		bot.send_message(message.chat.id, "Of the current projects that are under active development,\nI can name 'CityOfFuture'.\nCityOfFuture - an innovative model in the field\nof urban planning of the future.")
	elif message.text == "Team  members":
		bot.send_message(message.chat.id, "Choose  one", reply_markup=englname_type)
	elif message.text == "Maksat  Irisbekov":	
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo='https://sun9-27.userapi.com/c855524/v855524728/985a5/A8O5QVHNUL4.jpg')
		bot.send_message(message.chat.id, "Maksat Irisbekov - Chief Engineer,\nChief Programmer,\nFounder of the team.\nStudent of 77th school")
	elif message.text == "Dias  Ilyas":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://pp.userapi.com/c850624/v850624725/197a7d/OV51tc07ae8.jpg")
		bot.send_message(message.chat.id, "Dias Ilyas - Ideological mastermind.\nCreative manager and SMM-specialist.\nBot devoloper.Student of NIS PMD Shymkent")
	elif message.text == "Miras  Burkhan":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://sun9-5.userapi.com/c850624/v850624725/197a75/u03w2Fy4woE.jpg")
		bot.send_message(message.chat.id, "Miras Burhan - 3D simulator and Creative manager.\nStudent of NIS PMD Shymkent")
	elif message.text == "Maksat  Kantai":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://pp.userapi.com/c850624/v850624725/197a6e/OxrbNwXPmB8.jpg")
		bot.send_message(message.chat.id, "Maksat Kantai - Arduino engineer and\nPython programmer.Bot devoloper.\nStudent of 80th school")
	elif message.text == "Aigerim  Turegeldyeva":
		chat_id= bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://sun9-4.userapi.com/c850624/v850624725/197a9c/ZZ_HzFKTKKA.jpg")
		bot.send_message(message.chat.id, "Aigerim Turegeldyeva - Chief Designer and Art Director.\nStudent of NIS PMD Shymkent")
	elif message.text == "back":
		bot.send_message(message.chat.id, "1 - About  us\n2 - Our  goal\n3 - Current  projects\n4 - Team  members\n5 - Our  instagram  site\n6 - Order  a  projects\n7 - Back", reply_markup=englnum_type)
	elif message.text == "Our  instagram  site":
		bot.send_message(message.chat.id, "↓ Blob Industries ↓", reply_markup=insta_engl)
	elif message.text == "Order  a  projects":
		bot.send_message(message.chat.id, "you  definitely  want  to  order  a  project ?", reply_markup=engl_project)
	elif message.text == "Yes":
		bot.send_message(message.from_user.id, "Now you fill up the questionnaire then the questionnaire will be sent to the team leader Maksate Irisbekova in Blob Industries.\n(If you change your mind, just write the word 'cancel')\n\nWrite your name:", reply_markup=None)
		bot.register_next_step_handler(message, englget_name)
	elif message.text == "No":
		bot.send_message(message.chat.id, "1 - About  us\n2 - Our  goal\n3 - Current  projects\n4 - Team  members\n5 - Our  instagram  site\n6 - Order  a  projects\n7 - Back", reply_markup=englnum_type)
	elif message.text == "Back":
		bot.send_message(message.chat.id, "Тіл  танданыңыз\n\nВыберите  язык\n\nChoose  language", reply_markup=language_type)
	elif message.text == 'Русский':
		bot.send_message(message.chat.id, "Привет! Я - BlobBala!\n1 - О  нас\n2 - Наша  цель\n3 - Нынешние  проекты\n4 - Состав\n5 - Наш  сайт  Instagram\n6 - Заказать  проекты\n7 - Назад", reply_markup=rusnum_type)
	elif message.text == "О  нас":
		bot.send_message(message.chat.id, "Blob Industries - команда\nединомышленников в\nсфере робототехники.\nКоманда существует с Июля 2019 года.")
	elif message.text == "Наша  цель":
		bot.send_message(message.chat.id, "Цель - внести лепту в\nразвитие нашего,\nсовременного общества\nне только Казахстана, но\nи мира. Внедрить в\nэталон социума\nинновационные\nтехнологии и обеспечить\nидеальную работу\nсистем")
	elif message.text == "Нынешние  проекты":
		bot.send_message(message.chat.id, "Из нынешних проектов,\nкоторые в находятся в\nактивном разработке, я\nмогу назвать\n'CityOfFuture'.\nCityOfFuture -\nинновационная модель в\nсфере градостроения\nбудущего.")
	elif message.text == "Состав":
		bot.send_message(message.chat.id, "Выберите одного", reply_markup=rusname_type)
	elif message.text == "Максат  Ирисбеков":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://sun9-27.userapi.com/c855524/v855524728/985a5/A8O5QVHNUL4.jpg")
		bot.send_message(message.chat.id, "Максат  Ирисбеков - Главный инженер,\nГлавный программист,\nОснователь команды.\nПобедитель U-Hack Atyrau, Makeaton, SilkWay")
	elif message.text == "Диас  Ильяс":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://pp.userapi.com/c850624/v850624725/197a7d/OV51tc07ae8.jpg")
		bot.send_message(message.chat.id, "Ильяс Диас - идейный вдохновитель.\nКреативный менеджер и SMM-специалист.\nРазработчик Ботов")
	elif message.text == "Мирас  Бурхан":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://sun9-5.userapi.com/c850624/v850624725/197a75/u03w2Fy4woE.jpg")
		bot.send_message(message.chat.id, "Мирас  Бурхан - 3D моделировщик и Креативный менеджер.\nУченик НИШ ФМН Шымкент")
	elif message.text == "Максат  Кантай":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://pp.userapi.com/c850624/v850624725/197a6e/OxrbNwXPmB8.jpg")
		bot.send_message(message.chat.id, "Максат  Кантай - Ардуино-инженер,\nПрограммист Python и разработчик Ботов.\nУченик 80-школы")
	elif message.text == "Айгерим  Турегельдыева":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://sun9-4.userapi.com/c850624/v850624725/197a9c/ZZ_HzFKTKKA.jpg")
		bot.send_message(message.chat.id, "Айгерим  Турегельдыева - Главный дизайнер и Арт-директор.\nУченица НИШ ФМГ Шымкент")
	elif message.text == "назад":
		bot.send_message(message.chat.id, "1 - О  нас\n2 - Наша  цель\n3 - Нынешние  проекты\n4 - Состав\n5 - Наш  сайт  Instagram\n6 - Заказать  проекты\n7 - Назад", reply_markup=rusnum_type)
	elif message.text == "Наш  Instagram  сайт":
		bot.send_message(message.chat.id, "↓ Блоб Индустрия ↓", reply_markup=insta_rus)
	elif message.text == "Заказать  проекты":
		bot.send_message(message.chat.id, "вы точно хотите заказать проект ?", reply_markup=rus_project)
	elif message.text == "Да":
		bot.send_message(message.from_user.id, "Сейчас вы пополните анкету потом анкета будет отправлено лидеру команды Максате Ирисбекове в Blob Industries\n(Если передумаете напишите просто слово 'Отменить')\n\nНапишите своё имя:", reply_markup=None)
		bot.register_next_step_handler(message, get_name)
	elif message.text == "Нет":
		bot.send_message(message.chat.id, "1 - О  нас\n2 - Наша  цель\n3 - Нынешние  проекты\n4 - Состав\n5 - Наш  сайт  Instagram\n6 - Заказать  проекты\n7 - Назад", reply_markup=rusnum_type)
	elif message.text == "Назад":
		bot.send_message(message.chat.id, "Тіл  танданыңыз\n\nВыберите  язык\n\nChoose  language", reply_markup=language_type)
	elif message.text == "Қазақша":   	  
		bot.send_message(message.chat.id, "Сәлем Мен BlobBalaмын!\n1 - Біз  туралы\n2 - Біздің  мақсатымыз\n3 - Ағымдағы  жобалар\n4 - Команда  мүшелері\n5 - Біздің  инстаграм  парақшамыз\n6 - Жобаға  тапсырыс  беру\n7 - Артқа", reply_markup=kaznum_type)	
	elif message.text == "Біз  туралы":
		bot.send_message(message.chat.id, "Blob Industries - мақсаттары бір, робототехника саласының майталмандарынан тұратын топ.\nКоманда 2019 жылдың шілдесінен бастап бар.")
	elif message.text == "Біздің  мақсатымыз":
		bot.send_message(message.chat.id, "Мақсат - қазіргі Қазақстан қоғамының ғана емес,\nбүкіл әлемнің дамуына үлес қосу.\nҚоғам стандартына инновациялық технологияларды енгізіп, робототехника саласының жетістіктерін қолжетімді ету.")
	elif message.text == "Ағымдағы  жобалар":
		bot.send_message(message.chat.id, "Қазіргі кезде белсенді дамып келе жатқан\nжобалардың ішінен 'CityOfFuture' деп атауға болады.\nCityOfFuture - болашақ қала құрылысы саласындағы инновациялық модель.")
	elif message.text == "Команда  мүшелері":
		bot.send_message(message.chat.id, "Біреуін тандаңыз", reply_markup=kazname_type)
	elif message.text == "Мақсат  Ирисбеков":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://sun9-27.userapi.com/c855524/v855524728/985a5/A8O5QVHNUL4.jpg")
		bot.send_message(message.chat.id, "Мақсат  Ирисбеков - бас инженер, бас бағдарламаушы,\nкоманданың негізін салушы.77-мектеп оқушысы.\nU-Hack Atyrau,Makeaton, SilkWay және т.б.\nжарыстардың жеңімпазы")
	elif message.text == "Мақсат  Кантай":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://pp.userapi.com/c850624/v850624725/197a6e/OxrbNwXPmB8.jpg")
		bot.send_message(message.chat.id, "Мақсат  Кантай - Arduino инженері,\nPython бағдарламаушысы, Бот құрастырушы.\n80-мектеп оқушысы")
	elif message.text == "Әйгерім  Төрегелдиева":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://sun9-4.userapi.com/c850624/v850624725/197a9c/ZZ_HzFKTKKA.jpg")
		bot.send_message(message.chat.id, "Әйгерім  Төрегелдиева - бас дизайнер, көркемдік жетекші.\nНЗМ ФМБ оқушысы")
	elif message.text == "Диас   Ильяс":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://pp.userapi.com/c850624/v850624725/197a7d/OV51tc07ae8.jpg")
		bot.send_message(message.chat.id, "Диас  Ильяс - идеялық және шығармашылық менеджер.\nБот құрастырушы және SMM менеджері.\nНЗМ ФМБ үздік оқушысы.")		
	elif message.text == "Мирас   Бурхан":
		chat_id = bot.get_updates()[-1].message.chat.id
		bot.send_photo(chat_id=chat_id, photo="https://sun9-5.userapi.com/c850624/v850624725/197a75/u03w2Fy4woE.jpg")
		bot.send_message(message.chat.id, "Мирас  Бурхан - 3D модельер, шығармашылық менеджер.\nНЗМ ФМБ оқушысы.")
	elif message.text == "артқа":
		bot.send_message(message.chat.id, "1 - Біз  туралы\n2 - Біздің  мақсатымыз\n3 - Ағымдағы  жобалар\n4 - Команда  мүшелері\n5 - Біздің  инстаграм  парақшамыз\n6 - Жобаға  тапсырыс  беру\n7 - Артқа", reply_markup=kaznum_type)
	elif message.text == "Біздің  инстаграм  парақшамыз":
		bot.send_message(message.chat.id, "↓ Блоб Индустриясы ↓", reply_markup=insta_kaz)
	elif message.text == "Жобаға  тапсырыс  беру":
		bot.send_message(message.chat.id, "Жобаға тапсырыс бергіңіз келе ме ?", reply_markup=kaz_project)
	elif message.text == "Иә":
		bot.send_message(message.from_user.id, "Енді сіз анкетаны толтырасыз, содан кейін анкета Blob Industries-де топ жетекшісі Максат Ирисбековаға жіберіледі.\n(Егер сіз өз ойыңызды өзгертсеңіз,'бас тарту' сөзін жазыңыз)\n\nӨз атыңызды жазыңыз:", reply_markup=None)
		bot.register_next_step_handler(message, kazget_name)
	elif message.text == "Жоқ":
		bot.send_message(message.chat.id, "1 - Біз  туралы\n2 - Біздің  мақсатымыз\n3 - Ағымдағы  жобалар\n4 - Команда  мүшелері\n5 - Біздің  инстаграм  парақшамыз\n6 - Жобаға  тапсырыс  беру\n7 - Артқа", reply_markup=kaznum_type)
	elif message.text == "Артқа":
		bot.send_message(message.chat.id, "Тіл  танданыңыз\n\nВыберите  язык\n\nChoose  language", reply_markup=language_type)

def get_name(message): #получаем фамилию
    global name
    name = message.text
    if name == "Отменить" or name == "отменить":
    	bot.send_message(message.chat.id, "1 - О  нас\n2 - Наша  цель\n3 - Нынешние  проекты\n4 - Состав\n5 - Наш  сайт  Instagram\n6 - Заказать  проекты\n7 - Назад", reply_markup=rusnum_type)
    else:
    	bot.send_message(message.chat.id, '(Если передумаете напишите просто слово "Отменить")\n\nУкажите фамилию:')
    	bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    if surname == "Отменить" or surname == "отменить":
    	bot.send_message(message.chat.id, "1 - О  нас\n2 - Наша  цель\n3 - Нынешние  проекты\n4 - Состав\n5 - Наш  сайт  Instagram\n6 - Заказать  проекты\n7 - Назад", reply_markup=rusnum_type)
    else:
    	bot.send_message(message.chat.id, '(Если передумаете напишите просто слово "Отменить")\n\nНапишите свой номер:')
    	bot.register_next_step_handler(message, get_telephone)

def get_telephone(message):
	global num
	num = message.text
	if num == "Отменить" or num == "отменить":
		bot.send_message(message.chat.id, "1 - О  нас\n2 - Наша  цель\n3 - Нынешние  проекты\n4 - Состав\n5 - Наш  сайт  Instagram\n6 - Заказать  проекты\n7 - Назад", reply_markup=rusnum_type)
	else:
		bot.send_message(message.chat.id, '(Если передумаете напишите просто слово "Отменить")\n\nНапишите имя проекта:')
		bot.register_next_step_handler(message, get_project_name)

def get_project_name(message):
	global project_name
	project_name = message.text
	if project_name == "Отменить" or project_name == "отменить":
		bot.send_message(message.chat.id, "1 - О  нас\n2 - Наша  цель\n3 - Нынешние  проекты\n4 - Состав\n5 - Наш  сайт  Instagram\n6 - Заказать  проекты\n7 - Назад", reply_markup=rusnum_type)
	else:
		bot.send_message(message.chat.id, "(Если передумаете напишите просто слово 'Отменить')\n\nО проекте:")
		bot.register_next_step_handler(message, get_project)

def get_project(message):
	global project 
	project = message.text
	keyboard = types.InlineKeyboardMarkup()
	key_yes = types.InlineKeyboardButton(text="Да", callback_data='yes')
	keyboard.add(key_yes)
	key_no = types.InlineKeyboardButton(text="Нет", callback_data='no')
	keyboard.add(key_no)
	question = str(time.ctime()) + "\n" + "Фамилия:\n" + "    " +surname + "\nИмя:\n" + "    " + name + "\nТелефон номер:\n" + "    " + str(num) + "\n" + "\nНазвание проекта:\n" + '    " ' + project_name + ' "    ' +  "\n" + "О проекте:\n" + project + "\n\n\n" + "Отправить ?"
	if project == "Отменить" or project == "отменить":
		bot.send_message(message.chat.id, "1 - О  нас\n2 - Наша  цель\n3 - Нынешние  проекты\n4 - Состав\n5 - Наш  сайт  Instagram\n6 - Заказать  проекты\n7 - Назад", reply_markup=rusnum_type)
	else:
		bot.send_message(message.chat.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	if call.data == "yes":
		chat_id = "732957488"
		questioncall = str(time.ctime()) + "\n" + "Фамилия:\n" + "    " +surname + "\nИмя:\n" + "    " + name + "\nТелефон номер:\n" + "    " + str(num) + "\n" + "\nНазвание проекта:\n" + '    " ' + project_name + ' "    ' +  "\n" + "О проекте::\n" + project
		bot.send_message(chat_id, text = questioncall)
		bot.send_message(call.message.chat.id, "Сообщения отправлено!)\nЖдите ответа от Максата")
		bot.send_message(call.message.chat.id, "1 - О  нас\n2 - Наша  цель\n3 - Нынешние  проекты\n4 - Состав\n5 - Наш  сайт  Instagram\n6 - Заказать  проекты\n7 - Назад", reply_markup=rusnum_type)
	elif call.data == 'no':
		bot.send_message(call.message.chat.id, "Отправка отменена\n\n\n1 - О  нас\n2 - Наша  цель\n3 - Нынешние  проекты\n4 - Состав\n5 - Наш  сайт  Instagram\n6 - Заказать  проекты\n7 - Назад", reply_markup=rusnum_type)
	elif call.data == "englyes":
		chat_id = "732957488"
		englquestioncall = str(time.ctime()) + "\n" + "Surname:\n" + "    " +englsurname + "\nName:\n" + "    " + englname + "\nTelephone numbers:\n" + "    " + str(englnum) + "\n" + "\nProject name:\n" + '    " ' + englproject_name + ' "    ' +  "\n" + " About the project:\n" + englproject + "\n\n\n" + "Submit ?"
		bot.send_message(chat_id, text=englquestioncall)
		bot.send_message(call.message.chat.id, "Messages sent!)\nWait for a response from Maksat")
		bot.send_message(call.message.chat.id, "1 - About  us\n2 - Our  goal\n3 - Current  projects\n4 - Team  members\n5 - Our  instagram  site\n6 - Order  a  projects\n7 - Back", reply_markup=englnum_type)
	elif call.data == 'englno':
		bot.send_message(call.message.chat.id, "Sending canceled\n\n\n1 - About  us\n2 - Our  goal\n3 - Current  projects\n4 - Team  members\n5 - Our  instagram  site\n6 - Order  a  projects\n7 - Back", reply_markup=englnum_type)
	elif call.data == "kazyes":
		chat_id = "732957488"
		kazquestioncall = str(time.ctime()) + "\n" + "Тегі:\n" + "    " +kazsurname + "\nАты:\n" + "    " + kazname + "\nТелефон нөмері:\n" + "    " + str(kaznum) + "\n" + "\nЖобаның аты:\n" + '    " ' + kazproject_name + ' "    ' +  "\n" + " Жоба Сипаттамасы:\n" + kazproject
		bot.send_message(chat_id, text=kazquestioncall)
		bot.send_message(call.message.chat.id, "Хабарламалар жіберілді!)\nМақсаттан жауап күтіңіз")
		bot.send_message(call.message.chat.id, "1 - Біз  туралы\n2 - Біздің  мақсатымыз\n3 - Ағымдағы  жобалар\n4 - Команда  мүшелері\n5 - Біздің  инстаграм  парақшамыз\n6 - Жобаға  тапсырыс  беру\n7 - Артқа", reply_markup=kaznum_type)
	elif call.data == "kazno":
		bot.send_message(call.message.chat.id, "Жыберілуге бас тартылды\n\n\n1 - Біз  туралы\n2 - Біздің  мақсатымыз\n3 - Ағымдағы  жобалар\n4 - Команда  мүшелері\n5 - Біздің  инстаграм  парақшамыз\n6 - Жобаға  тапсырыс  беру\n7 - Артқа", reply_markup=kaznum_type)

def englget_name(message): #получаем фамилию
    global englname
    englname = message.text
    if englname == "Cancel" or englname == "cancel":
    	bot.send_message(message.chat.id, "1 - About  us\n2 - Our  goal\n3 - Current  projects\n4 - Team  members\n5 - Our  instagram  site\n6 - Order  a  projects\n7 - Back", reply_markup=englnum_type)
    else:
    	bot.send_message(message.chat.id, 'If you change your mind, just write the word "cancel"\n\nEnter last name:')
    	bot.register_next_step_handler(message, englget_surname)

def englget_surname(message):
	global englsurname
	englsurname = message.text
	if englsurname == "Cancel" or englsurname == "cancel":
		bot.send_message(message.chat.id, "1 - About  us\n2 - Our  goal\n3 - Current  projects\n4 - Team  members\n5 - Our  instagram  site\n6 - Order  a  projects\n7 - Back", reply_markup=englnum_type)
	else:
		bot.send_message(message.chat.id, 'If you change your mind, just write the word "cancel"\n\nWrite your number:')
		bot.register_next_step_handler(message, englget_telephone)

def englget_telephone(message):
	global englnum
	englnum = message.text
	if englnum == "Cancel" or englnum == "cancel":
		bot.send_message(message.chat.id, "1 - About  us\n2 - Our  goal\n3 - Current  projects\n4 - Team  members\n5 - Our  instagram  site\n6 - Order  a  projects\n7 - Back", reply_markup=englnum_type)
	else:
		bot.send_message(message.chat.id, 'If you change your mind, just write the word "cancel"\n\nWrite the name of the project:')
		bot.register_next_step_handler(message, englget_project_name)

def englget_project_name(message):
	global englproject_name
	englproject_name = message.text
	if englproject_name == "Cancel" or englproject_name == "cancel":
		bot.send_message(message.chat.id, "1 - About  us\n2 - Our  goal\n3 - Current  projects\n4 - Team  members\n5 - Our  instagram  site\n6 - Order  a  projects\n7 - Back", reply_markup=englnum_type)
	else:
		bot.send_message(message.chat.id, "If you change your mind, write just the word 'cancel'\n\nAbout the project:")
		bot.register_next_step_handler(message, englget_project)

def englget_project(message):
	global englproject 
	englproject = message.text
	englkeyboard = types.InlineKeyboardMarkup()
	englkey_yes = types.InlineKeyboardButton(text="Yes", callback_data='englyes')
	englkeyboard.add(englkey_yes)
	englkey_no = types.InlineKeyboardButton(text="No", callback_data='englno')
	englkeyboard.add(englkey_no)
	englquestion = str(time.ctime()) + "\n" + "Surname:\n" + "    " +englsurname + "\nName:\n" + "    " + englname + "\nTelephone numbers:\n" + "    " + str(englnum) + "\n" + "\nProject name:\n" + '    " ' + englproject_name + ' "    ' +  "\n" + " Project Description:\n" + englproject + "\n\n\n" + "Submit ?"
	if englproject == "Cancel" or englproject == "cancel":
		bot.send_message(message.chat.id, "1 - About  us\n2 - Our  goal\n3 - Current  projects\n4 - Team  members\n5 - Our  instagram  site\n6 - Order  a  projects\n7 - Back", reply_markup=englnum_type)
	else:
		bot.send_message(message.chat.id, text=englquestion, reply_markup=englkeyboard)

def kazget_name(message): #получаем фамилию
    global kazname
    kazname = message.text
    if kazname == "Бас тарту" or kazname == "бас тарту":
    	bot.send_message(message.chat.id, "1 - Біз  туралы\n2 - Біздің  мақсатымыз\n3 - Ағымдағы  жобалар\n4 - Команда  мүшелері\n5 - Біздің  инстаграм  парақшамыз\n6 - Жобаға  тапсырыс  беру\n7 - Артқа", reply_markup=kaznum_type)
    else:
    	bot.send_message(message.chat.id, '(Егер сіз өзіңіздің көзқарасыңызды өзгертсеңіз, «бас тарту» сөзін жазыңыз)\n\nТегіңізді енгізіңіз:')
    	bot.register_next_step_handler(message, kazget_surname)

def kazget_surname(message):
	global kazsurname
	kazsurname = message.text
	if kazsurname == "Бас тарту" or kazsurname == "бас тарту":
		bot.send_message(message.chat.id, "1 - Біз  туралы\n2 - Біздің  мақсатымыз\n3 - Ағымдағы  жобалар\n4 - Команда  мүшелері\n5 - Біздің  инстаграм  парақшамыз\n6 - Жобаға  тапсырыс  беру\n7 - Артқа", reply_markup=kaznum_type)
	else:
		bot.send_message(message.chat.id, 'Егер сіз өзіңіздің көзқарасыңызды өзгертсеңіз, «бас тарту» сөзін жазыңыз\n\nНөміріңізді жазыңыз:')
		bot.register_next_step_handler(message, kazget_telephone)

def kazget_telephone(message):
	global kaznum
	kaznum = message.text
	if kaznum == "Бас тарту" or kaznum == "бас тарту":
		bot.send_message(message.chat.id, "1 - Біз  туралы\n2 - Біздің  мақсатымыз\n3 - Ағымдағы  жобалар\n4 - Команда  мүшелері\n5 - Біздің  инстаграм  парақшамыз\n6 - Жобаға  тапсырыс  беру\n7 - Артқа", reply_markup=kaznum_type)
	else:
		bot.send_message(message.chat.id, 'Егер ойыңызды өзгертсеңіз, «бас тарту» сөзін жазыңыз\n\nЖобаның атын жазыңыз:')
		bot.register_next_step_handler(message, kazget_project_name)

def kazget_project_name(message):
	global kazproject_name
	kazproject_name = message.text
	if kazproject_name == "Бас тарту" or kazproject_name == "бас тарту":
		bot.send_message(message.chat.id, "1 - Біз  туралы\n2 - Біздің  мақсатымыз\n3 - Ағымдағы  жобалар\n4 - Команда  мүшелері\n5 - Біздің  инстаграм  парақшамыз\n6 - Жобаға  тапсырыс  беру\n7 - Артқа", reply_markup=kaznum_type)
	else:
		bot.send_message(message.chat.id, "Егер сіз өзіңіздің көзқарасыңызды өзгертсеңіз, «бас тарту» сөзін жазыңыз\n\nЖоба жайлы:")
		bot.register_next_step_handler(message, kazget_project)

def kazget_project(message):
	global kazproject 
	kazproject = message.text
	kazkeyboard = types.InlineKeyboardMarkup()
	kazkey_yes = types.InlineKeyboardButton(text="Иә", callback_data='kazyes')
	kazkeyboard.add(kazkey_yes)
	kazkey_no = types.InlineKeyboardButton(text="Жоқ", callback_data='kazno')
	kazkeyboard.add(kazkey_no)
	kazquestion = str(time.ctime()) + "\n" + "Тегі:\n" + "    " +kazsurname + "\nАты:\n" + "    " + kazname + "\nТелефон нөмері:\n" + "    " + str(kaznum) + "\n" + "\nЖобаның аты:\n" + '    " ' + kazproject_name + ' "    ' +  "\n" + " Жоба Сипаттамасы:\n" + kazproject + "\n\n\n" + "Жіберілсін бе ?"
	if kazproject == "Бас тарту" or kazproject == "бас тарту":
		bot.send_message(message.chat.id, "1 - Біз  туралы\n2 - Біздің  мақсатымыз\n3 - Ағымдағы  жобалар\n4 - Команда  мүшелері\n5 - Біздің  инстаграм  парақшамыз\n6 - Жобаға  тапсырыс  беру\n7 - Артқа", reply_markup=kaznum_type)
	else:
		bot.send_message(message.chat.id, text=kazquestion, reply_markup=kazkeyboard)

if __name__ == '__main__':
	bot.polling(none_stop=True)
  
