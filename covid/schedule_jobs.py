from covid.api.miner.controller import CovidCasesRaw
import sched, time

s = sched.scheduler(time.time, time.sleep)

def job_get_cases():
    c = CovidCasesRaw()
    c.save_cases()
    print("Estou trabalhando.....")

def run_schedule():
    s.enter(10, 1, job_get_cases)
    print("running schedule....")
    s.run()