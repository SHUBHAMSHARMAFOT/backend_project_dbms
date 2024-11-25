import subprocess


def run_app_1_service():
    subprocess.Popen(["/Users/shubhamsharma/Desktop/shub/college/sem 3 /dbms/mini project dbms/venv/bin/python", "employee_app/app.py"])

def run_app_2_service():
    subprocess.Popen(["/Users/shubhamsharma/Desktop/shub/college/sem 3 /dbms/mini project dbms/venv/bin/python", "product_app/app.py"])


if __name__ == '__main__':
    run_app_1_service()
    run_app_2_service()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating all processes. Alvida!")
