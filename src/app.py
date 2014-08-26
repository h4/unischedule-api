# coding=utf-8
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '[]'


@app.route('/api/get_faculties')
def faculties():
    data = {
        "faculties": [
            {"faculty_name": "Институт машиностроения \"ЛМЗ-ВТУЗ\"", "faculty_id": 0, "date_start": "26.08.2014",
             "date_end": "26.09.2014"},
            {"faculty_name": "Инженерно-строительный институт", "faculty_id": 1, "date_start": "26.08.2014",
             "date_end": "26.09.2014"},
            {"faculty_name": "Институт энергетики и транспортных систем", "faculty_id": 2, "date_start": "26.08.2014",
             "date_end": "26.09.2014"},
            {"faculty_name": "(Институт международных образовательных программ)", "faculty_id": 3,
             "date_start": "26.08.2014", "date_end": "26.09.2014"},
            {"faculty_name": "Институт прикладной лингвистики", "faculty_id": 4, "date_start": "26.08.2014",
             "date_end": "26.09.2014"},
            {"faculty_name": "Институт военно-технического образования и безопасности", "faculty_id": 5,
             "date_start": "26.08.2014", "date_end": "26.09.2014"},
            {"faculty_name": "Институт гуманитарного образования", "faculty_id": 6, "date_start": "26.08.2014",
             "date_end": "26.09.2014"},
            {"faculty_name": "Инженерно-экономический институт", "faculty_id": 7, "date_start": "26.08.2014",
             "date_end": "26.09.2014"},
            {"faculty_name": "Институт прикладной математики и механики", "faculty_id": 8, "date_start": "26.08.2014",
             "date_end": "26.09.2014"},
            {"faculty_name": "Институт информационных технологий и управления", "faculty_id": 9,
             "date_start": "26.08.2014", "date_end": "26.09.2014"},
            {"faculty_name": "Институт физики, нанотехнологий и телекоммуникаций", "faculty_id": 10,
             "date_start": "26.08.2014", "date_end": "26.09.2014"},
            {"faculty_name": "Институт металлургии, машиностроения и транспорта", "faculty_id": 11,
             "date_start": "26.08.2014", "date_end": "26.09.2014"}
        ]
    }
    return jsonify(data)


@app.route('/api/get_chairs')
def chairs():
    data = {
        "chairs": [
            {
                "chair_abbr": "СУЗиС",
                "chair_id": 0,
                "chair_name": "Строительство уникальных зданий и сооружений",
            },
            {
                "chair_abbr": "ВиГС",
                "chair_id": 1,
                "chair_name": "Водохозяйственное и гидротехническое строительство",
            },
            {
                "chair_abbr": "ГСиПЭ",
                "chair_id": 2,
                "chair_name": "Гражданское строительство и прикладная экология",
            },
            {
                "chair_id": 3,
                "chair_name": "Гидравлика",
            },
            {
                "chair_abbr": "СМиСК",
                "chair_id": 4,
                "chair_name": "Строительная механика и строительные конструкции",
            },
            {
                "chair_id": 5,
                "chair_name": "Сопротивление материалов",
            },
        ]
    }
    return jsonify(data)


@app.route('/api/get_chairs_group')
def chairs_group():
    data = {
        "groups": [
            {
                "group_name": "13101/4",
                "group_id": "13774"
            },
            {
                "group_name": "23101/4",
                "group_id": "13775"
            },
            {
                "group_name": "33101/4",
                "group_id": "13776"
            },
            {
                "group_name": "53101/10",
                "group_id": "13777"
            },
            {
                "group_name": "63101/10",
                "group_id": "13778"
            },
            {
                "group_name": "з13101/1",
                "group_id": "13779"
            },
            {
                "group_name": "з13101/7",
                "group_id": "13780"
            },
            {
                "group_name": "23101/5",
                "group_id": "13781"
            },
            {
                "group_name": "13101/5",
                "group_id": "13782"
            },
            {
                "group_name": "53101/15",
                "group_id": "13783"
            },
            {
                "group_name": "63101/13",
                "group_id": "13784"
            },
            {
                "group_name": "63101/15",
                "group_id": "13785"
            },
            {
                "group_name": "33101/5",
                "group_id": "13786"
            },
            {
                "group_name": "33101/6",
                "group_id": "13787"
            },
            {
                "group_name": "33101/1",
                "group_id": "13788"
            },
            {
                "group_name": "53101/3",
                "group_id": "13789"
            },
            {
                "group_name": "23101/3",
                "group_id": "13790"
            },
            {
                "group_name": "33101/3",
                "group_id": "13791"
            },
            {
                "group_name": "63101/14",
                "group_id": "13792"
            },
            {
                "group_name": "з43101/7",
                "group_id": "13793"
            },
            {
                "group_name": "з53101/8",
                "group_id": "13794"
            },
            {
                "group_name": "з53101/7",
                "group_id": "13795"
            },
            {
                "group_name": "43101/13",
                "group_id": "13796"
            },
            {
                "group_name": "43101/15",
                "group_id": "13797"
            },
            {
                "group_name": "43101/16",
                "group_id": "13798"
            },
            {
                "group_name": "53101/16",
                "group_id": "13799"
            },
            {
                "group_name": "з33101/1",
                "group_id": "13800"
            },
            {
                "group_name": "з43101/1",
                "group_id": "13801"
            },
            {
                "group_name": "з53101/1",
                "group_id": "13802"
            },
            {
                "group_name": "з63101/1",
                "group_id": "13803"
            },
            {
                "group_name": "з33101/2",
                "group_id": "13804"
            },
            {
                "group_name": "з53101/2",
                "group_id": "13805"
            },
            {
                "group_name": "з63101/2",
                "group_id": "13806"
            },
            {
                "group_name": "53101/2",
                "group_id": "13807"
            },
            {
                "group_name": "з53101/4",
                "group_id": "13808"
            },
            {
                "group_name": "53101/5",
                "group_id": "13809"
            },
            {
                "group_name": "53101/7",
                "group_id": "13810"
            },
            {
                "group_name": "53101/4",
                "group_id": "13811"
            },
            {
                "group_name": "13101/1",
                "group_id": "13812"
            },
            {
                "group_name": "23101/1",
                "group_id": "13813"
            },
            {
                "group_name": "53101/11",
                "group_id": "13814"
            },
            {
                "group_name": "63101/11",
                "group_id": "13815"
            },
            {
                "group_name": "43101/10",
                "group_id": "13816"
            },
            {
                "group_name": "з53101/3",
                "group_id": "13817"
            },
            {
                "group_name": "53101/1",
                "group_id": "13818"
            },
        ]
    }
    return jsonify(data)


