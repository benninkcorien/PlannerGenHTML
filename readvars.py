import yaml

with open("config.yaml", "r", encoding="utf-8") as config_file:
    config_data = yaml.safe_load(config_file)

pagewidth = config_data.get("width")
pageheight = config_data.get("height")
startyear = config_data.get("startyear")
startmonth = config_data.get("startmonth")
startday = config_data.get("startday")
howmanymonths = config_data.get("howmanymonths")
