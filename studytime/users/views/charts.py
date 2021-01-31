from json import dumps 

def category_chart(sessions):
    labels = []
    data = []
    for session in sessions:
        labels.append(str(session.session_date))
        data.append(str(session.session_time))
    
    chart = {
        "labels": labels,
        "data": data,
    }

    chartJSON = dumps(chart) 
    return chartJSON