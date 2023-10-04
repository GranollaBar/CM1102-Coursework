#!/usr/bin/python3
import cgi#, cgitb
#cgitb.enable() # displays any errors; useful for debugging
form = cgi.FieldStorage() 
year = form.getvalue('year-input')
option = form.getvalue('all-Radio-option')

def easter_calculation(year, option):
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    days_sup = {"1": "1st", "2": "2nd", "3": "3rd", "21": "21st", "22": "22nd", "23": "23rd", "31": "31st"}
    a = year % 19   
    b = year // 100   
    c = year % 100   
    d = b // 4   
    e = b % 4   
    g = (8 * b + 13) // 25   
    h = (19 * a + b - d - g + 15) % 30   
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    month = (h - m + r + 90) // 25
    day = (h - m + r + month + 19) % 32

    numerical_final_date = (f"{day}/{month}/{year}")

    try:
        full_final_date = (f'{days_sup[str(day)]} {months[month-1]}, {year}')
    except:
        full_final_date = (f'{day}th {months[month-1]}, {year}')

    final_sup = ''
    for char in full_final_date[:]:
        if char.isalpha():
            final_sup += char
            if len(final_sup) == 2:
                full_final_date.replace(final_sup, '')
                break

    if str(option) == 'Numerical':
        return (f'<br> <p>{numerical_final_date}</p>')
    elif str(option) == 'Full':
        return (f'<br> <p>{day}<sup>{final_sup}</sup> {months[month-1]}, {year}</p>')
    elif str(option) == 'Both':
        return (f'<br> <p>{numerical_final_date}</p> OR <br> <p>{day}<sup>{final_sup}</sup> {months[month-1]}, {year}</p> <br>')
    else:
        return ('<br> <p> </p>')


easter_date = easter_calculation(int(year),option)

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html lang="en" dir="ltr">')
print('<head> <meta charset="utf-8">')
print('<meta charset="utf-8">')
print('<title>GranollDates</title>')
print('<link rel="stylesheet" href="../Style.css">')
print('</head>')
print('<body>')

print('<br>')
print('<div class="box">')
print('<br> <h1 class="title">GranollDates</h1>')
print('<hr class="horizontal-line">')
print('<div class="information">')
print('<br> <h1 class="inside-title">Easter Date Calculator</h1>')
print('<br> <div class="date-calculator">')
print('<fieldset class="calculator-border">')
print('<legend class="legend-title">Easter Calculator</legend>')

print('<br> <p><b><u>Enter A Year To Find The Day & Month Easter Falls On</u></b></p>')
print('<form action="easter_calculator.py" method="post">')
print('<div class="txt-field">')
print('<input type="number" name="year-input" required>')
print('<span></span>')
print('<label>Year</label>')
print('</div>')

print('<div class="radio">')
print('<input class="radio-input" type="radio" name="all-Radio-option" value="Numerical" id="myradio1">')
print('<label class="radio-label" for="myradio1">Numerical Date</label>')
print('<input class="radio-input" type="radio" name="all-Radio-option" value="Full" id="myradio2">')
print('<label class="radio-label" for="myradio2">Full Date</label>')
print('<input class="radio-input" type="radio" name="all-Radio-option" value="Both" id="myradio3">')
print('<label class="radio-label" for="myradio3">Both Options</label>')
print('</div>')

print('<br> <br> <br>')

print('<div class="submit-button">')
print('<nav>')
print('<form action="easter_calculator.py" method="post">')
print('<button class="button">Submit</button>')
print('</form>')
print('</nav>')
print('</div>')

print('<br> <br>')

print(easter_date)

print('</form>')
print('<br>')
print('</fieldset>')
print('</div>')
print('<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>')
print('<hr class="horizontal-line">')
print('<div class="footer1">&copy; GranollDates</div>') 
print('<div class="footer2">Created By Joshua Noble</div>')
print('</div>')
print('</div>')

print('</body>')
print('</html>')
