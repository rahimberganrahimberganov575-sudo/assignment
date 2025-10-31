def calculate_sales_amount(meal_type, standart_tables, service_level):
    if meal_type == "breakfast":
        if   service_level == "low":
           price =30
        elif service_level == "medium":
           price =  45 
        elif service_level == "high":
           price =  60 
           
    elif meal_type == "lunch":
        if   service_level == "low":
           price =  40
        elif service_level == "medium":
           price =  65
        elif service_level == "high":
           price =  90 

    elif meal_type == "dinner":
        if   service_level == "low":
           price =  55     
        elif service_level == "medium":
           price =  85
        elif service_level == "high": 
           price =  125
      
    return price * standart_tables     
     


def calculate_efficiency_score(shift_years, standard_tables, served_tables):
   expected_tables = 1000 + (shift_years * 100)
   table_capacity = expected_tables - standard_tables
   efficiency_percentage = ((served_tables - standard_tables) / table_capacity )* 100
   return efficiency_percentage
   

def determine_service_rating(efficiency_percent):
   if   efficiency_percent < 50:
      return "Learning Stage"
   elif efficiency_percent < 60:
      return "Capable Stage"
   elif efficiency_percent < 70:
      return "Skilled Stage"
   elif efficiency_percent < 85:
      return "Accomplished Stage"
   else:
      return "Master stage "
   

def calculate_tip_earnings(sales, tables, rating_bonus):
   base_tips = sales * 0.05 + tables * 2
   if   rating_bonus == "Learning Stage":
        bonus = 0.5
   elif rating_bonus == "Capable Stage":
        bonus = 1.0
   elif rating_bonus == "Skilled Stage":
        bonus = 1.2
   elif rating_bonus == "Accomplished Stage":
        bonus = 1.5
   elif rating_bonus == "Master stage ":
        bonus = 1.8
   
   return  round((bonus * base_tips), 1)
   


def requires_mentoring(service_weeks, total_tables, avg_efficiency):
   if   service_weeks >= 6 and avg_efficiency < 50:
     return True
   elif total_tables < 100 and avg_efficiency < 60:
     return True
   elif service_weeks >= 4 and avg_efficiency < 40: 
     return True
   else :
     return False

def generate_service_summary(server, meal_type, tables, service_level, shift_years, standard_tables, served_tables, service_weeks):
   total_sales_amount = calculate_sales_amount(meal_type, tables, service_level)
   efficiency_percentage = calculate_efficiency_score(shift_years, standard_tables, served_tables)
   rating = determine_service_rating(efficiency_percentage)
   tip_earnings = calculate_tip_earnings(total_sales_amount, tables, rating )
   requires_monitoring =  "Yes" if requires_mentoring(service_weeks,standard_tables , efficiency_percentage) else  "No"

   print("="* 40)
   print(f"Service Summary for: {server}")
   print ("-" * 40)
   print(f"Meal_type : {meal_type}")
   print(f"Tables Served : {tables}  tables ")
   print(f"Service Level: {service_level}")
   print(f"Sales Amount: ${total_sales_amount:.0f}")
   print(f"Efficiency Analysis:")
   print(f"Experience: {shift_years} years  Standard: {standard_tables}  Served Tables: {served_tables}  ")
   print(f"Efficiency : {efficiency_percentage:.1f} %")
   print(f"Service Rating: {rating}")
   print(f"Tip Earnings: $ {tip_earnings:.1f}")
   print(f"Service Weeks: {service_weeks}")
   print(f"Mentoring Required: {requires_monitoring}")

 
print("\n RESTAURANT SERVICE ANALYZER")


generate_service_summary( "Quinn" , "dinner" , 45, "high" ,3 ,800 , 1150 ,3 )
generate_service_summary( "Reese " , "lunch", 60 , "medium", 5, 900, 1300, 5)
generate_service_summary( "Skyler", "breakfast" , 30 , "low" ,  8,  850,  950,  7)