import allure
import json

def before_all(context):
    with open("config/test_data.json") as f:
        context.test_data = json.load(f)
        
def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")
    print(f"Tags: {scenario.tags}")

def after_scenario(context, scenario):
    print(f"Finished scenario: {scenario.name}")
    print(f"Status: {scenario.status}")
    
    if scenario.status == "failed":
        if hasattr(context, "driver"):
            screenshot = context.driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
    
    if hasattr(context, "driver"):
        context.driver.quit()

def after_all(context):
    with open("allure-results/environment.properties", "w") as f:
        f.write("Browser=Chrome\n")
        f.write("Browser.Version=125\n")
        f.write("Platform=Windows 10\n")
        f.write("Python.Version=3.10\n")
