from django.shortcuts import render
from datetime import date
def index(request):
    today = date.today()
    context={
        'judul':'Welcome',
        'author':'ilman teguh praseya',
        'article':'Respondent extrema primis, media utrisque, omnia omnibus. Quae est igitur causa istarum angustiarum? Sed haec in pueris; Nunc haec primum fortasse audientis servire debemus. Quid me istud rogas? Frater et T. Torquatus, is qui consul cum Cn. Venit ad extremum;',
        'aside':'Ita graviter et severe voluptatem secrevit a bono. Nunc vides, quid faciat. At hoc in eo M.',
        'date': today,
        'banner':'img/mountains-4420690.jpg',
        'css':'css/gaya.css',
        'nav':[
            ['/','Home'],
            ['/blog/','Blog'],
            ['/about/','About'],
        ]
    }
    return render(request,'index.html',context)