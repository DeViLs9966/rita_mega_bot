import ast
from pathlib import Path

FILES = ["rita_main.py", "check_bot_diagnostics.py"]
FUNC_NAME = "analyze_and_fix_script"

fixed_function_code = '''
async def analyze_and_fix_script(script_path, log_path) -> bool:
    import asyncio
    from pathlib import Path
    import openai
    import logging

    logger = logging.getLogger(__name__)

    if isinstance(script_path, str):
        script_path = Path(script_path)
    if isinstance(log_path, str):
        log_path = Path(log_path)

    try:
        if not script_path.exists() or not log_path.exists():
            logger.warning(f"[WARN] Файл не найден: {script_path} или {log_path}")
            return False

        with log_path.open("r", encoding="utf-8") as f:
            lines = f.readlines()

        error_lines = [line for line in lines if "[ERROR]" in line]
        last_errors = "".join(error_lines[-100:]) if error_lines else ""

        if not last_errors.strip():
            logger.info("[INFO] Нет ошибок в логах — ничего не исправляем.")
            return False

        original_code = script_path.read_text(encoding="utf-8")

        response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ты Python-программист. Исправь ошибки в скрипте."},
                {"role": "user", "content": f"Вот скрипт:\\n\\n{original_code}"},
                {"role": "user", "content": f"Вот ошибки из логов:\\n\\n{last_errors}"},
            ],
            temperature=0.2,
        )

        fixed_code = response.choices[0].message.content

        if fixed_code.strip() != original_code.strip():
            script_path.write_text(fixed_code, encoding="utf-8")
            logger.info(f"[FIX] ✅ Код в {script_path} обновлен.")
            return True
        else:
            logger.info(f"[INFO] Изменений не требуется в {script_path}.")
            return False

    except Exception as e:
        logger.error(f"[ERROR] Исключение в analyze_and_fix_script: {e}")
        return False
'''.strip()


def remove_function_code(source_code: str, func_name: str) -> str:
    """
    Удаляет из исходника все определения функции с именем func_name (включая async def).
    Возвращает новый код без этих функций.
    """
    try:
        tree = ast.parse(source_code)
    except Exception as e:
        print(f"Ошибка парсинга AST: {e}")
        return source_code

    # Найдем все позиции (start,end) функций func_name
    positions = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == func_name:
            start = node.lineno - 1  # линии в ast с 1, индексы с 0
            end = getattr(node, 'end_lineno', None)
            if end is None:
                # если Python <3.8, end_lineno нет — попробуем определить по телу
                if node.body:
                    end = node.body[-1].lineno
                else:
                    end = start
            else:
                end = end - 1
            positions.append((start, end))

    if not positions:
        return source_code  # ничего не нашли

    lines = source_code.splitlines()
    # Удаляем функции с конца, чтобы не смещать индексы
    for start, end in sorted(positions, reverse=True):
        # удаляем строки с start по end включительно
        del lines[start:end + 1]

    return "\n".join(lines)


def fix_file(path: Path):
    if not path.exists():
        print(f"❌ Файл не найден: {path}")
        return False

    code = path.read_text(encoding="utf-8")
    new_code = remove_function_code(code, FUNC_NAME)

    if code == new_code:
        print(f"⚠️ Функция {FUNC_NAME} не найдена в {path.name}")
        return False

    # Вставляем новую функцию в конец файла
    new_code = new_code.rstrip() + "\n\n" + fixed_function_code + "\n"
    path.write_text(new_code, encoding="utf-8")
    print(f"✅ {path.name} обновлён: старая функция удалена, новая вставлена.")
    return True


if __name__ == "__main__":
    for f in FILES:
        fix_file(Path(f))
