def get_compulsory(message) -> str:
    message = message + " : "
    response = input(message)
    if response is None:
        get_compulsory(message)
    else:
        return response

class Data:
    date = ""
    start_time = ""
    firewood_usage_kg = ""
    firewood_mc = ""
    briquette_usage_kg = ""
    initial_pressure = ""
    average_loading = ""
    flue_gas_1 = ""
    flue_gas_2 = ""
    final_pressure = ""
    end_time = ""

    def __init__(self,date,start_time,firewood_usage_kg,firewood_mc,briquette_usage_kg,initial_pressure,average_loading,flue_gas_1,flue_gas_2,final_pressure,end_time) -> None:
        self.date = date
        self.start_time = start_time
        self.firewood_usage_kg = firewood_usage_kg
        self.firewood_mc = firewood_mc
        self.briquette_usage_kg = briquette_usage_kg
        self.initial_pressure = initial_pressure
        self.average_loading = average_loading
        self.flue_gas_1 = flue_gas_1
        self.flue_gas_2 = flue_gas_2
        self.final_pressure = final_pressure
        self.end_time = end_time


    def create_fuel_record():
        date = get_compulsory("Enter the DATE")

        start_time = get_compulsory("Enter the START_TIME")

        firewood_usage_kg = get_compulsory("Enter the FIREWOOD USAGE KG")

        firewood_mc = get_compulsory("Enter the FIREWOOD MC (%)")

        briquette_usage = get_compulsory("Enter the BRIQUETTE USAGE KG")

        initial_pressure = get_compulsory("Enter the INITIAL PRESSURE")

        average_loading = get_compulsory("Enter the Average LOADING")

        flue_gas_1 = get_compulsory("Enter the FLUE GAS 1")

        flue_gas_2 = get_compulsory("Enter the FLUE GAS 2")

        final_pressure = get_compulsory("Enter the FINAL PRESSURE")

        end_time = get_compulsory("Enter the END TIME")

        return Data(date,start_time,firewood_usage_kg,firewood_mc,briquette_usage,initial_pressure,average_loading,flue_gas_1,flue_gas_2,final_pressure,end_time)