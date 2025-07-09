import subprocess
from multiprocessing import Process

def run_behave(feature, result_folder):
    cmd = f'behave -f allure_behave.formatter:AllureFormatter -o allure-results/{result_folder} {feature}'
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    processes = []

    tests = [
        ("features/login/login_positive.feature", "positive"),
        ("features/login/login_negative.feature", "negative"),
    ]

    for feature, result_folder in tests:
        p = Process(target=run_behave, args=(feature, result_folder))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # merge results
    import shutil
    shutil.copytree("allure-results/positive", "allure-results", dirs_exist_ok=True)
    shutil.copytree("allure-results/negative", "allure-results", dirs_exist_ok=True)
