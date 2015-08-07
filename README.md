# mutt_cal
Маленькая утилитка, для отображения ics файлов в mutt.
Необходимо две библиотеки:

Нужны две библиотеки:
    easy_install prettytable
    easy_install icalendar

В конфигурации mutt добавить
	В mailcap - 
	text/calendar; mutt_cal.py %s; copiousoutput
	в autoview -
	auto_view text/calendar
	