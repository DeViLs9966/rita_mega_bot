# utils/fix_syntax.py

def fix_unclosed_syntax(code: str) -> str:
    """
    Простая попытка исправить незакрытые скобки и кавычки.
    Добавляет недостающие закрывающие символы в конце кода.
    """
    # Считаем открытые и закрытые скобки
    open_parens = code.count('(') - code.count(')')
    open_brackets = code.count('[') - code.count(']')
    open_braces = code.count('{') - code.count('}')
    # Считаем кавычки (не учитывая эскейпы, для простоты)
    double_quotes = code.count('"')
    single_quotes = code.count("'")

    fixed_code = code

    if open_parens > 0:
        fixed_code += ')' * open_parens
    if open_brackets > 0:
        fixed_code += ']' * open_brackets
    if open_braces > 0:
        fixed_code += '}' * open_braces
    # Если кавычек нечетное количество - добавляем закрывающую
    if double_quotes % 2 != 0:
        fixed_code += '"'
    if single_quotes % 2 != 0:
        fixed_code += "'"

    return fixed_code


async def try_fix_syntax(script_path, logger, send_admin_message):
    """
    Пример асинхронной функции для попытки автоисправления синтаксиса.
    Возвращает True если исправлено, False иначе.
    """
    import shutil

    code = script_path.read_text(encoding='utf-8')

    try:
        compile(code, str(script_path), 'exec')
        return True  # Код валидный, исправлять не надо
    except SyntaxError as e:
        msg = str(e)
        if "was never closed" in msg or "unexpected EOF" in msg:
            fixed_code = fix_unclosed_syntax(code)
            try:
                compile(fixed_code, str(script_path), 'exec')
                # Резервное копирование оригинала
                backup_path = script_path.with_suffix(script_path.suffix + ".bak")
                shutil.copy(script_path, backup_path)
                logger.info(f"[BACKUP] Создана резервная копия: {backup_path}")

                # Запись исправленного кода
                script_path.write_text(fixed_code, encoding='utf-8')
                logger.info(f"[FIX] Исправлены незакрытые скобки/кавычки в {script_path}")
                await send_admin_message(f"🛠️ Автофикс: исправлены незакрытые конструкции в {script_path.name}")
                return True
            except SyntaxError as e2:
                logger.error(f"[FAIL] Ошибка после попытки исправления: {e2}")
                return False
        else:
            logger.error(f"[FAIL] Синтаксическая ошибка: {msg}")
            return False
