import subprocess
import time
import signal

RITA_MAIN = "rita_main.py"
CHECK_DIAG = "check_bot_diagnostics.py"

def acquire_wakelock():
    try:
        subprocess.run(["termux-wake-lock"], check=True)
        print("[monitor] WakeLock активирован")
    except Exception as e:
        print(f"[monitor] Ошибка при активации WakeLock: {e}")

def release_wakelock():
    try:
        subprocess.run(["termux-wake-unlock"], check=True)
        print("[monitor] WakeLock освобожден")
    except Exception as e:
        print(f"[monitor] Ошибка при освобождении WakeLock: {e}")

def start_script(script_name):
    print(f"[monitor] Запуск {script_name}")
    return subprocess.Popen(["python", script_name])

def is_process_alive(proc):
    return proc and proc.poll() is None

def main():
    acquire_wakelock()
    main_proc = start_script(RITA_MAIN)
    diag_proc = start_script(CHECK_DIAG)

    try:
        while True:
            if not is_process_alive(main_proc):
                print("[monitor] rita_main.py упал, перезапуск...")
                main_proc = start_script(RITA_MAIN)
            if not is_process_alive(diag_proc):
                print("[monitor] check_bot_diagnostics.py упал, перезапуск...")
                diag_proc = start_script(CHECK_DIAG)
            time.sleep(10)
    except KeyboardInterrupt:
        print("[monitor] Остановка мониторинга по Ctrl+C")
    finally:
        for p in [main_proc, diag_proc]:
            if is_process_alive(p):
                p.send_signal(signal.SIGINT)
                p.wait(timeout=5)
        release_wakelock()

if __name__ == "__main__":
    main()
