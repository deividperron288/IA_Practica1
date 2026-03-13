def is_year_leap(year):

    if year < 1582:
        print("No está dentro del período del calendario Gregoriano")
        return None
    else:
        if year % 4 != 0:
            #print("año común")
            return False
        elif year % 100 != 0:
            #print("año bisiesto")
            return True
        elif year % 400 != 0:
            #print("año común")
            return False
        else:
            #print("año bisiesto")
            return True
def days_in_month(year, month):
    meses =["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiempre","Octubre","Nobiembre","Diciembre"]
    dias_meses = [31,28,31,30,31,30,31,31,30,31,30,30]
    if is_year_leap(year) == True and month == 2:
        return 29
    else:
        return dias_meses[month - 1]
    

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    print(result)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")