@app.route('/api/get_schedule')
def schedule():
    data = {
        "group_name": "13101/4",
        "days": [
            {
                "weekday": 1,
                "lessons": [
                    {
                        "subject": "Информатика",
                        "type": 0,
                        "time_start": "12:00",
                        "time_end": "13:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                            {
                                "teacher_name": "Панфилов А.А."
                            },
                        ],
                        "auditories": [
                            {
                                "auditory_name": "304",
                            },
                            {
                                "auditory_name": "305"
                            }
                        ]
                    },
                    {
                        "subject": "Информатика",
                        "type": 2,
                        "time_start": "14:00",
                        "time_end": "15:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                            {
                                "teacher_name": "Панфилов А.А."
                            },
                        ],
                        "auditories": [
                            {
                                "auditory_name": "304",
                            },
                            {
                                "auditory_name": "305"
                            }
                        ]
                    }
                ]
            },
            {
                "weekday": 2,
                "lessons": [
                    {
                        "subject": "Математика",
                        "type": 2,
                        "time_start": "10:00",
                        "time_end": "11:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                            {
                                "teacher_name": "Антонова Л.Н."
                            },
                        ],
                        "auditories": [
                            {
                                "auditory_name": "329, ГЗ",
                            }
                        ]
                    },
                    {
                        "subject": "История отрасли",
                        "type": 0,
                        "time_start": "12:00",
                        "time_end": "13:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                            {
                                "teacher_name": "Павлов С.Я."
                            },
                        ],
                        "auditories": [
                            {
                                "auditory_name": "301а",
                            },
                        ]
                    },
                    {
                        "subject": "Физика",
                        "type": 1,
                        "time_start": "14:00",
                        "time_end": "15:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                        ],
                        "auditories": [
                            {
                                "auditory_name": "155 ГЗ",
                            },
                        ]
                    },
                ]
            },
            {
                "weekday": 3,
                "lessons": [
                    {
                        "subject": "История",
                        "type": 2,
                        "time_start": "10:00",
                        "time_end": "11:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                        ],
                        "auditories": [
                            {
                                "auditory_name": "215, ГЗ",
                            }
                        ]
                    },
                    {
                        "subject": "Английский язык",
                        "type": 0,
                        "time_start": "12:00",
                        "time_end": "13:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                        ],
                        "auditories": [
                            {
                                "auditory_name": "211 ГК",
                            },
                        ]
                    },
                    {
                        "subject": "Инженерная графика",
                        "type": 0,
                        "time_start": "14:00",
                        "time_end": "15:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                            {
                                "teacher_name": "Баденко В.Л.",
                            }
                        ],
                        "auditories": [
                            {
                                "auditory_name": "216 ГЗ",
                            },
                        ]
                    },
                ]
            },
            {
                "weekday": 4,
                "lessons": [
                    {
                        "subject": "Физика",
                        "type": 2,
                        "time_start": "10:00",
                        "time_end": "11:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                            {
                                "teacher_name": "Приходько А.В.",
                            }
                        ],
                        "auditories": [
                            {
                                "auditory_name": "215, ГЗ",
                            }
                        ]
                    },
                    {
                        "subject": "Химия",
                        "type": 0,
                        "time_start": "12:00",
                        "time_end": "13:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                        ],
                        "auditories": [
                            {
                                "auditory_name": "10 ХК",
                            },
                        ]
                    },
                ]
            },
            {
                "weekday": 5,
                "lessons": [
                    {
                        "subject": "Математика",
                        "type": 2,
                        "time_start": "10:00",
                        "time_end": "11:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                            {
                                "teacher_name": "Антонова Л.Н.",
                            }
                        ],
                        "auditories": [
                            {
                                "auditory_name": "503",
                            }
                        ]
                    },
                    {
                        "subject": "Химия",
                        "type": 2,
                        "time_start": "12:00",
                        "time_end": "13:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                            {
                                "teacher_name": "Иванова Н.И.",
                            }
                        ],
                        "auditories": [
                            {
                                "auditory_name": "52 ХК",
                            },
                        ]
                    },
                ]
            },
            {
                "weekday": 6,
                "lessons": [
                    {
                        "subject": "Английский язык",
                        "type": 0,
                        "time_start": "10:00",
                        "time_end": "11:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                        ],
                        "auditories": [
                            {
                                "auditory_name": "207а, ГК",
                            }
                        ]
                    },
                    {
                        "subject": "Инженерная графика",
                        "type": 0,
                        "time_start": "12:00",
                        "time_end": "13:40",
                        "parity": "",
                        "date_start": "",
                        "date_end": "",
                        "teachers": [
                            {
                                "teacher_name": "Баденко В.Л.",
                            }
                        ],
                        "auditories": [
                            {
                                "auditory_name": "216 Гк",
                            },
                        ]
                    },
                ]
            },
        ]
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug = True)
